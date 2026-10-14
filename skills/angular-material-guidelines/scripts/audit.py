#!/usr/bin/env python3
"""Audita templates Angular contra los lineamientos de Angular Material.

Uso:
  audit.py [rutas...] [--json]   auditoría completa (por defecto: .); exit 1 si hay ERROR
  audit.py --wrappers [rutas...] [--json]
                                 inventario de componentes/servicios UI propios y si Material los reemplaza
  audit.py --hook                modo hook PostToolUse (lee el evento JSON por stdin)
  audit.py --selftest            prueba rápida del propio script

Silenciar un hallazgo intencional: en la línea anterior (o la misma) poner
  <!-- mat-guidelines-ignore: regla-id — motivo -->
"""
import json
import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

SKIP_DIRS = {'node_modules', 'dist', '.angular', '.git', 'coverage', '.nx'}
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr'}
BTN_NEW = {'matbutton', '[matbutton]', 'maticonbutton', 'matfab', 'matminifab'}
LEGACY = {'mat-button': 'matButton', 'mat-raised-button': 'matButton="elevated"',
          'mat-flat-button': 'matButton="filled"', 'mat-stroked-button': 'matButton="outlined"',
          'mat-icon-button': 'matIconButton', 'mat-fab': 'matFab', 'mat-mini-fab': 'matMiniFab'}
ICON_ONLY = {'maticonbutton', 'mat-icon-button', 'matminifab', 'mat-mini-fab'}
FAB = {'matfab', 'mat-fab'}
LABEL = {'aria-label', '[aria-label]', '[attr.aria-label]', 'aria-labelledby', '[aria-labelledby]', '[attr.aria-labelledby]'}
LINK = {'href', '[href]', '[attr.href]', 'routerlink', '[routerlink]'}
TABINDEX = {'tabindex', '[tabindex]', '[attr.tabindex]'}
NOT_FOCUSABLE = {'span', 'div', 'p', 'i', 'img', 'mat-icon', 'label', 'li', 'td', 'th', 'section', 'small', 'strong'}
CHIP_PARENTS = {'mat-chip': {'mat-chip-set', 'mat-chip-listbox', 'mat-chip-grid'},
                'mat-chip-option': {'mat-chip-listbox'}, 'mat-chip-row': {'mat-chip-grid'}}
FIELD_CONTROLS = {'mat-select', 'mat-chip-grid', 'mat-date-range-input'}
# Cada uno es una sección propia: puede tener su propia acción filled (diálogo, paso, tab, panel, card).
SECTIONS = {'ng-template', 'mat-step', 'mat-tab', 'mat-expansion-panel', 'mat-card'}


class Auditor(HTMLParser):
    def __init__(self, major, line_offset=0):
        super().__init__(convert_charrefs=True)
        self.major, self.off = major, line_offset
        self.stack, self.findings, self.filled, self.fabs = [], [], {}, []

    def add(self, sev, rule, msg, spans):
        self.findings.append({'line': spans[0][0], 'sev': sev, 'rule': rule, 'msg': msg, 'spans': spans})

    def _span(self):
        line = self.getpos()[0] + self.off
        return (line, line + (self.get_starttag_text() or '').count('\n'))

    def _nearest(self, key):
        return next((e for e in reversed(self.stack) if key in e), None)

    def handle_starttag(self, tag, attrs):
        a = {k: (v or '') for k, v in attrs}
        sp = self._span()
        anc = {e['tag'] for e in self.stack}
        legacy, new = [n for n in a if n in LEGACY], [n for n in a if n in BTN_NEW]
        if legacy or new:
            self._button(tag, a, sp, legacy, new)
        if ('matinput' in a or tag in FIELD_CONTROLS) and 'mat-form-field' not in anc:
            self.add('ERROR', 'control-sin-form-field',
                     f'<{tag}{" matInput" if "matinput" in a else ""}> fuera de <mat-form-field>: pierde label, hint, error y estilo consistente.', [sp])
        if tag in CHIP_PARENTS and not anc & CHIP_PARENTS[tag]:
            self.add('ERROR', 'chip-sin-contenedor',
                     f'<{tag}> debe ir dentro de {" / ".join(sorted(CHIP_PARENTS[tag]))}.', [sp])
        if a.keys() & {'mattooltip', '[mattooltip]'} and tag in NOT_FOCUSABLE and not a.keys() & TABINDEX:
            self.add('WARN', 'tooltip-no-enfocable',
                     f'matTooltip en <{tag}> no enfocable: teclado y táctil no lo verán. Úsalo en un elemento interactivo '
                     'o agrega tabindex="0", y no pongas ahí información esencial.', [sp])
        if tag in ('button', 'a'):
            d = self._nearest('dlg')
            if d:
                d['dlg'] += 1
        if a.get('type') == 'submit':
            f = self._nearest('toggles')
            if f:
                f['submit'] = True
        if tag == 'mat-slide-toggle':
            f = self._nearest('toggles')
            if f:
                f['toggles'].append(sp)
        s = self._nearest('opts')
        if s and tag == 'mat-option':
            s['opts'] += 1
        if s and '*ngfor' in a:
            s['skip'] = True
        if tag in VOID:
            return
        e = {'tag': tag, 'span': sp}
        if tag == 'mat-dialog-actions' or a.keys() & {'mat-dialog-actions', 'matdialogactions'}:
            e['dlg'] = 0
        if tag == 'mat-select':
            e.update(opts=0, skip=bool(a.keys() & {'multiple', '[multiple]'}))
        if tag == 'form':
            e.update(toggles=[], submit=bool(a.keys() & {'(ngsubmit)', '(submit)'}))
        self.stack.append(e)

    def _button(self, tag, a, sp, legacy, new):
        if self.major is not None and self.major < 20 and new:
            self.add('ERROR', 'api-boton-no-disponible',
                     f'{new[0]} requiere Angular Material v20+ (proyecto en v{self.major}); sin la directiva queda sin estilo. '
                     'Usa mat-flat-button / mat-stroked-button / mat-raised-button / mat-button / mat-icon-button / mat-fab / mat-mini-fab.', [sp])
        if self.major is not None and self.major >= 20:
            for n in legacy:
                self.add('WARN', 'boton-legacy', f'Selector legado `{n}`; en código nuevo (v20+) usa `{LEGACY[n]}`.', [sp])
        kinds = set(legacy) | set(new)
        icon_only = kinds & ICON_ONLY or (kinds & FAB and not a.keys() & {'extended', '[extended]'})
        if icon_only and not a.keys() & LABEL:
            self.add('ERROR', 'icon-button-sin-label',
                     'Botón solo-ícono sin aria-label/aria-labelledby: el lector de pantalla no sabe qué hace (matTooltip no lo reemplaza).', [sp])
        if tag == 'button' and a.keys() & {'routerlink', '[routerlink]'}:
            self.add('ERROR', 'button-navega', '<button> con routerLink: para navegar usa <a matButton routerLink="...">.', [sp])
        if tag == 'a' and not a.keys() & LINK:
            self.add('ERROR', 'a-sin-destino', '<a> con estilo de botón sin href/routerLink: si ejecuta una acción usa <button>.', [sp])
        if a.get('matbutton') == 'filled' or 'mat-flat-button' in a:
            section = next((e['span'] for e in reversed(self.stack) if e['tag'] in SECTIONS), None)
            self.filled.setdefault(section, []).append(sp)
        if kinds & FAB:
            self.fabs.append(sp)

    def handle_data(self, data):
        s = self._nearest('opts')
        if s and '@for' in data:
            s['skip'] = True

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                for e in reversed(self.stack[i:]):
                    self._close_el(e)
                del self.stack[i:]
                return

    def _close_el(self, e):
        span = (e['span'][0], self.getpos()[0] + self.off)
        if e.get('dlg', 0) > 2:
            self.add('WARN', 'dialog-mas-de-2-acciones',
                     f'mat-dialog-actions con {e["dlg"]} acciones: máximo 2 (confirmar y descartar).', [span])
        if 'opts' in e and not e['skip'] and 2 <= e['opts'] <= 5:
            self.add('WARN', 'select-pocas-opciones',
                     f'mat-select con {e["opts"]} opciones fijas: con ≤5 opciones y espacio disponible usa '
                     'mat-radio-group (o mat-button-toggle-group si son opuestas).', [span])
        if e.get('submit') and e.get('toggles'):
            self.add('WARN', 'slide-toggle-en-form-con-submit',
                     'mat-slide-toggle en un form que se envía: el switch implica efecto inmediato; '
                     'si se guarda al enviar usa mat-checkbox.', e['toggles'])

    def finish(self):
        for e in reversed(self.stack):
            self._close_el(e)
        self.stack = []
        for spans in self.filled.values():
            if len(spans) > 1:
                self.add('WARN', 'multiples-filled',
                         f'{len(spans)} botones filled en la misma sección (líneas {", ".join(str(s[0]) for s in spans)}): '
                         'una sola acción principal por sección; degrada las demás a tonal/outlined/text.', spans)
        if len(self.fabs) > 1:
            self.add('WARN', 'multiples-fab',
                     f'{len(self.fabs)} FAB (líneas {", ".join(str(s[0]) for s in self.fabs)}): un FAB por pantalla.', self.fabs)


def ignored(lines, f):
    for s in f['spans']:
        for ln in (s[0] - 1, s[0]):
            if 1 <= ln <= len(lines) and 'mat-guidelines-ignore' in lines[ln - 1] and f['rule'] in lines[ln - 1]:
                return True
    return False


def audit_source(path, text, major):
    if path.suffix == '.ts':
        # ponytail: asume templates inline sin backticks internos; templateUrl se audita vía su .html
        chunks = []
        for m in re.finditer(r'\btemplate\s*:\s*`', text):
            end = text.find('`', m.end())
            if end != -1:
                chunks.append((m.end(), text[m.end():end]))
    else:
        chunks = [(0, text)]
    lines, out = text.splitlines(), []
    for start, tpl in chunks:
        p = Auditor(major, text.count('\n', 0, start))
        p.feed(tpl)
        p.close()
        p.finish()
        out += [f for f in p.findings if not ignored(lines, f)]
    return sorted(out, key=lambda f: f['line'])


# --- Inventario de wrappers y componentes UI propios ---
# Palabras del nombre (inglés/español; "a-b" = par consecutivo) → equivalente en Angular Material.
# None = Material no lo cubre.
_EQ = [
    ('matButton / matIconButton / matFab', 'button btn boton'),
    ('matIconButton', 'icon-button boton-icono'),
    ('mat-icon', 'icon icono'),
    ('mat-form-field + matInput', 'input field form-field text-field textfield campo campo-texto entrada'),
    ('mat-form-field + textarea matInput (cdkTextareaAutosize)', 'textarea'),
    ('mat-select', 'select combobox combo selector'),
    ('mat-select (si guarda un valor) o mat-menu (si son acciones)', 'dropdown desplegable'),
    ('mat-autocomplete', 'autocomplete typeahead autocompletar'),
    ('mat-checkbox', 'checkbox casilla'),
    ('mat-radio-group', 'radio radio-group'),
    ('mat-slide-toggle (on/off) o mat-button-toggle-group (opciones opuestas)', 'toggle switch interruptor'),
    ('mat-button-toggle-group', 'segmented'),
    ('mat-slider', 'slider range deslizador'),
    ('mat-datepicker / mat-date-range-input',
     'datepicker date-picker date-input date-range calendar calendario selector-fecha'),
    ('mat-timepicker (v19.1+)', 'timepicker time-picker time-input selector-hora'),
    ('MatDialog', 'modal dialog popup confirm dialogo confirmacion'),
    ('MatBottomSheet', 'bottom-sheet bottomsheet action-sheet'),
    ('MatSnackBar', 'toast toaster snackbar snack-bar notification notifications notify notificacion'),
    ('MatSnackBar si es temporal; un aviso fijo en la página no tiene equivalente', 'alert alerta aviso'),
    ('matTooltip', 'tooltip'),
    ('mat-menu (acciones) o CDK Overlay (contenido interactivo)', 'popover'),
    ('mat-menu', 'menu context-menu'),
    ('mat-tab-group / mat-tab-nav-bar', 'tabs tab tabset pestanas pestana'),
    ('mat-expansion-panel / mat-accordion',
     'accordion collapse collapsible expansion expandable acordeon colapsable'),
    ('mat-stepper', 'stepper wizard steps asistente pasos'),
    ('mat-table + matSort + mat-paginator', 'table datatable data-table tabla'),
    ('mat-table (datos) o mat-grid-list (mosaicos)', 'grid'),
    ('mat-paginator', 'paginator pagination pager paginacion paginador'),
    ('mat-list-item', 'list-item'),
    ('mat-card', 'card tarjeta'),
    ('mat-chip', 'chip chips tag tags pill etiqueta'),
    ('matBadge', 'badge insignia'),
    ('mat-progress-spinner / mat-progress-bar', 'spinner loader loading cargando cargador'),
    ('mat-progress-bar', 'progress progress-bar progreso barra-progreso'),
    ('mat-sidenav / mat-drawer', 'sidebar sidenav drawer side-menu offcanvas barra-lateral'),
    ('mat-toolbar', 'navbar topbar toolbar appbar header encabezado cabecera barra-superior'),
    ('mat-divider', 'divider separator separador divisor'),
    ('mat-tree', 'tree arbol'),
    (None, 'avatar breadcrumb breadcrumbs migas skeleton carousel carrusel rating stars estrellas '
           'upload uploader dropzone file-upload subir-archivo'),
]
EQUIV = {w: eq for eq, words in _EQ for w in words.split()}
OVERLAYS = ('MatDialog', 'MatSnackBar', 'MatBottomSheet')  # únicos equivalentes que un servicio puede reimplementar
SAME_KIT = 'el componente Material equivalente de cada módulo usado (dos kits de UI rompen la consistencia)'
LIBS = {
    'ngx-toastr': 'MatSnackBar',
    'sweetalert2': 'MatDialog (confirmaciones) / MatSnackBar (avisos)',
    '@sweetalert2/ngx-sweetalert2': 'MatDialog (confirmaciones) / MatSnackBar (avisos)',
    'ngx-smart-modal': 'MatDialog',
    'ngx-spinner': 'mat-progress-spinner / mat-progress-bar',
    'ngx-pagination': 'mat-paginator',
    '@ng-select/ng-select': 'mat-select / mat-autocomplete',
    'ngx-material-timepicker': 'mat-timepicker (v19.1+)',
    'ngx-bootstrap': SAME_KIT, '@ng-bootstrap/ng-bootstrap': SAME_KIT, 'primeng': SAME_KIT, 'ng-zorro-antd': SAME_KIT,
}
DECORATOR = re.compile(r'@(Component|Directive|Injectable)\s*\(([\s\S]*?)\)\s*'
                       r'(?:export\s+)?(?:default\s+)?(?:abstract\s+)?class\s+(\w+)')
CREATES_DOM = re.compile(r'document\.|Renderer2|createComponent|ViewContainerRef|appendChild|ApplicationRef')


def _equiv(name):
    """'app-confirm-dialog' / '[appTooltip]' / 'ToastService' → (palabra, equivalente) o None."""
    first = re.split(r'[,\s]', name.strip())[0]
    tokens = [t.lower() for t in re.findall(r'[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])', first)]
    for i in range(len(tokens) - 1, -1, -1):  # desde el final: el núcleo del nombre suele ir al final
        for key in (f'{tokens[i - 1]}-{tokens[i]}' if i else None, tokens[i]):
            if key in EQUIV:
                return key, EQUIV[key]
    return None


def ui_components(path, text):
    """Componentes, directivas y servicios propios cuyo nombre corresponde a una pieza de UI."""
    matches = list(DECORATOR.finditer(text))
    file_material = {'material/' + x for x in re.findall(r"@angular/material/([\w-]+)", text)}
    out = []
    for n, m in enumerate(matches):
        kind, body, cls = m.groups()
        sel = re.search(r"selector\s*:\s*['\"`]([^'\"`]+)", body)
        hit = _equiv(sel.group(1) if sel else cls)
        if not hit:
            continue
        tpl = ''
        t = re.search(r'template\s*:\s*`([\s\S]*?)`', body)
        u = re.search(r"templateUrl\s*:\s*['\"`]([^'\"`]+)", body)
        if t:
            tpl = t.group(1)
        elif u and (path.parent / u.group(1)).is_file():
            tpl = read(path.parent / u.group(1))
        material = sorted(set(re.findall(r'<(mat-[a-z-]+)', tpl))
                          | set(re.findall(r'[\s\[](mat[A-Z]\w*|mat-[a-z-]+)', tpl)) | file_material)
        if kind == 'Injectable':
            src = text[m.start():matches[n + 1].start() if n + 1 < len(matches) else len(text)]
            if not (hit[1] or '').startswith(OVERLAYS) or not (material or CREATES_DOM.search(src)):
                continue  # servicio de estado/datos, no de UI
        first = re.split(r'[,\s]', sel.group(1).strip())[0] if sel else ''
        out.append({
            'nombre': cls if not sel else first if '[' in first else f'<{first}>',
            'tipo': 'SIN-EQUIVALENTE' if hit[1] is None else 'WRAPPER' if material else 'REIMPLEMENTA',
            'equivalente': hit[1], 'material': material, 'clase': cls, 'selector': first,
            'delgado': bool(material and tpl and len(re.findall(r'<[a-z][\w-]*', tpl)) <= 3),
            'line': text.count('\n', 0, m.start()) + 1,
        })
    return out


def _use_pattern(item):
    sel = item['selector']
    if not sel:
        return rf"\b{item['clase']}\b"
    attr = re.search(r'\[([\w-]+)', sel)
    if attr:
        return rf'[\s\[]{re.escape(attr.group(1))}[\s\]=>/]'
    return rf'<{re.escape(sel)}[\s>/]'


def inventory(root):
    files = [(os.path.relpath(f), read(f)) for f in iter_files(root)]
    items = []
    for rel, text in files:
        if rel.endswith('.ts'):
            items += [dict(x, file=rel) for x in ui_components(Path(rel), text)]
    for it in items:  # usos = archivos que lo usan
        pat = re.compile(_use_pattern(it))
        it['usos'] = sum(1 for rel, text in files if rel != it['file'] and pat.search(text))
    # Un wrapper se coloca por selector en templates. Sin usos por selector es una página (ruta),
    # el contenido de un MatDialog/MatBottomSheet o código muerto: no es un wrapper.
    no_wrappers = sum(1 for it in items if it['selector'] and not it['usos'])
    items = [it for it in items if not it['selector'] or it['usos']]
    libs = {}
    for d in [root if root.is_dir() else root.parent, *root.parents]:
        pkg = d / 'package.json'
        if pkg.is_file():
            data = json.loads(read(pkg))
            deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
            libs = {lib: eq for lib, eq in LIBS.items() if lib in deps}
            break
    return items, libs, no_wrappers


def print_inventory(items, libs, no_wrappers):
    groups = [('REIMPLEMENTA', 'Reimplementa algo que Angular Material ya ofrece → candidato a reemplazar'),
              ('WRAPPER', 'Envuelve Angular Material → decide si aporta valor'),
              ('SIN-EQUIVALENTE', 'Sin equivalente en Angular Material → mantener')]
    for tipo, title in groups:
        group = sorted((i for i in items if i['tipo'] == tipo), key=lambda i: -i['usos'])
        if group:
            print(f'{title} ({len(group)}):')
        for i in group:
            mats = i['material']
            extra = f"  usa: {', '.join(mats[:6])}{' …' if len(mats) > 6 else ''}" if mats else ''
            extra += '  [posible pass-through]' if i['delgado'] else ''
            extra += f"  → {i['equivalente']}" if i['equivalente'] else ''
            print(f"  {i['file']}:{i['line']}  {i['nombre']}  usos: {i['usos']}{extra}")
    if libs:
        print('Librerías de UI con equivalente en Angular Material:')
        for lib, eq in libs.items():
            print(f'  {lib} → {eq}')
    if not items and not libs:
        print('Sin componentes UI propios reconocibles por nombre.')
    if no_wrappers:
        print(f'({no_wrappers} componente(s) con nombre de UI no se usan por selector: páginas, contenido de '
              'diálogos o código muerto; no son wrappers.)')


def material_version(start):
    """(usa_material, major|None) buscando hacia arriba node_modules y package.json."""
    for d in [start, *start.parents]:
        try:
            mod = d / 'node_modules/@angular/material/package.json'
            if mod.is_file():
                return True, int(json.loads(mod.read_text())['version'].split('.')[0])
            pkg = d / 'package.json'
            if pkg.is_file():
                data = json.loads(pkg.read_text())
                spec = {**data.get('dependencies', {}), **data.get('devDependencies', {})}.get('@angular/material')
                if spec:
                    m = re.search(r'\d+', spec)
                    return True, int(m.group()) if m else None
        except (OSError, ValueError, KeyError):
            continue
    return False, None


def iter_files(root):
    if root.is_file():
        yield root
        return
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for n in files:
            if n.endswith(('.html', '.ts')) and not n.endswith(('.spec.ts', '.d.ts')):
                yield Path(dirpath) / n


def read(path):
    return path.read_text(encoding='utf-8', errors='replace')


def edited_ranges(ti, text):
    if 'content' in ti:  # Write
        return [(1, text.count('\n') + 1)]
    news = [e.get('new_string', '') for e in ti.get('edits', [])] or [ti.get('new_string', '')]
    out = []
    for new in filter(None, news):
        i = text.find(new)
        while i != -1:
            start = text.count('\n', 0, i) + 1
            out.append((start, start + new.count('\n')))
            i = text.find(new, i + 1)
    return out


def hook(event):
    ti = event.get('tool_input') or {}
    path = Path(ti.get('file_path') or '')
    if path.suffix not in ('.html', '.ts') or path.name.endswith(('.spec.ts', '.d.ts')) or not path.is_file():
        return
    uses, major = material_version(path.parent)
    if not uses:
        return
    text = read(path)
    ranges = edited_ranges(ti, text)
    hits = [f for f in audit_source(path, text, major)
            if any(s <= hi and e >= lo for s, e in f['spans'] for lo, hi in ranges)]
    if 'content' in ti and path.suffix == '.ts':  # componente nuevo (o reescrito) que reimplementa Material
        lines = text.splitlines()
        for it in ui_components(path, text):
            f = {'line': it['line'], 'spans': [(it['line'], it['line'])], 'sev': 'WARN', 'rule': 'reimplementa-material',
                 'msg': f"{it['nombre']} parece reimplementar {it['equivalente']}: usa el componente de Angular "
                        'Material (o un wrapper existente del proyecto) salvo que no cubra un requisito real. '
                        'Si es una página o un componente de feature (no una pieza de UI reutilizable), ignora el aviso.'}
            if it['tipo'] == 'REIMPLEMENTA' and not ignored(lines, f):
                hits.append(f)
    if not hits:
        return
    body = '\n'.join(f"- L{f['line']} {f['sev']} {f['rule']}: {f['msg']}" for f in hits)
    msg = (f'mat-guidelines (skill angular-material-guidelines) en {path}:\n{body}\n'
           'Corrige los ERROR. En las WARN corrige o, si la regla no aplica aquí, agrega en la línea anterior '
           '`mat-guidelines-ignore: <regla> — motivo` como comentario (`<!-- -->` en HTML, `//` en TS).')
    if any(f['sev'] == 'ERROR' for f in hits):
        out = {'decision': 'block', 'reason': msg}
    else:
        out = {'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': msg}}
    print(json.dumps(out, ensure_ascii=False))


def selftest():
    tpl = '''
<button matIconButton><mat-icon>edit</mat-icon></button>
<button matIconButton aria-label="Editar"><mat-icon>edit</mat-icon></button>
<button matButton="filled" routerLink="/x">Ir</button>
<a matButton (click)="go()">Acción</a>
<button matButton="filled">Guardar</button>
<input matInput>
<mat-form-field><mat-label>Ok</mat-label><input matInput></mat-form-field>
<mat-chip-option>Sola</mat-chip-option>
<mat-form-field><mat-select><mat-option value="a">A</mat-option><mat-option value="b">B</mat-option></mat-select></mat-form-field>
<mat-form-field><mat-select>@for (o of opts; track o) {<mat-option [value]="o">{{o}}</mat-option>}</mat-select></mat-form-field>
<form (ngSubmit)="save()"><mat-slide-toggle>Activo</mat-slide-toggle></form>
<mat-dialog-actions><button matButton>A</button><button matButton>B</button><button matButton>C</button></mat-dialog-actions>
<span matTooltip="info">?</span>
<!-- mat-guidelines-ignore: tooltip-no-enfocable — demo -->
<span matTooltip="ok">?</span>
<button mat-flat-button (click)="x = a > b">Legacy</button>
<ng-template><mat-dialog-actions><button matButton="filled">Confirmar</button></mat-dialog-actions></ng-template>
'''
    got = Counter(f['rule'] for f in audit_source(Path('t.html'), tpl, 20))
    assert got == Counter({'icon-button-sin-label': 1, 'button-navega': 1, 'a-sin-destino': 1, 'control-sin-form-field': 1,
                           'chip-sin-contenedor': 1, 'select-pocas-opciones': 1, 'slide-toggle-en-form-con-submit': 1,
                           'dialog-mas-de-2-acciones': 1, 'tooltip-no-enfocable': 1, 'boton-legacy': 1,
                           'multiples-filled': 1}), got
    old = Counter(f['rule'] for f in audit_source(Path('t.html'), tpl, 19))
    assert old['api-boton-no-disponible'] == 9 and not old['boton-legacy'], old
    ts = 'import x;\n@Component({\n  template: `\n    <button matIconButton></button>`\n})'
    assert [f['line'] for f in audit_source(Path('c.ts'), ts, 20)] == [4]
    assert edited_ranges({'new_string': '<b>\n</b>'}, 'a\n<b>\n</b>\nc') == [(2, 3)]
    comps = '''
@Component({ selector: 'app-modal', template: `<div class="backdrop"><ng-content /></div>` })
export class ModalComponent {}
@Component({ selector: 'app-button', template: `<button mat-flat-button><ng-content /></button>` })
export class ButtonComponent {}
@Component({ selector: 'app-tabla-productos', template: `<table><tr><td>x</td></tr></table>` })
export class TablaProductosComponent {}
@Component({ selector: 'app-user-avatar', template: `<img [src]="url">` })
export class UserAvatarComponent {}
@Component({ selector: 'app-product-page', template: `<mat-card></mat-card>` })
export class ProductPageComponent {}
@Directive({ selector: '[appTooltip]' })
export class TooltipDirective {}
@Injectable({ providedIn: 'root' })
export class ToastService { show() { document.body.appendChild(el); } }
@Injectable({ providedIn: 'root' })
export class MenuService { items = []; }
'''
    got = {i['nombre']: (i['tipo'], i['equivalente'], i['delgado']) for i in ui_components(Path('x.ts'), comps)}
    assert got == {'<app-modal>': ('REIMPLEMENTA', 'MatDialog', False),
                   '<app-button>': ('WRAPPER', 'matButton / matIconButton / matFab', True),
                   '<app-tabla-productos>': ('REIMPLEMENTA', 'mat-table + matSort + mat-paginator', False),
                   '<app-user-avatar>': ('SIN-EQUIVALENTE', None, False),
                   '[appTooltip]': ('REIMPLEMENTA', 'matTooltip', False),
                   'ToastService': ('REIMPLEMENTA', 'MatSnackBar', False)}, got
    assert re.search(_use_pattern({'selector': '[appTooltip]'}), '<span appTooltip="x">')
    assert re.search(_use_pattern({'selector': 'app-button'}), '<app-button>Hola</app-button>')
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / 'package.json').write_text('{"dependencies": {"@angular/material": "^21.0.0", "ngx-toastr": "^19"}}')
        (root / 'ui.ts').write_text(comps)
        (root / 'page.html').write_text('<app-modal></app-modal><app-button>Ok</app-button>')
        cwd = os.getcwd()
        os.chdir(tmp)
        try:
            items, libs, no_wrappers = inventory(root)
        finally:
            os.chdir(cwd)
        assert {i['nombre']: i['usos'] for i in items} == {'<app-modal>': 1, '<app-button>': 1, 'ToastService': 0}, items
        assert no_wrappers == 3 and libs == {'ngx-toastr': 'MatSnackBar'}, (no_wrappers, libs)
    print('selftest OK')


def main(argv):
    if '--selftest' in argv:
        selftest()
        return 0
    if '--hook' in argv:
        try:
            hook(json.load(sys.stdin))
        except Exception:  # un hook roto nunca debe trabar la edición
            pass
        return 0
    paths = [a for a in argv if not a.startswith('--')] or ['.']
    if '--wrappers' in argv:
        for p in paths:
            items, libs, no_wrappers = inventory(Path(p).resolve())
            if '--json' in argv:
                print(json.dumps({'componentes': items, 'librerias': libs, 'no_wrappers': no_wrappers},
                                 ensure_ascii=False, indent=2))
            else:
                print_inventory(items, libs, no_wrappers)
        return 0
    results, majors = [], set()
    for p in paths:
        root = Path(p).resolve()
        _, major = material_version(root if root.is_dir() else root.parent)
        majors.add(major)
        for f in iter_files(root):
            text = read(f)
            if f.suffix == '.ts' and 'template' not in text:
                continue
            results += [dict(x, file=os.path.relpath(f)) for x in audit_source(f, text, major)]
    errors = sum(r['sev'] == 'ERROR' for r in results)
    if '--json' in argv:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(f"{r['file']}:{r['line']}  {r['sev']:<5} {r['rule']}: {r['msg']}")
        version = ', '.join(f'v{m}' if m else 'desconocida' for m in majors)
        print(f"\n{errors} error(es), {len(results) - errors} advertencia(s). Angular Material: {version}.")
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

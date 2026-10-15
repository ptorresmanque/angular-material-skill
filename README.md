**Español** · [English](README.en.md)

# angular-material-skill

Plugin para [Claude Code](https://claude.com/claude-code) que hace que Claude elija y use correctamente cada componente de [Angular Material](https://material.angular.dev), según las guías de uso de [Material Design 3](https://m3.material.io).

Por ejemplo: Dialog solo para decisiones críticas y Snackbar para confirmaciones; un solo botón `filled` por sección; Radio cuando hay pocas opciones; Slide Toggle solo si el cambio se aplica al instante; botones de ícono siempre con `aria-label`.

## Qué incluye

| Pieza | Qué hace |
|---|---|
| **Skill** `angular-material-guidelines` | Se activa sola al escribir, revisar o auditar código con `@angular/material`. Detecta la versión del proyecto (la API `matButton="filled"` solo existe desde la v20) y aplica las reglas de decisión. Incluye **lineamientos completos para los 37 componentes** del catálogo: cuándo usarlo, cuándo no (y qué usar en su lugar), API clave, reglas, accesibilidad y un ejemplo correcto. |
| **Auditor** `scripts/audit.py` | Revisa los templates `.html` y los templates inline de los `.ts`, y reporta incumplimientos con archivo y línea. Usa solo Python estándar, sin dependencias. |
| **Inventario de wrappers** `audit.py --wrappers` | Reconoce los componentes, directivas y servicios de UI propios (`app-button`, `app-modal`, `ToastService`…, con nombres en inglés o español) y las librerías de terceros (ngx-toastr, sweetalert2, ng-select…). Indica si cada uno envuelve Material, si reimplementa algo que Material ya trae o si no tiene equivalente, y cuántos archivos lo usan. |
| **Hook** `PostToolUse` | Después de cada edición que hace Claude, audita **solo las líneas modificadas**. Si hay un ERROR, Claude debe corregirlo antes de seguir. La deuda previa del archivo no se reporta. También avisa si Claude crea un componente que reimplementa uno de Material. Solo actúa en proyectos que dependen de `@angular/material`. |

## Instalación

### Como plugin (recomendado: skill + hook)

En Claude Code:

```
/plugin marketplace add ptorresmanque/angular-material-skill
/plugin install angular-material-skill@angular-material-skill
```

### Solo la skill (sin hook)

```bash
npx skills add ptorresmanque/angular-material-skill
```

También puedes copiar `skills/angular-material-guidelines/` a `~/.claude/skills/`. Si en ese caso quieres el hook, agrégalo a `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.claude/skills/angular-material-guidelines/scripts/audit.py --hook",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

**Requisito:** `python3` 3.8 o superior en el PATH.

## Uso

Se activa sola. Pídele a Claude cosas como "crea el formulario de producto", "agrega una confirmación antes de eliminar" o "audita la UI del proyecto".

También puedes ejecutar el auditor directamente:

```bash
python3 skills/angular-material-guidelines/scripts/audit.py ruta/al/proyecto/src
python3 skills/angular-material-guidelines/scripts/audit.py src --json
```

Termina con código de salida 1 si encuentra algún ERROR, así que sirve para CI.

### Inventario de wrappers

```bash
python3 skills/angular-material-guidelines/scripts/audit.py --wrappers src
```

```
Reimplementa algo que Angular Material ya ofrece → candidato a reemplazar (1):
  src/app/shared/modal/modal.component.ts:4  <app-modal>  usos: 12  → MatDialog
Envuelve Angular Material → decide si aporta valor (1):
  src/app/shared/button/button.component.ts:6  <app-button>  usos: 40  usa: mat-flat-button  [posible pass-through]  → matButton / matIconButton / matFab
Librerías de UI con equivalente en Angular Material:
  ngx-toastr → MatSnackBar
```

El script solo propone candidatos. La skill guía a Claude para decidir con cada uno si conviene reemplazarlo, mantenerlo (cuando encapsula lógica real) o reimplementarlo por dentro con Material manteniendo su API. Los componentes que nadie usa por selector (páginas o contenido de diálogos) no aparecen, porque no son wrappers.

### Reglas del auditor

**ERROR**: la documentación de Angular Material lo exige ("must", "always").

| Regla | Detecta |
|---|---|
| `icon-button-sin-label` | Botón de solo ícono sin `aria-label` |
| `button-navega` / `a-sin-destino` | `<button routerLink>` en vez de `<a>`, o `<a>` con estilo de botón sin destino |
| `api-boton-no-disponible` | API `matButton` usada en Angular Material < v20 |
| `control-sin-form-field` / `campo-sin-label` | Control fuera de `mat-form-field`, o campo sin `mat-label` |
| `progress-sin-label` · `paginator-sin-label` · `tabla-sin-label` · `lista-sin-label` · `chips-sin-label` · `tab-nav-sin-label` | Progress, paginador, tabla, `mat-nav-list`/`mat-selection-list`, chip-listbox/grid o `<nav mat-tab-nav-bar>` sin `aria-label` |
| `badge-sin-descripcion` | `matBadge` sin `matBadgeDescription` |
| `sort-sin-descripcion` | `mat-sort-header` sin `sortActionDescription` |
| `chip-sin-contenedor` / `chip-remove-en-icono` | Chip fuera de su contenedor, o `matChipRemove` fuera de un `<button>` |
| `icono-clicable` | `mat-icon` con `(click)` |
| `lista-multilinea-sin-titulo` | Ítem con `matListItemLine` sin `matListItemTitle` |
| `datepicker-sin-toggle` / `datepicker-sin-confirmacion` | Datepicker sin `mat-datepicker-toggle` o sin `mat-datepicker-actions` |

**WARN**: la documentación lo recomienda ("should", "avoid"), o la regla es heurística.

| Regla | Detecta |
|---|---|
| `multiples-filled` / `multiples-fab` | Más de un botón `filled` en la misma sección, o más de un FAB |
| `select-pocas-opciones` | `mat-select` con ≤ 5 opciones fijas |
| `slide-toggle-en-form-con-submit` | Switch en un formulario que se envía |
| `dialog-mas-de-2-acciones` | Diálogo con más de 2 acciones |
| `tooltip-no-enfocable` / `click-sin-teclado` | Tooltip o `(click)` en un elemento que no recibe foco (`span`, `mat-card`, `mat-chip`…) |
| `grupo-sin-label` · `stepper-sin-label` · `slider-sin-label` | Radio/button-toggle group, stepper o thumb de slider sin label |
| `control-anidado` | Control interactivo dentro de `mat-option`, `mat-list-option`, `mat-chip-option`, un header de expansion panel, un checkbox, radio o switch, un `mat-menu` sin `mat-menu-item`, o dentro de otro botón o enlace |
| `menu-trigger-no-boton` | `matMenuTriggerFor` en algo que no es un botón |
| `lista-interactiva` | `mat-list-item` clicable dentro de un `mat-list` común |
| `tree-control-legacy` | `mat-tree` con `treeControl` |
| `datepicker-sin-formato` | Campo de fecha sin `mat-hint` con el formato |
| `boton-legacy` | Selector antiguo (`mat-flat-button`…) en v20+ |
| `reimplementa-material` | Solo en el hook, al crear un componente: reimplementa algo que Material ya trae |

Si una WARN no aplica en un caso concreto, se silencia con un comentario en la línea anterior (`<!-- -->` en HTML, `//` en TS):

```html
<!-- mat-guidelines-ignore: select-pocas-opciones — filtro compacto en toolbar -->
```

Algunas decisiones no se pueden detectar de forma estática: usar un Dialog donde bastaba un Snackbar, información esencial escondida en un tooltip, tabs usadas como pasos o Grid List usada para maquetar. Esas las cubre la skill cuando Claude revisa el código.

## Estructura

```
.claude-plugin/          manifiesto del plugin y del marketplace
hooks/hooks.json         hook PostToolUse
skills/angular-material-guidelines/
├── SKILL.md                  reglas de decisión (núcleo) e índice
├── references/
│   ├── componentes/*.md      lineamientos de cada uno de los 37 componentes
│   ├── decisiones.md         tablas para elegir entre componentes parecidos
│   └── wrappers.md           equivalencias para componentes propios y librerías
└── scripts/audit.py          auditor (python3 audit.py --selftest)
```

## Fuentes

- [material.angular.dev](https://material.angular.dev/components/categories): catálogo y API de componentes.
- [m3.material.io](https://m3.material.io): guías de uso de Material Design 3.

Los umbrales numéricos ("≤ 5 opciones") son reglas prácticas de UX, no valores oficiales.

## Licencia

[MIT](LICENSE)

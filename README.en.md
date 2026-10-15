[Español](README.md) · **English**

# angular-material-skill

A [Claude Code](https://claude.com/claude-code) plugin that makes Claude pick and use the right [Angular Material](https://material.angular.dev) component for each situation, following the [Material Design 3](https://m3.material.io) usage guidelines.

For example: Dialog only for critical decisions and Snackbar for confirmations; a single `filled` button per section; Radio buttons when there are only a few options; Slide Toggle only when the change applies immediately; icon buttons always with an `aria-label`.

> The skill instructions and the audit messages are written in Spanish. Claude applies them no matter what language you work in.

## What's included

| Piece | What it does |
|---|---|
| **Skill** `angular-material-guidelines` | Activates on its own when writing, reviewing or auditing code that uses `@angular/material`. Detects the project's version (the `matButton="filled"` API only exists from v20) and applies the decision rules. Includes **full guidelines for all 37 components** in the catalog: when to use it, when not to (and what to use instead), key API, rules, accessibility and a correct example. |
| **Auditor** `scripts/audit.py` | Checks `.html` templates and inline templates in `.ts` files, and reports violations with file and line. Uses only the Python standard library, no dependencies. |
| **Wrapper inventory** `audit.py --wrappers` | Recognizes your own UI components, directives and services (`app-button`, `app-modal`, `ToastService`…, named in English or Spanish) and third-party UI libraries (ngx-toastr, sweetalert2, ng-select…). It tells you whether each one wraps Material, reimplements something Material already provides, or has no equivalent, and how many files use it. |
| **Hook** `PostToolUse` | After every edit Claude makes, audits **only the changed lines**. If there's an ERROR, Claude has to fix it before moving on. Existing issues elsewhere in the file are not reported. It also warns when Claude creates a component that reimplements a Material one. It only runs in projects that depend on `@angular/material`. |

## Installation

### As a plugin (recommended: skill + hook)

In Claude Code:

```
/plugin marketplace add ptorresmanque/angular-material-skill
/plugin install angular-material-skill@angular-material-skill
```

### Skill only (no hook)

```bash
npx skills add ptorresmanque/angular-material-skill
```

You can also copy `skills/angular-material-guidelines/` into `~/.claude/skills/`. If you want the hook in that case, add it to `~/.claude/settings.json`:

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

**Requirement:** `python3` 3.8 or later on your PATH.

## Usage

It activates on its own. Ask Claude things like "build the product form", "add a confirmation before deleting" or "audit the project's UI".

You can also run the auditor directly:

```bash
python3 skills/angular-material-guidelines/scripts/audit.py path/to/project/src
python3 skills/angular-material-guidelines/scripts/audit.py src --json
```

It exits with code 1 if it finds any ERROR, so you can use it in CI.

### Wrapper inventory

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

The output is in Spanish. Each item falls into one of three groups:
- **REIMPLEMENTA**: doesn't use Material, but Material provides the equivalent. Candidate to replace.
- **WRAPPER**: wraps Material. Decide whether it adds value.
- **SIN-EQUIVALENTE**: Material has no equivalent. Keep it.

The script only suggests candidates. The skill guides Claude to decide, for each one, whether to replace it, keep it (when it encapsulates real logic), or reimplement it internally with Material while keeping its API. Components nobody uses through their selector (routed pages or dialog content) aren't listed, because they aren't wrappers.

### Auditor rules

**ERROR**: required by the Angular Material docs ("must", "always").

| Rule | Detects |
|---|---|
| `icon-button-sin-label` | Icon-only button without `aria-label` |
| `button-navega` / `a-sin-destino` | `<button routerLink>` instead of `<a>`, or a button-styled `<a>` with no destination |
| `api-boton-no-disponible` | `matButton` API used with Angular Material < v20 |
| `control-sin-form-field` / `campo-sin-label` | Control outside `mat-form-field`, or a field without `mat-label` |
| `progress-sin-label` · `paginator-sin-label` · `tabla-sin-label` · `lista-sin-label` · `chips-sin-label` · `tab-nav-sin-label` | Progress indicator, paginator, table, `mat-nav-list`/`mat-selection-list`, chip listbox/grid or `<nav mat-tab-nav-bar>` without `aria-label` |
| `badge-sin-descripcion` | `matBadge` without `matBadgeDescription` |
| `sort-sin-descripcion` | `mat-sort-header` without `sortActionDescription` |
| `chip-sin-contenedor` / `chip-remove-en-icono` | Chip outside its container, or `matChipRemove` not on a `<button>` |
| `icono-clicable` | `mat-icon` with `(click)` |
| `lista-multilinea-sin-titulo` | Item with `matListItemLine` but no `matListItemTitle` |
| `datepicker-sin-toggle` / `datepicker-sin-confirmacion` | Datepicker without `mat-datepicker-toggle` or without `mat-datepicker-actions` |

**WARN**: recommended by the docs ("should", "avoid"), or a heuristic rule.

| Rule | Detects |
|---|---|
| `multiples-filled` / `multiples-fab` | More than one `filled` button in the same section, or more than one FAB |
| `select-pocas-opciones` | `mat-select` with ≤ 5 fixed options |
| `slide-toggle-en-form-con-submit` | Switch inside a form that gets submitted |
| `dialog-mas-de-2-acciones` | Dialog with more than 2 actions |
| `tooltip-no-enfocable` / `click-sin-teclado` | Tooltip or `(click)` on an element that can't receive focus (`span`, `mat-card`, `mat-chip`…) |
| `grupo-sin-label` · `stepper-sin-label` · `slider-sin-label` | Radio/button-toggle group, stepper or slider thumb without a label |
| `control-anidado` | Interactive control inside `mat-option`, `mat-list-option`, `mat-chip-option`, an expansion panel header, a checkbox, radio or switch, a `mat-menu` without `mat-menu-item`, or inside another button or link |
| `menu-trigger-no-boton` | `matMenuTriggerFor` on something that isn't a button |
| `lista-interactiva` | Clickable `mat-list-item` inside a plain `mat-list` |
| `tree-control-legacy` | `mat-tree` with `treeControl` |
| `datepicker-sin-formato` | Date field without a `mat-hint` showing the format |
| `boton-legacy` | Legacy selector (`mat-flat-button`…) on v20+ |
| `reimplementa-material` | Hook only, when creating a component: reimplements something Material already provides |

If a WARN doesn't apply in a specific case, silence it with a comment on the line above (`<!-- -->` in HTML, `//` in TS):

```html
<!-- mat-guidelines-ignore: select-pocas-opciones — compact filter in a toolbar -->
```

Some decisions can't be detected statically: using a Dialog where a Snackbar would do, essential information hidden in a tooltip, tabs used as steps, or Grid List used for page layout. The skill covers those when Claude reviews the code.

## Structure

```
.claude-plugin/          plugin and marketplace manifests
hooks/hooks.json         PostToolUse hook
skills/angular-material-guidelines/
├── SKILL.md                  decision rules (core) and index
├── references/
│   ├── componentes/*.md      guidelines for each of the 37 components
│   ├── decisiones.md         tables for choosing between similar components
│   └── wrappers.md           equivalences for custom components and libraries
└── scripts/audit.py          auditor (python3 audit.py --selftest)
```

## Sources

- [material.angular.dev](https://material.angular.dev/components/categories): component catalog and API.
- [m3.material.io](https://m3.material.io): Material Design 3 usage guidelines.

Numeric thresholds ("≤ 5 options") are practical UX rules of thumb, not official values.

## License

[MIT](LICENSE)

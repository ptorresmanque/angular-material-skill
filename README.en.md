[Español](README.md) · **English**

# angular-material-skill

A [Claude Code](https://claude.com/claude-code) plugin that makes Claude pick and use the right [Angular Material](https://material.angular.dev) component for each situation, following the [Material Design 3](https://m3.material.io) usage guidelines.

For example: Dialog only for critical decisions and Snackbar for confirmations; a single `filled` button per section; Radio buttons when there are only a few options; Slide Toggle only when the change applies immediately; icon buttons always with an `aria-label`.

> The skill instructions and the audit messages are written in Spanish. Claude applies them no matter what language you work in.

## What's included

| Piece | What it does |
|---|---|
| **Skill** `angular-material-guidelines` | Activates on its own when writing, reviewing or auditing code that uses `@angular/material`. Detects the project's version (the `matButton="filled"` API only exists from v20) and applies the decision rules for each component. |
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

| ERROR | WARN |
|---|---|
| `icon-button-sin-label`: icon-only button without `aria-label` | `multiples-filled`: more than one `filled` button in the same section |
| `button-navega`: `<button routerLink>` (navigation needs an `<a>`) | `multiples-fab`: more than one FAB on the screen |
| `a-sin-destino`: button-styled `<a>` with no `href`/`routerLink` | `select-pocas-opciones`: `mat-select` with ≤ 5 fixed options |
| `control-sin-form-field`: input, select or chip-grid outside `mat-form-field` | `slide-toggle-en-form-con-submit`: switch inside a form that gets submitted |
| `chip-sin-contenedor`: chip outside its `mat-chip-set`/`listbox`/`grid` | `dialog-mas-de-2-acciones`: dialog with more than 2 actions |
| `api-boton-no-disponible`: `matButton` used with Angular Material < v20 | `tooltip-no-enfocable`: tooltip on an element that can't receive focus |
| | `boton-legacy`: legacy selector (`mat-flat-button`…) on v20+ |
| | `reimplementa-material` (hook only, when creating a component): reimplements something Material already provides |

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
├── SKILL.md             decision rules (core)
├── references/componentes.md   full per-component table
└── scripts/audit.py     auditor (python3 audit.py --selftest)
```

## Sources

- [material.angular.dev](https://material.angular.dev/components/categories): component catalog and API.
- [m3.material.io](https://m3.material.io): Material Design 3 usage guidelines.

Numeric thresholds ("≤ 5 options") are practical UX rules of thumb, not official values.

## License

[MIT](LICENSE)

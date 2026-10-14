**Español** · [English](README.en.md)

# angular-material-skill

Plugin para [Claude Code](https://claude.com/claude-code) que hace que Claude elija y use correctamente cada componente de [Angular Material](https://material.angular.dev), según las guías de uso de [Material Design 3](https://m3.material.io).

Por ejemplo: Dialog solo para decisiones críticas y Snackbar para confirmaciones; un solo botón `filled` por sección; Radio cuando hay pocas opciones; Slide Toggle solo si el cambio se aplica al instante; botones de ícono siempre con `aria-label`.

## Qué incluye

| Pieza | Qué hace |
|---|---|
| **Skill** `angular-material-guidelines` | Se activa sola al escribir, revisar o auditar código con `@angular/material`. Detecta la versión del proyecto (la API `matButton="filled"` solo existe desde la v20) y aplica las reglas de decisión de cada componente. |
| **Auditor** `scripts/audit.py` | Revisa los templates `.html` y los templates inline de los `.ts`, y reporta incumplimientos con archivo y línea. Usa solo Python estándar, sin dependencias. |
| **Hook** `PostToolUse` | Después de cada edición que hace Claude, audita **solo las líneas modificadas**. Si hay un ERROR, Claude debe corregirlo antes de seguir. La deuda previa del archivo no se reporta. Solo actúa en proyectos que dependen de `@angular/material`. |

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

### Reglas del auditor

| ERROR | WARN |
|---|---|
| `icon-button-sin-label`: botón de solo ícono sin `aria-label` | `multiples-filled`: más de un botón `filled` en la misma sección |
| `button-navega`: `<button routerLink>` (para navegar se usa `<a>`) | `multiples-fab`: más de un FAB en la pantalla |
| `a-sin-destino`: `<a>` con estilo de botón sin `href`/`routerLink` | `select-pocas-opciones`: `mat-select` con ≤ 5 opciones fijas |
| `control-sin-form-field`: input, select o chip-grid fuera de `mat-form-field` | `slide-toggle-en-form-con-submit`: switch en un formulario que se envía |
| `chip-sin-contenedor`: chip fuera de su `mat-chip-set`/`listbox`/`grid` | `dialog-mas-de-2-acciones`: diálogo con más de 2 acciones |
| `api-boton-no-disponible`: `matButton` usado en Angular Material < v20 | `tooltip-no-enfocable`: tooltip en un elemento que no recibe foco |
| | `boton-legacy`: selector antiguo (`mat-flat-button`…) en v20+ |

Si una WARN no aplica en un caso concreto, se silencia con un comentario en la línea anterior:

```html
<!-- mat-guidelines-ignore: select-pocas-opciones — filtro compacto en toolbar -->
```

Algunas decisiones no se pueden detectar de forma estática: usar un Dialog donde bastaba un Snackbar, información esencial escondida en un tooltip, tabs usadas como pasos o Grid List usada para maquetar. Esas las cubre la skill cuando Claude revisa el código.

## Estructura

```
.claude-plugin/          manifiesto del plugin y del marketplace
hooks/hooks.json         hook PostToolUse
skills/angular-material-guidelines/
├── SKILL.md             reglas de decisión (núcleo)
├── references/componentes.md   tabla completa por componente
└── scripts/audit.py     auditor (python3 audit.py --selftest)
```

## Fuentes

- [material.angular.dev](https://material.angular.dev/components/categories): catálogo y API de componentes.
- [m3.material.io](https://m3.material.io): guías de uso de Material Design 3.

Los umbrales numéricos ("≤ 5 opciones") son reglas prácticas de UX, no valores oficiales.

## Licencia

[MIT](LICENSE)

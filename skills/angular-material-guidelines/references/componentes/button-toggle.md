# Button Toggle — `mat-button-toggle-group`

Botones conmutables agrupados; equivale al *segmented button* de M3. Fuentes: [Angular Material](https://material.angular.dev/components/button-toggle/overview) · [M3](https://m3.material.io/components/segmented-buttons/guidelines).

## Úsalo cuando
- Hay 2–5 opciones **opuestas** que siempre deben verse y que cambian una vista o un filtro: lista/cuadrícula, día/semana/mes.
- Es una barra de formato con selección múltiple (`multiple`): negrita, cursiva, subrayado.

## No lo uses cuando
- Es un único encendido/apagado: usa `mat-slide-toggle`.
- Hay más de 5 opciones: usa `mat-select` o `mat-chip-listbox`.
- Son acciones y no estados: usa botones.
- Es navegación entre secciones de contenido: usa `mat-tab-group`.

## API clave
- Por defecto se elige uno solo, y `value` y `ngModel` reflejan esa opción.
- Con `multiple` funciona como checkboxes: el grupo no tiene `value` y no admite `ngModel`.
- `appearance`: por defecto sigue M3. `legacy` usa el estilo anterior. Se configura de forma global con `MAT_BUTTON_TOGGLE_DEFAULT_OPTIONS`.
- `vertical`: orientación vertical.
- `hideSingleSelectionIndicator` / `hideMultipleSelectionIndicator`: ocultan el check, pero no conviene hacerlo.

## Reglas
- Usa etiquetas cortas.
- Todas las opciones llevan solo texto, o todas ícono + texto. No las mezcles.
- Si una opción debe venir marcada, márcala desde el inicio. Un grupo exclusivo sin selección confunde.

## Accesibilidad
- El grupo tiene `role="group"`. Dale un label que describa el conjunto ("Estilo de fuente"). `[auditor: grupo-sin-label]`
- Si un toggle es solo un ícono, ponle `aria-label`. Se enlaza como input `[aria-label]`, sin el prefijo `attr.`.

## Ejemplo
```html
<mat-button-toggle-group [(value)]="vista" aria-label="Vista de productos">
  <mat-button-toggle value="lista">Lista</mat-button-toggle>
  <mat-button-toggle value="grilla">Cuadrícula</mat-button-toggle>
</mat-button-toggle-group>
```

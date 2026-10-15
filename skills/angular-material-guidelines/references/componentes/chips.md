# Chips — `mat-chip-set`, `mat-chip-listbox`, `mat-chip-grid`

Elementos compactos para mostrar etiquetas, filtrar o ingresar varios valores. Fuentes: [Angular Material](https://material.angular.dev/components/chips/overview) · [M3](https://m3.material.io/components/chips/guidelines).

## Elige el patrón según la interacción

| Necesidad | Contenedor + chip | Tipo de chip en M3 |
|---|---|---|
| Mostrar etiquetas no interactivas (tags) | `mat-chip-set` + `mat-chip` | — |
| Filtrar o elegir entre opciones visibles | `mat-chip-listbox` + `mat-chip-option` (`multiple` para filtros acumulables) | Filter |
| Ingresar varios valores (destinatarios, keywords) | `mat-chip-grid` + `mat-chip-row` + `<input matChipInputFor>` | Input |
| Acciones sugeridas ("Agregar al calendario") | Botones (`matButton="outlined"`) | Assist / suggestion |

El chip estático (`mat-chip`) **no es interactivo**. No le pongas `(click)`. `[auditor: click-sin-teclado]`

## No lo uses cuando
- Las opciones son excluyentes y quieres un control compacto con estado: usa `mat-button-toggle-group`.
- Son muchas opciones: usa `mat-select` o un autocomplete con chips.
- Es contenido extenso: un chip lleva una o dos palabras.

## API clave
- Cada chip va siempre dentro de su contenedor. `[auditor: chip-sin-contenedor]`
- Íconos:
  - `matChipAvatar` adelante.
  - `matChipTrailingIcon` o `matChipRemove` atrás.
  - Con `matChipRemove` hay que implementar el output `(removed)`.
- Chips editables: `editable` en `mat-chip-row` + `(edited)`.
- Separadores de entrada: `matChipInputSeparatorKeyCodes`. `MAT_CHIPS_DEFAULT_OPTIONS` los configura de forma global.
- Con autocomplete: importa `MatAutocompleteModule` **antes** que `MatChipsModule`.

## Reglas
- Usa textos cortos.
- Los chips de filtro reflejan su estado con el check. No lo ocultes (`hideSingleSelectionIndicator`).
- Muestra el `input` como hermano de `mat-chip-grid`, ambos dentro de `mat-form-field`.

## Accesibilidad
- `mat-chip-listbox` y `mat-chip-grid` llevan siempre `aria-label` o `aria-labelledby`. `[auditor: chips-sin-label]`
- El input del chip-grid también lleva `aria-label`.
- `matChipRemove` va siempre en un `<button>`, nunca en un `mat-icon`. `[auditor: chip-remove-en-icono]`
- No pongas controles interactivos dentro de `mat-chip-option`. Única excepción: el botón `matChipRemove`. `[auditor: control-anidado]`
- Chips editables: explica cómo editarlos con `aria-description` ("Presiona Enter para editar").
- Para mostrar etiquetas estáticas como lista, usa `role="list"` en `mat-chip-set` y `role="listitem"` en cada `mat-chip`.

## Ejemplo
```html
<mat-chip-listbox multiple aria-label="Filtrar por talla" [(ngModel)]="tallas">
  @for (t of ['S', 'M', 'L', 'XL']; track t) {
    <mat-chip-option [value]="t">{{ t }}</mat-chip-option>
  }
</mat-chip-listbox>
```

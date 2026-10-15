# Select — `mat-select` / `<select matNativeControl>`

Control para elegir uno o varios valores de un conjunto de opciones. Fuente: [Angular Material](https://material.angular.dev/components/select/overview).

## Primero: ¿nativo o `mat-select`?
La documentación de Angular Material dice: **cuando sea posible, prefiere el `<select>` nativo**. Da la experiencia más accesible en más plataformas, y en móvil abre el selector del sistema.

| Necesitas… | Usa |
|---|---|
| Una opción, con texto simple | `<select matNativeControl>` dentro de `mat-form-field` |
| Selección múltiple, opciones con íconos o formato, `mat-select-trigger` personalizado, o el mismo estilo que el resto de los overlays | `mat-select` |

## Úsalo cuando
- Se elige entre muchas opciones (más de ~5) y hay poco espacio.

## No lo uses cuando
- Son ≤ 5 opciones y hay espacio: usa `mat-radio-group`, o `mat-button-toggle-group` si son opuestas. `[auditor: select-pocas-opciones]`
- Son muchísimas opciones o hay que buscar: usa `mat-autocomplete`.
- Son acciones: usa `mat-menu`.
- Son pocas opciones múltiples a la vista: usa checkboxes o `mat-chip-listbox`.

## API clave
- `mat-option` con `[value]`. Usa `mat-optgroup` para agrupar.
- `multiple` es fijo: no lo enlaces a un valor que cambie. Usa `@if` para alternar entre dos selects.
- `compareWith`: compara opciones cuando los valores son objetos.
- Una opción con `[value]="null"` permite volver a "ninguno". `canSelectNullableOptions` hace seleccionable la opción null.
- `mat-select-trigger`: personaliza el texto que se muestra en el campo.
- `panelClass`, `panelWidth`, `disableOptionCentering`, `typeaheadDebounceInterval`.
- `MAT_SELECT_CONFIG`: defaults globales.

## Reglas
- Siempre dentro de `mat-form-field` con `mat-label`. `[auditor: control-sin-form-field]` `[auditor: campo-sin-label]`
- Ordena las opciones de forma lógica (alfabética, frecuencia o magnitud) y agrupa con `mat-optgroup` cuando hay categorías.
- Para "sin selección", usa una opción explícita ("Todas", "Ninguna") en vez de dejar el campo vacío sin explicación.

## Accesibilidad
- Implementa el patrón combobox + listbox (ARIA 1.2).
- Siempre con label: `mat-label`, `aria-label` o `aria-labelledby`.
- No pongas botones ni checkboxes dentro de `mat-option`. `[auditor: control-anidado]`
- No ocultes el check de selección (`hideSingleSelectionIndicator`).

## Ejemplo
```html
<mat-form-field>
  <mat-label>País</mat-label>
  <select matNativeControl formControlName="pais">
    @for (p of paises; track p.codigo) { <option [value]="p.codigo">{{ p.nombre }}</option> }
  </select>
</mat-form-field>

<mat-form-field>
  <mat-label>Categorías</mat-label>
  <mat-select formControlName="categorias" multiple>
    @for (g of grupos; track g.nombre) {
      <mat-optgroup [label]="g.nombre">
        @for (c of g.categorias; track c.id) { <mat-option [value]="c.id">{{ c.nombre }}</mat-option> }
      </mat-optgroup>
    }
  </mat-select>
</mat-form-field>
```

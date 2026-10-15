# Autocomplete — `mat-autocomplete`

Input de texto con un panel de sugerencias que se filtra mientras se escribe. Fuente: [Angular Material](https://material.angular.dev/components/autocomplete/overview).

## Úsalo cuando
- Hay muchas opciones (más de ~15) y el usuario sabe qué busca: comunas, productos, usuarios.
- Las opciones vienen de una búsqueda remota.
- Se permite escribir un valor que no está en la lista. Si debe ser de la lista, usa `requireSelection`.

## No lo uses cuando
- Son pocas opciones fijas: usa `mat-select` o `mat-radio-group`.
- Hay que elegir varios valores: usa `mat-chip-grid` + autocomplete (ver `chips.md`).
- Son acciones y no valores: usa `mat-menu`.

## API clave
- `<input matInput [matAutocomplete]="auto">` + `<mat-autocomplete #auto>` con `mat-option`.
- `displayWith`: muestra un texto cuando el valor es un objeto.
- `requireSelection`: obliga a elegir una opción.
- `autoActiveFirstOption`: Enter elige la primera opción.
- `mat-optgroup`: agrupa opciones.
- `MAT_AUTOCOMPLETE_DEFAULT_OPTIONS`: defaults globales.

## Reglas
- Filtra mientras se escribe. En búsquedas remotas usa debounce (~300 ms) y cancela la petición anterior (`switchMap`).
- Sin resultados, muestra una opción deshabilitada "Sin resultados" en vez de un panel vacío.
- Si el filtro no busca por el inicio del texto, explica el criterio en un `mat-hint`.
- Si el valor es obligatorio de la lista, combina `requireSelection` con un `mat-error` que lo explique.
- Va dentro de `mat-form-field` como cualquier input. `[auditor: control-sin-form-field]`

## Accesibilidad
- Implementa el patrón combobox + listbox.
- Siempre con label: `mat-label`, `aria-label` o `aria-labelledby`. `[auditor: campo-sin-label]`
- No pongas botones, checkboxes ni enlaces dentro de `mat-option`. `[auditor: control-anidado]`
- No ocultes el check de la opción elegida (`hideSingleSelectionIndicator`): dificulta saber cuál está seleccionada.

## Ejemplo
```html
<mat-form-field>
  <mat-label>Comuna</mat-label>
  <input matInput [formControl]="comuna" [matAutocomplete]="auto">
  <mat-autocomplete #auto [displayWith]="nombreComuna" requireSelection>
    @for (c of filtradas(); track c.id) {
      <mat-option [value]="c">{{ c.nombre }}</mat-option>
    } @empty {
      <mat-option disabled>Sin resultados</mat-option>
    }
  </mat-autocomplete>
  <mat-error>Elige una comuna de la lista</mat-error>
</mat-form-field>
```

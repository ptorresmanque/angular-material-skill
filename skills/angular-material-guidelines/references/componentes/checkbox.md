# Checkbox — `mat-checkbox`

Casilla de verificación con estilo Material sobre un `<input type="checkbox">` nativo. Fuentes: [Angular Material](https://material.angular.dev/components/checkbox/overview) · [M3](https://m3.material.io/components/checkbox/guidelines).

## Úsalo cuando
- Se pueden elegir varias opciones de una lista.
- Es un booleano que se aplica **al enviar** el formulario ("Acepto los términos").
- Hace falta un "Seleccionar todo" sobre una lista: un checkbox padre con estado `indeterminate`.

## No lo uses cuando
- El cambio se aplica al instante (una preferencia): usa `mat-slide-toggle`.
- Solo se puede elegir una opción de varias: usa `mat-radio-group`.
- Es una acción: usa un botón.

## API clave
- `labelPosition`: `after` (por defecto) o `before`.
- `indeterminate`: estado mixto. Cualquier clic lo quita.
- `MAT_CHECKBOX_DEFAULT_OPTIONS.clickAction`: `check-indeterminate` (por defecto), `check` o `noop`.
- Compatible con `FormsModule`, `ReactiveFormsModule` y signal forms.

## Reglas
- Escribe labels en positivo y concretos: "Recibir novedades por correo", no "No recibir correos".
- Pon las listas de checkboxes en vertical, con un título para el grupo (`<fieldset>`/`<legend>` o `role="group"` con label).
- El checkbox padre pasa a `indeterminate` cuando sus hijos están mixtos.
- Si marcarlo es obligatorio (términos), usa el validador `requiredTrue` y explica el error con texto visible.

## Accesibilidad
- El label es el contenido del elemento. Si no hay texto visible, usa `aria-label` o `aria-labelledby` como input (`[aria-label]`, sin `attr.`).
- No pongas enlaces ni botones dentro del label: lee el documento en otra parte. `[auditor: control-anidado]`
- Si el checkbox muestra u oculta contenido, usa `aria-expanded` y `aria-controls`.

## Ejemplo
```html
<section role="group" aria-labelledby="t-notif">
  <h3 id="t-notif">Notificaciones</h3>
  <mat-checkbox [checked]="todas()" [indeterminate]="algunas()" (change)="marcarTodas($event.checked)">
    Todas
  </mat-checkbox>
  @for (n of canales; track n.id) {
    <mat-checkbox [(ngModel)]="n.activo">{{ n.nombre }}</mat-checkbox>
  }
</section>
```

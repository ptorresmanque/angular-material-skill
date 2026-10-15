# Radio Button — `mat-radio-group`, `mat-radio-button`

Elección de **una** opción entre varias visibles. Fuentes: [Angular Material](https://material.angular.dev/components/radio/overview) · [M3](https://m3.material.io/components/radio-button/guidelines).

## Úsalo cuando
- Se elige una sola opción entre pocas (≤ 5–7) y conviene verlas todas para compararlas: método de envío, tipo de cuenta.

## No lo uses cuando
- Son muchas opciones: usa `mat-select` o un autocomplete.
- Se pueden elegir varias: usa `mat-checkbox`.
- Es un único sí/no que se aplica al instante: usa `mat-slide-toggle`. Si se aplica al enviar, usa un checkbox.
- Son opciones opuestas que cambian una vista: usa `mat-button-toggle-group`.

## API clave
- `mat-radio-group` con `value`, `name` y `(change)`. Es compatible con formularios.
- `labelPosition` (`after` | `before`), `disabled`, `required`.
- `MAT_RADIO_DEFAULT_OPTIONS`: defaults globales.

## Reglas
- Pon siempre los radios dentro de un `mat-radio-group`: es más fácil usarlos solo con teclado. La excepción es cuando el DOM lo impide (por ejemplo, radios en celdas de una tabla).
- Lista vertical, ordenada de forma lógica (frecuencia, magnitud o alfabética).
- Preselecciona una opción razonable, salvo que necesites obligar a elegir de manera consciente.
- Usa labels cortos. Si hace falta, agrega texto de apoyo debajo, fuera del label interactivo.

## Accesibilidad
- Cada `mat-radio-group` lleva `aria-label` o `aria-labelledby` (el título de la pregunta). `[auditor: grupo-sin-label]`
- El label de cada radio es su contenido. Sin texto, usa `[aria-label]` como input (sin `attr.`).
- No pongas controles interactivos dentro del label. `[auditor: control-anidado]`

## Ejemplo
```html
<label id="lbl-envio">Método de envío</label>
<mat-radio-group aria-labelledby="lbl-envio" formControlName="envio" class="vertical">
  <mat-radio-button value="retiro">Retiro en tienda</mat-radio-button>
  <mat-radio-button value="domicilio">Despacho a domicilio</mat-radio-button>
  <mat-radio-button value="express">Express (24 h)</mat-radio-button>
</mat-radio-group>
```

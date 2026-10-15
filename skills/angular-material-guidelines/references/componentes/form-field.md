# Form Field — `mat-form-field`

Contenedor de un control de formulario: le agrega label, hint, error, prefijos y sufijos. Fuentes: [Angular Material](https://material.angular.dev/components/form-field/overview) · [M3](https://m3.material.io/components/text-fields/guidelines).

## Úsalo cuando
Siempre envuelve con él a `input`/`textarea` con `matInput`, `<select matNativeControl>`, `mat-select`, `mat-chip-grid`, los inputs del datepicker y del timepicker, y cualquier control propio que implemente `MatFormFieldControl`. `[auditor: control-sin-form-field]`

## No lo uses cuando
- El control es un checkbox, radio, slide toggle, slider o button toggle. Esos no son controles de form field.

## Apariencia
- `fill` (por defecto) u `outline`. Ofrecen la misma funcionalidad; la elección es visual.
  - M3: `outline` tiene menos peso visual y simplifica los formularios con muchos campos.
- Usa **una sola apariencia por región**. No mezcles las dos en el mismo formulario.
- Fíjala de forma global con `MAT_FORM_FIELD_DEFAULT_OPTIONS` en vez de repetir `appearance` en cada campo.

## API clave
- `mat-label`: el label flotante.
- `mat-hint`: texto de ayuda.
  - `align="start" | "end"`.
  - `hintLabel` es un atajo para el hint de inicio.
- `mat-error`: mensaje de error.
- Prefijos y sufijos:
  - Íconos: `matIconPrefix`, `matIconSuffix`.
  - Texto: `matTextPrefix`, `matTextSuffix`.
- `floatLabel`: `auto` o `always`.
- `hideRequiredMarker`: oculta el asterisco de obligatorio.
- `subscriptSizing="dynamic"`: el espacio del hint o error crece solo si hace falta.

## Reglas
- Siempre con `mat-label`. El `placeholder` es un ejemplo de formato, **no** un label. `[auditor: campo-sin-label]`
- Un `mat-error` por error, con texto que diga cómo corregirlo ("Ingresa un correo válido", no "Campo inválido").
- Muestra el formato esperado en `mat-hint` cuando no es obvio (fechas, RUT, teléfono).
- El ancho del campo debe insinuar el largo esperado del dato: un código postal no ocupa todo el ancho.
- Usa ícono de prefijo solo si ayuda a reconocer el campo (búsqueda, moneda). No lo pongas por decorar.

## Accesibilidad
- `mat-label` se asocia al control con un `<label for>`. Sin label flotante, el control necesita `aria-label`, `aria-labelledby` o `<label for>`.
- `mat-hint` y `mat-error` se agregan al `aria-describedby`. `mat-error` usa `aria-live="polite"`.
- No comuniques los errores solo con color: usa texto.
- Prefijos y sufijos de texto (`$`, `kg`): si aportan significado, inclúyelo en el `aria-label` del input. Si son decorativos, ponles `aria-hidden="true"`.

## Ejemplo
```html
<mat-form-field>
  <mat-label>Monto</mat-label>
  <span matTextPrefix aria-hidden="true">$&nbsp;</span>
  <input matInput type="number" formControlName="monto" aria-label="Monto en pesos">
  <mat-hint>Sin puntos ni decimales</mat-hint>
  <mat-error>Ingresa un monto mayor a 0</mat-error>
</mat-form-field>
```

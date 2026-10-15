# Input — `matInput`

Directiva que integra `<input>` y `<textarea>` nativos con `mat-form-field`. Fuentes: [Angular Material](https://material.angular.dev/components/input/overview) · [M3](https://m3.material.io/components/text-fields/guidelines).

## Úsalo cuando
- Hay texto libre, números, correos, teléfonos, contraseñas, URLs o búsquedas.
- Hay texto largo: usa `<textarea matInput>` con `cdkTextareaAutosize`.

## No lo uses cuando
- El valor sale de una lista cerrada: usa `mat-select` o `<select matNativeControl>`.
- Es una fecha o una hora: usa `mat-datepicker` o `mat-timepicker` (que también llevan `matInput`).
- Es un valor aproximado en un rango: usa `mat-slider`.
- Son varios valores sueltos: usa `mat-chip-grid`.

## API clave
- Tipos soportados: `color`, `date`, `datetime-local`, `email`, `month`, `number`, `password`, `search`, `tel`, `text`, `time`, `url`, `week`. Con otro tipo, `matInput` lanza un error.
- Admite todos los atributos nativos y las directivas de formularios: `formControl`, `ngModel` y signal forms.
- `errorStateMatcher`: controla cuándo se muestran los errores. Prefiere uno global (ver `core.md`).
- `cdkTextareaAutosize` con `cdkAutosizeMinRows` y `cdkAutosizeMaxRows`: el textarea crece con el contenido.

## Reglas
- Siempre dentro de `mat-form-field`. `[auditor: control-sin-form-field]`
- Usa el `type`, el `autocomplete` y el `inputmode` correctos: `type="email" autocomplete="email"`, `inputmode="numeric"` para RUT o códigos. En móvil, eso define el teclado.
- Muestra un contador para campos con largo máximo, con `mat-hint align="end"`: `{{ valor.length }}/200`.
- No valides mientras el usuario escribe por primera vez. Los errores aparecen al salir del campo o al enviar (es el comportamiento por defecto).

## Accesibilidad
- Toma el label del `mat-label` del form field. Sin él, necesita `aria-label`, `aria-labelledby` o `<label for>`. `[auditor: campo-sin-label]`
- `mat-hint` y `mat-error` se agregan al `aria-describedby`, y `aria-invalid` se actualiza solo.
- No dependas solo del color para los errores: el mensaje debe decir qué pasa ("Error: …" o un ícono más texto).

## Ejemplo
```html
<mat-form-field>
  <mat-label>Comentario</mat-label>
  <textarea matInput cdkTextareaAutosize cdkAutosizeMinRows="3" maxlength="200"
            formControlName="comentario"></textarea>
  <mat-hint align="end">{{ form.value.comentario?.length ?? 0 }}/200</mat-hint>
</mat-form-field>
```

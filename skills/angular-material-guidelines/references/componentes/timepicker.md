# Timepicker — `mat-timepicker`

Selección de la hora, escribiendo o eligiendo de una lista de opciones (Angular Material v19.1+). Fuentes: [Angular Material](https://material.angular.dev/components/timepicker/overview) · [M3](https://m3.material.io/components/time-pickers/guidelines).

## Úsalo cuando
- Hay que elegir una hora del día: reserva, horario de entrega.
- Hay que elegir fecha y hora: combínalo con `mat-datepicker` sobre el **mismo** control (la fecha guarda también la hora).

## No lo uses cuando
- Es una duración ("2 h 30 min"): usa inputs numéricos o un select.
- Hay pocas franjas fijas ("Mañana / Tarde"): usa `mat-radio-group` o `mat-button-toggle-group`.

## API clave
- `<input matInput [matTimepicker]="picker">` + `<mat-timepicker-toggle matIconSuffix [for]="picker">` + `<mat-timepicker #picker>`.
- `interval` (`'30m'`, `'1h'`, `90`) **u** `options` (una lista propia de `MatTimepickerOption`), nunca los dos.
- `matTimepickerMin` y `matTimepickerMax` en el input (también filtran las opciones de la lista), con los errores `matTimepickerMin`, `matTimepickerMax` y `matTimepickerParse`.
- Necesita un adaptador de fechas y formatos con `timeInput` y `timeOptionLabel` (ver `core.md`).

## Reglas
- Siempre dentro de `mat-form-field` con `mat-label`, y con `mat-error` para la hora inválida o fuera de rango. `[auditor: campo-sin-label]`
- Elige un `interval` acorde al negocio (15 o 30 min para reservas), así la lista no es eterna.
- Incluye el toggle para que la lista se pueda abrir sin escribir.
- Usa el formato de hora del locale (24 h en es-CL).

## Accesibilidad
- Implementa el patrón combobox + listbox. Toma el label del form field. Fuera de un form field, usa `ariaLabel` o `ariaLabelledby` en `mat-timepicker`.

## Ejemplo
```html
<mat-form-field>
  <mat-label>Hora de retiro</mat-label>
  <input matInput [matTimepicker]="hora" matTimepickerMin="09:00" matTimepickerMax="19:00" formControlName="retiro">
  <mat-timepicker-toggle matIconSuffix [for]="hora" />
  <mat-timepicker #hora interval="30m" />
  <mat-error>Elige una hora entre 09:00 y 19:00</mat-error>
</mat-form-field>
```

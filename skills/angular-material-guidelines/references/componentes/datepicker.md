# Datepicker — `mat-datepicker`, `mat-date-range-input`

Ingreso de fechas, escribiendo o eligiendo en un calendario. Fuentes: [Angular Material](https://material.angular.dev/components/datepicker/overview) · [M3](https://m3.material.io/components/date-pickers/guidelines).

## Úsalo cuando
- Hay que capturar una fecha (agendar, filtrar por fecha).
- Hay que capturar un rango (check-in/check-out, período de un reporte). Usa `mat-date-range-input` + `mat-date-range-picker`, no dos datepickers separados.

## No lo uses cuando
- Es una fecha lejana y conocida, como la de nacimiento. El datepicker sirve, pero permite escribirla y abre en `startView="multi-year"`.
- Es solo una hora: usa `mat-timepicker`. Para fecha y hora, combina ambos.
- Es un mes o año sin día: usa `startView="multi-year"` y cierra al elegir el mes (`monthSelected`), o un select.

## API clave
- `<input matInput [matDatepicker]="picker">` + `<mat-datepicker-toggle matIconSuffix [for]="picker">` + `<mat-datepicker #picker>`.
- Validación:
  - `min` / `max`: límites del rango permitido.
  - `[matDatepickerFilter]`: deshabilita días (por ejemplo, fines de semana).
  - Errores disponibles: `matDatepickerParse`, `matDatepickerMin`, `matDatepickerMax`, `matDatepickerFilter`.
- `startView` (`month` | `year` | `multi-year`), `startAt`.
- `<mat-datepicker-actions>` con `matDatepickerCancel` y `matDatepickerApply`: botones de confirmación.
- `touchUi`: calendario en diálogo para móvil.
- `mat-calendar`: calendario inline, sin input.
- Requiere un adaptador de fechas y un locale (ver `core.md`).

## Reglas
- Siempre comunica el formato ("DD-MM-AAAA") con un `mat-hint`. `[auditor: datepicker-sin-formato]`
- Siempre incluye el toggle: es la única forma de abrir el calendario para usuarios móviles de lectores de pantalla, y en ChromeOS el atajo Alt+↓ no llega. `[auditor: datepicker-sin-toggle]`
- Incluye los botones de confirmación (`mat-datepicker-actions`): la documentación pide habilitarlos siempre, para que quien usa tecnologías de asistencia confirme su elección. `[auditor: datepicker-sin-confirmacion]`
- Explica con `mat-error` el motivo de cada error (fecha inválida, fuera de rango).
- Para rangos, usa `comparisonStart`/`comparisonEnd` si hay que mostrar un período de comparación.

## Accesibilidad
- El popup es un `role="dialog"` y el calendario un `role="grid"` con navegación por teclado completa.
- El input necesita un label (`mat-label`). `[auditor: campo-sin-label]`

## Ejemplo
```html
<mat-form-field>
  <mat-label>Fecha de entrega</mat-label>
  <input matInput [matDatepicker]="picker" [min]="hoy" formControlName="entrega">
  <mat-hint>DD-MM-AAAA</mat-hint>
  <mat-datepicker-toggle matIconSuffix [for]="picker" />
  <mat-datepicker #picker>
    <mat-datepicker-actions>
      <button matButton matDatepickerCancel>Cancelar</button>
      <button matButton="filled" matDatepickerApply>Aplicar</button>
    </mat-datepicker-actions>
  </mat-datepicker>
  <mat-error>Ingresa una fecha válida desde hoy</mat-error>
</mat-form-field>
```

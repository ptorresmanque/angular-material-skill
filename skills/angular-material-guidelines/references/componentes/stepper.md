# Stepper — `mat-stepper`

Flujo tipo asistente que divide una tarea en pasos ordenados. Fuente: [Angular Material](https://material.angular.dev/components/stepper/overview).

## Úsalo cuando
- Hay un proceso **secuencial**, con validación entre pasos y un orden lógico: checkout, onboarding, alta de un registro complejo.

## No lo uses cuando
- Las secciones no tienen orden y se recorren libremente: usa `mat-tab-group`.
- Es un formulario corto (1 paso con pocos campos): un formulario simple basta.
- Son secciones opcionales de un formulario largo: usa `mat-expansion-panel`.

## API clave
- `orientation`: `horizontal` (por defecto) o `vertical`. Con `labelPosition` y `headerPosition`.
- `linear` + `[stepControl]` en cada `mat-step`: no se avanza si el paso es inválido.
- Cada `mat-step` admite `label` o `<ng-template matStepLabel>`, y además `optional`, `editable`, `completed` y `hasError` / `errorMessage`.
- Botones de navegación: `matStepperNext` y `matStepperPrevious`. `stepper.reset()` reinicia el flujo.
- Contenido diferido: `<ng-template matStepContent>`.
- `STEPPER_GLOBAL_OPTIONS`:
  - `showError`: muestra el error en el encabezado del paso.
  - `displayDefaultIndicatorType`.
- Íconos de paso propios: `matStepperIcon`. Textos traducidos: `MatStepperIntl`.

## Reglas
- Usa entre 3 y 6 pasos con labels cortos y descriptivos ("Datos", "Envío", "Pago").
- En cada paso, una acción principal ("Siguiente" filled o tonal) y "Atrás" como text. El último paso confirma ("Pagar", "Crear cuenta").
- Usa `linear` cuando cada paso depende del anterior.
- Si un paso no se puede rehacer después de completarlo (por ejemplo, un pago), usa `editable="false"`.
- Usa orientación vertical en pantallas chicas: cambia `orientation` con `BreakpointObserver`.
- Al final, muestra un resumen antes de confirmar.

## Accesibilidad
- Se trata como tabs: `role="tablist"`, `tab` y `tabpanel`.
- El stepper y cada paso llevan `aria-label` o `aria-labelledby`. `[auditor: stepper-sin-label]`
- Si un error impide avanzar, comunícalo a la tecnología asistiva con `mat-error` dentro de `mat-form-field` o una región live. En steppers no lineales, anuncia los errores al salir del paso.

## Ejemplo
```html
<mat-stepper linear [orientation]="esMovil() ? 'vertical' : 'horizontal'" aria-label="Proceso de compra">
  <mat-step [stepControl]="datos" label="Datos" aria-label="Paso 1: datos">
    <form [formGroup]="datos">…
      <button matButton="filled" matStepperNext type="button">Siguiente</button>
    </form>
  </mat-step>
  <mat-step [stepControl]="pago" label="Pago" [editable]="false" aria-label="Paso 2: pago">…</mat-step>
</mat-stepper>
```

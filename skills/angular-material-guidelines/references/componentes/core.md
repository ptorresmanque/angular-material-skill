# Core — `@angular/material/core`

Piezas compartidas por otros componentes; casi nunca se usan solas. Fuente: [Angular Material](https://material.angular.dev/components/core/overview).

## Qué contiene y cómo usarlo
- **`mat-option` / `mat-optgroup`:** las opciones de `mat-select`, `mat-autocomplete` y `mat-timepicker`. Agrupa con `mat-optgroup label="…"` cuando hay más de ~10 opciones en categorías naturales.
- **Adaptador de fechas:** el datepicker y el timepicker lo necesitan. Provéelo **una sola vez** en la configuración de la app:
  - `provideNativeDateAdapter()`.
  - `provideMomentDateAdapter()`, `provideLuxonDateAdapter()` o `provideDateFnsAdapter()`, si necesitas parseo y zonas horarias más robustos.
- **`MAT_DATE_LOCALE` / `MAT_DATE_FORMATS`:** fija el locale del proyecto (por ejemplo `'es-CL'`) y un formato de entrada único para toda la app.
- **`ErrorStateMatcher`:** define cuándo se muestran los errores. Para que sea igual en toda la app, provéelo de forma global (`{ provide: ErrorStateMatcher, useClass: ShowOnDirtyErrorStateMatcher }`) en vez de configurarlo campo por campo.
- **Theming:** usa `mat.theme(...)`, `mat.theme-overrides` y `mat.<componente>-overrides` en un solo archivo de estilos globales. No sobrescribas clases internas `.mdc-*` ni `.mat-mdc-*`: cambian entre versiones.
- **`MatRipple` y el pseudo-checkbox:** ver `ripple.md`.

## Reglas
- No mezcles adaptadores de fecha en la misma app.
- Usa un solo locale y un solo formato de fecha. Comunica el formato en los campos (ver `datepicker.md`).
- Personaliza con tokens y overrides, no con CSS que apunte a la estructura interna.

## Ejemplo
```ts
// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideNativeDateAdapter(),
    { provide: MAT_DATE_LOCALE, useValue: 'es-CL' },
    { provide: ErrorStateMatcher, useClass: ShowOnDirtyErrorStateMatcher },
    { provide: MAT_FORM_FIELD_DEFAULT_OPTIONS, useValue: { appearance: 'outline' } },
  ],
};
```

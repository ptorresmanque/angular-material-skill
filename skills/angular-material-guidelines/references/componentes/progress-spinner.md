# Progress Spinner — `mat-progress-spinner`, `mat-spinner`

Indicador circular de progreso o actividad. Fuentes: [Angular Material](https://material.angular.dev/components/progress-spinner/overview) · [M3](https://m3.material.io/components/progress-indicators/guidelines).

## Úsalo cuando
- La carga ocurre en un espacio compacto y centrado: dentro de un botón (con `showProgress`), en una card, en un panel o al cargar más ítems.
- Aplican las mismas esperas que en `progress-bar.md`: nada bajo 200 ms; indeterminate entre 200 ms y 5 s; determinate sobre 5 s.

## No lo uses cuando
- Carga la página o una sección grande: usa una `mat-progress-bar` en el borde superior, o skeletons.
- No bloquees toda la pantalla con un overlay y un spinner para cargas cortas. Deja ver y usar lo que ya está cargado.
- Cargan varios elementos: usa un solo indicador para el grupo.

## API clave
- `mode`: `determinate` (por defecto) con `value` de 0 a 100, o `indeterminate`. `<mat-spinner>` es un alias del modo indeterminate.
- `diameter`, `strokeWidth`.
- `MAT_PROGRESS_SPINNER_DEFAULT_OPTIONS`: defaults globales.

## Reglas
- Céntralo en el elemento que carga.
- Usa un tamaño acorde al contenedor: unos 20 px en botones y 40–48 px en paneles.
- En botones, usa `showProgress` + `progressIndicator` en vez de reemplazar el botón (ver `button.md`).
- Usa el mismo tipo de indicador para el mismo proceso en toda la app.

## Accesibilidad
- Tiene `role="progressbar"`. Siempre lleva `aria-label` o `aria-labelledby`. `[auditor: progress-sin-label]`
- No cambies `aria-valuemin` ni `aria-valuemax`.

## Ejemplo
```html
@if (cargandoMas()) {
  <mat-progress-spinner mode="indeterminate" diameter="40" aria-label="Cargando más resultados" />
}
```

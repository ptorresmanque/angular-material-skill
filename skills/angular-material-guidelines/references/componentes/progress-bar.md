# Progress Bar — `mat-progress-bar`

Indicador lineal de progreso o actividad. Fuentes: [Angular Material](https://material.angular.dev/components/progress-bar/overview) · [M3](https://m3.material.io/components/progress-indicators/guidelines).

## Cuándo mostrar un indicador (M3)

| Espera esperada | Qué mostrar |
|---|---|
| Menos de 200 ms | Nada; muestra el resultado directo |
| Entre 200 ms y 5 s | Un indicador de carga (indeterminate) |
| Más de 5 s | Un indicador de progreso (determinate) y, si se puede, deja que el usuario siga trabajando |

## Úsalo cuando
- Se conoce el porcentaje: subidas, descargas, procesamiento de un lote (`mode="determinate"`).
- Carga una vista o sección completa: una barra `indeterminate` en el borde superior del contenedor (página, card, tabla).

## No lo uses cuando
- La carga ocurre en un espacio chico o centrado (un botón, un ícono): usa `mat-progress-spinner`.
- Cargan varios elementos a la vez: usa **un solo** indicador para el grupo, no uno por elemento.

## Modos
- `determinate`: el modo por defecto, con `value` de 0 a 100.
- `indeterminate`.
- `buffer`: usa `value` + `bufferValue`.
- `query`: precarga antes de que se conozca el avance.

## Reglas
- Ubícalo en el borde de un contenedor; los lineales funcionan mejor así.
- Pasa de `indeterminate` a `determinate` en cuanto se conozca el avance.
- Usa el mismo tipo de indicador para el mismo tipo de proceso en todo el producto.
- El valor determinate debe reflejar el avance real. No lo simules.

## Accesibilidad
- Tiene `role="progressbar"`. Siempre lleva `aria-label` o `aria-labelledby`. `[auditor: progress-sin-label]`
- No cambies `aria-valuemin` ni `aria-valuemax` (0 y 100).

## Ejemplo
```html
@if (cargando()) {
  <mat-progress-bar mode="indeterminate" aria-label="Cargando pedidos" />
}
<mat-progress-bar mode="determinate" [value]="avance()" aria-label="Subiendo archivo" />
```

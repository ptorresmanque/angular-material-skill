# Slider — `mat-slider`

Selección de un valor (o un rango) arrastrando sobre una pista. Fuentes: [Angular Material](https://material.angular.dev/components/slider/overview) · [M3](https://m3.material.io/components/sliders/guidelines).

## Úsalo cuando
- Se elige un valor **aproximado** en un rango y el efecto se ve de inmediato: volumen, brillo, intensidad de un filtro.
- Se elige un rango mínimo–máximo en un filtro: precio, fechas relativas. Usa un slider de rango.

## No lo uses cuando
- Se necesita un valor exacto: usa un `input type="number"`, o combina ambos.
- El rango es enorme y la precisión importa (por ejemplo, 0–100.000 con paso 1).
- El cambio no se ve hasta enviar: M3 pide que el efecto de un slider sea inmediato.

## API clave
- Un valor: `<mat-slider><input matSliderThumb></mat-slider>`.
- Rango: `<input matSliderStartThumb>` + `<input matSliderEndThumb>`.
- `min`, `max`, `step`, `disabled`.
- `discrete`: muestra la etiqueta con el valor al arrastrar. `displayWith` le da formato ("$10k").
- `showTickMarks`: muestra marcas en cada paso.

## Reglas
- Muestra el valor actual (con `discrete` o un texto al lado) y los extremos del rango.
- Usa `step` y `showTickMarks` cuando solo valen algunos valores.
- No uses sliders de rango en vertical (M3).

## Accesibilidad
- Cada thumb es un `<input type="range">`. Ponle `aria-label` o `aria-labelledby`. En un rango, ponlo en cada thumb ("Precio mínimo", "Precio máximo"). `[auditor: slider-sin-label]`
- La pista activa e inactiva deben tener un contraste de al menos 3:1 con el fondo, o usa marcas con ese contraste.

## Ejemplo
```html
<label id="lbl-precio">Precio</label>
<mat-slider min="0" max="200000" step="5000" discrete [displayWith]="formatoPrecio">
  <input matSliderStartThumb [(value)]="desde" aria-label="Precio mínimo">
  <input matSliderEndThumb [(value)]="hasta" aria-label="Precio máximo">
</mat-slider>
```

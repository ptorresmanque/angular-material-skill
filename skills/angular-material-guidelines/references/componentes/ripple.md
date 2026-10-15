# Ripples — `matRipple`

Efecto de onda que confirma un toque o un clic en el punto de contacto. Fuente: [Angular Material](https://material.angular.dev/components/ripple/overview).

## Úsalo cuando
- Un elemento clicable **propio** debe dar el mismo feedback que los componentes Material (por ejemplo, un mosaico seleccionable).

## No lo uses cuando
- El elemento ya es un componente Material: botones, list items, tabs y chips ya traen su ripple.
- El elemento no es interactivo: el ripple sugiere que se puede hacer clic.
- Quieres "volver accesible" un `<div>` clicable. El ripple es solo visual: usa un `<button>` o `<a>`.

## API clave
- `matRippleColor`, `matRippleCentered`, `matRippleUnbounded`, `matRippleRadius`.
- `matRippleDisabled`, `matRippleTrigger` (otro elemento dispara el efecto), `launch()` (efecto manual).
- `MAT_RIPPLE_GLOBAL_OPTIONS`: `disabled`, y `animation` con `enterDuration` y `exitDuration` para toda la app.

## Reglas
- Ponlo en el mismo elemento interactivo (`<button>`/`<a>`), no en un contenedor que no recibe foco.
- Respeta la preferencia de movimiento reducido: desactiva o acorta la animación con `MAT_RIPPLE_GLOBAL_OPTIONS` cuando `prefers-reduced-motion` está activo.
- En tablas nativas no funciona sobre `<tr>`: usa la variante de `mat-table` con `display: flex` si necesitas ripple en las filas.

## Ejemplo
```html
<button type="button" class="mosaico" matRipple (click)="elegir(plan)">
  {{ plan.nombre }}
</button>
```

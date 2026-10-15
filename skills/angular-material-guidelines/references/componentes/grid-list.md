# Grid List — `mat-grid-list`

Lista bidimensional de mosaicos con columnas y alto de fila fijos. Fuente: [Angular Material](https://material.angular.dev/components/grid-list/overview).

## Úsalo cuando
- Hay una galería de mosaicos visuales: fotos, portadas, íconos de apps, a veces con mosaicos que ocupan varias filas o columnas.

## No lo uses cuando
- Quieres maquetar una página o un formulario: usa CSS Grid o Flexbox. El grid list fija los altos y recorta el contenido.
- Son cards con contenido de largo variable: usa CSS Grid con `mat-card`.
- Son datos que se comparan: usa `mat-table`.

## API clave
- `cols`: número de columnas (obligatorio).
- `rowHeight`: alto de las filas.
  - Fijo (`'120px'`).
  - Proporción `ancho:alto` (`'4:3'`).
  - `'fit'`, que necesita alto en el contenedor.
- `gutterSize`: espacio entre mosaicos. Por defecto `1px`.
- `mat-grid-tile` con `colspan` y `rowspan`. `colspan` no puede superar `cols`.
- `mat-grid-tile-header` y `mat-grid-tile-footer`: títulos sobre el mosaico.

## Reglas
- Haz `cols` responsive con `BreakpointObserver` (por ejemplo 2 / 3 / 4 columnas).
- Si pones texto sobre imágenes (header/footer), asegura el contraste con el fondo semitransparente del header/footer.
- No pongas formularios dentro de los mosaicos.

## Accesibilidad
- Por defecto es decorativo y no tiene roles.
- Si presenta una lista de elementos no interactivos, usa `role="list"` en el grid y `role="listitem"` en cada mosaico.
- El contenido interactivo dentro de un mosaico (por ejemplo un enlace) necesita su propio tratamiento: usa `<a>` o `<button>` con label.

## Ejemplo
```html
<mat-grid-list [cols]="columnas()" rowHeight="4:3" gutterSize="8px" role="list">
  @for (foto of fotos; track foto.id) {
    <mat-grid-tile role="listitem">
      <a [routerLink]="['/fotos', foto.id]"><img [src]="foto.url" [alt]="foto.descripcion"></a>
      <mat-grid-tile-footer>{{ foto.titulo }}</mat-grid-tile-footer>
    </mat-grid-tile>
  }
</mat-grid-list>
```

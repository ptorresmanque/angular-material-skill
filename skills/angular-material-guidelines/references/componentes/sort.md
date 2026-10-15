# Sort Header — `matSort`, `mat-sort-header`

Encabezados de tabla que ordenan los datos. Fuente: [Angular Material](https://material.angular.dev/components/sort/overview).

## Úsalo cuando
- El usuario necesita ordenar una tabla por una columna (fecha, monto, nombre) para encontrar o comparar.

## No lo uses cuando
- La columna no tiene un orden con sentido (acciones, imágenes, descripciones largas). No la hagas ordenable.
- Los datos se ordenan solos de una forma fija y obvia.

## API clave
- `matSort` en la tabla. `mat-sort-header="id"` en cada encabezado ordenable (por defecto, el id es el de la columna).
- `matSortActive` y `matSortDirection`: orden inicial.
- `matSortStart` (`asc` | `desc`) y `matSortDisableClear` (evita el tercer estado sin orden).
- `(matSortChange)`: emite el `Sort` (`active`, `direction`).
- `MAT_SORT_DEFAULT_OPTIONS`: defaults globales.
- Con `MatTableDataSource`, `dataSource.sort = sort` ordena en el cliente. Con datos del servidor, pide el orden a la API.

## Reglas
- Muestra el orden inicial con sentido (por ejemplo, la fecha más reciente primero).
- Al cambiar el orden, vuelve el paginador a la página 0.
- Para fechas y montos, empieza en `desc` si es lo más útil.

## Accesibilidad
- Cada `mat-sort-header` lleva **siempre** `sortActionDescription` ("Ordenar por fecha"). El texto del encabezado describe la columna, no la acción. `[auditor: sort-sin-descripcion]`
- Los lectores de pantalla no anuncian el cambio de `aria-sort`. Anúncialo tú con `LiveAnnouncer` en `(matSortChange)`.
- Si hay muchas tablas, crea una directiva que aplique la descripción y el anuncio de forma consistente.

## Ejemplo
```html
<table mat-table [dataSource]="datos" matSort matSortActive="fecha" matSortDirection="desc"
       (matSortChange)="anunciar($event)" aria-label="Pedidos">
  <ng-container matColumnDef="fecha">
    <th mat-header-cell *matHeaderCellDef mat-sort-header sortActionDescription="Ordenar por fecha">Fecha</th>
    <td mat-cell *matCellDef="let p">{{ p.fecha | date }}</td>
  </ng-container>
  …
</table>
```
```ts
anunciar(s: Sort) {
  this.live.announce(s.direction ? `Ordenado por ${s.active}, ${s.direction === 'asc' ? 'ascendente' : 'descendente'}` : 'Orden quitado');
}
```

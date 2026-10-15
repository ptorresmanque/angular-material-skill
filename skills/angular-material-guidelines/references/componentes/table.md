# Table — `mat-table`

Tabla de datos con estilo Material, construida sobre la tabla del CDK. Fuente: [Angular Material](https://material.angular.dev/components/table/overview).

## Úsalo cuando
- Hay que comparar **varios atributos** entre filas: pedidos, usuarios, inventario.
- Se necesita ordenar, filtrar, paginar o seleccionar filas.

## No lo uses cuando
- Cada elemento tiene un solo atributo principal: usa `mat-list`.
- En móvil hay muchas columnas: muestra solo las esenciales, o cambia a una lista o a cards con `BreakpointObserver`.
- Se necesita edición inline masiva, agrupación o virtualización de miles de filas: considera un data grid especializado (ver `wrappers.md`).

## API clave
- Prefiere la tabla nativa `<table mat-table>`: admite `colspan`/`rowspan` y columnas que se ajustan al contenido.
- Columnas: `matColumnDef`, `mat-header-cell`/`*matHeaderCellDef`, `mat-cell`/`*matCellDef`. Filas: `mat-header-row` y `mat-row` con la lista de columnas.
- Datos:
  - En el cliente: `MatTableDataSource`, con `.filter`, `.sort` y `.paginator`.
  - En el servidor: un `DataSource` propio.
- Filas especiales:
  - Pie: `mat-footer-row` (por ejemplo, totales).
  - Sin datos: `*matNoDataRow`, para el estado vacío.
- Encabezados y columnas fijas: `sticky`, `stickyEnd`.
- `trackBy` / `track` para listas que cambian.

## Reglas
- Ordena las columnas por importancia; lo más identificador va a la izquierda.
- Alinea los números a la derecha, con el mismo formato y unidad en el encabezado. El texto va a la izquierda.
- Usa encabezados cortos. Haz ordenables solo las columnas que tiene sentido ordenar (ver `sort.md`).
- Siempre ten un estado vacío (`*matNoDataRow`) y uno de carga (una `mat-progress-bar` sobre la tabla).
- Acciones por fila: hasta 2 `matIconButton` con `aria-label`; si son más, un menú ⋮. La acción principal también puede ser un enlace en la celda identificadora.
- Selección: una columna de checkbox (`SelectionModel`) con un checkbox `indeterminate` en el encabezado ("Seleccionar todo").
- Con muchos datos, usa paginación o carga incremental (ver `paginator.md`).

## Accesibilidad
- Siempre lleva `aria-label` o `aria-labelledby` en la tabla. `[auditor: tabla-sin-label]`
- Tiene `role="table"` por defecto. Cambia a `grid` o `treegrid` solo si además implementas la navegación por teclado.

## Ejemplo
```html
<table mat-table [dataSource]="dataSource" matSort aria-label="Pedidos del mes">
  <ng-container matColumnDef="numero">
    <th mat-header-cell *matHeaderCellDef>N.º</th>
    <td mat-cell *matCellDef="let p"><a [routerLink]="['/pedidos', p.id]">{{ p.numero }}</a></td>
  </ng-container>
  <ng-container matColumnDef="total">
    <th mat-header-cell *matHeaderCellDef mat-sort-header sortActionDescription="Ordenar por total" class="num">Total ($)</th>
    <td mat-cell *matCellDef="let p" class="num">{{ p.total | number }}</td>
  </ng-container>
  <tr mat-header-row *matHeaderRowDef="columnas; sticky: true"></tr>
  <tr mat-row *matRowDef="let fila; columns: columnas"></tr>
  <tr class="mat-row" *matNoDataRow><td class="mat-cell" [attr.colspan]="columnas.length">Sin pedidos para este filtro</td></tr>
</table>
<mat-paginator [pageSizeOptions]="[10, 25, 50]" aria-label="Paginación de pedidos" />
```

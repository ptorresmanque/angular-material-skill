# Paginator — `mat-paginator`

Controles para navegar datos paginados; normalmente acompaña a una tabla. Fuente: [Angular Material](https://material.angular.dev/components/paginator/overview).

## Úsalo cuando
- Una tabla o lista supera las ~25–50 filas.
- Los datos vienen de una API paginada. Pagina en el servidor con `(page)` y `length`.

## No lo uses cuando
- Es un feed continuo (noticias, actividad): usa scroll infinito o `cdk-virtual-scroll-viewport`.
- Son pocos registros: muéstralos todos.

## API clave
- `length`: total de registros. `pageSize`: por defecto 50. `pageIndex`.
- `pageSizeOptions`: tamaños de página que el usuario puede elegir.
- `(page)`: emite un `PageEvent`.
- `showFirstLastButtons`, `hidePageSize`, `disabled`.
- `selectConfig`: configura el `mat-select` interno.
- `MatPaginatorIntl`: textos traducidos. `MAT_PAGINATOR_DEFAULT_OPTIONS`: defaults globales.
- Con `MatTableDataSource`, basta con `dataSource.paginator = paginator` para paginar en el cliente.

## Reglas
- Usa pocas opciones de tamaño: `[10, 25, 50]`.
- Vuelve a la página 0 cuando cambian el filtro o el orden.
- Muestra `showFirstLastButtons` cuando hay muchas páginas.
- Traduce los textos con un `MatPaginatorIntl` propio provisto a nivel de app ("Filas por página", "1 – 10 de 100").
- Ubícalo debajo de la tabla, alineado a la derecha (es lo esperado).

## Accesibilidad
- Tiene `role="group"`. **Debes** agregar un `aria-label` que diga qué pagina. `[auditor: paginator-sin-label]`
- Los labels de los botones internos se definen en `MatPaginatorIntl`.

## Ejemplo
```html
<mat-paginator [length]="total()" [pageSize]="25" [pageSizeOptions]="[10, 25, 50]"
               showFirstLastButtons (page)="cargar($event)" aria-label="Paginación de pedidos" />
```

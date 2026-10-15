# Card — `mat-card`

Contenedor de contenido y acciones sobre **un solo tema**. Fuentes: [Angular Material](https://material.angular.dev/components/card/overview) · [M3](https://m3.material.io/components/cards/guidelines).

## Úsalo cuando
- Hay unidades de contenido independientes y heterogéneas (texto, imagen, acciones) que sirven de entrada a un detalle: un producto, un artículo, un resumen en un dashboard.
- Hay colecciones de elementos así, mostradas en grilla, en lista vertical o en carrusel.

## No lo uses cuando
- El contenido se ordena bien con espacio, títulos o dividers. M3 pide no forzar contenido en cards.
- Es una lista homogénea de un atributo: usa `mat-list`.
- Hay que comparar varios atributos entre elementos: usa `mat-table`.
- Quieres maquetar la página o agrupar todo un formulario solo para darle fondo: usa el layout, no cards.
- Quieres poner una card dentro de otra: aplana la jerarquía o usa dividers.

## Variantes
- `appearance="raised"` (elevated, la opción por defecto), `outlined` o `filled`.
- Las tres tienen la misma funcionalidad, así que la elección es solo visual.
- Usa una variante consistente por contexto. El default global se configura con `MAT_CARD_CONFIG`.
  - **Elevated:** separa más del fondo que filled.
  - **Filled:** la de menor énfasis.
  - **Outlined:** tiene borde visible y es la de mayor énfasis.

## Estructura
`mat-card` no agrega padding. Usa sus secciones, que aplican el padding estándar:
- `mat-card-header`: contiene `mat-card-title`, `mat-card-subtitle` y opcionalmente `img mat-card-avatar`. Con `mat-card-title-group` puedes combinar título y subtítulo con una imagen (`matCardSmImage`, `matCardMdImage`, `matCardLgImage`, `matCardXlImage`).
- `img mat-card-image`: imagen a todo el ancho.
- `mat-card-content`: el contenido principal.
- `mat-card-actions`: los botones. `align="start"` (por defecto) o `align="end"`.
- `mat-card-footer`: pie anclado abajo.

## Reglas
- Jerarquía clara: título → subtítulo → texto de apoyo → acciones.
- Acciones dentro de `mat-card-actions`, con la jerarquía de botones: a lo más una principal. Las secundarias van como text o outlined, o en un menú overflow (⋮).
- Si toda la card lleva a un detalle, pon un `<a>` en el título (o en toda la card) en vez de `(click)` sobre `mat-card`. Un `(click)` en un elemento no enfocable deja fuera a quien usa teclado. `[auditor: click-sin-teclado]`
- No pongas texto sobre imágenes sin un scrim o forma de fondo que asegure contraste.
- Dividers: full-width para separar el área interactiva de la que no lo es, inset para contenido relacionado.
- En una colección, todas las cards deben tener la misma estructura y el mismo tamaño de imagen.

## Accesibilidad
- Si la card representa una agrupación con significado, dale un rol: `role="group"`, `role="region"` (con label) o uno de landmark. Si es solo decorativa, no le pongas rol.
- Foco:
  - Usa `tabindex="0"` solo si la card es el mecanismo principal de interacción.
  - Usa `tabindex="-1"` si se le envía el foco por código.
  - Si es decorativa, no la hagas tabulable.

## Ejemplo
```html
<mat-card appearance="outlined" role="group" aria-labelledby="titulo-{{ p.id }}">
  <mat-card-header>
    <mat-card-title id="titulo-{{ p.id }}">
      <a [routerLink]="['/productos', p.id]">{{ p.nombre }}</a>
    </mat-card-title>
    <mat-card-subtitle>{{ p.categoria }}</mat-card-subtitle>
  </mat-card-header>
  <img mat-card-image [src]="p.imagen" [alt]="p.nombre">
  <mat-card-content>{{ p.resumen }}</mat-card-content>
  <mat-card-actions align="end">
    <button matButton type="button" (click)="guardar(p)">Guardar</button>
    <button matButton="filled" type="button" (click)="agregar(p)">Agregar al carro</button>
  </mat-card-actions>
</mat-card>
```

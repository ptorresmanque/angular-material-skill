# Menu — `mat-menu`

Panel flotante y temporal con una lista de acciones. Fuentes: [Angular Material](https://material.angular.dev/components/menu/overview) · [M3](https://m3.material.io/components/menus/guidelines).

## Úsalo cuando
- Hay acciones que no necesitan estar siempre visibles:
  - Un menú overflow (⋮) en una fila o card.
  - El menú de usuario.
  - Un menú contextual (clic derecho).
- Hay navegación secundaria desde un botón. Admite submenús.

## No lo uses cuando
- Las acciones deben estar siempre a la vista: usa botones o una toolbar.
- El valor elegido se guarda en un formulario: usa `mat-select`.
- Son opciones de configuración con estado (marcar/desmarcar): Material no soporta `menuitemcheckbox` ni `menuitemradio`, así que usa checkboxes o toggles fuera del menú.
- En móvil, con muchas opciones: considera `MatBottomSheet`.

## API clave
- Disparador: `[matMenuTriggerFor]="menu"`. Panel: `<mat-menu #menu>`. Ítems: `<button mat-menu-item>`.
- Submenús: un `mat-menu-item` con `[matMenuTriggerFor]`.
- Contenido diferido: `<ng-template matMenuContent>`. Datos por ítem: `[matMenuTriggerData]`.
- Posición: `xPosition` (`before` | `after`), `yPosition` (`above` | `below`), `overlapTrigger`.
- Menú contextual: `matContextMenuTriggerFor`.
- `MAT_MENU_DEFAULT_OPTIONS`: defaults globales.

## Reglas
- Los íconos van antes del texto, y o todos los ítems los tienen o ninguno.
- Agrupa ítems relacionados con `mat-divider` (uno o dos grupos).
- Ordena por frecuencia de uso. Las acciones destructivas van al final y separadas.
- Si una acción no está disponible, deshabilítala en vez de ocultarla (M3). Pero si todas están deshabilitadas, deshabilita u oculta el disparador.
- Usa textos cortos con verbo ("Duplicar", "Mover a…").

## Accesibilidad
- El disparador debe ser un `<button>` (o `<a>`). Recibe `aria-haspopup`, `aria-expanded` y `aria-controls`. `[auditor: menu-trigger-no-boton]`
- Los disparadores e ítems sin texto visible llevan `aria-label`. `[auditor: icon-button-sin-label]`
- Dentro del menú solo van `mat-menu-item`. Nada de inputs, checkboxes ni otros botones. `[auditor: control-anidado]`
- Al abrirse, el foco va al primer ítem; al cerrarse, vuelve al disparador.

## Ejemplo
```html
<button matIconButton [matMenuTriggerFor]="acciones" [matMenuTriggerData]="{ pedido: p }"
        aria-label="Más acciones del pedido">
  <mat-icon>more_vert</mat-icon>
</button>
<mat-menu #acciones>
  <ng-template matMenuContent let-pedido="pedido">
    <button mat-menu-item (click)="duplicar(pedido)"><mat-icon>content_copy</mat-icon>Duplicar</button>
    <button mat-menu-item (click)="exportar(pedido)"><mat-icon>download</mat-icon>Exportar</button>
    <mat-divider />
    <button mat-menu-item (click)="eliminar(pedido)"><mat-icon>delete</mat-icon>Eliminar</button>
  </ng-template>
</mat-menu>
```

# Bottom Sheet — `MatBottomSheet`

Panel modal anclado al borde inferior, pensado principalmente para móvil como alternativa a un diálogo o un menú. Fuentes: [Angular Material](https://material.angular.dev/components/bottom-sheet/overview) · [M3](https://m3.material.io/components/bottom-sheets/guidelines).

## Úsalo cuando
- Hay acciones contextuales en móvil: compartir, abrir con, opciones de un archivo.
- Hay una lista de opciones larga en pantallas compactas.
- Hay contenido suplementario que complementa la pantalla.

## No lo uses cuando
- Estás en escritorio: usa `mat-menu` para acciones o `MatDialog` para contenido.
- Es una decisión crítica o una confirmación: usa `MatDialog`.
- Es la navegación principal: usa `mat-sidenav`.

## API clave
- `bottomSheet.open(Componente, { data, ariaLabel, autoFocus, restoreFocus, hasBackdrop })`.
- `MAT_BOTTOM_SHEET_DATA`: inyecta los datos en el componente del panel.
- `MatBottomSheetRef`: `dismiss(resultado)` y `afterDismissed()`.
- `MAT_BOTTOM_SHEET_DEFAULT_OPTIONS`: defaults globales.
- Solo puede haber un bottom sheet abierto a la vez.

## Reglas
- El contenido típico es un `mat-nav-list` (enlaces) o un `mat-action-list` (acciones), con íconos al inicio.
- Ciérralo al elegir una opción y devuelve el resultado con `dismiss(valor)`.
- Decide según el tamaño de pantalla con `BreakpointObserver`: bottom sheet en `Handset`, menú o diálogo en escritorio.

## Accesibilidad
- Crea un `role="dialog"`. Dale nombre con `ariaLabel` en la configuración.
- No uses `disableClose`: rompe el cierre con Escape que espera el patrón dialog.
- Atrapa el foco mientras está abierto (`autoFocus`: `first-tabbable` por defecto, también `first-header`, `dialog` o un selector).
- Si el elemento que lo abrió ya no existe (por ejemplo, un ítem de menú), devuelve el foco a mano en `afterDismissed()`.

## Ejemplo
```ts
const ref = this.bottomSheet.open(CompartirSheet, {
  ariaLabel: 'Compartir documento',
  data: { documento },
});
ref.afterDismissed().subscribe(destino => destino && this.compartir(destino));
```
```html
<!-- compartir-sheet.html -->
<mat-nav-list aria-label="Compartir en">
  <a mat-list-item href="..." (click)="ref.dismiss('correo')">
    <mat-icon matListItemIcon>mail</mat-icon>
    <span matListItemTitle>Correo</span>
  </a>
</mat-nav-list>
```

# Dialog — `MatDialog`

Ventana modal que bloquea la app hasta que el usuario decide o reconoce algo. Fuentes: [Angular Material](https://material.angular.dev/components/dialog/overview) · [M3](https://m3.material.io/components/dialogs/guidelines).

## Úsalo cuando
- Hay información crítica o una decisión que bloquea el flujo: confirmar una eliminación, una alerta que requiere acuse.
- Hay una tarea corta y enfocada: un formulario de 1–4 campos.
- En móvil, hay una tarea de varios pasos: usa un diálogo a pantalla completa.

## No lo uses cuando
- La información es de importancia baja o media: usa `MatSnackBar`.
- Solo hay que elegir entre opciones: usa `mat-menu` o `mat-select`.
- El contenido es largo o navegable: usa una página o ruta.
- Es en móvil y son acciones contextuales: usa `MatBottomSheet`.
- Estás pensando en abrir un diálogo sobre otro diálogo. Solo un diálogo a pantalla completa puede tener otro encima.

## API clave
- `dialog.open(Componente, { data, width, maxWidth, autoFocus, restoreFocus, role, ariaLabel })`. Usa `role: 'alertdialog'` para confirmaciones destructivas.
- Contenido: `mat-dialog-title`, `mat-dialog-content`, `mat-dialog-actions` (`align="end"`) y `[mat-dialog-close]="resultado"`.
- `MAT_DIALOG_DATA` para recibir datos y `MatDialogRef.close(resultado)` / `afterClosed()` para devolver el resultado.
- `MAT_DIALOG_DEFAULT_OPTIONS`: ancho y comportamiento por defecto para toda la app.

## Reglas
- **Máximo 2 acciones:** confirmar y descartar. Con una sola, que sea de acuse ("Entendido"). Nada de un tercer "Más información". `[auditor: dialog-mas-de-2-acciones]`
- El botón de confirmar va más cerca del borde (a la derecha en LTR). Descartar va como text; confirmar como filled o text según el peso de la acción.
- Deshabilita confirmar hasta que la elección sea válida. Descartar nunca se deshabilita.
- El título es una pregunta o afirmación concreta ("¿Eliminar 3 archivos?"), no "¿Está seguro?" ni "Advertencia".
- Las confirmaciones destructivas nombran la acción en el botón ("Eliminar"), no "Aceptar".
- El componente del diálogo devuelve el resultado con `close()`. La lógica de negocio queda en quien lo abrió.

## Accesibilidad
- `role="dialog"`. Nómbralo con `mat-dialog-title` o con `ariaLabel` / `ariaLabelledBy` en la configuración.
- No uses `disableClose` salvo para evitar pérdida de datos: rompe el Escape que espera el patrón.
- El foco queda atrapado mientras está abierto y vuelve al disparador al cerrar. Si el disparador desaparece (por ejemplo, un ítem de menú), usa `restoreFocus: false` y devuelve el foco a mano en `afterClosed()`.

## Ejemplo
```html
<h2 mat-dialog-title>¿Eliminar «{{ data.nombre }}»?</h2>
<mat-dialog-content>Se quitará del catálogo y no se puede deshacer.</mat-dialog-content>
<mat-dialog-actions align="end">
  <button matButton mat-dialog-close>Cancelar</button>
  <button matButton="filled" [mat-dialog-close]="true">Eliminar</button>
</mat-dialog-actions>
```

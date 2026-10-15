# Snackbar — `MatSnackBar`

Mensaje breve y no intrusivo en el borde inferior sobre el resultado de un proceso. Fuentes: [Angular Material](https://material.angular.dev/components/snack-bar/overview) · [M3](https://m3.material.io/components/snackbar/guidelines).

## Úsalo cuando
- Hay una confirmación de importancia baja o media: "Pedido guardado", "Copiado al portapapeles".
- Una acción se puede deshacer: "Eliminado · Deshacer".

## No lo uses cuando
- Es un error crítico o algo que el usuario **debe** leer: usa `MatDialog` o un mensaje fijo en la página.
- Es un error de validación de un campo: usa `mat-error`.
- Es información que el usuario necesitará después: el snackbar desaparece.

## API clave
- `snackBar.open(mensaje, accion?, config)` o `openFromComponent(Componente, config)`.
- Contenido propio: `matSnackBarLabel`, `matSnackBarActions`, `matSnackBarAction`.
- Configuración:
  - `duration`, `politeness` (`polite` por defecto; `assertive` para errores).
  - `horizontalPosition`, `verticalPosition`, `panelClass`.
- `MatSnackBarRef`: `onAction()`, `afterDismissed()`, `dismiss()`.
- `MAT_SNACK_BAR_DEFAULT_OPTIONS`: duración y posición por defecto para toda la app.
- Solo se muestra uno a la vez: abrir otro cierra el anterior.

## Reglas
- Texto corto (1–2 líneas), en pasado o presente, sin títulos ni íconos decorativos.
- **Máximo una acción**, opcionalmente con un "Cerrar". La acción es un verbo corto ("Deshacer", "Ver").
- **Si tiene acción, no le pongas `duration`**: quien usa lector de pantalla necesita tiempo para llegar a ella. Ciérralo cuando el usuario actúe.
- Los mensajes sin acción se cierran solos (por ejemplo, 4–6 s, con un default global).
- La acción del snackbar debe tener también otra forma de ejecutarse (atajo, menú): el snackbar no mueve el foco.
- No cubras la navegación inferior ni el FAB: ajusta la posición si hace falta.

## Accesibilidad
- Se anuncia con una región `aria-live`, sin mover el foco.
- Si el usuario movió el foco al snackbar y este se cierra, devuélvele el foco a un lugar lógico.

## Ejemplo
```ts
const ref = this.snackBar.open('Pedido eliminado', 'Deshacer'); // con acción: sin duration
ref.onAction().subscribe(() => this.restaurar(pedido));

this.snackBar.open('Cambios guardados', undefined, { duration: 5000 }); // sin acción
```

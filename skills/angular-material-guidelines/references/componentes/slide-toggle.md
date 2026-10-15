# Slide Toggle — `mat-slide-toggle`

Interruptor de encendido y apagado; equivale al *switch* de M3. Fuentes: [Angular Material](https://material.angular.dev/components/slide-toggle/overview) · [M3](https://m3.material.io/components/switch/guidelines).

## Úsalo cuando
- Se enciende o apaga una opción **independiente** y el efecto es **inmediato**, sin botón Guardar: preferencias, notificaciones, modo oscuro.

## No lo uses cuando
- El valor se aplica al enviar un formulario: usa `mat-checkbox`. `[auditor: slide-toggle-en-form-con-submit]`
- Hay varias opciones relacionadas para elegir: usa checkboxes.
- Son opciones opuestas (lista/mapa): usa `mat-button-toggle-group`.
- Es una acción ("Exportar"): un switch no reemplaza a un botón.

## API clave
- `checked`, `(change)`, `disabled`. Es compatible con formularios. No tiene estado indeterminate.
- `labelPosition`, `hideIcon`, `fullWidth` (switch y label en extremos opuestos).
- `MAT_SLIDE_TOGGLE_DEFAULT_OPTIONS`: defaults globales.

## Reglas
- El label describe lo que pasa **cuando está encendido** ("Recibir notificaciones"), en texto corto al lado. No escribas texto dentro del switch.
- Aplica el cambio en `(change)` y confirma solo si el efecto no es evidente. Si falla, revierte el estado y avisa con un snackbar.
- Pónlos apilados, típicamente en pantallas de configuración.
- Los íconos del switch deben comunicar el estado (✓ / ✕), no otra cosa.

## Accesibilidad
- Usa un `<button role="switch">` interno, rotulado por el contenido.
- Sin texto visible, usa `[aria-label]` o `[aria-labelledby]` como input (sin `attr.`).
- No pongas controles interactivos dentro del label. `[auditor: control-anidado]`

## Ejemplo
```html
<mat-slide-toggle [checked]="prefs().notificaciones" (change)="guardarPreferencia('notificaciones', $event.checked)">
  Recibir notificaciones por correo
</mat-slide-toggle>
```

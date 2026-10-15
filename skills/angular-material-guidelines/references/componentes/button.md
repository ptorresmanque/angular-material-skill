# Button — `matButton`, `matIconButton`, `matFab`, `matMiniFab`

Botones nativos `<button>` y enlaces `<a>` con estilo Material. Fuentes: [Angular Material](https://material.angular.dev/components/button/overview) · [M3](https://m3.material.io/components/buttons/guidelines).

## Elección
- `<button>` ejecuta una acción en la página. `<a>` navega a otra URL o ruta. `[auditor: button-navega]` `[auditor: a-sin-destino]`
- La jerarquía la define la apariencia:

| Apariencia (v20+) | Úsala para | < v20 |
|---|---|---|
| `matButton="filled"` | La acción final o principal de la sección (Guardar, Pagar). **Una por sección.** `[auditor: multiples-filled]` | `mat-flat-button` |
| `matButton="tonal"` | Una acción importante pero no final (Siguiente). | no existe |
| `matButton="outlined"` | Una acción secundaria que debe verse (Exportar). | `mat-stroked-button` |
| `matButton` (text) | Acciones de baja prioridad (Cancelar) o muchas opciones juntas. | `mat-button` |
| `matButton="elevated"` | Solo sobre fondos con imagen o patrón. | `mat-raised-button` |
| `matIconButton` | Acciones compactas en toolbars, filas o cards. | `mat-icon-button` |
| `matFab` (`extended`) | La acción constructiva principal de la pantalla. **Uno por pantalla.** `[auditor: multiples-fab]` | `mat-fab` |
| `matMiniFab` | Un FAB secundario o un espacio reducido. | `mat-mini-fab` |

En < v20 la API nueva no aplica estilos. `[auditor: api-boton-no-disponible]` En v20+, usa la API nueva en código nuevo. `[auditor: boton-legacy]`

## Reglas
- Dentro de un `<form>`, un `<button>` sin `type` es `submit`. Pon `type="button"` en todos los botones que no envían el formulario.
- Etiquetas con verbos concretos ("Guardar cambios", no "Aceptar"). No las escribas en MAYÚSCULAS: los lectores de pantalla las deletrean.
- Para explicar por qué un botón está deshabilitado, usa `disabledInteractive` + `matTooltip`. Con `disabled` nativo el botón no recibe foco ni eventos. Si usas `disabledInteractive`, bloquea tú la acción.
- Para acciones lentas, usa `showProgress` con un elemento `progressIndicator` (por ejemplo, `mat-progress-spinner`) en vez de cambiar el texto.
- Íconos: van antes del texto por defecto. Con `iconPositionEnd` van después (por ejemplo, "Enviar →").
- `color` solo funciona con temas M2. En M3 los colores se ajustan con `mat.button-overrides`.
- Usa el FAB extendido cuando el ícono solo no se entiende. Los mini FAB no admiten `extended`.

## Accesibilidad
- Botones de solo ícono (`matIconButton`, `matFab` sin `extended`, `matMiniFab`): siempre con `aria-label` o `aria-labelledby`. Un tooltip no reemplaza el label. `[auditor: icon-button-sin-label]`
- Área táctil mínima de 48×48 px.
- Para botones con estado de encendido o apagado, usa `mat-button-toggle`.

## Ejemplo
```html
<div class="acciones">
  <button matButton type="button" (click)="cancelar()">Cancelar</button>
  <button matButton="filled" type="submit" [disabled]="form.invalid"
          [showProgress]="guardando()">
    Guardar
    <mat-progress-spinner progressIndicator mode="indeterminate" diameter="20"
                          aria-label="Guardando" />
  </button>
</div>
```

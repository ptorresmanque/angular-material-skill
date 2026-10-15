# Tooltip — `matTooltip`

Texto flotante breve que aparece al pasar el puntero o enfocar un elemento. Fuentes: [Angular Material](https://material.angular.dev/components/tooltip/overview) · [M3](https://m3.material.io/components/tooltips/guidelines).

## Úsalo cuando
- Hay que nombrar un botón de solo ícono (además de su `aria-label`).
- Hay que dar una pista breve y no esencial sobre un control.
- Hay que mostrar el texto completo de un elemento truncado.
- Hay que explicar por qué un botón está deshabilitado. Combínalo con `disabledInteractive` en el botón.

## No lo uses cuando
- La información es esencial para completar la tarea: ponla visible (hint, texto de ayuda).
- El contenido es interactivo (enlaces, botones) o largo: el tooltip no admite clics. Usa un `mat-menu`, un diálogo o texto en la página.
- En interfaces táctiles es la única forma de ver la información: no hay hover.
- Repite exactamente el texto visible del elemento.

## API clave
- `matTooltip`, `matTooltipPosition` (`above` | `below` | `left` | `right` | `before` | `after`).
- `matTooltipShowDelay`, `matTooltipHideDelay`, `matTooltipDisabled`, `matTooltipClass`, `matTooltipTouchGestures`.
- `MAT_TOOLTIP_DEFAULT_OPTIONS`: delays y posición por defecto para toda la app.

## Reglas
- Una línea de texto, sin formato ni íconos.
- Úsalo en elementos que reciben foco (botones, enlaces, inputs), no en `span`, `div` ni `mat-icon` sueltos. `[auditor: tooltip-no-enfocable]`
- Usa una posición y unos delays consistentes en toda la app (configuración global).
- En un botón de ícono, el tooltip complementa el `aria-label`, no lo reemplaza. `[auditor: icon-button-sin-label]`

## Accesibilidad
- Agrega `aria-describedby` apuntando a una copia oculta del texto: se lee al enfocar el elemento.
- No muestres tooltips solo con eventos de puntero personalizados (`click`, `mouseenter`). Quien usa teclado debe poder hacer lo mismo.

## Ejemplo
```html
<button matIconButton aria-label="Exportar a Excel" matTooltip="Exportar a Excel" (click)="exportar()">
  <mat-icon>download</mat-icon>
</button>

<button matButton="filled" [disabled]="!puedeEnviar()" disabledInteractive
        [matTooltip]="puedeEnviar() ? '' : 'Completa los campos obligatorios'">
  Enviar
</button>
```

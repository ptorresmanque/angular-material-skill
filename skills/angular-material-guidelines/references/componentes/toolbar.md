# Toolbar — `mat-toolbar`

Contenedor para encabezados, títulos y acciones; se usa como la *top app bar* de M3. Fuentes: [Angular Material](https://material.angular.dev/components/toolbar/overview) · [M3](https://m3.material.io/components/app-bars/guidelines).

## Úsalo cuando
- Es el encabezado de la app o de la página: navegación (☰ o ←), título y 1–2 acciones esenciales.
- Es el encabezado de una sección o de un diálogo a pantalla completa.

## No lo uses cuando
- Hay muchas acciones de edición sobre un contenido: agrúpalas en un menú o usa botones en el contenido.
- Es el pie de página.
- Es la navegación principal con muchos destinos: usa `mat-sidenav`. La toolbar solo tiene el botón que lo abre.

## API clave
- Una fila, o varias con `mat-toolbar-row`. Con filas, todo el contenido va dentro de las filas.
- La toolbar no posiciona su contenido: usa flex y un espaciador (`flex: 1 1 auto`).

## Reglas
- Estructura típica: ícono de navegación al inicio → título → espaciador → acciones (`matIconButton` con label) → avatar o menú de usuario.
- Pon **1–2 acciones** en la barra (M3). El resto va en un menú ⋮, pero evita el overflow si se puede.
- A lo más **una** acción destacada (filled o tonal). No pongas varias filled en la barra. `[auditor: multiples-filled]`
- El título es el de la página actual. Usa un `<h1>` (u otro nivel según la página) dentro de la toolbar para la jerarquía.
- Solo una toolbar principal por pantalla. Si es fija (sticky), que no tape contenido.

## Accesibilidad
- Por defecto es decorativa, sin roles. Usa un heading para el título.
- Agrega `role="toolbar"` (con `aria-label`) solo si es una barra de herramientas real, con la navegación por teclado que ese rol implica.
- Los botones de ícono llevan `aria-label`. `[auditor: icon-button-sin-label]`

## Ejemplo
```html
<mat-toolbar>
  <button matIconButton aria-label="Abrir menú" (click)="nav.toggle()"><mat-icon>menu</mat-icon></button>
  <h1>Pedidos</h1>
  <span class="spacer"></span>
  <button matIconButton aria-label="Buscar" (click)="buscar()"><mat-icon>search</mat-icon></button>
  <button matIconButton [matMenuTriggerFor]="usuario" aria-label="Cuenta de usuario"><mat-icon>account_circle</mat-icon></button>
</mat-toolbar>
```

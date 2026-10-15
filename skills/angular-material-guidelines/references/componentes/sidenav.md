# Sidenav / Drawer — `mat-sidenav`, `mat-drawer`

Contenido lateral colapsable (normalmente navegación) junto al contenido principal. Fuentes: [Angular Material](https://material.angular.dev/components/sidenav/overview) · [M3](https://m3.material.io/components/navigation-drawer/guidelines).

## Úsalo cuando
- Es la navegación principal de la app (`mat-sidenav`) y hay **5 o más destinos** o **2 o más niveles** de jerarquía (M3).
- Hay un panel lateral dentro de una sección (filtros, detalle): `mat-drawer`.

## No lo uses cuando
- Hay pocos destinos (2–5) en móvil: una barra de tabs o de navegación es más directa.
- Ya hay otro componente de navegación principal en la misma pantalla: M3 pide usar solo uno.
- El contenido es temporal y bloqueante: usa `MatDialog`. Si son acciones en móvil: usa `MatBottomSheet`.

## API clave
- Estructura: `mat-sidenav-container` > `mat-sidenav` + `mat-sidenav-content`. Lo que no debe verse afectado (como el header) va fuera del container.
- `mode`:
  - `side`: fijo junto al contenido, para escritorio.
  - `over`: se superpone con backdrop, para móvil.
  - `push`: empuja el contenido.
- Apertura y posición:
  - `opened` y `(openedChange)`.
  - `position`: `start` o `end`. Solo uno por lado.
  - `disableClose`.
- Cambios de layout:
  - `fixedInViewport` y `fixedTopGap` (solo sidenav).
  - `autosize`: recalcula cuando cambia el ancho.
- `autoFocus`: atrapa el foco en `over`/`push`. Por defecto el foco va al primer elemento tabulable; `cdkFocusInitial` cambia cuál.

## Reglas
- Responsive con `BreakpointObserver`: `side` y abierto en escritorio; `over` y cerrado en móvil, con un botón ☰ en la toolbar.
- En `over`, ciérralo al navegar (en `(click)` del enlace o al cambiar de ruta).
- Para los destinos, usa `mat-nav-list` con `[activated]`/`routerLinkActive`. Siempre hay un destino activo y visible.
- No pongas otro sidenav dentro del contenido.

## Accesibilidad
- Dale un rol: `role="navigation"` si contiene enlaces (o `region`/`directory` según el contenido). Al contenido principal, `role="main"`.
- El `mat-nav-list` interno lleva `aria-label`. `[auditor: lista-sin-label]`
- El botón ☰ lleva `aria-label` y `aria-expanded`. `[auditor: icon-button-sin-label]`

## Ejemplo
```html
<mat-toolbar>
  @if (esMovil()) {
    <button matIconButton aria-label="Abrir menú" [attr.aria-expanded]="nav.opened" (click)="nav.toggle()">
      <mat-icon>menu</mat-icon>
    </button>
  }
  <h1>Mi app</h1>
</mat-toolbar>
<mat-sidenav-container>
  <mat-sidenav #nav role="navigation" [mode]="esMovil() ? 'over' : 'side'" [opened]="!esMovil()">
    <mat-nav-list aria-label="Secciones">…</mat-nav-list>
  </mat-sidenav>
  <mat-sidenav-content role="main"><router-outlet /></mat-sidenav-content>
</mat-sidenav-container>
```

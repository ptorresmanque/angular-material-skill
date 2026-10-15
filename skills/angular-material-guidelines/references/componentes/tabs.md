# Tabs — `mat-tab-group`, `mat-tab-nav-bar`

Organizan contenido relacionado del **mismo nivel** en vistas separadas, mostrando una a la vez. Fuentes: [Angular Material](https://material.angular.dev/components/tabs/overview) · [M3](https://m3.material.io/components/tabs/guidelines).

## Úsalo cuando
- Hay vistas del mismo nivel que el usuario recorre en cualquier orden: "Detalles / Reseñas / Envío".
- Hay subsecciones con rutas propias: usa `mat-tab-nav-bar` + `mat-tab-nav-panel` con `routerLink`.

## No lo uses cuando
- El contenido es secuencial y se lee o completa en orden: usa `mat-stepper` (M3).
- Hay más de ~6 secciones o son destinos principales de la app: usa `mat-sidenav`.
- Es un cambio de vista sobre los mismos datos (lista/cuadrícula): usa `mat-button-toggle-group`.
- El contenido tiene que compararse en paralelo: muéstralo junto.

## API clave
- `mat-tab-group` con `mat-tab` (`label` o `<ng-template mat-tab-label>`).
  - `selectedIndex`, `(selectedTabChange)`.
  - `dynamicHeight`, `preserveContent`.
  - `mat-stretch-tabs`, `mat-align-tabs` (`start` | `center` | `end`).
  - `animationDuration`.
- Contenido diferido: `<ng-template matTabContent>`.
- `mat-tab-nav-bar` sobre un `<nav>`, con `<a mat-tab-link [active]>` y `[tabPanel]` apuntando a un `mat-tab-nav-panel`.
- `MAT_TABS_CONFIG`: defaults globales.

## Reglas
- Usa labels cortos y claros, relacionados con el título de la página. No los trunques si no es necesario.
- Todos los tabs llevan solo texto, o todos ícono + texto. No los mezcles. Usa íconos solos solo si son universalmente reconocibles.
- M3 distingue dos niveles:
  - **Primary tabs** bajo la app bar, para los destinos del contenido.
  - **Secondary tabs** dentro de un área de contenido.
- No pases de dos niveles.
- Badges en los tabs: máximo 4 caracteres, y desaparecen cuando el usuario ve ese tab.
- Usa contenido diferido para tabs con carga pesada.

## Accesibilidad
- Implementa el patrón ARIA Tabs (`tablist`, `tab`, `tabpanel`) con teclado (←/→, Inicio/Fin).
- Los tabs sin texto descriptivo llevan `aria-label`.
- El `<nav mat-tab-nav-bar>` lleva **siempre** label. Coloca el `mat-tab-nav-panel` justo después. `[auditor: tab-nav-sin-label]`

## Ejemplo
```html
<nav mat-tab-nav-bar [tabPanel]="panel" aria-label="Secciones del producto">
  @for (s of secciones; track s.ruta) {
    <a mat-tab-link [routerLink]="s.ruta" routerLinkActive #rla="routerLinkActive" [active]="rla.isActive">{{ s.titulo }}</a>
  }
</nav>
<mat-tab-nav-panel #panel><router-outlet /></mat-tab-nav-panel>
```

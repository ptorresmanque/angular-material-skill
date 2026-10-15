# Wrappers, librerías y equivalencias

Cómo decidir si un componente propio o una librería de UI se reemplaza por Angular Material. Los criterios de decisión están en la sección 5 de `SKILL.md`.

## Qué reemplaza Material

| Componente propio o librería | Equivalente en Angular Material |
|---|---|
| Modal, popup, confirmación; `ngx-smart-modal`; `sweetalert2` (confirmaciones) | `MatDialog` |
| Toast, notificación temporal; `ngx-toastr`; `sweetalert2` (avisos) | `MatSnackBar` |
| Action sheet (móvil) | `MatBottomSheet` |
| Dropdown que guarda un valor; `@ng-select/ng-select` | `mat-select`, o `mat-autocomplete` si hay búsqueda |
| Dropdown de acciones, menú contextual | `mat-menu` |
| Tooltip | `matTooltip` |
| Popover con contenido interactivo | `mat-menu` si son acciones; si no, CDK Overlay |
| Tabs | `mat-tab-group` o `mat-tab-nav-bar` |
| Acordeón, colapsable | `mat-expansion-panel` / `mat-accordion` |
| Wizard, pasos | `mat-stepper` |
| Tabla con orden y paginación; `ngx-pagination` | `mat-table` + `matSort` + `mat-paginator` |
| Spinner, loader; `ngx-spinner` | `mat-progress-spinner` / `mat-progress-bar` |
| Datepicker, calendario para elegir fecha | `mat-datepicker` / `mat-date-range-input` |
| Timepicker; `ngx-material-timepicker` | `mat-timepicker` (v19.1+) |
| Switch, toggle | `mat-slide-toggle`, o `mat-button-toggle-group` si las opciones son opuestas |
| Tags, pills | `mat-chip-set` / `mat-chip-listbox` / `mat-chip-grid` |
| Contador sobre un ícono | `matBadge` |
| Sidebar, drawer, offcanvas | `mat-sidenav` / `mat-drawer` |
| Navbar, header | `mat-toolbar` como base |
| `ngx-bootstrap`, `@ng-bootstrap/ng-bootstrap`, `primeng`, `ng-zorro-antd` | El componente Material equivalente de cada módulo que se use. Dos kits de UI en la misma app rompen la consistencia. |

## Sin equivalente en Angular Material (mantener)

- Avatar.
- Breadcrumb.
- Skeleton.
- Carrusel.
- Rating.
- Subida de archivos o dropzone.
- Aviso fijo en la página (banner o alerta inline).
- Data grid con edición inline, agrupación o virtualización pesada (por ejemplo, ag-grid).

Si construyes uno de estos, úsalo sobre CDK (`Overlay`, `A11y`, `ListKeyManager`) y con tokens del tema, para que se vea y se comporte como Material.

## Configuración global en vez de wrappers

Si un wrapper solo existe para fijar defaults o estilos, reemplázalo por configuración global:

| Necesidad | Configuración global |
|---|---|
| Appearance de todos los campos (`fill` / `outline`), subscriptSizing | provider `MAT_FORM_FIELD_DEFAULT_OPTIONS` |
| Ancho, `autoFocus` y `hasBackdrop` de todos los diálogos | provider `MAT_DIALOG_DEFAULT_OPTIONS` |
| Duración y posición de todos los snackbars | provider `MAT_SNACK_BAR_DEFAULT_OPTIONS` |
| Delays y posición de los tooltips | provider `MAT_TOOLTIP_DEFAULT_OPTIONS` |
| Comportamiento por defecto de los botones (p. ej. `disabledInteractive`) | provider `MAT_BUTTON_CONFIG` |
| Colores, formas y tipografía de un componente | mixin Sass `mat.<componente>-overrides((...))` (ver la pestaña Styling de cada componente) |
| Paleta, tipografía y densidad de toda la app | mixin `mat.theme((...))` y `mat.theme-overrides` |

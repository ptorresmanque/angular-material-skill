# Referencia por componente

Cuándo usar y cuándo evitar cada componente de material.angular.dev. Los umbrales numéricos ("≤ 5 opciones", "> 15") son reglas prácticas de UX, no valores oficiales.

Contenido: [Acciones](#acciones) · [Formularios](#formularios) · [Selección](#selección) · [Mensajes y overlays](#mensajes-y-overlays) · [Navegación](#navegación-y-estructura) · [Datos](#mostrar-datos) · [Indicadores](#indicadores-y-utilidades) · [Wrappers y equivalencias](#wrappers-y-equivalencias)

## Acciones

| Componente | Úsalo cuando… | Evítalo cuando… |
|---|---|---|
| `matButton="filled"` | Es la acción final o principal de la sección: Guardar, Confirmar, Pagar. Una por sección. | Ya existe otra filled en la misma sección. |
| `matButton="tonal"` | Es una acción importante pero no final (por ejemplo "Siguiente"). | El proyecto está en < v20 (no existe). |
| `matButton="outlined"` | Es una acción secundaria que debe verse, como "Exportar" junto a un "Guardar". | — |
| `matButton` (text) | Es una acción de baja prioridad ("Cancelar" en un diálogo) o hay muchas opciones juntas. | — |
| `matButton="elevated"` | El botón está sobre un fondo con imagen o patrón. | El fondo es plano: usa filled, tonal u outlined. |
| `matIconButton` | Son acciones compactas en toolbars, filas o cards. Siempre con `aria-label`. | El ícono no es universal: agrega texto. |
| `matFab` / `extended` | Es la acción constructiva principal de la pantalla. Usa `extended` si el ícono no basta. | Ya hay otro FAB en la pantalla. |
| `matMiniFab` | Necesitas un FAB secundario o hay poco espacio. | — |
| Button Toggle | Hay 2–5 opciones opuestas siempre visibles (vista lista/cuadrícula), o una barra de formato (`multiple`). | Es un único on/off: usa Slide Toggle. |

## Formularios

| Componente | Úsalo cuando… | Evítalo cuando… |
|---|---|---|
| Form Field | Envuelves input, select, textarea, chip-grid o datepicker. Usa la misma `appearance` en toda la app. | — |
| Input (`matInput`) | Es texto libre, número, email o `textarea`. Aprovecha los tipos nativos. | El valor viene de una lista cerrada (Select) o es una fecha (Datepicker). |
| Datepicker | Hay que capturar una fecha. Para rangos, `mat-date-range-input`. | Es una fecha muy lejana: permite escribirla y usa `startView="multi-year"`. |
| Timepicker | Hay que elegir una hora. Para fecha y hora, combínalo con el Datepicker. | Es una duración: usa un input numérico. |
| Slider | Es un valor aproximado dentro de un rango (volumen, rango de precio en filtros). | Se necesita un valor exacto: usa Input. |
| Autocomplete | Hay más de ~15 opciones, o se permite texto que no está en la lista (comunas, productos, usuarios). | Son pocas opciones fijas: usa Select o Radio. |

## Selección

| Componente | Úsalo cuando… | Evítalo cuando… |
|---|---|---|
| Checkbox | Hay selección múltiple, o es un booleano que se aplica al enviar ("Acepto los términos"). `indeterminate` para un "Seleccionar todo". | El cambio debe aplicarse al instante: usa Slide Toggle. |
| Radio Button | Se elige una opción entre ≤ 5–7 y conviene verlas todas para comparar. | Son muchas: usa Select. |
| Slide Toggle | Es un on/off que se aplica de inmediato, sin botón Guardar (preferencias). | Requiere guardar, o las opciones son opuestas. |
| Select | Se elige una opción entre muchas con poco espacio. Admite `multiple`. | Son ≤ 5 opciones (Radio) o muchísimas con búsqueda (Autocomplete). |
| Chips: `mat-chip-set` | Solo se muestran etiquetas (tags). | — |
| Chips: `mat-chip-listbox` | Son filtros o selección ("Talla: S M L"). Agrega `multiple` para filtros acumulables. | — |
| Chips: `mat-chip-grid` | El usuario ingresa varios valores (destinatarios, keywords), con autocomplete si conviene. | — |

## Mensajes y overlays

La importancia del mensaje decide el componente.

| Componente | Úsalo cuando… | Evítalo cuando… |
|---|---|---|
| Snackbar | Es una confirmación de importancia baja o media que puede desaparecer sola. Máximo una acción ("Deshacer"). | El error es crítico y el usuario debe leerlo. |
| Dialog | Es información crítica o una decisión que bloquea el flujo. Máximo 2 acciones. En móvil, una tarea de varios pasos puede ir en un diálogo a pantalla completa. | La información es de baja prioridad (Snackbar) o solo hay que elegir opciones (Menu). |
| Bottom Sheet | Hay acciones contextuales en móvil (compartir, opciones de archivo). | Estás en escritorio: usa Menu o Dialog. |
| Menu | Hay acciones o navegación que salen de un botón (el ⋮ de una fila, el menú de usuario). Admite submenús. | El valor elegido debe quedar guardado en un form: usa Select. |
| Tooltip | Es una etiqueta de botón de ícono o una pista breve no esencial. | La información es esencial, el usuario está en táctil o el contenido es interactivo. |

## Navegación y estructura

| Componente | Úsalo cuando… |
|---|---|
| Toolbar | Necesitas el header de la app o de una sección. |
| Sidenav | Es la navegación principal: `side` en escritorio, `over` en móvil. Para paneles secundarios → `mat-drawer`. |
| Tabs | Son vistas del mismo nivel sin orden. Si cambian de ruta → `mat-tab-nav-bar`. No las uses para pasos obligatorios. |
| Stepper | Es un proceso secuencial con validación. `linear` obliga a completar cada paso; en móvil, modo vertical. |
| Expansion Panel | Quieres mostrar contenido bajo demanda: FAQ, configuración, formularios largos. `mat-accordion` si debe haber un solo panel abierto. |

## Mostrar datos

| Componente | Úsalo cuando… | Evítalo cuando… |
|---|---|---|
| Table | Hay varios atributos que se comparan por columnas. | Estás en móvil con muchas columnas: usa List o Cards. |
| Sort Header | Ordenar por columna aporta valor (siempre junto a Table). | — |
| Paginator | Hay más de ~25–50 filas. Si los datos vienen de una API, pagina en el servidor. | Encaja mejor el scroll infinito o el virtual scroll del CDK. |
| List | Los ítems tienen una sola dimensión. `mat-selection-list` para elegir ítems, `mat-nav-list` para links. | Hay que comparar atributos: usa Table. |
| Card | Es una unidad de contenido independiente que lleva a un detalle. | Hay cards anidadas o todo está en cards. |
| Grid List | Es una galería de mosaicos con `rowspan`/`colspan`. | Quieres maquetar la página: usa CSS Grid o Flexbox. |
| Tree | Los datos son jerárquicos (archivos, categorías anidadas). | La jerarquía es de un solo nivel: usa List o Expansion Panel. |

## Indicadores y utilidades

| Componente | Úsalo cuando… |
|---|---|
| Badge | Muestras un contador o estado pequeño sobre otro elemento. No sirve para textos largos. |
| Progress Bar | El progreso tiene un % conocido (`determinate`), o es la carga de una vista completa (`indeterminate` arriba de la página). |
| Progress Spinner | La carga ocurre en un espacio compacto (botón, card, panel). Para páginas completas, considera skeletons. |
| Icon | Usas Material Symbols o SVG. Si es decorativo, `aria-hidden`; si es lo único que comunica, lleva label. |
| Divider | Separas grupos en listas o menús y el espacio en blanco no alcanza. |
| Ripples (`matRipple`) | Quieres feedback táctil en elementos clicables propios (los componentes Material ya lo traen). |
| Core | No se usa directamente: contiene `mat-option`, los adaptadores de fecha y el theming. |

## Wrappers y equivalencias

### Qué reemplaza Material

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

### Sin equivalente en Angular Material (mantener)

- Avatar.
- Breadcrumb.
- Skeleton.
- Carrusel.
- Rating.
- Subida de archivos o dropzone.
- Aviso fijo en la página (banner o alerta inline).
- Data grid con edición inline, agrupación o virtualización pesada (por ejemplo, ag-grid).

Si construyes uno de estos, úsalo sobre CDK (`Overlay`, `A11y`, `ListKeyManager`) y con tokens del tema, para que se vea y se comporte como Material.

### Configuración global en vez de wrappers

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

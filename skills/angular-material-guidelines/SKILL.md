---
name: angular-material-guidelines
description: Lineamientos obligatorios para elegir y usar componentes de Angular Material (material.angular.dev) según Material Design 3, más un script que audita templates. Úsala SIEMPRE que escribas, generes, revises, refactorices o audites código Angular que use @angular/material — formularios, botones, mat-select, autocomplete, chips, dialog, snackbar, bottom sheet, menu, tooltip, sidenav, toolbar, tabs, stepper, expansion panel, table, paginator, list, card, tree, etc. — aunque el usuario no diga "lineamientos" y solo pida "crea un formulario", "haz la pantalla de listado", "agrega un modal de confirmación", "muestra un mensaje de guardado", "revisa la UI" o "audita el proyecto" en un proyecto Angular Material. También cuando un hook reporte hallazgos de `mat-guidelines`.
---

# Lineamientos Angular Material

Estos lineamientos existen para que todas las pantallas comuniquen igual: una sola acción principal por sección, mensajes con el nivel de interrupción correcto y controles que muestran sus opciones de la forma más directa. Las fuentes son material.angular.dev y las guías de uso de m3.material.io. Si el usuario pide algo que contradice una regla, avísale en una línea por qué y propone la alternativa. Si insiste, hazlo y deja el comentario `mat-guidelines-ignore` (ver más abajo).

## 1. Antes de escribir código

1. **Detecta la versión** en `node_modules/@angular/material/package.json` (o en `package.json`). La API de botones cambia:

   | Apariencia | v20+ (usa esta en código nuevo) | < v20 |
   |---|---|---|
   | filled | `matButton="filled"` | `mat-flat-button` |
   | tonal | `matButton="tonal"` | no existe → `mat-flat-button` o `mat-stroked-button` |
   | outlined | `matButton="outlined"` | `mat-stroked-button` |
   | elevated | `matButton="elevated"` | `mat-raised-button` |
   | text | `matButton` | `mat-button` |
   | solo ícono | `matIconButton` | `mat-icon-button` |
   | FAB / mini | `matFab` / `matMiniFab` | `mat-fab` / `mat-mini-fab` |

   En v20+ los selectores legados siguen funcionando. No migres masivamente código existente salvo que te lo pidan; el código nuevo sí va con la API nueva. En < v20, `matButton="..."` no da error, pero queda **sin estilo**, así que nunca la uses ahí.
2. **Respeta las convenciones del proyecto.** Mira si hay `MAT_FORM_FIELD_DEFAULT_OPTIONS` (appearance `fill` u `outline`) o wrappers propios, y síguelos para que la app sea consistente.
3. **Elige el componente** con las reglas de la sección 2. Si tienes dudas sobre un componente específico, lee `references/componentes.md`, que tiene la tabla completa con cuándo usarlo y cuándo evitarlo.

## 2. Reglas de decisión

### Jerarquía de botones
- `<button>` ejecuta acciones; `<a matButton href|routerLink>` navega. Nunca uses `<button routerLink>` ni `<a (click)>` sin destino.
- **Una sola `filled` por sección**: la acción final o principal (Guardar, Confirmar, Pagar). La acción importante pero no final va en `tonal`; la secundaria visible, en `outlined`; la de baja prioridad, en text (como "Cancelar"). `elevated` solo va sobre fondos con imagen o patrón.
- `matIconButton` se usa para acciones compactas (toolbars, filas, cards) y **siempre** lleva `aria-label`. Un `matTooltip` no reemplaza el label.
- **Un FAB por pantalla**, para la acción constructiva principal ("Nuevo pedido"). Usa `extended` si el ícono solo no se entiende.
- Para mostrar por qué un botón está deshabilitado, usa `disabledInteractive` + tooltip. Para acciones lentas, `showProgress`.

### Mensajes y overlays (elige según la importancia del mensaje)
- **Snackbar**: confirmación de importancia baja o media ("Guardado", "Eliminado · Deshacer"). Máximo una acción. No sirve para errores críticos.
- **Dialog**: información crítica o una decisión que bloquea el flujo (confirmar una eliminación, un formulario corto). Máximo 2 acciones: confirmar (la más cercana al borde) y descartar. El título debe ser una pregunta concreta, no "¿Está seguro?". No uses Dialog para información de baja prioridad.
- **Bottom Sheet**: acciones contextuales en **móvil** (compartir, opciones de archivo). En escritorio prefiere Menu o Dialog.
- **Menu**: lista de **acciones** o navegación que sale de un botón. Si el valor elegido debe quedar guardado, usa Select.
- **Tooltip**: solo pistas no esenciales o etiquetas de botones de ícono. No funciona en táctil ni sirve para contenido interactivo, y el elemento que lo lleva debe poder recibir foco.

### Formularios y selección
- Todo `matInput`, `mat-select`, `mat-chip-grid` o `mat-date-range-input` va dentro de `<mat-form-field>` con `<mat-label>`, y con `<mat-error>` cuando tiene validaciones.
- Pocas opciones a la vista (≤ 5) → `mat-radio-group`. Si son opuestas y compactas (lista/cuadrícula, día/semana/mes) → `mat-button-toggle-group`.
- Muchas opciones → `mat-select`. Muchísimas, o hay que buscar o escribir libre → `mat-autocomplete`.
- Se aplica **al instante** → `mat-slide-toggle`. Se aplica **al guardar** el form, o hay selección múltiple → `mat-checkbox` (`indeterminate` para "seleccionar todo").
- Un valor exacto → input. Un valor aproximado en un rango → `mat-slider`.
- Fecha → Datepicker (rangos con `mat-date-range-input`). Hora → Timepicker. Fecha y hora → ambos.
- Chips:
  - `mat-chip-set` para mostrar etiquetas.
  - `mat-chip-listbox` + `mat-chip-option` para filtros o selección.
  - `mat-chip-grid` + `mat-chip-row` para ingresar varios valores (con autocomplete si conviene).
  - Cada chip va dentro de su contenedor.

### Navegación y estructura
- **Toolbar**: el header de la app o de una sección.
- **Sidenav**: la navegación principal; `mode="side"` en escritorio y `over` en móvil (`BreakpointObserver`). Para paneles secundarios como filtros → `mat-drawer`.
- **Tabs**: vistas del mismo nivel sin orden (`mat-tab-nav-bar` si cambian de ruta).
- **Stepper**: pasos con orden y validación (checkout, onboarding).
- **Expansion Panel / accordion**: mostrar contenido bajo demanda (FAQ, secciones de configuración).

### Mostrar datos
- **Un atributo por ítem** → `mat-list`.
- **Varios atributos que se comparan** → `mat-table` + `matSort` + `mat-paginator` (paginación en el servidor si los datos vienen de una API).
- **Contenido independiente que lleva a un detalle** → `mat-card`, sin cards anidadas ni todo en cards.
- **Galería de mosaicos** → `mat-grid-list`. Para maquetar la página usa CSS Grid o Flexbox.
- **Jerarquía** → `mat-tree`.

### Indicadores
- **Progress bar**: progreso con % conocido (`determinate`), o carga de una vista completa (`indeterminate` arriba).
- **Spinner**: cargas en espacios compactos (dentro de un botón, card o panel).
- **Badge**: contadores pequeños sobre otro elemento.
- **Divider**: solo cuando el espacio en blanco no alcanza para separar.
- **mat-icon**: si es decorativo, `aria-hidden="true"`; si es lo único que comunica, lleva label.

## 3. Verificación (obligatoria al terminar)

Después de crear o modificar templates, ejecuta la auditoría sobre lo que tocaste. El script está en `scripts/audit.py`, dentro del directorio base de esta skill (se indica al cargarla):

```bash
python3 <directorio-de-esta-skill>/scripts/audit.py <archivos-o-carpetas>
```

- Corrige siempre los **ERROR**.
- Las **WARN** son heurísticas: corrígelas o, si en este caso la regla no aplica, deja en la línea anterior un comentario con justificación: `<!-- mat-guidelines-ignore: regla-id — motivo -->` (en un `.ts` con template inline, dentro del template).
- Hay reglas que el script no puede ver. Repásalas tú: Dialog vs Snackbar en el `.ts`, información esencial escondida en tooltips, Tabs usadas como pasos, abuso de cards, Grid List usada como layout.

Si la skill se instaló como plugin (o se configuró el hook a mano), un **hook PostToolUse** en Edit/Write ejecuta esta auditoría sobre las líneas que editas en proyectos con `@angular/material`. Cuando te devuelva hallazgos, resuélvelos antes de seguir.

## 4. Auditar un proyecto existente

1. Ejecuta `audit.py src/` (agrega `--json` si necesitas procesar la salida).
2. Haz la revisión manual de la sección 3 sobre los componentes principales.
3. Entrega un reporte agrupado por regla: cuántos casos hay, los archivos y líneas, y la corrección propuesta. Ordena primero los ERROR.
4. Si solo te pidieron auditar, ofrece corregir. Si te pidieron corregir, aplica primero los ERROR y luego las WARN que tengan sentido, y vuelve a ejecutar el script para confirmar.

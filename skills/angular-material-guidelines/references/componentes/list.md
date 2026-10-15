# List — `mat-list`, `mat-nav-list`, `mat-action-list`, `mat-selection-list`

Grupo vertical de elementos de texto, íconos e imágenes, pensado para leer rápido. Fuentes: [Angular Material](https://material.angular.dev/components/list/overview) · [M3](https://m3.material.io/components/lists/guidelines).

## Elige la variante según la interacción

| Los ítems… | Variante | Ítem |
|---|---|---|
| Solo muestran información | `mat-list` | `mat-list-item` |
| Navegan a otra ruta o URL | `mat-nav-list` | `<a mat-list-item>` |
| Ejecutan una acción | `mat-action-list` | `<button mat-list-item>` |
| Se seleccionan (uno o varios) | `mat-selection-list` (`[multiple]="false"` para uno) | `mat-list-option` |

Si un ítem tiene `(click)` o `routerLink` dentro de un `mat-list` común, usa la variante correcta. `[auditor: lista-interactiva]`

## No lo uses cuando
- Hay que comparar varios atributos entre filas: usa `mat-table`.
- El contenido es heterogéneo y con media: usa `mat-card`.
- Son datos jerárquicos: usa `mat-tree`.

## API clave
- Directivas para el contenido del ítem:
  - `matListItemTitle`: el título.
  - `matListItemLine`: cada línea extra.
  - `matListItemIcon` / `matListItemAvatar`: al inicio.
  - `matListItemMeta`: al final.
- `lines`: activa el ajuste de texto en varias líneas.
- `matSubheader`: título de sección.
- `[activated]`: marca el ítem activo en `mat-nav-list`.
- `mat-selection-list`: `(selectionChange)`, `togglePosition`, `hideSingleSelectionIndicator` (no lo ocultes).

## Reglas
- Un ítem con más de una línea **debe** usar `matListItemTitle`. `[auditor: lista-multilinea-sin-titulo]`
- Pon los visuales y el texto principal en la misma posición en todos los ítems. No varíes el orden de los elementos.
- Limita el texto de apoyo a 1–3 líneas y trunca según el tamaño de pantalla.
- Agrupa con `matSubheader` y separa grupos con `mat-divider`.

## Accesibilidad
- `mat-nav-list` y `mat-selection-list` llevan siempre `aria-label` o `aria-labelledby`. `[auditor: lista-sin-label]`
- En `mat-nav-list` envuelve los `<a>` en `<ul>`/`<li>`. En `mat-action-list` usa `role="list"` y envuelve los botones en `<li>`.
- No anides controles interactivos dentro de los enlaces de `mat-nav-list` ni dentro de `mat-list-option`. `[auditor: control-anidado]`
- `mat-list` común es decorativo. Si presenta contenido, usa `role="list"` en la lista y `role="listitem"` en cada ítem.

## Ejemplo
```html
<mat-nav-list aria-label="Secciones de la cuenta">
  <ul>
    @for (s of secciones; track s.ruta) {
      <li>
        <a mat-list-item [routerLink]="s.ruta" routerLinkActive #rla="routerLinkActive" [activated]="rla.isActive">
          <mat-icon matListItemIcon>{{ s.icono }}</mat-icon>
          <span matListItemTitle>{{ s.titulo }}</span>
          <span matListItemLine>{{ s.descripcion }}</span>
        </a>
      </li>
    }
  </ul>
</mat-nav-list>
```

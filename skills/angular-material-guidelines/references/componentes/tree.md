# Tree — `mat-tree`

Muestra datos jerárquicos que se expanden y colapsan. Fuente: [Angular Material](https://material.angular.dev/components/tree/overview).

## Úsalo cuando
- Hay datos con varios niveles de jerarquía: un explorador de archivos, categorías anidadas, un organigrama, permisos por módulo.

## No lo uses cuando
- La jerarquía tiene un solo nivel: usa `mat-list`, o `mat-expansion-panel` si el contenido es extenso.
- Es la navegación principal: usa `mat-nav-list` (con subgrupos si hace falta) dentro de `mat-sidenav`.
- Son datos tabulares con jerarquía: considera una tabla con filas expandibles.

## Tipos
- **Plano (flat):** los nodos se renderizan como hermanos, con sangría. Es más fácil de estilizar y es compatible con scroll virtual. Es el preferido para árboles grandes.
- **Anidado (nested):** los hijos van dentro del padre en el DOM, con `matTreeNodeOutlet`.

## API clave
- `[dataSource]` + `[childrenAccessor]` (o `[levelAccessor]` para datos planos). **No uses `treeControl`.** `[auditor: tree-control-legacy]`
- `mat-tree-node` / `mat-nested-tree-node` con `*matTreeNodeDef` (y `when:` para nodos con hijos).
- `isExpandable` en los nodos que se expanden.
- `matTreeNodeToggle` en el botón que expande o colapsa.
- `matTreeNodePadding`: sangría por nivel en árboles planos.
- `(activation)`: emite cuando el usuario activa un nodo con el teclado.
- `trackBy`: para datos que cambian.

## Reglas
- Pon el toggle en un `matIconButton` con `aria-label` dinámico ("Expandir Frutas" / "Colapsar Frutas") y un ícono que indique el estado (chevron).
- Si el nodo ejecuta una acción, escucha `(click)` **y** `(activation)`, para que también funcione con el teclado.
- Carga los hijos bajo demanda cuando el árbol es grande. Muestra un `mat-progress-spinner` pequeño (con `aria-label`) en el nodo que está cargando.
- No mezcles nodos expandibles y no expandibles sin una alineación consistente: deja el espacio del toggle vacío.

## Accesibilidad
- Implementa el widget tree (roles, ARIA y teclado), pero **solo con `childrenAccessor`/`levelAccessor`**. Con `treeControl` no se aplican las mejoras de accesibilidad.
- Marca `isExpandable` en todos los nodos expandibles para que se anuncie el estado.

## Ejemplo
```html
<mat-tree [dataSource]="categorias" [childrenAccessor]="hijos" aria-label="Categorías">
  <mat-tree-node *matTreeNodeDef="let n" matTreeNodePadding (click)="abrir(n)" (activation)="abrir($event)">
    {{ n.nombre }}
  </mat-tree-node>
  <mat-tree-node *matTreeNodeDef="let n; when: tieneHijos" matTreeNodePadding isExpandable>
    <button matIconButton matTreeNodeToggle [attr.aria-label]="'Expandir o colapsar ' + n.nombre">
      <mat-icon>chevron_right</mat-icon>
    </button>
    {{ n.nombre }}
  </mat-tree-node>
</mat-tree>
```

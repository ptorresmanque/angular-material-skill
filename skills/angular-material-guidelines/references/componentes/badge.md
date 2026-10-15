# Badge — `matBadge`

Indicador pequeño de estado o conteo sobre otro elemento. Fuentes: [Angular Material](https://material.angular.dev/components/badge/overview) · [M3](https://m3.material.io/components/badges/guidelines).

## Úsalo cuando
- Hay que mostrar un conteo asociado a un destino: notificaciones sin leer en un icon button, ítems del carrito, pendientes en un tab o ítem de navegación.
- Hay que marcar un estado "nuevo" sin cantidad. Para eso usa `matBadgeSize="small"`, que no muestra texto.

## No lo uses cuando
- El texto es largo: M3 limita el badge a 4 caracteres, incluido el "+". Para más texto usa un chip o texto normal.
- Es decoración sin significado.
- Es la única forma de comunicar información importante.

## API clave
- `matBadge`: el contenido.
- `matBadgePosition`: `above|below` + `before|after`. Por defecto `above after`.
- `matBadgeSize`: `small` | `medium` | `large`. El tamaño `small` no muestra texto.
- `matBadgeOverlap`: si el badge se superpone al contenido. Sí sobre íconos, no sobre texto.
- `matBadgeHidden`: oculta el badge.
- `matBadgeDescription`: descripción para lectores de pantalla (obligatoria).

## Reglas
- Limita el contenido a 4 caracteres: "99+".
- Oculta el badge con `[matBadgeHidden]` cuando el conteo es 0 y cuando el usuario ya vio el destino.
- Aplícalo a elementos de bloque.
- No cambies la posición de forma arbitraria. En RTL se invierte sola.
- Usa el color por defecto. Si lo personalizas, mantén un contraste de al menos 3:1.

## Accesibilidad
- `matBadgeDescription` es obligatorio. `[auditor: badge-sin-descripcion]`
  - En un elemento interactivo se aplica como `aria-describedby`.
  - En uno no interactivo se agrega como texto oculto.
- `mat-icon` es `aria-hidden` por defecto. Pon el badge en el botón que contiene el ícono, y ese botón debe tener su `aria-label`.

## Ejemplo
```html
<button matIconButton aria-label="Notificaciones"
        [matBadge]="pendientes()" [matBadgeHidden]="!pendientes()"
        [matBadgeDescription]="pendientes() + ' notificaciones sin leer'">
  <mat-icon>notifications</mat-icon>
</button>
```

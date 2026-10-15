# Divider — `mat-divider`

Línea que separa grupos de contenido. Fuentes: [Angular Material](https://material.angular.dev/components/divider/overview) · [M3](https://m3.material.io/components/divider/guidelines).

## Úsalo cuando
- Hay que separar secciones de contenido no relacionado: un divider de ancho completo.
- Hay que separar elementos relacionados dentro de una sección, como los ítems de una lista con avatar o ícono: un divider `inset`.
- Hay que separar el área interactiva de la no interactiva en un contenedor, por ejemplo en una card.
- Hay que agrupar ítems de un menú.

## No lo uses cuando
- El espacio en blanco o un título ya separa: demasiadas líneas ensucian la interfaz.
- Va entre todos los ítems de una lista simple sin avatar ni ícono: el espaciado basta.

## API clave
- `[inset]="true"`: línea con sangría.
- `[vertical]="true"`: línea vertical.

## Reglas
- Úsalos con moderación.
- Si en la misma pantalla usas dividers de ancho completo e inset, el de ancho completo separa tipos de contenido y el inset separa ítems anidados.
- En listas con dividers inset, no pongas uno en el último ítem: se superpone con el divider de la sección.

## Accesibilidad
- Tiene `role="separator"` y no recibe foco. No le agregues interacción.

## Ejemplo
```html
<mat-list>
  <h3 matSubheader>Carpetas</h3>
  @for (c of carpetas; track c.id; let ultimo = $last) {
    <mat-list-item>
      <mat-icon matListItemIcon>folder</mat-icon>
      <span matListItemTitle>{{ c.nombre }}</span>
      @if (!ultimo) { <mat-divider [inset]="true" /> }
    </mat-list-item>
  }
  <mat-divider />
</mat-list>
```

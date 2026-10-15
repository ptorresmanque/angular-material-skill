# Icon — `mat-icon`

Muestra íconos de fuente (Material Symbols) o SVG. Fuente: [Angular Material](https://material.angular.dev/components/icon/overview).

## Usos y cómo tratarlos

| Uso | Ejemplo | Cómo |
|---|---|---|
| **Decorativo** (no aporta significado) | Ícono junto a un texto que ya lo dice | Nada: `mat-icon` ya es `aria-hidden="true"` por defecto |
| **Interactivo** | Borrar, editar, abrir menú | Dentro de un `<button matIconButton>` o `<a>` con `aria-label`. Nunca `(click)` en el `mat-icon`. `[auditor: icono-clicable]` |
| **Indicador** (comunica algo y no es interactivo) | Estado "pagado" con un check | Agrega un texto oculto al lado (`<span class="cdk-visually-hidden">Pagado</span>`), o usa `aria-hidden="false"` + `aria-label` |

## API clave
- Íconos de fuente:
  - Ligadura: `<mat-icon>delete</mat-icon>`.
  - `fontSet` para elegir Material Symbols Outlined, Rounded o Sharp.
  - `fontIcon` para íconos de fuente por clase CSS.
- SVG:
  - `svgIcon="namespace:nombre"`, registrado con `MatIconRegistry` (`addSvgIcon`, `addSvgIconSet`, `addSvgIconLiteral`).
  - Las URLs pasan por `DomSanitizer`. Registra solo recursos de confianza.
- `MAT_ICON_DEFAULT_OPTIONS` / `MatIconRegistry.setDefaultFontSetClass()`: el set por defecto para toda la app.
- `class="mat-icon-rtl-mirror"`: invierte íconos direccionales (flechas) en RTL.

## Reglas
- Usa **un solo estilo** de íconos en toda la app (por ejemplo, solo Outlined), definido de forma global.
- Usa íconos reconocibles. Si el significado no es universal, acompáñalos de texto.
- No uses el ícono como única señal de un estado: agrega texto o color con contraste, además del texto oculto.
- Los íconos interactivos tienen un área táctil de 48×48 px; `matIconButton` ya la da.

## Ejemplo
```html
<button matIconButton aria-label="Eliminar pedido" (click)="eliminar(p)">
  <mat-icon>delete</mat-icon>
</button>

<span class="estado">
  <mat-icon>check_circle</mat-icon>
  <span class="cdk-visually-hidden">Pagado</span>
</span>
```

# Expansion Panel — `mat-expansion-panel`, `mat-accordion`

Panel con un encabezado que muestra u oculta su contenido (como `<details>`/`<summary>`). Fuente: [Angular Material](https://material.angular.dev/components/expansion/overview).

## Úsalo cuando
- Quieres revelar contenido de a poco: preguntas frecuentes, secciones de configuración, detalles opcionales.
- Hay formularios largos donde el usuario edita solo una parte. Combínalo con `mat-accordion` para que haya un panel abierto a la vez.

## No lo uses cuando
- El contenido es esencial y casi todos lo necesitan: muéstralo directo.
- Hay pasos con un orden: usa `mat-stepper`.
- Son vistas al mismo nivel que se recorren seguido: usa `mat-tab-group`.
- Es navegación: usa `mat-nav-list` o `mat-sidenav`.
- Son datos jerárquicos profundos: usa `mat-tree`.

## API clave
- `mat-expansion-panel-header` con `mat-panel-title` y `mat-panel-description`.
- Estado del panel:
  - `expanded`, `disabled` y `hideToggle`.
  - Eventos `(opened)` y `(closed)`.
- `mat-accordion`:
  - `multi`: permite varios paneles abiertos.
  - `displayMode`: `default` o `flat`.
  - `togglePosition`: `after` o `before`.
- Contenido diferido: `<ng-template matExpansionPanelContent>`, para contenido pesado.
- `mat-action-row`: fila de acciones al pie del panel.

## Reglas
- El título es corto. La descripción resume el estado ("3 direcciones guardadas"), no repite el título.
- Usa contenido diferido cuando el panel carga datos o componentes pesados.
- Las acciones del panel van en `mat-action-row` con la jerarquía de botones, no en el header.
- Si hay pocos paneles y el usuario los compara, permite varios abiertos (`multi`).

## Accesibilidad
- El header es un `role="button"` con `aria-controls`. **No pongas botones ni enlaces dentro del header.** `[auditor: control-anidado]`

## Ejemplo
```html
<mat-accordion>
  <mat-expansion-panel>
    <mat-expansion-panel-header>
      <mat-panel-title>Direcciones</mat-panel-title>
      <mat-panel-description>{{ direcciones().length }} guardadas</mat-panel-description>
    </mat-expansion-panel-header>
    <ng-template matExpansionPanelContent>
      <app-lista-direcciones />
    </ng-template>
    <mat-action-row>
      <button matButton type="button" (click)="agregar()">Agregar dirección</button>
    </mat-action-row>
  </mat-expansion-panel>
</mat-accordion>
```

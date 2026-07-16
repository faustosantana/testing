# 02 — DESIGN SYSTEM

## Nombre conceptual

**SGB Atlas Design System**

Atlas comunica control territorial, trazabilidad, activos y vision institucional.

## Fundamentos

| Fundamento | Definicion |
| --- | --- |
| Grid | 12 columnas desktop, 8 tablet, 4 movil. |
| Espaciado | Escala 4/8/12/16/24/32/48/64. |
| Radio | 8 px para controles, 12 px para cards, 16 px para paneles. |
| Elevacion | Sutil, solo para overlays, modales y cards destacadas. |
| Densidad | Compacta profesional, con opcion comfortable para usuarios nuevos. |
| Tema | Claro por defecto, oscuro opcional posterior para centro de monitoreo. |

## Tokens semanticos

| Token | Uso |
| --- | --- |
| `surface/base` | Fondo principal. |
| `surface/panel` | Cards y contenedores. |
| `text/primary` | Titulos y datos criticos. |
| `text/secondary` | Metadata y ayudas. |
| `action/primary` | Accion principal. |
| `status/success` | Aprobado, activo, completo. |
| `status/warning` | Atencion, vencimiento, pendiente. |
| `status/danger` | Critico, vencido, bloqueado. |
| `status/info` | Informacion, borrador, seguimiento. |

## Patrones globales

- header compacto con busqueda global;
- sidebar por modulos;
- breadcrumbs persistentes;
- panel derecho para detalles contextuales;
- command palette para usuarios avanzados;
- filtros guardables;
- vistas tabla/kanban/mapa cuando aplique;
- activity feed por expediente;
- audit trail siempre disponible segun permisos.

## Estados globales

- loading;
- empty;
- error;
- no permission;
- pending approval;
- archived;
- critical alert;
- offline/degraded.

## Regla de consistencia

Cada modulo debe compartir:

1. titulo claro;
2. accion primaria unica;
3. filtros visibles;
4. tabla o lista principal;
5. panel de detalle;
6. historial/auditoria;
7. exportacion controlada cuando aplique.

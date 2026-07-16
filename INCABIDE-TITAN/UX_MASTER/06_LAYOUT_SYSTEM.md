# 06 — LAYOUT SYSTEM

## Estructura base

```text
Top bar: busqueda global, alertas, usuario
Sidebar: modulos principales
Content: titulo, KPIs, filtros, tabla/lista/mapa
Right panel: detalle contextual
Footer opcional: estado del sistema / ayuda
```

## Layouts principales

| Layout | Uso |
| --- | --- |
| Executive cockpit | Direccion y supervision de KPIs. |
| Operational list | Tablas, filtros y acciones masivas. |
| Record detail | Expediente de bien, caso, contrato o subasta. |
| Split view | Lista izquierda + detalle derecho. |
| Map view | Bienes por ubicacion territorial. |
| Workflow view | Timeline, cadena de custodia, aprobaciones. |
| Report builder | Filtros, visualizaciones y exportacion. |

## Grid y espaciado

- Desktop: 12 columnas.
- Tablet: 8 columnas.
- Mobile: 4 columnas.
- Max width para lectura: controlar lineas largas.
- Cards con separacion consistente.
- Acciones primarias alineadas al titulo o panel contextual.

## Densidad de informacion

| Vista | Densidad |
| --- | --- |
| Director | Baja densidad, alto contexto, KPIs. |
| Gerente | Densidad media, alertas y listas priorizadas. |
| Operador | Densidad alta controlada, tablas y formularios. |
| Auditor | Densidad alta, trazabilidad y filtros. |

## Responsive

- Mobile prioriza consulta, aprobaciones simples y alertas.
- Formularios complejos deben ser desktop-first.
- Tablas se transforman en cards en movil.
- Mapas deben permitir lista alternativa.

## Regla de oro

Cada pantalla debe responder: "Que esta pasando, que requiere atencion y cual es la siguiente accion segura".

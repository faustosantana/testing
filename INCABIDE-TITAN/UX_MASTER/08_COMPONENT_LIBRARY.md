# 08 — COMPONENT LIBRARY

## Biblioteca base

| Componente | Variantes | Uso |
| --- | --- | --- |
| Botones | primary, secondary, ghost, danger, icon, split | Acciones principales y secundarias. |
| Tablas | compacta, avanzada, seleccion multiple, sticky columns | Inventario, auditoria, usuarios, reportes. |
| Cards | KPI, resumen, alerta, expediente, documento | Dashboards y vistas de resumen. |
| Modales | confirmacion, formulario corto, seleccion, alerta critica | Acciones focalizadas. |
| Filtros | chips, panel avanzado, fechas, provincia, estado, categoria | Busqueda y segmentacion. |
| Buscador | global, contextual, typeahead | Casos, bienes, documentos. |
| Breadcrumbs | simple, con acciones | Contexto de navegacion. |
| Timeline | vertical, horizontal, agrupada | Expediente, cadena de custodia, auditoria. |
| Badges | estado, prioridad, confidencialidad, rol | Lectura rapida. |
| Indicadores | semaforo, progreso, SLA, health | Dashboards y soporte. |
| Graficas | barras, lineas, dona, area, sparkline | KPIs y reportes. |
| Mapas | cluster, heatmap, puntos, provincia | Bienes por ubicacion. |
| Estados | empty, loading, error, no permission, success | Feedback del sistema. |

## Botones

| Tipo | Uso |
| --- | --- |
| Primary | Una accion principal por pantalla. |
| Secondary | Acciones alternativas seguras. |
| Ghost | Acciones de baja prioridad. |
| Danger | Acciones destructivas con confirmacion. |
| Icon | Acciones repetitivas en tablas con tooltip. |

## Tablas enterprise

Requisitos:

- columnas configurables;
- filtros guardables;
- ordenamiento;
- seleccion multiple con permisos;
- acciones por fila;
- exportacion controlada;
- estado vacio;
- paginacion;
- columnas sticky para codigo/estado;
- indicadores de confidencialidad.

## Cards KPI

Cada card debe tener:

- etiqueta;
- valor principal;
- variacion;
- periodo;
- semaforo;
- accion secundaria opcional;
- enlace a detalle.

## Timeline

Debe soportar:

- fecha/hora;
- usuario;
- accion;
- estado anterior/nuevo;
- documento relacionado;
- comentario;
- evidencia;
- indicador de evento critico.

## Mapas

Componentes:

- mapa por provincia;
- clusters;
- panel de filtros;
- lista sincronizada;
- leyenda;
- tooltip de bien;
- drill-down por provincia/municipio.

## Modales

Reglas:

- usar para decisiones cortas;
- no usar para formularios largos;
- siempre indicar consecuencia;
- confirmar acciones destructivas;
- permitir cancelar sin perdida.

## Estados

Estados requeridos:

- sin datos;
- sin permisos;
- cargando;
- error recuperable;
- error critico;
- guardado exitoso;
- borrador;
- pendiente aprobacion.

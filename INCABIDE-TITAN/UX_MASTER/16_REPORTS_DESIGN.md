# 16 — REPORTS DESIGN

## Objetivo

Reportes modernos, filtrables, exportables y orientados a decision.

## Tipos de reportes

| Tipo | Uso |
| --- | --- |
| Ejecutivo | KPIs agregados y tendencias. |
| Operativo | Listas accionables y pendientes. |
| Auditoria | Eventos, accesos, cambios y exportaciones. |
| Financiero | Valor, pagos, depreciacion y conciliacion. |
| Territorial | Bienes por provincia/municipio. |
| Documental | Documentos faltantes, vencidos o confidenciales. |

## Estructura

1. Titulo y descripcion.
2. Filtros principales.
3. KPIs de resumen.
4. Visualizacion.
5. Tabla detallada.
6. Acciones: exportar, guardar, compartir segun permisos.

## Filtros estandar

- periodo;
- provincia;
- municipio;
- categoria;
- estado;
- responsable;
- entidad remitente;
- valor;
- nivel de alerta.

## Exportacion

- PDF para presentacion;
- Excel/CSV para analisis;
- registro de auditoria en exportaciones sensibles;
- marca de agua o metadata cuando aplique.

## Buenas practicas

- cada grafica debe explicar que decision habilita;
- no usar mas de 5 colores por grafica;
- tablas deben permitir drill-down;
- reportes guardados por usuario/rol;
- reportes ejecutivos con fecha de corte clara.

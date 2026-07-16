# 09 — DASHBOARD DESIGN

## Tipos de dashboard

| Dashboard | Audiencia | Proposito |
| --- | --- | --- |
| Ejecutivo | Director / alta direccion | Decision en menos de 30 segundos. |
| Operativo | Gerentes / supervisores | Priorizacion diaria. |
| Tecnico | TI / soporte | Salud de plataforma. |
| Auditoria | Auditor / cumplimiento | Control de eventos sensibles. |

## Dashboard Ejecutivo

Debe responder rapidamente:

- cuantos bienes existen;
- valor economico;
- bienes por provincia;
- bienes por estado;
- alertas;
- proximas subastas;
- procesos criticos;
- KPIs.

## Estructura ejecutiva

```text
Header: estado institucional + fecha de corte
Fila 1: KPIs principales
Fila 2: mapa provincial + bienes por estado
Fila 3: alertas criticas + proximas subastas
Fila 4: procesos criticos + tendencias
Panel derecho: acciones ejecutivas y decisiones pendientes
```

## KPIs ejecutivos

| KPI | Descripcion |
| --- | --- |
| Total de bienes | Conteo general y variacion. |
| Valor economico estimado | Total y tendencia. |
| Bienes por estado | Custodia, subasta, donacion, devolucion, destruccion. |
| Bienes por provincia | Distribucion territorial. |
| Alertas criticas | Riesgos, vencimientos, bloqueos. |
| Proximas subastas | Eventos por fecha y valor estimado. |
| Procesos criticos | Casos o bienes con accion urgente. |
| Cumplimiento operativo | Porcentaje de procesos dentro de plazo. |

## Dashboard Operativo

Enfocado en:

- tareas pendientes;
- bienes recientes;
- vencimientos;
- aprobaciones;
- documentos incompletos;
- pagos atrasados;
- soporte/incidentes;
- excepciones de auditoria.

## Reglas visuales

- no mas de 7 KPIs principales visibles al primer scroll;
- alertas criticas siempre arriba;
- graficas con drill-down;
- cada KPI debe llevar a una lista filtrada;
- mapas con resumen numerico alternativo;
- uso moderado de color.

## Alertas

| Tipo | Ejemplo |
| --- | --- |
| Critica | Bien sin documentacion obligatoria. |
| Operativa | Contrato por vencer. |
| Seguridad | Acceso fallido repetido. |
| Proceso | Aprobacion detenida. |
| Subasta | Evento proximo o conciliacion pendiente. |

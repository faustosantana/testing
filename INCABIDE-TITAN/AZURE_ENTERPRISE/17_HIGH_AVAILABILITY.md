# 17 — HIGH AVAILABILITY

## Objetivo

Definir opciones de alta disponibilidad para cumplir el requisito de redundancia y disponibilidad, sin fijar nivel final hasta validar RTO/RPO y presupuesto.

## Opciones

| Capa | Opcion HA | Estado |
| --- | --- | --- |
| Entrada | Front Door o Application Gateway con redundancia segun servicio. | PENDIENTE DE VALIDACION |
| Aplicacion | Multiples replicas en Container Apps o alternativa. | PENDIENTE DE VALIDACION |
| Base de datos | HA de PostgreSQL Flexible Server si se aprueba. | PENDIENTE DE VALIDACION |
| Storage | Redundancia local/zonal/regional segun decision. | PENDIENTE DE VALIDACION |
| Observabilidad | Workspace y alertas configuradas. | Recomendado |

## Riesgos

- HA aumenta costo.
- Region seleccionada puede limitar zonas.
- RTO/RPO no definidos.
- Volumen de carga no definido.

## Recomendacion conceptual

Diseñar para HA razonable desde el inicio, pero activar niveles avanzados segun aprobacion de INCABIDE/PADF y estrategia economica.

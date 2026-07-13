# 12 — DISASTER RECOVERY

## Objetivo

Definir recuperacion ante fallas mayores, cumpliendo DRP, alta disponibilidad y redundancia exigidas por la RFP.

## Escenarios

| Escenario | Respuesta |
| --- | --- |
| Falla aplicacion | Reinicio/rollback del contenedor. |
| Falla base de datos | Restauracion o failover segun HA validada. |
| Corrupcion datos | Restauracion punto en tiempo si disponible. |
| Incidente seguridad | Contencion, rotacion secretos, analisis, remediacion. |
| Falla region | Estrategia PENDIENTE DE VALIDACION. |

## Modelo DR conceptual

- backups cifrados;
- runbook de recuperacion;
- pruebas periodicas;
- roles de respuesta;
- comunicacion;
- evidencias;
- plan de remediacion.

## RTO/RPO

`PENDIENTE DE VALIDACION`. La RFP exige DRP pero no fija tiempos.

## Alternativas

| Modelo | Ventaja | Riesgo |
| --- | --- | --- |
| Backup/restore regional | Menor complejidad. | Mayor RTO. |
| HA zonal | Mayor disponibilidad. | Costo y region. |
| Replica regional | Mejor continuidad. | Mayor costo y complejidad. |

## Criticidad

Critica por tratarse de datos sensibles y operacion institucional.

# 18 — BUSINESS CONTINUITY

## Objetivo

Mantener continuidad operacional del SGB ante incidentes tecnicos, fallas de seguridad, errores de despliegue o indisponibilidad parcial.

## Capacidades

- soporte con SLA;
- monitoreo y alertas;
- backups restaurables;
- runbooks;
- rollback;
- DRP;
- control de accesos;
- comunicacion de incidentes.

## Escenarios de continuidad

| Escenario | Respuesta |
| --- | --- |
| Caida aplicacion | Alertar, diagnosticar, reiniciar/rollback. |
| Error release | Rollback y validacion. |
| Falla backup | Escalamiento y remediacion. |
| Incidente critico | Soporte fuera de horario segun RFP. |
| Brecha seguridad | Contencion, investigacion, remediacion. |

## Pendiente de validacion

- Ventanas de mantenimiento.
- Responsables INCABIDE.
- Protocolo de comunicacion.
- Horario operativo real.
- Limite de soporte critico.

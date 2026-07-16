# 11 — OPERATION MODEL

## Objetivo

Definir como se operara el SGB despues de su puesta en produccion, considerando disponibilidad, seguridad, soporte, cambios y transferencia a INCABIDE.

## Modelo operativo

| Dimension | Diseno objetivo |
| --- | --- |
| Gobierno | Roles claros entre Justech, PADF e INCABIDE. |
| Operacion diaria | Monitoreo, alertas, revision de backups y seguimiento de incidentes. |
| Cambios | Solicitud, evaluacion, aprobacion, despliegue y evidencia. |
| Seguridad | Revision de accesos, logs, vulnerabilidades y eventos. |
| Continuidad | Backups, restauracion, DRP y runbooks. |
| Transferencia | Documentacion y capacitacion para equipo tecnico INCABIDE. |

## Roles operativos

| Rol | Responsabilidad |
| --- | --- |
| Administrador INCABIDE | Gestion de usuarios, accesos y validaciones funcionales. |
| Equipo tecnico INCABIDE | Operacion basica, revision de runbooks y ejecucion guiada. |
| Soporte Justech | Atencion de incidentes, escalamiento y mantenimiento durante soporte. |
| DevSecOps | Cambios tecnicos, seguridad, despliegues y monitoreo. |
| QA | Validacion de correcciones y evidencias. |

## Rutinas operativas

| Frecuencia | Actividad |
| --- | --- |
| Diaria | Revisar disponibilidad, alertas criticas y errores. |
| Semanal | Revisar logs, backups, capacidad y tickets. |
| Mensual | Revisar usuarios privilegiados, vulnerabilidades y salud del sistema. |
| Por release | Ejecutar pruebas, evidencias, aprobacion y plan de rollback. |
| Por incidente | Registrar, clasificar, atender, cerrar y documentar lecciones. |

## Gestion de incidentes

1. Recepcion por canal autorizado.
2. Clasificacion: critico, mayor, menor.
3. Confirmacion de impacto.
4. Asignacion responsable.
5. Diagnostico.
6. Solucion o workaround.
7. Validacion con usuario.
8. Cierre documentado.
9. Analisis causa raiz cuando aplique.

## Gestion de accesos

- altas, bajas y cambios autorizados;
- revision periodica de privilegios;
- MFA para administradores;
- segregacion de cuentas;
- trazabilidad de accesos;
- entrega segura de credenciales;
- declaracion de no retencion por proveedor.

## Entregables operativos

- runbook de operacion;
- matriz de roles;
- procedimiento de soporte;
- procedimiento de backup/restore;
- procedimiento de despliegue;
- procedimiento de escalamiento;
- checklist de salud;
- reporte periodico de soporte.

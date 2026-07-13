# 17 — DISASTER RECOVERY

## Objetivo

Definir el enfoque conceptual de recuperacion ante desastres para proteger la continuidad del SGB y cumplir el requisito de backups cifrados y DRP.

## Escenarios de contingencia

| Escenario | Impacto | Respuesta esperada |
| --- | --- | --- |
| Caida de aplicacion | Usuarios sin acceso. | Restart/rollback y health checks. |
| Falla base de datos | Perdida o indisponibilidad transaccional. | Restauracion desde backup validado. |
| Corrupcion de datos | Datos inconsistentes. | Restauracion parcial o plan compensatorio. |
| Incidente seguridad | Riesgo de confidencialidad/integridad. | Contencion, investigacion y remediacion. |
| Perdida de archivos | Evidencia o documentos no disponibles. | Restauracion de almacenamiento. |
| Error de despliegue | Version productiva inestable. | Rollback controlado. |

## Componentes DR

- backups automaticos cifrados;
- prueba de restauracion;
- runbook de recuperacion;
- inventario de responsables;
- criterios de escalamiento;
- comunicacion de incidente;
- evidencias de recuperacion;
- revision posterior.

## RTO/RPO

La RFP exige DRP, alta disponibilidad y backups, pero no define RTO ni RPO. Estos valores deben confirmarse con PADF/INCABIDE antes de arquitectura detallada.

## Estrategia de backup conceptual

| Elemento | Enfoque |
| --- | --- |
| Base de datos | Backup automatico cifrado y restauracion probada. |
| Media storage | Replicacion/backup segun politica aprobada. |
| Configuracion | Versionado seguro sin secretos. |
| Secretos | Vault con control de acceso y recuperacion. |
| Codigo | Repositorio Git designado por INCABIDE. |

## Prueba de restauracion

1. Seleccionar backup.
2. Restaurar en entorno controlado.
3. Verificar integridad de base de datos.
4. Verificar archivos asociados.
5. Ejecutar health checks.
6. Documentar resultado.
7. Registrar aprobacion.

## Runbook DR minimo

- criterio de activacion;
- responsables;
- contactos;
- pasos de restauracion;
- validaciones;
- comunicacion a usuarios;
- cierre;
- lecciones aprendidas.

## Evidencia para RFP

El Hito 4 exige registro de respaldo operativo y restaurable; el Hito 5 exige procedimiento de restauracion en documentacion tecnica.

# 11 — BACKUP RECOVERY

## Objetivo

Garantizar backups automaticos, cifrados y restaurables para base de datos, archivos y configuracion operativa.

## Alcance

| Recurso | Estrategia conceptual |
| --- | --- |
| PostgreSQL | Backups automaticos del servicio gestionado; retencion pendiente. |
| Blob Storage | Versionado/replicacion/backup segun politica. |
| Configuracion | Repositorio y documentacion versionada, sin secretos. |
| Secretos | Key Vault con proteccion y controles. |
| Imagenes | ACR con retencion y tags controlados. |

## Requisitos

- backups automaticos;
- cifrado;
- prueba de restauracion;
- evidencia de respaldo operativo;
- procedimiento de restauracion en documentacion tecnica.

## Restore test

1. Seleccionar backup.
2. Restaurar en entorno controlado.
3. Validar integridad.
4. Validar aplicacion.
5. Documentar resultado.
6. Registrar evidencia.

## Riesgos

- RPO/RTO no definidos;
- retencion no definida;
- volumen desconocido;
- costos de almacenamiento no estimables aun;
- restore no probado.

## Pendiente de validacion

- RPO.
- RTO.
- Retencion.
- Region secundaria.
- Frecuencia de prueba restore.

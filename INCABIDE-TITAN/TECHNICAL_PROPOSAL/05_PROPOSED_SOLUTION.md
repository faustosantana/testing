# 05 — PROPOSED SOLUTION

## Objetivo

Describir la solucion tecnica propuesta para responder al alcance funcional, tecnico, de seguridad, operacion y evolucion definido en la RFP.

## Solucion propuesta

La solucion propone modernizar el SGB existente mediante una arquitectura cloud en Microsoft Azure, manteniendo compatibilidad con Django/Python y PostgreSQL/PostGIS/unaccent, incorporando contenerizacion, configuracion segura, almacenamiento de medios, API funcional, monitoreo, backups, seguridad reforzada y documentacion operativa.

## Componentes de solucion

| Componente | Rol en la solucion |
| --- | --- |
| SGB Django/Python | Aplicacion base y modulos funcionales. |
| PostgreSQL/PostGIS/unaccent | Persistencia transaccional, geografica y busqueda sin acentos. |
| Azure | Plataforma obligatoria de despliegue. |
| Contenedores | Unidad de ejecucion y despliegue. |
| Blob Storage | Archivos, documentos y multimedia. |
| Key Vault / Managed Identity | Gestion segura de secretos. |
| WAF / Firewall / VPN / MFA | Seguridad de acceso, red y aplicacion. |
| Monitor / Log Analytics / App Insights | Observabilidad y auditoria tecnica. |
| QA/UAT | Evidencia de aceptacion por hito y modulo. |

## Relacion con la RFP

Responde al Anexo 2: descripcion general del servicio, Etapa I, requisitos de seguridad, SLA, evidencias, Etapa II y entregables por modulo.

## Requisitos cubiertos

- TEC-010 a TEC-026.
- AZ-001 a AZ-015.
- SEC-001 a SEC-038.
- FUNC-GEN-001 a FUNC-GEN-010.
- FUNC-001 a FUNC-191.

## Evidencias necesarias

- Arquitectura implementada.
- Repositorio Git.
- Evidencias de seguridad.
- Documentacion tecnica.
- UAT y actas.

## Dependencias

- Validacion de region Azure.
- Validacion de modelo de computo.
- Alcance API.
- Datos/volumen/usuarios.

## Pendientes de informacion de Justech

- Confirmar stack operativo propuesto por Justech.
- Confirmar herramientas DevSecOps.
- Confirmar capacidades de monitoreo y soporte.

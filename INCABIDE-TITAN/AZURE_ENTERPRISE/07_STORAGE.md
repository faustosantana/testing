# 07 — STORAGE

## Objetivo

Almacenar archivos, documentos, imagenes, videos y evidencias del SGB de forma segura, cifrada, escalable y auditable.

## Servicio recomendado

Azure Blob Storage.

## Justificacion

La RFP exige un servicio de almacenamiento para archivos y documentos del sistema. Blob Storage ofrece almacenamiento de objetos, cifrado, control de acceso, integracion privada y escalabilidad.

## Diseno conceptual

| Elemento | Decision |
| --- | --- |
| Contenedores logicos | Por dominio o confidencialidad, PENDIENTE DE VALIDACION. |
| Acceso | Private Endpoint + RBAC/Managed Identity recomendado. |
| Cifrado | En reposo por defecto; CMK PENDIENTE DE VALIDACION. |
| Retencion | PENDIENTE DE VALIDACION. |
| Versionado | Recomendado para documentos sensibles. |
| Lifecycle | PENDIENTE DE VALIDACION por retencion legal. |

## Riesgos

- volumen multimedia desconocido;
- tipos/tamanos de archivo no definidos;
- retencion legal no definida;
- necesidad de antivirus/malware scanning pendiente;
- costos variables por almacenamiento/transacciones.

## Alternativas

- Azure Files: util para compatibilidad de filesystem, menos ideal para objetos web.
- Base de datos: no recomendado para multimedia.
- Storage externo: no recomendado por gobierno y seguridad.

## Criticidad

Alta: almacena evidencia y documentos del ciclo de vida del bien.

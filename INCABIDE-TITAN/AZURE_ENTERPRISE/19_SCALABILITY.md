# 19 — SCALABILITY

## Objetivo

Permitir que el SGB crezca en usuarios, modulos, documentos, datos geoespaciales e integraciones.

## Escalabilidad por capa

| Capa | Estrategia |
| --- | --- |
| Entrada | WAF/entrada gestionada con capacidad escalable. |
| Aplicacion | Replicas de contenedores segun carga. |
| Base de datos | Escalado vertical/horizontal segun capacidades PostgreSQL. |
| Storage | Blob Storage escalable para multimedia. |
| Observabilidad | Ajuste de ingesta y retencion. |
| API | Versionado y limites segun consumo. |

## Variables necesarias

- usuarios totales;
- usuarios concurrentes;
- volumen de activos;
- volumen multimedia;
- frecuencia de reportes;
- integraciones;
- crecimiento anual;
- SLA esperado.

## Riesgos

- sobredimensionar sin datos;
- subdimensionar para Hito 4;
- reportes pesados;
- multimedia sin limites;
- API sin rate limits.

## Pendiente de validacion

Todas las variables de carga y crecimiento.

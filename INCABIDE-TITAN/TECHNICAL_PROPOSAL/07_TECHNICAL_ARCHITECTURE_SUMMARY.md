# 07 — TECHNICAL ARCHITECTURE SUMMARY

## Objetivo

Resumir la arquitectura tecnica de la solucion, alineada con el Solution Blueprint y Azure Enterprise Architecture.

## Arquitectura resumida

La solucion se organiza en capas:

- experiencia web SGB;
- aplicacion Django/Python;
- API funcional del SGB;
- PostgreSQL 14+ con PostGIS/unaccent;
- almacenamiento de medios;
- seguridad e identidad;
- monitoreo y auditoria;
- backups y recuperacion;
- integraciones externas controladas.

## Relacion con la RFP

Responde al requerimiento de desplegar el SGB sobre una plataforma tecnologica segura, moderna y escalable, con Azure como plataforma obligatoria.

## Requisitos cubiertos

- TEC-001 a TEC-026.
- AZ-001 a AZ-015.
- SEC-003 a SEC-038.
- QA-004 a QA-012.

## Evidencias necesarias

- Diagrama de arquitectura implementada.
- Componentes activos y documentados.
- Credenciales entregadas de forma segura.
- API validada.
- Certificado TLS.

## Dependencias

- Region Azure.
- Tenant/suscripcion.
- Modelo de computo.
- Ambientes.
- RTO/RPO.

## Pendientes de informacion de Justech

- Arquitectos asignados.
- Experiencia real en arquitectura Azure.
- Certificaciones reales disponibles.

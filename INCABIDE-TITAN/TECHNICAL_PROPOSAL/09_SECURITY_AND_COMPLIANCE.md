# 09 — SECURITY AND COMPLIANCE

## Objetivo

Describir el enfoque de seguridad y cumplimiento para proteger datos sensibles de INCABIDE y cumplir la RFP.

## Enfoque

La solucion adopta seguridad reforzada desde el diseno:

- cifrado en transito y reposo;
- MFA para accesos administrativos;
- controles de acceso por rol;
- auditoria;
- minimizacion de datos;
- gestion segura de credenciales;
- WAF con proteccion OWASP Top 10;
- DDoS;
- VPN para administracion;
- secretos en vault;
- monitoreo y alertas;
- escaneos;
- pentest tercero post-produccion.

## Relacion con la RFP

Responde a la Ley 172-13, residencia/transmision de datos, confidencialidad, seguridad de infraestructura y evidencias requeridas antes de aprobar produccion.

## Requisitos cubiertos

- SEC-001 a SEC-038.
- PEN-012/PEN-013 riesgos por brecha de seguridad.
- QA-015, QA-024, QA-031/032 equivalentes de cierre.

## Evidencias necesarias

- Documento de arquitectura de seguridad.
- Informe de vulnerabilidades CVSS.
- Reporte TLS minimo A.
- Evidencia MFA.
- Registro de backup restaurable.
- Declaracion sin credenciales en codigo.
- Informe pentest.

## Dependencias

- Politicas de seguridad INCABIDE/PADF.
- Proveedor de pentest.
- Definicion de retencion de logs.
- Decision sobre llaves gestionadas.

## Pendientes de informacion de Justech

- Politicas internas de seguridad.
- Certificaciones de seguridad reales.
- Procedimientos de gestion de incidentes.
- Herramientas de escaneo disponibles.

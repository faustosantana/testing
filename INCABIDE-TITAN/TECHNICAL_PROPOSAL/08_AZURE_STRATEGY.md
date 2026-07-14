# 08 — AZURE STRATEGY

## Estrategia Azure

La RFP establece que Microsoft Azure es la plataforma obligatoria para el despliegue del SGB. La estrategia propuesta adopta una arquitectura Azure Enterprise orientada a seguridad, operacion, trazabilidad y transferencia de control a INCABIDE. No se plantea Azure como un servidor en la nube, sino como una plataforma gobernada que integra red, identidad, contenedores, base de datos, almacenamiento, secretos, monitoreo, backups y recuperacion.

## Arquitectura objetivo

La arquitectura Azure recomendada se compone de:

- Microsoft Entra ID para identidad, MFA y RBAC;
- Azure Virtual Network con subredes segmentadas;
- Azure Front Door WAF y/o Application Gateway WAF para proteccion web;
- Azure Firewall y NSG para control de trafico;
- VPN Gateway o Bastion para administracion segura;
- Azure Container Apps o alternativa validada para ejecutar contenedores;
- Azure Container Registry para imagenes privadas;
- Azure Database for PostgreSQL Flexible Server con PostGIS y unaccent, sujeto a validacion;
- Azure Blob Storage para documentos y multimedia;
- Azure Key Vault y Managed Identity para secretos;
- Azure Monitor, Application Insights, Log Analytics y Defender for Cloud;
- politicas de backup, restore test y DRP.

## Red y seguridad

La red debe separar entrada, aplicacion, datos, endpoints privados, administracion y firewall. Los servicios de datos —PostgreSQL, Storage y Key Vault— deben exponerse preferiblemente mediante Private Endpoints, reduciendo exposicion publica. Los accesos administrativos deben realizarse por VPN, Bastion o mecanismo seguro aprobado, evitando puertos administrativos abiertos a Internet.

## Alta disponibilidad y continuidad

La arquitectura permite aplicar alta disponibilidad por capas: entrada, aplicacion, base de datos, almacenamiento y monitoreo. El nivel final depende de RTO, RPO, region, presupuesto y criticidad acordada con INCABIDE/PADF. La base minima debe incluir backups automaticos cifrados, prueba de restauracion y plan de recuperacion ante desastres.

## Decisiones pendientes de validacion

Algunas decisiones no pueden cerrarse sin validacion de PADF/INCABIDE:

- region Azure;
- tenant y suscripcion;
- ambientes requeridos;
- Container Apps vs VM Docker si PADF exige una lectura literal del componente VM;
- WAF unico o doble capa;
- DDoS Basic vs Standard;
- VPN Gateway vs Bastion;
- RTO/RPO;
- retencion de logs y backups;
- volumen de datos y multimedia.

Estas decisiones deben mantenerse explicitas para evitar compromisos prematuros.

## Trazabilidad RFP

Este capitulo cubre AZ-001 a AZ-015, SEC-010 a SEC-038, QA-007 a QA-012 y los requerimientos de estimacion de infraestructura Azure sin incluir precios.

## Informacion pendiente de Justech

Justech debe confirmar:

- experiencia real en Azure;
- certificaciones Microsoft/Azure reales, si existen;
- herramientas de monitoreo y operacion;
- capacidad de administrar infraestructura cloud por un ano;
- postura sobre costos, soporte y transferencia de suscripcion.

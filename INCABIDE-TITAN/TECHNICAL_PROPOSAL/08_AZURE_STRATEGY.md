# 08 — AZURE STRATEGY

## Objetivo

Presentar la estrategia Azure de alto nivel para desplegar el SGB cumpliendo seguridad, operacion, monitoreo, backups y transferencia de control.

## Estrategia

La estrategia Azure se basa en servicios nativos y controles Enterprise:

- Microsoft Entra ID para identidad, MFA y RBAC.
- Azure Virtual Network con subredes segmentadas.
- Private Endpoints para servicios de datos.
- WAF, Firewall, NSG y VPN/Bastion para proteccion de red y acceso.
- Plataforma de contenedores validada para ejecutar Docker.
- Azure Database for PostgreSQL compatible con PostGIS/unaccent.
- Blob Storage para medios y documentos.
- Key Vault y Managed Identity para secretos.
- Azure Monitor, Application Insights, Log Analytics y Defender for Cloud.
- Backup, Recovery y DRP.

## Relacion con la RFP

La RFP exige Microsoft Azure, computo para contenedores, PostgreSQL 14+ o equivalente, almacenamiento, dominio personalizado, TLS, WAF, DDoS, VPN, MFA, monitoreo, backups y DRP.

## Requisitos cubiertos

- AZ-001 a AZ-015.
- SEC-010 a SEC-038.
- QA-007 a QA-012.
- COST-017 como base para estimacion posterior, sin precios.

## Evidencias necesarias

- Arquitectura implementada.
- Evidencias de configuracion.
- TLS activo.
- Backups restaurables.
- Accesos verificados.

## Dependencias

- Region y tenant.
- Suscripcion Azure.
- DNS.
- Nivel HA/DR.
- Volumen de datos y usuarios.

## Pendientes de informacion de Justech

- Capacidad Azure real.
- Certificaciones Microsoft reales.
- Partner/designaciones reales si existen.
- Herramientas de monitoreo/operacion usadas por Justech.

# 05 — SECURITY ARCHITECTURE

## Objetivo

Implementar seguridad reforzada para datos sensibles del SGB, cumpliendo cifrado, MFA, RBAC, auditoria, WAF, DDoS, secretos, monitoreo, escaneos, backups y DRP.

## Capas de seguridad

| Capa | Controles |
| --- | --- |
| Identidad | Entra ID, MFA, RBAC, minimo privilegio. |
| Perimetro | WAF, DDoS, TLS, firewall. |
| Red | VNet, subredes, NSG, VPN, private endpoints. |
| Aplicacion | Autorizacion, validacion, auditoria, secretos fuera del codigo. |
| Datos | Cifrado, backups, acceso privado, logs. |
| Operacion | Monitor, Defender, alertas, pentest, escaneos. |

## Servicios

| Servicio | Objetivo | Justificacion | Dependencias | Ventajas | Riesgos | Alternativas | Criticidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WAF | Proteger OWASP Top 10. | Requisito RFP. | Front Door/App Gateway. | Proteccion web. | Falsos positivos. | WAF externo. | Critica |
| Defender for Cloud | Postura cloud y recomendaciones. | Escaneos y hardening. | Suscripcion. | Visibilidad de riesgo. | Costo/planes. | Herramientas externas. | Alta |
| Key Vault | Secretos y llaves. | Credenciales nunca en codigo. | Entra/MI. | Control y auditoria. | Permisos mal configurados. | Secretos en variables no recomendado. | Critica |
| Managed Identity | Acceso sin secretos. | Reduce credenciales. | Entra ID. | Rotacion simplificada. | Compatibilidad app. | Service principal. | Alta |
| TLS | Cifrado en transito. | Requisito RFP. | DNS/certificados. | Confianza. | Gestion de renovacion. | Cert manual. | Critica |
| Backup cifrado | Recuperacion. | Requisito RFP. | Politicas. | Continuidad. | Restore no probado. | Backup manual no recomendado. | Critica |

## Evidencias esperadas

- documento de arquitectura de seguridad;
- capturas/configuracion de controles;
- reporte de vulnerabilidades CVSS;
- certificado TLS con calificacion minima requerida;
- prueba de MFA;
- respaldo restaurable;
- declaracion de no credenciales en codigo;
- pentest tercero post-produccion.

## Pendiente de validacion

- Nivel DDoS.
- WAF final.
- Politica de retencion de logs.
- Proveedor de pentest.
- Criterios de severidad post-pentest.

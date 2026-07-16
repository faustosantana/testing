# AZURE DECISION MATRIX

## Decisiones pendientes

| ID | Decision | Opciones | Recomendacion preliminar | Estado |
| --- | --- | --- | --- | --- |
| ADM-001 | Region Azure | East US, South Central US, Brazil South u otra aprobada. | Seleccionar por legal/latencia. | PENDIENTE DE VALIDACION |
| ADM-002 | Tenant | INCABIDE, proveedor, nuevo tenant. | Tenant INCABIDE si existe. | PENDIENTE DE VALIDACION |
| ADM-003 | Suscripcion | INCABIDE vs proveedor. | INCABIDE para transferencia. | PENDIENTE DE VALIDACION |
| ADM-004 | Ambientes | Dev, Test, UAT, Prod. | Minimo QA/UAT y Prod; dev segun ejecucion. | PENDIENTE DE VALIDACION |
| ADM-005 | Computo | Container Apps, VM Docker, AKS, App Service. | Container Apps si se acepta gestionado. | PENDIENTE DE VALIDACION |
| ADM-006 | Base de datos | PostgreSQL Flexible Server vs VM. | Flexible Server. | PENDIENTE DE VALIDACION |
| ADM-007 | WAF | Front Door WAF, App Gateway WAF, ambos. | Definir segun exposicion. | PENDIENTE DE VALIDACION |
| ADM-008 | DDoS | Basic vs Standard. | Segun riesgo y presupuesto. | PENDIENTE DE VALIDACION |
| ADM-009 | VPN/admin | P2S, S2S, Bastion. | Bastion/VPN segun operacion INCABIDE. | PENDIENTE DE VALIDACION |
| ADM-010 | Private Endpoints | Datos/Storage/Key Vault. | Recomendado para datos sensibles. | PENDIENTE DE VALIDACION |
| ADM-011 | DNS | Gestion INCABIDE vs proveedor. | INCABIDE con coordinacion. | PENDIENTE DE VALIDACION |
| ADM-012 | TLS | Certificado INCABIDE vs gestion proveedor. | Certificado institucional si existe. | PENDIENTE DE VALIDACION |
| ADM-013 | Entra ID usuarios | SSO vs usuarios aplicacion. | SSO si INCABIDE lo aprueba. | PENDIENTE DE VALIDACION |
| ADM-014 | CMK/HSM | Llaves Microsoft vs customer-managed. | Definir por cumplimiento. | PENDIENTE DE VALIDACION |
| ADM-015 | Retencion logs | 30/90/180/365 dias u otro. | Segun auditoria. | PENDIENTE DE VALIDACION |
| ADM-016 | Backup retention | Periodo legal/operativo. | Segun RPO/RTO. | PENDIENTE DE VALIDACION |
| ADM-017 | HA | Sin HA, zonal, regional. | Segun criticidad aprobada. | PENDIENTE DE VALIDACION |
| ADM-018 | DR | Backup/restore, warm standby, replica. | Segun RTO/RPO. | PENDIENTE DE VALIDACION |
| ADM-019 | Defender plan | Basico vs planes pagos. | Segun controles requeridos. | PENDIENTE DE VALIDACION |
| ADM-020 | SIEM | Log Analytics only vs SIEM institucional. | Integrar si existe. | PENDIENTE DE VALIDACION |
| ADM-021 | Egress/API | Limites y consumidores. | Definir por API. | PENDIENTE DE VALIDACION |
| ADM-022 | Storage redundancy | LRS/ZRS/GRS. | Segun continuidad. | PENDIENTE DE VALIDACION |
| ADM-023 | Malware scanning | Nativo/tercero/proceso. | Recomendado para multimedia. | PENDIENTE DE VALIDACION |
| ADM-024 | Pentest provider | Aprobado por PADF/INCABIDE o proveedor tercero. | Validar antes. | PENDIENTE DE VALIDACION |

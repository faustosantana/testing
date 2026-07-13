# 23 — DECISION LOG

## Registro de decisiones

| ID | Decision | Estado | Razon | Impacto |
| --- | --- | --- | --- | --- |
| AZ-DEC-001 | Usar Microsoft Azure. | Decidido por RFP | Plataforma obligatoria. | Base arquitectonica. |
| AZ-DEC-002 | Region Azure. | PENDIENTE DE VALIDACION | Azure no tiene region RD. | Legal, latencia, costo. |
| AZ-DEC-003 | Tenant/suscripcion. | PENDIENTE DE VALIDACION | Propiedad y operacion. | Accesos/costos. |
| AZ-DEC-004 | Container Apps vs VM vs AKS. | PENDIENTE DE VALIDACION | RFP permite VM o gestionado. | Operacion/costo. |
| AZ-DEC-005 | PostgreSQL gestionado. | Recomendado | PostgreSQL 14+ requerido. | Operacion/HA. |
| AZ-DEC-006 | WAF: Front Door, App Gateway o ambos. | PENDIENTE DE VALIDACION | OWASP Top 10. | Seguridad/costo. |
| AZ-DEC-007 | DDoS nivel. | PENDIENTE DE VALIDACION | RFP exige DDoS. | Seguridad/costo. |
| AZ-DEC-008 | VPN/Bastion. | PENDIENTE DE VALIDACION | Admin seguro. | Operacion. |
| AZ-DEC-009 | RTO/RPO. | PENDIENTE DE VALIDACION | DRP. | HA/backup. |
| AZ-DEC-010 | Retencion logs/backups. | PENDIENTE DE VALIDACION | Auditoria/DR. | Costo/cumplimiento. |
| AZ-DEC-011 | Entra ID SSO usuarios finales. | PENDIENTE DE VALIDACION | Identidad institucional. | UX/seguridad. |
| AZ-DEC-012 | CMK vs Microsoft-managed keys. | PENDIENTE DE VALIDACION | KMS/HSM. | Seguridad/costo. |

## Regla

Ninguna decision pendiente debe convertirse en compromiso final sin validacion PADF/INCABIDE o supuesto aprobado.

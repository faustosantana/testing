# WHY THIS ARCHITECTURE

## Por que protege mejor a INCABIDE

Esta arquitectura protege a INCABIDE porque trata el SGB como una plataforma institucional de datos sensibles, no como una aplicacion aislada.

## Protecciones clave

| Riesgo | Proteccion arquitectonica |
| --- | --- |
| Acceso no autorizado | Entra ID, MFA, RBAC, minimo privilegio. |
| Exposicion publica de datos | Private Endpoints, VNet, NSG, Firewall. |
| Ataques web | WAF OWASP Top 10, TLS, DDoS. |
| Credenciales en codigo | Key Vault y Managed Identity. |
| Perdida de datos | Backups cifrados y restore probado. |
| Falta de auditoria | Log Analytics, Activity Logs, auditoria aplicacion. |
| Incidentes sin visibilidad | Monitor, App Insights, Defender. |
| Cambios inseguros | DevSecOps, escaneos y aprobaciones. |
| Dependencia del proveedor | Documentacion, accesos completos y runbooks. |
| Integraciones riesgosas | API controlada y separacion de PGR opcional. |

## Por que es defendible

- Usa servicios Azure nativos alineados a requisitos RFP.
- Marca decisiones no definidas como pendientes.
- No fuerza una topologia sin datos de carga.
- Prioriza controles exigidos: WAF, DDoS, VPN, MFA, cifrado, backups, DRP, monitoreo.
- Mantiene PostgreSQL/PostGIS/unaccent como base preferida.
- Permite VM o servicio gestionado segun validacion.
- Genera evidencias necesarias para aprobacion.

## Por que no es solo "un dibujo"

Cada componente tiene objetivo, justificacion, dependencias, ventajas, riesgos, alternativas y criticidad. La arquitectura incluye operacion, gobierno, costos, seguridad, continuidad y decisiones pendientes.

## Resultado

INCABIDE obtiene una base cloud segura, auditable y transferible para operar el SGB y evolucionarlo por modulos, reduciendo riesgos de seguridad, indisponibilidad, perdida de datos y falta de control operativo.

# 02 — LOGICAL ARCHITECTURE

## Capas logicas

| Capa | Responsabilidad | Componentes Azure |
| --- | --- | --- |
| Entrada | DNS, TLS, proteccion web. | DNS, Azure Front Door o Application Gateway WAF. |
| Red | Aislamiento, segmentacion, control. | VNet, subredes, NSG, Firewall, Private Endpoints. |
| Identidad | Acceso, MFA, RBAC. | Microsoft Entra ID, Managed Identity. |
| Aplicacion | Ejecucion del SGB. | Container Apps o VM/AKS pendiente de validacion, ACR. |
| Datos | Persistencia y archivos. | Azure Database for PostgreSQL, Blob Storage. |
| Secretos | Credenciales y llaves. | Key Vault. |
| Seguridad | Postura, escaneo, alertas. | Defender for Cloud, WAF, DDoS, logs. |
| Observabilidad | Metricas, logs, trazas. | Monitor, App Insights, Log Analytics. |
| Continuidad | Backups y recuperacion. | Backup policies, PostgreSQL backup, Storage redundancy. |

## Flujo logico de solicitud

1. Usuario accede al dominio institucional.
2. TLS protege la comunicacion.
3. WAF inspecciona trafico web.
4. Solicitud llega a plataforma de contenedores.
5. Aplicacion consulta PostgreSQL por canal privado.
6. Documentos se leen/escriben en Blob Storage.
7. Secretos se obtienen via Managed Identity y Key Vault.
8. Logs y metricas se envian a observabilidad.

## Controles logicos

- autenticacion administrativa con MFA;
- RBAC por rol;
- secretos fuera del codigo;
- trafico privado a base de datos y storage;
- auditoria centralizada;
- alertas de disponibilidad y seguridad;
- backups cifrados;
- DRP documentado.

## Pendiente de validacion

- Integracion con Entra ID para usuarios finales.
- Alcance exacto de API.
- Ambientes no productivos requeridos.
- Separacion final de subredes por entorno.

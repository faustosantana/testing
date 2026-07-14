# 25 — DEFINITIVE AZURE ARCHITECTURE

## Objetivo

Definir la arquitectura Azure objetivo, lista para incorporarse directamente en la Oferta Tecnica, sin desplegar infraestructura ni escribir IaC.

## Decision tecnica principal

La arquitectura objetivo recomendada es una arquitectura Azure Enterprise por capas:

```text
Internet / usuarios autorizados
  -> DNS institucional + TLS
  -> Azure Front Door WAF
  -> Application Gateway WAF
  -> Azure Container Apps internal environment
  -> Azure Database for PostgreSQL Flexible Server
  -> Azure Blob Storage
  -> Key Vault
  -> Azure Monitor / App Insights / Log Analytics / Defender for Cloud
```

## Justificacion

Esta arquitectura protege mejor a INCABIDE porque:

- mantiene la aplicacion en contenedores, como requiere la RFP;
- evita exponer directamente la capa de aplicacion;
- usa defensa en profundidad con WAF, red segmentada, NSG, Firewall y Private Endpoints;
- mantiene secretos fuera del codigo con Key Vault y Managed Identity;
- preserva PostgreSQL 14+ con PostGIS/unaccent como base preferida;
- separa documentos y multimedia en Blob Storage;
- provee monitoreo, auditoria, backups y DRP;
- deja decisiones dependientes de PADF/INCABIDE marcadas como `PENDIENTE DE VALIDACION`.

## Arquitectura objetivo por dominio

| Dominio | Decision arquitectura | Estado |
| --- | --- | --- |
| Region Azure | Region con mejor balance juridico, latencia y disponibilidad. | PENDIENTE DE VALIDACION |
| Tenant / suscripcion | Preferible tenant/suscripcion de INCABIDE para transferencia de control. | PENDIENTE DE VALIDACION |
| Entrada publica | Azure Front Door WAF para edge, TLS y proteccion web inicial. | PENDIENTE DE VALIDACION |
| Entrada regional | Application Gateway WAF para control regional y enrutamiento a aplicacion. | PENDIENTE DE VALIDACION |
| Computo | Azure Container Apps internal environment para contenedores SGB. | PENDIENTE DE VALIDACION |
| Registro de imagenes | Azure Container Registry privado. | Recomendado |
| Base de datos | Azure Database for PostgreSQL Flexible Server con PostGIS/unaccent. | PENDIENTE DE VALIDACION |
| Archivos | Azure Blob Storage para documentos y multimedia. | Recomendado |
| Secretos | Azure Key Vault con Managed Identity. | Recomendado |
| Red | Hub/spoke simplificado con VNet, subredes, NSG, Firewall y Private Endpoints. | Recomendado |
| Identidad | Microsoft Entra ID, RBAC y MFA. | PENDIENTE DE VALIDACION |
| Monitoreo | Azure Monitor, Application Insights y Log Analytics. | Recomendado |
| Seguridad cloud | Microsoft Defender for Cloud. | PENDIENTE DE VALIDACION |
| Backups | Backups automaticos cifrados y restore test. | Recomendado |
| DR | Backup/restore + opcion zonal/regional segun RTO/RPO. | PENDIENTE DE VALIDACION |

## Red y segmentacion

Subredes recomendadas:

| Subred | Uso | Exposicion |
| --- | --- | --- |
| `snet-appgw` | Application Gateway WAF. | Publica controlada |
| `snet-containerapps` | Entorno interno de Azure Container Apps. | Privada |
| `snet-private-endpoints` | Private Endpoints para PostgreSQL, Storage y Key Vault. | Privada |
| `snet-management` | Bastion/VPN/administracion. | Privada |
| `snet-firewall` | Azure Firewall. | Controlada |

## Seguridad

Controles obligatorios y arquitectura:

| Requisito RFP | Control Azure |
| --- | --- |
| MFA administrativo | Microsoft Entra ID + Conditional Access. |
| Minimo privilegio | Azure RBAC + roles SGB. |
| WAF OWASP Top 10 | Azure Front Door WAF y/o Application Gateway WAF. |
| Firewall IP/puerto | Azure Firewall + NSG. |
| VPN administrativa | VPN Gateway o Azure Bastion. |
| Secretos en vault | Azure Key Vault. |
| Cifrado en transito | TLS/HTTPS. |
| Cifrado en reposo | PostgreSQL, Storage, Key Vault. |
| Auditoria | Activity Logs, App logs, SGB audit trail. |
| Monitoreo y alertas | Azure Monitor + Log Analytics. |
| Backups cifrados | PostgreSQL backups + Storage redundancy/backup. |
| DRP | Runbooks + restore test + RTO/RPO definidos. |

## Alta disponibilidad

| Capa | Estrategia |
| --- | --- |
| Entrada | Azure Front Door y Application Gateway WAF segun configuracion final. |
| Aplicacion | Multiples replicas de Container Apps. |
| Base de datos | Alta disponibilidad de PostgreSQL Flexible Server si se aprueba. |
| Storage | Redundancia LRS/ZRS/GRS segun decision. |
| Monitoreo | Alertas y dashboards. |

Nivel exacto de HA: `PENDIENTE DE VALIDACION`.

## Disaster Recovery

Modelo recomendado por fases:

1. Backup/restore probado como linea base.
2. Alta disponibilidad zonal si la region lo permite.
3. Replica regional o estrategia warm standby si RTO/RPO lo justifican.

RTO/RPO: `PENDIENTE DE VALIDACION`.

## Dev / Test / Prod

| Ambiente | Proposito | Recomendacion |
| --- | --- | --- |
| Dev | Adaptacion tecnica y pruebas internas. | Separado, con costos controlados. |
| Test/QA | Validacion funcional y seguridad. | Separado de produccion. |
| UAT | Validacion PADF/INCABIDE. | Puede compartir base con QA si se aprueba. |
| Prod | Operacion institucional. | Controles completos. |

Cantidad final de ambientes: `PENDIENTE DE VALIDACION`.

## Backup

| Recurso | Backup |
| --- | --- |
| PostgreSQL | Automatic backups + restore test. |
| Blob Storage | Versioning/retention/redundancy segun decision. |
| Key Vault | Soft delete + purge protection recomendados. |
| ACR | Retencion de imagenes versionadas. |
| Configuracion | Git + documentacion versionada, sin secretos. |

## Monitoreo

| Capa | Señales |
| --- | --- |
| Front Door / WAF | Requests, bloqueos, amenazas, latencia. |
| Application Gateway | Backend health, errores, WAF events. |
| Container Apps | CPU, memoria, replicas, errores, logs. |
| PostgreSQL | conexiones, storage, CPU, slow queries. |
| Storage | capacidad, errores, transacciones. |
| Seguridad | alertas Defender, login fallidos, cambios RBAC. |

## Gobierno

Controles recomendados:

- Resource groups por ambiente.
- Naming convention.
- Tags obligatorios.
- Azure Policy.
- RBAC por rol.
- Activity Logs.
- Budgets/alerts sin precios en propuesta tecnica.
- Locks para recursos criticos.
- Inventario de recursos.

## Cost assumptions

La arquitectura queda lista para estimacion, pero no incluye precios. Variables requeridas:

- region;
- ambientes;
- usuarios;
- concurrencia;
- volumen de activos;
- volumen multimedia;
- retencion logs/backups;
- HA/DR;
- nivel WAF/DDoS;
- Defender plans;
- egress;
- soporte critico;
- crecimiento.

## Decisiones pendientes

Las siguientes decisiones deben resolverse antes de dimensionar o comprometer costos:

1. Region Azure.
2. Tenant y suscripcion.
3. Dev/Test/UAT/Prod final.
4. Container Apps vs VM Docker si PADF requiere lectura literal de VM.
5. WAF unico o doble capa Front Door + Application Gateway.
6. DDoS Basic vs Standard.
7. VPN Gateway vs Bastion.
8. RTO/RPO.
9. Retencion de logs y backups.
10. Volumen multimedia y datos.

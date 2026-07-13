# 01 — ARCHITECTURE OVERVIEW

## Objetivo

Definir una arquitectura Azure Enterprise para ejecutar el SGB de INCABIDE de forma segura, operable, auditable y preparada para evolucionar por modulos.

## Principios

- Microsoft Azure como plataforma obligatoria.
- Seguridad reforzada desde el diseno.
- Red segmentada y acceso administrativo controlado.
- PostgreSQL 14+ con PostGIS y unaccent como base preferida.
- Almacenamiento seguro para medios y documentos.
- Contenedores como unidad de ejecucion.
- Monitoreo, alertas, backups y DRP como capacidades base.
- Evidencias verificables para aprobacion.

## Vista conceptual

```text
Usuarios / administradores
  -> DNS + TLS
  -> Azure Front Door / WAF o Application Gateway WAF
  -> Red Azure segmentada
  -> Plataforma de contenedores
  -> PostgreSQL + Blob Storage
  -> Key Vault + Managed Identity
  -> Monitor + Log Analytics + Defender
  -> Backup + Recovery
```

## Componentes principales

| Componente | Objetivo | Justificacion | Dependencias | Ventajas | Riesgos | Alternativas | Criticidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Microsoft Entra ID | Identidad, MFA y RBAC. | RFP exige MFA, IAM y minimo privilegio. | Tenant definido. | Control centralizado. | Tenant no definido. | Cuentas locales temporales. | Critica |
| Azure Virtual Network | Red aislada y segmentada. | RFP exige VPC/subredes segmentadas. | Region y direccionamiento. | Aislamiento. | CIDR mal definido. | Red plana no recomendada. | Critica |
| Subredes | Separar entrada, app, datos, endpoints y administracion. | Requisito de segmentacion. | VNet. | Menor superficie de ataque. | Complejidad operativa. | Segmentacion minima. | Alta |
| Private Endpoints | Acceso privado a datos/secretos. | Protege servicios PaaS. | DNS privado. | Reduce exposicion publica. | DNS complejo. | Service endpoints. | Alta |
| Azure Firewall | Control central de salida/entrada segun diseno. | RFP exige firewall personalizable. | VNet/hub. | Gobierno de trafico. | Costo y configuracion. | NSG-only para menor alcance. | Alta |
| NSG | Reglas por subred/interfaz. | Control IP/puerto. | Subredes. | Microsegmentacion. | Reglas inconsistentes. | Firewall central solamente. | Alta |
| Azure Front Door | Entrada global, TLS, WAF opcional. | Publicacion segura y resiliente. | DNS/TLS. | Edge, WAF, performance. | Region/costo por validar. | App Gateway WAF. | Alta |
| Application Gateway WAF | WAF regional y reverse proxy. | OWASP Top 10. | VNet/subred. | Control regional. | Dimensionamiento pendiente. | Front Door WAF. | Alta |
| Azure Container Apps | Ejecutar contenedores gestionados. | RFP permite VM o servicio gestionado para Docker. | ACR, VNet integration. | Menos operacion que VM. | Aprobacion pendiente. | VM Docker, AKS. | Alta |
| Azure Container Registry | Registro privado de imagenes. | Publicacion de imagenes del sistema. | Pipeline/identidad. | Control de artefactos. | Vulnerabilidades en imagenes. | Registry externo. | Media |
| Azure Database for PostgreSQL | Base PostgreSQL gestionada. | PostgreSQL 14+ preferido. | Region/VNet/Private Endpoint. | Backups, gestion, HA posible. | PostGIS/unaccent deben validarse. | PostgreSQL en VM. | Critica |
| Azure Blob Storage | Medios y documentos. | RFP exige almacenamiento de medios. | Private Endpoint, RBAC. | Escalable y cifrado. | Volumen desconocido. | File share / DB no recomendado. | Alta |
| Key Vault | Secretos y llaves. | RFP exige vault/KMS/HSM. | Entra ID, Managed Identity. | Secretos fuera del codigo. | Politicas mal definidas. | Variables sin vault no recomendadas. | Critica |
| Managed Identity | Acceso sin secretos estaticos. | Reduce credenciales. | Entra ID. | Seguridad operacional. | Soporte app por validar. | Service principals con rotacion. | Alta |
| Azure Monitor | Metricas y alertas. | RFP exige monitoreo en tiempo real. | Recursos instrumentados. | Observabilidad. | Ruido de alertas. | Herramientas externas. | Alta |
| Application Insights | Telemetria aplicacion/API. | Diagnostico y SLA. | Instrumentacion Django. | Trazas y errores. | Instrumentacion requerida. | Logs basicos. | Media |
| Log Analytics | Centralizar logs. | Auditoria y monitoreo. | Workspace. | Consultas y alertas. | Retencion/costo por validar. | SIEM externo. | Alta |
| Defender for Cloud | Postura y recomendaciones. | Escaneos y seguridad cloud. | Suscripcion Azure. | Hardening continuo. | Planes/costo por validar. | Escaneos externos. | Alta |
| Backup/Recovery | Respaldo y restauracion. | RFP exige backups cifrados y DRP. | Politicas RPO/RTO. | Continuidad. | RTO/RPO no definidos. | Backups manuales no recomendados. | Critica |
| VPN/Bastion | Acceso administrativo seguro. | RFP exige VPN para administracion. | Red e identidad. | Reduce exposicion. | Modalidad pendiente. | IP allowlist temporal. | Alta |
| DNS/TLS | Dominio institucional seguro. | RFP exige dominio y certificado TLS. | Dominio INCABIDE. | Confianza y acceso externo. | DNS no controlado por proveedor. | Dominio temporal no final. | Critica |

## Decisiones pendientes de validacion

- Region Azure.
- Tenant y suscripcion.
- Servicios gestionados vs VM.
- Front Door WAF vs Application Gateway WAF o combinacion.
- Modelo VPN/Bastion.
- Ambientes requeridos.
- RTO/RPO.
- Volumen de datos y archivos.
- Retencion de logs.
- Nivel DDoS.

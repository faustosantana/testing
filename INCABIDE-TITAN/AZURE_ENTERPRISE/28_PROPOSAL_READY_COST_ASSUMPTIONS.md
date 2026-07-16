# 28 — PROPOSAL READY COST ASSUMPTIONS

## Objetivo

Registrar las variables necesarias para estimar correctamente la arquitectura Azure en la oferta economica posterior, sin incluir precios.

## Supuestos generales

| Variable | Por que importa | Estado |
| --- | --- | --- |
| Region Azure | Afecta disponibilidad, latencia, servicios y costos. | PENDIENTE DE VALIDACION |
| Tenant / suscripcion | Define propiedad, facturacion y transferencia. | PENDIENTE DE VALIDACION |
| Ambientes | Dev/Test/UAT/Prod multiplican recursos. | PENDIENTE DE VALIDACION |
| Duracion de ambientes no productivos | Afecta costo de operacion. | PENDIENTE DE VALIDACION |
| Horario de uso | Puede afectar escalado y apagado de no productivos. | PENDIENTE DE VALIDACION |

## Computo

| Variable | Necesaria para |
| --- | --- |
| Plataforma final: Container Apps, VM, AKS o App Service | Seleccionar modelo de costo. |
| CPU/memoria por contenedor | Dimensionar aplicacion. |
| Numero minimo/maximo de replicas | HA y escalabilidad. |
| Jobs/background workers | Procesos asincronos. |
| Trafico esperado | Escalado y networking. |

## Base de datos

| Variable | Necesaria para |
| --- | --- |
| Version PostgreSQL | Compatibilidad. |
| vCores/memoria | Performance. |
| Almacenamiento inicial | Dimensionamiento. |
| Crecimiento mensual | Proyeccion anual. |
| HA zonal | Continuidad. |
| Backup retention | Recuperacion y costo. |
| IOPS/performance tier | Reportes y consultas. |

## Storage multimedia

| Variable | Necesaria para |
| --- | --- |
| Cantidad de activos | Volumen documental. |
| Documentos promedio por activo | Storage. |
| Imagenes/videos promedio | Storage/transacciones. |
| Tamano promedio de archivo | Capacidad. |
| Retencion legal | Lifecycle. |
| Redundancia LRS/ZRS/GRS | Continuidad/costo. |

## Red y seguridad

| Variable | Necesaria para |
| --- | --- |
| Front Door WAF requerido | Edge/security. |
| Application Gateway WAF requerido | Regional WAF. |
| Doble WAF o WAF unico | Costo/operacion. |
| Azure Firewall | Trafico y seguridad. |
| DDoS Basic vs Standard | Proteccion. |
| VPN Gateway vs Bastion | Administracion. |
| Private Endpoints requeridos | Seguridad/costo. |
| Egress mensual | Costos red. |

## Observabilidad

| Variable | Necesaria para |
| --- | --- |
| Ingesta diaria de logs | Log Analytics. |
| Retencion logs | Auditoria. |
| Sampling Application Insights | Costos y diagnostico. |
| Alertas requeridas | Operacion. |
| Integracion SIEM | Seguridad institucional. |

## Backup y DR

| Variable | Necesaria para |
| --- | --- |
| RTO | Estrategia DR. |
| RPO | Frecuencia backup/replica. |
| Retencion backup | Costo y cumplimiento. |
| Region secundaria | DR regional. |
| Restore test frequency | Operacion. |
| Warm standby | Continuidad avanzada. |

## Seguridad avanzada

| Variable | Necesaria para |
| --- | --- |
| Defender for Cloud plan | Seguridad cloud. |
| Malware scanning storage | Multimedia. |
| Customer-managed keys | Key Vault/HSM. |
| Pentest provider | Costo externo posterior. |
| Vulnerability scanning | DevSecOps. |

## Variables funcionales

| Variable | Necesaria para |
| --- | --- |
| Usuarios totales | Identidad/capacidad. |
| Usuarios concurrentes | Compute/database. |
| Llamadas API esperadas | Compute/network. |
| Reportes pesados | Database/performance. |
| Importaciones masivas | Compute/storage. |
| Integraciones externas | API/security/network. |

## Regla

No calcular ni comprometer costo Azure hasta validar estas variables o documentar supuestos aprobados por Justech.

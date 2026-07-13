# AZURE — REQUISITOS OBLIGATORIOS Y DECISIONES PENDIENTES

Estado: analisis previo. No contiene arquitectura Azure.

## Requisitos obligatorios extraidos del RFP

| ID | Requisito Azure / infraestructura | Evidencia PDF | Estado |
| --- | --- | --- | --- |
| AZR-001 | Microsoft Azure es plataforma obligatoria y no sustituible. | p.7, L265-L270; p.14, L661-L664 | Obligatorio |
| AZR-002 | Seleccionar region Azure aprobada por INCABIDE. | p.7, L265-L270 | Decision pendiente |
| AZR-003 | Region debe balancear garantias juridicas y desempeno. | p.7, L265-L268 | Decision pendiente |
| AZR-004 | Implementar salvaguardas por tratamiento transfronterizo de datos. | p.7, L267-L270 | Decision pendiente |
| AZR-005 | Computo mediante VM o servicio gestionado para contenedores Docker. | p.15, L725-L728 | Decision pendiente |
| AZR-006 | PostgreSQL 14+ preferido con postgis y unaccent. | p.15, L729-L731 | Obligatorio/preferido |
| AZR-007 | Motor alternativo solo con capacidades equivalentes y validacion INCABIDE. | p.14, L663-L667 | Condicional |
| AZR-008 | Almacenamiento de medios para archivos y documentos. | p.15, L732 | Obligatorio |
| AZR-009 | VM cloud con capacidad necesaria para imagen contenerizada. | p.15, L738-L739 | Obligatorio si se usa VM |
| AZR-010 | Construccion/publicacion de imagenes y acceso web por dominio indicado. | p.15, L740-L742 | Obligatorio |
| AZR-011 | Configuracion de dominio personalizado y DNS. | p.16, L751-L752 | Obligatorio |
| AZR-012 | Aplicacion con certificado TLS activo. | p.17, L924-L927 | Obligatorio |
| AZR-013 | Componentes computo, base de datos y almacenamiento activos y documentados. | p.17, L907-L912 | Obligatorio |
| AZR-014 | Accesos completos de administracion a INCABIDE. | p.16, L817-L822 | Obligatorio |
| AZR-015 | Inventario firmado de credenciales cloud, base de datos, SSH y tokens API. | p.18, L1018-L1026 | Obligatorio |
| AZR-016 | Costo total de infraestructura cloud por 12 meses asumido por proveedor. | p.16, L810-L816 | Obligatorio |
| AZR-017 | Desglose de servicios, proveedor cloud, costo mensual y fechas. | p.18, L999-L1009 | Obligatorio |
| AZR-018 | Estimacion mensual/anual de servicios Azure y dimensionamiento. | p.26, L1530-L1545 | Obligatorio |

## Controles de seguridad que afectan Azure

| Control | Evidencia PDF | Decision Azure pendiente |
| --- | --- | --- |
| Red aislada con subredes segmentadas | p.18, L1060-L1065 | VNet/subnets. |
| Firewall por IP/puerto | p.19, L1070-L1071 | Azure Firewall/NSG/WAF decision posterior. |
| IAM minimo privilegio | p.19, L1072-L1073 | RBAC/Entra ID. |
| MFA administrativo | p.19, L1074 | Entra ID/MFA u otro. |
| Cifrado en transito/reposo | p.19, L1075 | TLS, storage/DB encryption. |
| KMS o HSM | p.19, L1076 | Key Vault/Managed HSM. |
| WAF OWASP Top 10 | p.19, L1077 | Front Door/App Gateway WAF. |
| DDoS | p.19, L1078 | Basic vs Standard. |
| VPN administrativa | p.19, L1079 | P2S/S2S/Bastion. |
| Vault de secretos | p.19, L1080 | Azure Key Vault. |
| Monitoreo y alertas | p.19, L1081 | Azure Monitor/Log Analytics/SIEM. |
| Escaneos automaticos | p.19, L1082 | Defender/CI security tools. |
| Backups cifrados y DRP | p.19, L1083 | Backup policy/RTO/RPO. |
| Alta disponibilidad, redundancia, Zero Trust | p.19, L1084 | Patron HA pendiente. |

## Decisiones que deben tomarse antes de disenar arquitectura

| ID | Decision | Por que es necesaria | Pregunta relacionada |
| --- | --- | --- | --- |
| DEC-AZ-001 | Tenant/suscripcion Azure: INCABIDE vs proveedor. | Afecta facturacion, accesos, PI, soporte y transferencia. | Q12-Q13 |
| DEC-AZ-002 | Region Azure. | Afecta residencia, latencia y cumplimiento Ley 172-13. | Q14-Q15 |
| DEC-AZ-003 | Modelo de computo: VM Docker Compose vs servicio gestionado. | RFP permite ambos, pero tambien menciona VM y Compose. | Q16-Q17 |
| DEC-AZ-004 | Base de datos gestionada vs autogestionada. | Afecta HA, backup, costo y operacion. | Q16 |
| DEC-AZ-005 | Ambientes requeridos. | Afecta costo mensual/anual. | Q30-Q31 |
| DEC-AZ-006 | Nivel de HA y redundancia. | RFP exige HA pero no define nivel. | Q18 |
| DEC-AZ-007 | RTO/RPO y retencion. | Necesario para DRP y backups. | Q19-Q21 |
| DEC-AZ-008 | WAF y DDoS. | Afecta costo y seguridad. | Q24-Q25 |
| DEC-AZ-009 | Acceso administrativo seguro. | Necesario para VPN/Bastion/MFA. | Q26 |
| DEC-AZ-010 | Identidad/SSO. | Roles y MFA pueden requerir Entra ID. | Q40-Q41 |
| DEC-AZ-011 | Monitoreo y SIEM. | Necesario para alertas y evidencias. | Q27 |
| DEC-AZ-012 | Estrategia de DNS y TLS. | Requisito Hito 4. | Q28-Q29 |
| DEC-AZ-013 | Escaneo y pentest. | Necesario para Hito 4 y 30 dias post-produccion. | Q36-Q37 |
| DEC-AZ-014 | Almacenamiento multimedia y limites. | Afecta costos y diseno. | Q55-Q56 |
| DEC-AZ-015 | Costos post-primer ano. | RFP transfiere costos a INCABIDE o renovacion. | Q74 |

## Riesgos Azure principales

1. Dimensionamiento sin usuarios, concurrencia, datos ni ambientes.
2. Region Azure no definida y datos sensibles transfronterizos.
3. Controles de seguridad de alto costo no dimensionados.
4. HA/DRP sin RTO/RPO.
5. Soporte y costos por un ano incluidos sin limites claros.
6. Entrega de accesos completos y declaracion de no retener credenciales requiere procedimiento seguro.

## Criterio para fase siguiente

No disenar arquitectura hasta recibir o decidir:

- region;
- tenant/suscripcion;
- ambientes;
- usuarios/concurrencia;
- volumen de datos y archivos;
- RTO/RPO;
- nivel WAF/DDoS;
- alcance API;
- criterio de seguridad y monitoreo;
- presupuesto objetivo o estrategia de costo.

# 03 — PHYSICAL ARCHITECTURE

## Objetivo

Traducir la arquitectura logica a una topologia fisica Azure defendible, sin fijar SKUs ni dimensionamiento.

## Topologia propuesta

| Zona | Recursos |
| --- | --- |
| Edge / entrada | DNS, TLS, Azure Front Door WAF o Application Gateway WAF. |
| Red hub/spoke simplificada | VNet principal, subredes, NSG, Firewall/VPN. |
| App subnet | Azure Container Apps environment o alternativa validada. |
| Data subnet | Private Endpoints hacia PostgreSQL y Storage. |
| Management subnet | Bastion/VPN y acceso administrativo controlado. |
| Observability | Log Analytics, Monitor, App Insights. |
| Security | Key Vault, Defender for Cloud, alertas. |

## Modelo fisico recomendado

La opcion preferida conceptual es servicios gestionados:

- Azure Container Apps para contenedores;
- Azure Database for PostgreSQL Flexible Server;
- Blob Storage para medios;
- Key Vault para secretos;
- Private Endpoints para datos;
- Monitor/Log Analytics para operacion.

## Justificacion

Servicios gestionados reducen operacion de infraestructura comparados con administrar todo en VM, manteniendo compatibilidad con el requisito de ejecutar contenedores Docker. La RFP permite VM o servicio gestionado configurado para contenedores.

## Alternativas

| Alternativa | Ventaja | Riesgo |
| --- | --- | --- |
| VM con Docker | Alinea lectura literal de VM/Docker Compose. | Mayor operacion, parches, hardening. |
| Azure Container Apps | Menor operacion y escalado gestionado. | Requiere validacion PADF/INCABIDE. |
| AKS | Control avanzado. | Complejidad probablemente superior al alcance inicial. |

## Pendiente de validacion

- Aceptacion de Container Apps como servicio gestionado.
- Region.
- Ambientes.
- Requerimientos de alta disponibilidad.
- Volumen de carga.

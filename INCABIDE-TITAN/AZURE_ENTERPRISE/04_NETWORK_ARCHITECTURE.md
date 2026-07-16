# 04 — NETWORK ARCHITECTURE

## Objetivo

Cumplir aislamiento de red, subredes segmentadas, firewall, reglas por IP/puerto y VPN administrativa exigidos por la RFP.

## Componentes

| Componente | Objetivo | Justificacion | Dependencias | Ventajas | Riesgos | Alternativas | Criticidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Azure VNet | Red privada del SGB. | Aislamiento requerido. | Region/CIDR. | Control de trafico. | CIDR mal planificado. | Red default no recomendada. | Critica |
| Subnet Edge/App | Separar entrada y app. | Segmentacion. | VNet. | Menor exposicion. | Complejidad. | Subred unica no recomendada. | Alta |
| Subnet Data/Private Endpoints | Acceso privado a PostgreSQL/Storage/Key Vault. | Reducir exposicion publica. | DNS privado. | Seguridad. | DNS complejo. | Public endpoints restringidos. | Alta |
| Subnet Management | VPN/Bastion/admin. | Acceso administrativo seguro. | Identidad. | Menos superficie publica. | Modelo pendiente. | IP allowlist temporal. | Alta |
| NSG | Reglas por subred. | Firewall por IP/puerto. | Subredes. | Microsegmentacion. | Reglas inconsistentes. | Firewall central. | Alta |
| Azure Firewall | Control centralizado. | Gobierno de trafico. | Hub/rutas. | Inspeccion y logging. | Costo y gestion. | NSG-only. | Alta |
| VPN/Bastion | Admin seguro. | RFP exige VPN. | Red/identidad. | Sin puertos publicos admin. | Modalidad pendiente. | Bastion o P2S/S2S. | Alta |
| Private DNS | Resolver private endpoints. | Necesario para PaaS privado. | Private Endpoints. | Transparencia app. | Errores DNS. | DNS publico con restricciones. | Alta |

## Segmentacion minima

- entrada;
- aplicacion;
- datos/endpoints privados;
- administracion;
- observabilidad/servicios compartidos cuando aplique.

## Trafico permitido

- Internet hacia WAF/entrada.
- WAF hacia aplicacion.
- Aplicacion hacia PostgreSQL por private endpoint.
- Aplicacion hacia Blob Storage por private endpoint.
- Aplicacion hacia Key Vault por private endpoint o canal seguro.
- Administracion por VPN/Bastion.

## Pendiente de validacion

- Rango CIDR.
- Modelo VPN: site-to-site, point-to-site o Bastion.
- Nivel Azure Firewall.
- Si se usara Front Door, App Gateway WAF o ambos.

# 13 — COST OPTIMIZATION

## Objetivo

Establecer principios de optimizacion de costos sin colocar precios.

## Principios

- dimensionar con base en usuarios, concurrencia y volumen real;
- separar ambientes productivos y no productivos;
- usar servicios gestionados cuando reduzcan operacion total;
- definir retencion de logs y backups;
- controlar egress y transacciones de storage;
- apagar o reducir ambientes no productivos si aplica;
- monitorear consumo mensual.

## Palancas de costo

| Area | Variable |
| --- | --- |
| Computo | CPU, memoria, replicas, horas activas, escalado. |
| Base de datos | vCores, almacenamiento, HA, backups, IOPS. |
| Storage | GB, transacciones, redundancia, retencion. |
| Seguridad | WAF, Firewall, DDoS, Defender, Key Vault. |
| Observabilidad | GB ingeridos, retencion, alertas. |
| Red | Egress, Private Endpoints, VPN, Firewall data processing. |

## Riesgos

- RFP exige infraestructura por 1 ano sin dimensionamiento base.
- Seguridad avanzada puede impactar costo.
- Soporte critico fuera de horario no esta limitado claramente.
- Volumen multimedia desconocido.

## Pendiente de validacion

- Presupuesto objetivo.
- Ambientes incluidos.
- Nivel HA/DR.
- Nivel DDoS.
- Retencion de logs/backups.

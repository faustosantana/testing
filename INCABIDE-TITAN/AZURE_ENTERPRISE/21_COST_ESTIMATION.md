# 21 — COST ESTIMATION

## Objetivo

Definir como se estimara costo Azure sin incluir precios en esta fase.

## Componentes a estimar

| Componente | Variables |
| --- | --- |
| Computo | Servicio elegido, replicas, CPU, memoria, horas, escalado. |
| Base de datos | vCores, memoria, almacenamiento, HA, backups, IOPS. |
| Storage | GB, transacciones, redundancia, retencion, versionado. |
| Red | WAF, Firewall, VPN, egress, private endpoints. |
| Seguridad | Defender, Key Vault, DDoS, escaneos. |
| Observabilidad | Ingesta logs, retencion, App Insights. |
| Backup/DR | Retencion, replica, pruebas restore. |
| Ambientes | Dev/test/prod/UAT cantidad y permanencia. |

## Variables criticas

- region;
- usuarios;
- concurrencia;
- volumen de activos;
- volumen multimedia;
- retencion logs;
- retencion backups;
- SLA/HA;
- DDoS Standard vs Basic;
- WAF elegido;
- soporte de ambientes no productivos.

## No incluido

No se incluyen precios, montos ni estimaciones numericas en esta fase.

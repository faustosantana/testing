# AZURE COST ASSUMPTIONS

## Objetivo

Registrar variables necesarias para calcular costos Azure correctamente. No contiene precios.

## Variables generales

- region Azure;
- moneda y tratamiento fiscal posterior;
- tenant/suscripcion;
- ambientes incluidos;
- duracion de ambientes no productivos;
- soporte post-primer ano;
- crecimiento esperado.

## Computo

- plataforma: Container Apps, VM, AKS o App Service;
- replicas minimas y maximas;
- CPU/memoria por contenedor;
- horas activas;
- escalado;
- jobs/background workers;
- entorno de pruebas.

## Base de datos

- version PostgreSQL;
- vCores;
- memoria;
- almacenamiento inicial;
- crecimiento mensual;
- HA;
- backups;
- retencion;
- IOPS/performance;
- replicas.

## Storage

- GB iniciales;
- crecimiento mensual;
- numero de archivos;
- tamano promedio;
- transacciones;
- redundancia;
- versionado;
- retencion;
- malware scanning si aplica.

## Red y seguridad

- Front Door;
- Application Gateway WAF;
- Azure Firewall;
- DDoS Standard;
- VPN/Bastion;
- Private Endpoints;
- egress mensual;
- DNS/TLS;
- Key Vault operaciones;
- Defender plans.

## Observabilidad

- GB logs ingeridos por dia;
- retencion;
- metricas;
- Application Insights sampling;
- alertas;
- dashboards;
- integracion SIEM.

## Continuidad

- RPO;
- RTO;
- frecuencia backup;
- retencion backup;
- region secundaria;
- pruebas restore;
- DR warm/cold standby.

## Variables de uso

- usuarios totales;
- usuarios concurrentes;
- activos registrados;
- documentos por activo;
- reportes generados;
- exportaciones;
- llamadas API;
- integraciones externas.

## Pendiente

Todas estas variables deben confirmarse antes de calcular costos y antes de comprometer la infraestructura por 1 ano.

# 08 — DATABASE

## Objetivo

Proveer persistencia transaccional, busqueda sin distincion de acentos y capacidades geoespaciales para el SGB.

## Servicio recomendado

Azure Database for PostgreSQL Flexible Server, sujeto a validacion de version, PostGIS y unaccent.

## Requisitos RFP

- PostgreSQL 14+ preferido.
- Extensiones postgis y unaccent.
- Motor alternativo solo si garantiza equivalencia y aprobacion INCABIDE.

## Diseno conceptual

| Area | Decision |
| --- | --- |
| Motor | PostgreSQL 14+ o superior compatible. |
| Extensiones | PostGIS, unaccent. |
| Acceso | Private Endpoint / red privada. |
| Backup | Automatico y cifrado. |
| HA | PENDIENTE DE VALIDACION. |
| Retencion | PENDIENTE DE VALIDACION. |
| Cifrado | En reposo y en transito. |
| Monitoreo | Query performance, conexiones, almacenamiento, errores. |

## Ventajas

- servicio gestionado;
- backups integrados;
- menor carga operativa;
- soporte PostgreSQL;
- integracion Azure Monitor;
- opciones de alta disponibilidad segun decision.

## Riesgos

- dimensionamiento desconocido;
- volumen de datos no definido;
- concurrencia no definida;
- RTO/RPO no definidos;
- compatibilidad exacta con codigo existente pendiente del diagnostico.

## Alternativas

| Alternativa | Ventaja | Riesgo |
| --- | --- | --- |
| PostgreSQL en VM | Maximo control. | Mayor administracion, parches, backup manual. |
| Motor alternativo | Potencial optimizacion. | Requiere equivalencia PostGIS/unaccent y aprobacion. |

## Criticidad

Critica: es el repositorio transaccional del SGB.

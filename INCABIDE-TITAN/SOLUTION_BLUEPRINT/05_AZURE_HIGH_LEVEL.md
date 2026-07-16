# 05 — AZURE HIGH LEVEL

## Objetivo

Definir una arquitectura Azure conceptual, alineada a la RFP, sin entrar en diseno detallado, SKUs, dimensionamiento ni costos.

## Vista de alto nivel

```text
Usuarios / Administradores
  -> DNS institucional + TLS
  -> Capa de entrada segura / WAF
  -> Red Azure segmentada
  -> Contenedores SGB
  -> PostgreSQL/PostGIS
  -> Almacenamiento de medios
  -> Key Vault / monitoreo / backups
```

## Servicios conceptuales

| Dominio | Capacidad Azure conceptual |
| --- | --- |
| Entrada segura | WAF, TLS, proteccion OWASP Top 10. |
| Red | VNet, subredes, reglas de acceso, VPN/Bastion segun decision. |
| Computo | VM con contenedores o servicio gestionado compatible con Docker. |
| Datos | PostgreSQL 14+ compatible con PostGIS y unaccent. |
| Archivos | Almacenamiento de medios con cifrado y control de acceso. |
| Secretos | Vault para credenciales, llaves y configuracion sensible. |
| Identidad | MFA, RBAC, integracion con identidad institucional si se aprueba. |
| Monitoreo | Logs, metricas, alertas y tableros operativos. |
| Backup / DR | Respaldos cifrados, restauracion probada y plan DRP. |

## Ambientes sugeridos conceptualmente

| Ambiente | Uso |
| --- | --- |
| Desarrollo | Ajustes tecnicos, refactorizacion y pruebas internas. |
| QA/UAT | Validacion de INCABIDE/PADF, mockups y pruebas funcionales. |
| Produccion | Operacion institucional del SGB. |

La cantidad final de ambientes depende de confirmacion PADF/INCABIDE y afecta costos posteriores.

## Seguridad Azure conceptual

- red segmentada;
- acceso administrativo por canal seguro;
- MFA para administradores;
- principio de minimo privilegio;
- secretos fuera del codigo;
- cifrado en reposo y transito;
- WAF y proteccion DDoS segun decision;
- monitoreo y alertas;
- backups cifrados;
- evidencias de configuracion.

## Residencia y transferencia de datos

La RFP reconoce que Azure no cuenta con region en Republica Dominicana. La solucion debe seleccionar una region aprobada por INCABIDE, con salvaguardas tecnicas y contractuales para tratamiento transfronterizo bajo Ley 172-13.

## Decisiones requeridas antes del diseno detallado

1. Region Azure.
2. Tenant y suscripcion.
3. Modelo de computo.
4. Base de datos gestionada o autogestionada.
5. Ambientes requeridos.
6. Usuarios y concurrencia.
7. Volumen de datos y multimedia.
8. RTO/RPO.
9. Nivel de WAF/DDoS.
10. Identidad institucional.
11. Monitoreo/SIEM.
12. Backup y retencion.
13. Estrategia DNS/TLS.

## Evidencias esperadas por RFP

- diagrama de arquitectura implementada;
- componentes activos y documentados;
- credenciales entregadas por mecanismo seguro;
- capturas o registros de despliegue;
- certificado TLS activo;
- evidencias de controles de seguridad;
- registro de backup restaurable.

# MAPA DE REQUISITOS ECONOMICOS

Estado: estructura para oferta economica posterior. No contiene precios.

## Reglas economicas del RFP

| ID | Regla | Evidencia PDF | Implicacion |
| --- | --- | --- | --- |
| ECO-001 | Moneda USD. | p.1, L13-L17; p.4, L128-L130 | Todos los valores en USD. |
| ECO-002 | Mecanismo contractual de precio fijo. | p.1, L13 | Control estricto de alcance. |
| ECO-003 | Valores netos. | p.4, L128-L130 | Confirmar impuestos/retenciones. |
| ECO-004 | Usar solo formato Anexo 3. | p.4, L128-L130; p.25-p.26 | No usar formato alterno. |
| ECO-005 | Incluir todos los impuestos y costos aplicables. | p.3, L92-L93 | Validar tributacion. |
| ECO-006 | Segmentar por etapas, fases o modulos. | p.3, L92-L98 | Modelo modular. |
| ECO-007 | PADF puede contratar paquete completo o modulos especificos. | p.3, L94-L98 | Precio individual por modulo. |
| ECO-008 | Puede indicarse descuento por paquete completo. | p.3, L94-L98; p.26, L1520-L1522 | Estrategia comercial posterior. |
| ECO-009 | Interconexion PGR opcional y cotizada por separado. | p.16, L755-L759; p.26, L1520-L1523 | Item separado. |
| ECO-010 | PADF no reembolsa costos de preparar propuesta. | p.26, L1524-L1529 | Costo de venta interno. |

## Etapa I — estructura obligatoria de costos

| Hito | Entregable | % pago RFP | Evidencia PDF | Monto |
| --- | --- | ---: | --- | --- |
| 1 | Analisis y Adaptacion del Codigo Fuente | 50% | p.25, L1456-L1462 | TBD |
| 2 | Personalizacion de Marca y Textos | 20% | p.25, L1463-L1468 | TBD |
| 3 | Infraestructura en la Nube | 10% | p.25, L1469-L1470 | TBD |
| 4 | Contenerizacion y Puesta en Produccion | 10% | p.25, L1471-L1474 | TBD |
| 5 | Documentacion Tecnica | 2% | p.25, L1475-L1476 | TBD |
| 6 | Transferencia de Conocimiento | 2% | p.25, L1477-L1478 | TBD |
| 7 | Infraestructura por 1 Ano | 2% | p.25, L1479-L1480 | TBD |
| 8 | Accesos a la Infraestructura | 2% | p.25, L1481-L1482 | TBD |
| 9 | Soporte Tecnico por 1 Ano | 2% | p.25, L1483-L1489 | TBD |
|  | **TOTAL ETAPA I** | **100%** | p.25, L1490-L1491 | TBD |

## Etapa II — estructura obligatoria de costos por modulo

| Modulo | Duracion referencia RFP | % pago referencia | Evidencia PDF | Monto |
| --- | ---: | ---: | --- | --- |
| Registro e Ingreso de Activos | 1.5 meses | 7.73% | p.20, L1139-L1156 | TBD |
| Gestion de Contratos y Clientes | 8 meses | 41.22% | p.20, L1157-L1176 | TBD |
| Modulo de Subasta / Ventas | 1 mes | 5.15% | p.20, L1177-L1200 | TBD |
| Descargo de Activos / Donaciones | 6.41 meses | 33.02% | p.21, L1210-L1229 | TBD |
| Soporte Multilenguaje | 2 meses | 10.30% | p.21, L1230-L1246 | TBD |
| Seguridad y Control de Acceso Avanzado | 0.5 meses | 2.58% | p.21, L1247-L1264 | TBD |
| Funciones Complementarias Transversales | Por definir | Por aclarar | p.21-p.22, L1279-L1311; p.26, L1511-L1518 | TBD |

## Infraestructura Azure — estructura de estimacion

| Componente | Especificacion pendiente | Costo mensual | Costo anual | Evidencia PDF |
| --- | --- | --- | --- | --- |
| Computo VM / servicio gestionado | TBD | TBD | TBD | p.26, L1536-L1537 |
| Base de Datos PostgreSQL o equivalente | TBD | TBD | TBD | p.26, L1538-L1539 |
| Almacenamiento de medios | TBD | TBD | TBD | p.26, L1540 |
| Redes y seguridad VPC/VNet, WAF, firewall | TBD | TBD | TBD | p.26, L1541-L1542 |
| Otros: backup, monitoreo, DNS | TBD | TBD | TBD | p.26, L1543-L1544 |
| **TOTAL INFRAESTRUCTURA** |  | TBD | TBD | p.26, L1545 |

## Costos que deben confirmarse antes de precio final

1. Ambientes incluidos.
2. Region Azure.
3. WAF y DDoS requeridos.
4. HA, redundancia, RTO/RPO.
5. Retencion de backups.
6. Volumen de datos y multimedia.
7. Usuarios/concurrencia.
8. Pentest tercero.
9. Herramientas de escaneo/monitoreo.
10. Soporte critico fuera de horario.
11. Garantias bancarias/aseguradoras.
12. Impuestos, retenciones y costos bancarios.

# 18 — MONITORING OBSERVABILITY

## Objetivo

Definir el modelo de observabilidad para disponibilidad, rendimiento, seguridad, auditoria y soporte del SGB.

## Pilares

| Pilar | Objetivo |
| --- | --- |
| Logs | Entender eventos, errores, accesos y auditoria. |
| Metricas | Medir salud, capacidad, rendimiento y uso. |
| Trazas | Diagnosticar flujos de aplicacion/API. |
| Alertas | Detectar incidentes y condiciones anormales. |
| Dashboards | Dar visibilidad tecnica y ejecutiva. |

## Monitoreo tecnico

- disponibilidad de aplicacion;
- estado de contenedores;
- latencia;
- errores HTTP;
- uso CPU/memoria;
- conexion a base de datos;
- tiempos de consulta;
- almacenamiento disponible;
- trabajos programados;
- estado de backups.

## Monitoreo de seguridad

- intentos fallidos de login;
- accesos administrativos;
- cambios de permisos;
- exportaciones masivas;
- eventos de WAF;
- alertas de firewall;
- vulnerabilidades detectadas;
- secretos expuestos;
- anomalias de acceso.

## Monitoreo funcional

- activos registrados;
- documentos cargados;
- contratos por vencer;
- pagos atrasados;
- procesos de disposicion en curso;
- aprobaciones pendientes;
- exportaciones generadas;
- UAT y tickets abiertos.

## Dashboards sugeridos

| Dashboard | Audiencia |
| --- | --- |
| Salud de Plataforma | TI INCABIDE / Justech |
| Seguridad y Accesos | Seguridad / Administradores |
| Operacion de Activos | Usuarios funcionales |
| Ejecutivos INCABIDE | Direccion |
| Soporte y SLA | Service Manager |

## Alertas minimas

- aplicacion no disponible;
- API no responde;
- certificado TLS por vencer;
- backup fallido;
- almacenamiento alto;
- errores 5xx elevados;
- intentos fallidos anormales;
- vulnerabilidad critica;
- WAF bloqueando patron alto;
- job critico fallido.

## Evidencias

- capturas de dashboards;
- reglas de alerta;
- logs de prueba;
- reporte de backup;
- reporte de incidentes;
- reporte mensual de salud.

## Diferenciador

Un centro de monitoreo visual con estado de aplicacion, seguridad, backups, soporte y SLA ayudaria a mostrar una propuesta de madurez superior frente a un despliegue local tradicional.

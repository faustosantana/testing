# 10 — MONITORING

## Objetivo

Cumplir monitoreo en tiempo real, registro de accesos, alertas y evidencia operativa.

## Servicios

| Servicio | Objetivo | Justificacion | Dependencias | Ventajas | Riesgos | Alternativas | Criticidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Azure Monitor | Metricas y alertas. | RFP exige monitoreo. | Recursos Azure. | Alertas nativas. | Alert fatigue. | Herramienta externa. | Alta |
| Application Insights | Telemetria app/API. | Diagnostico aplicacion. | Instrumentacion. | Trazas y errores. | Requiere integracion. | Logs app simples. | Media |
| Log Analytics | Logs centralizados. | Auditoria/seguridad. | Workspace. | Consultas KQL. | Retencion/costo. | SIEM externo. | Alta |
| Defender for Cloud | Postura seguridad. | Escaneos/hardening. | Planes habilitados. | Recomendaciones. | Costo. | Escaneos terceros. | Alta |

## Alertas minimas

- aplicacion no disponible;
- API no responde;
- errores 5xx;
- base de datos sin conexion;
- backup fallido;
- certificado TLS por vencer;
- intentos fallidos anormales;
- uso alto de almacenamiento;
- vulnerabilidad critica;
- evento WAF relevante.

## Logs requeridos

- accesos;
- errores aplicacion;
- auditoria funcional;
- cambios administrativos;
- eventos de seguridad;
- exportaciones;
- integraciones API;
- operaciones de backup/restore.

## Pendiente de validacion

- Retencion de logs.
- Integracion con SIEM institucional.
- Umbrales de alerta.
- Responsables de notificacion.

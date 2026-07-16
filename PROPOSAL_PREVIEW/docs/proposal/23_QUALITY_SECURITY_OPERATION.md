# 23 — QUALITY, SECURITY AND OPERATION

## 23.1 Plan Maestro de QA

El Plan Maestro de QA asegura que cada requisito de la RFP se traduzca en una prueba, evidencia y criterio de aceptacion. La calidad no se limita a ausencia de errores; una funcionalidad debe ser usable, coherente, consistente, segura, respetar permisos, evitar duplicidad y no introducir deuda tecnica evidente.

## 23.2 Estrategia de pruebas

| Tipo de prueba | Objetivo | Evidencia |
| --- | --- | --- |
| Funcional | Validar flujos del SGB | Casos ejecutados |
| Integracion | Validar API, base, storage y servicios | Reportes de integracion |
| Seguridad | Validar MFA, RBAC, WAF, secretos, vulnerabilidades | Reportes CVSS, evidencias MFA |
| Regresion | Confirmar que cambios no rompen flujos existentes | Matriz regresion |
| Backup/Restore | Validar recuperacion | Evidencia restore |
| UAT | Validacion PADF/INCABIDE | Actas UAT |

## 23.3 UAT

UAT debe ejecutarse con usuarios o representantes designados por INCABIDE. Cada prueba UAT debe tener:

- requisito asociado;
- escenario;
- datos de prueba;
- resultado esperado;
- resultado observado;
- evidencia;
- estado;
- aprobador.

## 23.4 Plan de migracion

La migracion es condicionada porque la RFP no define volumen ni fuente historica. Si se confirma migracion, se ejecutara mediante inventario, perfilamiento, mapeo, carga de prueba, validacion, carga controlada y reconciliacion.

## 23.5 Plan de reversa / Rollback

Cada release debe tener plan de reversa:

1. identificar version estable anterior;
2. preservar logs y evidencia;
3. ejecutar rollback de contenedor/configuracion;
4. validar base de datos y archivos;
5. ejecutar health checks;
6. documentar resultado.

## 23.6 Plan de continuidad

La continuidad se basa en:

- backups automaticos cifrados;
- restore test;
- monitoreo;
- alertas;
- DRP;
- runbooks;
- roles de respuesta;
- comunicacion de incidentes.

## 23.7 Gestion de incidentes

| Tipo | Tiempo RFP | Gestion |
| --- | --- | --- |
| Critico | 1 hora | Escalamiento inmediato y seguimiento ejecutivo |
| Mayor | 4 horas habiles | Diagnostico y correccion prioritaria |
| Menor | 8 horas habiles | Resolucion planificada |

Cada incidente debe registrar causa, impacto, accion, responsable, evidencia y cierre.

## 23.8 Gestion de problemas

Los problemas recurrentes se gestionan mediante analisis de causa raiz, acciones preventivas, revision de tendencias y actualizacion de runbooks.

## 23.9 Gestion de cambios

Todo cambio debe registrar descripcion, origen, requisito afectado, impacto tecnico, impacto de seguridad, impacto de operacion, aprobador, decision y evidencia. Cambios criticos no se implementan sin aprobacion.

## 23.10 DevSecOps

DevSecOps integra revision de codigo, escaneo de secretos, escaneo de dependencias, escaneo de contenedores, control de versiones, aprobaciones, despliegues controlados y evidencias de release.

## 23.11 Gestion documental

La documentacion incluye arquitectura, variables de entorno, procedimientos de contenedores, restauracion de backups, manuales, runbooks, actas, evidencias de seguridad y material de capacitacion.

## 23.12 Seguridad

La seguridad cubre MFA, RBAC, cifrado, WAF, DDoS, VPN, Key Vault, Managed Identity, auditoria, monitoreo, escaneos y pentest de tercero independiente posterior a produccion.

## 23.13 Auditoria

El sistema debe auditar accesos, cambios de datos, documentos, exportaciones, aprobaciones, cambios de permisos, integraciones y acciones administrativas.

## 23.14 Monitoreo

Monitoreo con Azure Monitor, Application Insights y Log Analytics:

- disponibilidad;
- errores;
- latencia;
- uso de recursos;
- conexiones a base de datos;
- eventos de seguridad;
- backups;
- WAF events;
- alertas.

## 23.15 Soporte

El soporte post-despliegue debe operar con canales definidos, clasificacion de incidentes, SLA, escalamiento, registro de tickets, evidencias y reportes de salud.

## 23.16 Operacion

La operacion incluye revision diaria de salud, revision de alertas, control de backups, gestion de incidentes, cambios, accesos, seguridad y documentacion.

## 23.17 Matriz integrada

| Area | Responsable principal | Evidencia |
| --- | --- | --- |
| QA | Quality Assurance Lead | Casos, reportes, matriz trazabilidad |
| UAT | QA Lead + usuarios INCABIDE | Actas UAT |
| Seguridad | Azure Architect / DevOps | Evidencias controles |
| DevSecOps | DevOps Engineer | Escaneos, builds, releases |
| Operacion | DevOps / Project Director | Reportes salud, tickets |
| Cambios | Project Director | Registro y aprobaciones |
| Documentacion | Technical Delivery / QA | Manuales, runbooks |

## 23.18 Criterio de salida

Un area se considera lista solo si:

- cumple requisito RFP;
- tiene evidencia;
- paso QA;
- paso UAT si aplica;
- no tiene defectos criticos;
- respeta seguridad y permisos;
- cuenta con aprobacion registrada.

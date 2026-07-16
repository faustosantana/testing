# 02 — SOLUTION ARCHITECTURE

## Arquitectura logica objetivo

La solucion se organiza en capas:

```text
Usuarios INCABIDE
  -> Portal Web SGB
  -> API SGB
  -> Servicios de Dominio
  -> Datos Operacionales
  -> Integraciones / Reportes / Auditoria
  -> Operacion, Seguridad y Observabilidad
```

## Capas de solucion

| Capa | Responsabilidad | Componentes logicos |
| --- | --- | --- |
| Experiencia | Interaccion de usuarios internos y administradores. | Interfaz web, reportes, formularios, dashboards. |
| Aplicacion | Reglas de negocio y modulos SGB. | Django, modulos existentes, nuevos modulos Etapa II. |
| API | Interoperabilidad y servicios externos. | API REST versionada, autenticacion, documentacion tecnica. |
| Datos | Persistencia transaccional y geoespacial. | PostgreSQL, PostGIS, unaccent, almacenamiento multimedia. |
| Seguridad | Identidad, acceso, cifrado, auditoria. | MFA, RBAC, secretos, logs, WAF, VPN. |
| Integracion | Sistemas externos y flujos masivos. | PGR opcional, sistema subastas, import/export. |
| Operacion | Continuidad y soporte. | Monitoreo, alertas, backups, runbooks, soporte. |

## Arquitectura fisica de alto nivel

```text
Internet / Red autorizada
  -> WAF / entrada segura
  -> Proxy inverso / balanceo logico
  -> Contenedores aplicacion Django
  -> Base de datos PostgreSQL/PostGIS
  -> Almacenamiento de medios
  -> Servicios de seguridad, monitoreo y backup
```

La implementacion fisica definitiva debe decidir si usa VM con Docker Compose o servicio gestionado de contenedores, segun aprobacion de INCABIDE y respuestas a preguntas PADF.

## Dominios funcionales

| Dominio | Alcance de solucion |
| --- | --- |
| Custodia de activos | Registro, clasificacion, ubicacion, identificadores, multimedia y geolocalizacion. |
| Gestion contractual | Clientes, contratos, pagos, alertas, documentos y estados de cuenta. |
| Disposicion | Subastas, ventas, donaciones, devoluciones, destruccion y conciliacion. |
| Control institucional | Roles, permisos, auditoria, aprobaciones y trazabilidad. |
| Inteligencia operativa | Reportes, exportaciones, dashboards y analisis. |
| Operacion tecnica | Cloud, seguridad, monitoreo, soporte y continuidad. |

## Flujo general de operacion

1. Un bien ingresa al sistema con identificador unico.
2. El bien se clasifica, ubica y documenta.
3. Usuarios autorizados gestionan estado, movimientos y evidencia.
4. Procesos de contratos, subastas, donaciones o devoluciones se ejecutan segun reglas.
5. Cada accion relevante genera auditoria.
6. Reportes y dashboards permiten seguimiento institucional.
7. Integraciones consumen o publican datos mediante API controlada.

## Controles transversales

- autenticacion multifactor para administradores;
- autorizacion por rol y accion;
- cifrado en transito y reposo;
- almacenamiento seguro de secretos;
- bitacoras de auditoria;
- monitoreo y alertas;
- respaldos automáticos cifrados;
- procedimientos de recuperacion;
- evidencias por hito.

## Limites de diseno

Este documento define arquitectura de solucion, no arquitectura detallada Azure ni configuracion final de servicios.

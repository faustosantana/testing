# 07 — TECHNICAL ARCHITECTURE SUMMARY

## Arquitectura tecnica propuesta

La arquitectura tecnica propuesta organiza el SGB en capas desacopladas, seguras y operables. El objetivo es permitir que el sistema existente evolucione desde una aplicacion Django/Python hacia una plataforma institucional moderna, desplegada en Microsoft Azure, con datos protegidos, documentos gestionados, API funcional, monitoreo, backups y capacidad de crecimiento modular.

La arquitectura se compone de:

- **Capa de experiencia:** interfaz web para direccion, operadores, gerentes, auditores y administradores.
- **Capa aplicativa:** SGB basado en Django/Python, con modulos existentes adaptados y modulos nuevos en Etapa II.
- **Capa de API:** servicios controlados para interoperabilidad del SGB, con alcance minimo pendiente de validacion.
- **Capa de datos:** PostgreSQL 14+ con PostGIS y unaccent como motor preferido.
- **Capa documental:** almacenamiento de documentos, imagenes, videos y evidencias.
- **Capa de seguridad:** identidad, permisos, MFA, cifrado, WAF, VPN, secretos y auditoria.
- **Capa de operacion:** monitoreo, logs, alertas, backups, DRP y soporte.

## Flujo tecnico de alto nivel

Un usuario autorizado accede al sistema mediante dominio institucional con TLS. La solicitud pasa por controles de entrada y WAF antes de alcanzar la aplicacion contenerizada. La aplicacion consulta PostgreSQL por canal controlado, accede a documentos en almacenamiento seguro, obtiene secretos mediante Key Vault o mecanismo equivalente, registra eventos en auditoria y envia metricas/logs a la plataforma de observabilidad.

## API e interoperabilidad

La RFP exige una API funcional del SGB, interoperable con sistemas externos. Esta propuesta distingue entre:

- **API base del SGB:** entregable obligatorio, diseñada para INCABIDE y validada en produccion.
- **Interconexion con PGR:** item independiente y opcional, dependiente de aprobacion de la Procuraduria General de la Republica, sin fecha fija ni penalidad atribuible al proveedor, conforme a la RFP.

Esta separacion protege alcance, cronograma, costo y responsabilidades.

## Datos y almacenamiento

La base de datos transaccional debe preservar compatibilidad con PostgreSQL 14+ y extensiones PostGIS/unaccent. Los documentos y archivos multimedia no deben tratarse como simples adjuntos sin gobierno; deben almacenarse con metadatos, clasificacion, permisos, auditoria y relacion directa con expedientes, bienes, contratos o procesos de disposicion.

## Observabilidad y operacion

La arquitectura incorpora monitoreo y alertas desde el diseno. El sistema debe registrar errores, accesos, eventos funcionales, actividad administrativa, exportaciones, cambios de permisos y eventos de seguridad. Esta informacion permite soporte, auditoria, continuidad y mejora continua.

## Trazabilidad RFP

Este capitulo cubre TEC-001 a TEC-026, AZ-001 a AZ-015, SEC-003 a SEC-038 y QA-004 a QA-012.

## Informacion pendiente de Justech

Justech debe confirmar:

- arquitectos asignados;
- experiencia real con Django/Python, PostgreSQL y Azure;
- herramientas de observabilidad usadas;
- enfoque de API y documentacion tecnica;
- certificaciones reales si seran incluidas.

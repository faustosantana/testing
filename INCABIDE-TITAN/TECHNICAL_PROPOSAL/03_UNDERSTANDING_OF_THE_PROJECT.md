# 03 — UNDERSTANDING OF THE PROJECT

## Comprension del contexto institucional

PADF acompana a INCABIDE en un proceso de fortalecimiento institucional para la administracion de bienes incautados, decomisados y en extincion de dominio en la Republica Dominicana. En este contexto, el Sistema de Gestion de Bienes (SGB) debe evolucionar desde una plataforma existente hacia una solucion moderna, segura, trazable y operable, capaz de sostener procesos sensibles donde la evidencia, la custodia, la auditoria y la toma de decisiones son elementos centrales.

La RFP establece que el SGB actual esta desarrollado en Django/Python, utiliza PostgreSQL 14+ con extensiones PostGIS y unaccent, y cubre procesos que van desde el registro de causas judiciales y bienes asociados hasta su disposicion final. Tambien indica que INCABIDE posee el codigo fuente y que este sera entregado al adjudicatario en su estado actual. Este punto es critico: la propuesta tecnica debe reconocer que el proyecto inicia con un diagnostico responsable del codigo existente y no con supuestos no verificados sobre su calidad interna.

## Comprension del problema tecnico

El documento de RFP identifica limitaciones que deben ser abordadas de forma estructurada:

- modulos potencialmente incompletos, en particular el modulo de Subastas;
- falta de preparacion del sistema para una infraestructura cloud moderna;
- necesidad de personalizacion visual, terminologica e institucional para INCABIDE;
- necesidad de nuevos modulos para soportar la operacion completa;
- requerimientos reforzados de seguridad, auditoria, continuidad, respaldo y soporte.

Por tanto, la adaptacion del SGB no puede tratarse como una simple instalacion tecnica. Debe abordarse como una modernizacion controlada, con diagnostico, refactorizacion, contenerizacion, despliegue en Azure, evidencias por hito, seguridad desde el diseno y transferencia operacional a INCABIDE.

## Comprension del alcance por etapas

La RFP divide el proyecto en dos etapas:

**Etapa I — Adaptacion y despliegue del sistema existente.** Esta etapa busca acondicionar, personalizar y desplegar el SGB original sin desarrollar nuevas funcionalidades. Incluye analisis del codigo fuente, actualizacion de dependencias, refactorizacion para nube, adaptacion de funcionalidades existentes afectadas por infraestructura, personalizacion visual y terminologica, implementacion de infraestructura Azure, contenerizacion, puesta en produccion, documentacion, capacitacion, entrega de accesos e inicio del soporte.

**Etapa II — Desarrollo progresivo de nuevos modulos.** Esta etapa incorpora capacidades adicionales priorizadas por INCABIDE: mejoras al registro de activos, gestion de contratos y clientes, subasta/ventas, descargo/donaciones, soporte multilenguaje, seguridad avanzada y funciones transversales como multimedia, geolocalizacion, auditoria, importacion/exportacion y reportes.

## Comprension del criterio de exito

El exito tecnico no se limita a que el sistema funcione. La RFP exige aprobaciones escritas, evidencias concretas, criterios de aceptacion por hito, UAT por modulo, documentacion, soporte y seguridad verificable. Por ello, Justech debe orientar la ejecucion hacia entregables aceptables, trazables y auditables.

## Trazabilidad RFP

Este capitulo cubre principalmente los requisitos TEC-001 a TEC-010, DOC-006, DOC-007, CRON-004, CRON-005, AZ-001, SEC-003 y QA-001 a QA-004.

## Informacion pendiente de Justech

Para completar la version final con evidencia corporativa, Justech debe confirmar:

- experiencia real en proyectos Django/Python, PostgreSQL, Azure y despliegues cloud;
- metodologia propia de diagnostico y modernizacion;
- equipo tecnico asignado;
- referencias comparables verificables.

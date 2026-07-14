# 05 — PROPOSED SOLUTION

## Vision general de la solucion

Justech propone abordar la adaptacion del SGB como una modernizacion integral, orientada a convertir el sistema existente en una plataforma institucional segura, trazable, operable y preparada para evolucionar por modulos. La solucion mantiene la base tecnologica indicada por la RFP —Django/Python y PostgreSQL 14+ con PostGIS y unaccent— y la adapta para operar sobre Microsoft Azure, plataforma obligatoria del proceso.

La propuesta tecnica se estructura alrededor de un principio central: cada bien administrado por INCABIDE debe contar con una historia digital completa. Esa historia inicia con el registro del caso y del bien, continua con su clasificacion, ubicacion, documentos, custodia, movimientos, aprobaciones y decisiones, y concluye con su disposicion final o cierre administrativo. En cada etapa, el sistema debe preservar evidencia, aplicar permisos, registrar auditoria y ofrecer informacion util para la toma de decisiones.

## Componentes de la solucion

La solucion se compone de las siguientes capas:

**Capa de experiencia.** Interfaz web para usuarios ejecutivos, operativos, administradores y auditores, con dashboards, expedientes, reportes, mapas, documentos, timeline y cadena de custodia.

**Capa de aplicacion.** SGB basado en Django/Python, con adaptacion de funcionalidades existentes durante Etapa I y evolucion modular durante Etapa II.

**Capa de API.** API funcional del SGB para INCABIDE, interoperable con sistemas externos. La interconexion especifica con PGR se mantiene separada, conforme a la RFP, por depender de aprobacion externa.

**Capa de datos.** PostgreSQL 14+ como motor preferido, con PostGIS para capacidades geoespaciales y unaccent para busqueda sin distincion de acentos. El almacenamiento documental y multimedia se gestiona fuera de la base transaccional mediante almacenamiento seguro.

**Capa Azure.** Infraestructura en Microsoft Azure con red segmentada, contenedores, base de datos gestionada o equivalente validado, almacenamiento, Key Vault, monitoreo, backups y controles de seguridad.

**Capa de seguridad.** MFA, RBAC, cifrado, WAF, DDoS, VPN, gestion segura de secretos, auditoria, escaneos y pentest.

**Capa de operacion.** Monitoreo, alertas, soporte, documentacion, capacitacion, runbooks, backup, restauracion y transferencia de control a INCABIDE.

## Etapa I: estabilizar, adaptar y desplegar

Durante la Etapa I, la solucion se enfoca en hacer operable el SGB existente en Azure. Esto incluye diagnosticar el codigo fuente, corregir dependencias, refactorizar configuraciones sensibles, adaptar funciones afectadas por el cambio de infraestructura, aplicar marca y terminologia INCABIDE, contenerizar, desplegar, documentar, capacitar, entregar accesos y activar soporte.

La Etapa I no se presenta como desarrollo de nuevas funcionalidades, sino como acondicionamiento tecnico, institucional y operativo del sistema existente, conforme al alcance de la RFP.

## Etapa II: evolucion modular

Durante la Etapa II, la solucion se expande mediante modulos priorizados por INCABIDE. Cada modulo debe contar con pantallas o prototipos validados antes del desarrollo, especificaciones funcionales, codigo fuente, pruebas funcionales, UAT, manual de usuario y acta de aceptacion parcial. Esta estructura permite que INCABIDE y PADF incorporen capacidades de forma progresiva sin perder control de alcance ni trazabilidad.

## Diferenciadores tecnicos

La propuesta se diferencia por:

- trazabilidad completa de requisitos;
- arquitectura Azure Enterprise;
- seguridad verificable;
- QA basado en evidencia y no solo en ausencia de errores;
- experiencia de usuario orientada a producto Enterprise moderno;
- separacion clara entre API base y PGR opcional;
- enfoque modular para Etapa II;
- transferencia real de conocimiento y accesos.

## Trazabilidad RFP

Este capitulo cubre TEC-001 a TEC-026, AZ-001 a AZ-015, SEC-001 a SEC-038, FUNC-GEN-001 a FUNC-GEN-010 y FUNC-001 a FUNC-191.

## Informacion pendiente de Justech

Para cerrar esta seccion con evidencia corporativa, Justech debe confirmar:

- stack operativo y herramientas reales;
- capacidades Azure y DevSecOps;
- experiencia comprobable;
- equipo asignado;
- certificaciones reales si seran mencionadas.

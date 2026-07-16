# 04 — CURRENT CHALLENGES

## Retos principales identificados

La RFP presenta un proyecto con alto valor institucional y con riesgos tecnicos que deben ser gestionados desde el inicio. El primer reto es que el codigo fuente sera recibido por el adjudicatario en su estado actual. Esto implica que cualquier compromiso tecnico responsable debe iniciar con un diagnostico formal de compatibilidad, dependencias, configuracion, patrones de desarrollo, seguridad y comportamiento de los modulos existentes.

El segundo reto es la preparacion cloud. La RFP indica expresamente que el SGB no esta preparado para una infraestructura de nube moderna. Por ello, la Etapa I debe contemplar la eliminacion de dependencias de archivos de configuracion, el uso de variables de entorno o mecanismos seguros de configuracion, la adaptacion del manejo de archivos, la validacion de reportes y la revision de geolocalizacion para operar correctamente en Azure.

El tercer reto es la seguridad. El SGB administra datos sensibles asociados a procesos penales, personas, bienes incautados y activos bajo custodia. La RFP exige cifrado, MFA, control de acceso por rol, auditoria, minimizacion de datos, gestion segura de credenciales, WAF, DDoS, VPN, monitoreo, alertas, escaneos, backups cifrados, DRP y pentest. La seguridad debe ser tratada como condicion de aceptacion, no como componente secundario.

El cuarto reto es la ambiguedad de ciertas dependencias. La API funcional del SGB es obligatoria, pero la interconexion efectiva con PGR depende de aprobacion externa y debe cotizarse por separado. El sistema de subastas existente debe integrarse y complementarse, pero su especificacion tecnica no forma parte del contenido recibido. La region Azure, tenant, ambientes, volumen de datos, usuarios, concurrencia, RTO/RPO y soporte critico fuera de horario tambien requieren validacion.

## Riesgos contractuales y operativos

La RFP contiene un regimen de penalidades que hace necesario controlar alcance, calidad, seguridad y plazos. Existen penalidades por atraso de hitos, incumplimiento de SLA, entregables incompletos, brechas de seguridad, paralizacion, subcontratacion no autorizada y violacion de confidencialidad o propiedad intelectual. Esto obliga a estructurar la ejecucion con evidencias, aprobaciones, control de cambios, QA riguroso y trazabilidad.

## Enfoque de mitigacion

La respuesta tecnica debe mitigar estos retos mediante:

- diagnostico inicial del codigo fuente y dependencias;
- matriz de requisitos y cumplimiento;
- arquitectura Azure defendible;
- controles de seguridad verificables;
- enfoque DevSecOps;
- pruebas funcionales y UAT;
- documentacion tecnica;
- capacitacion;
- soporte y escalamiento;
- supuestos y exclusiones claramente definidos.

## Trazabilidad RFP

Este capitulo cubre TEC-003 a TEC-018, AZ-001 a AZ-015, SEC-001 a SEC-038, SUP-001 a SUP-008 y PEN-001 a PEN-021.

## Informacion pendiente de Justech

Justech debe confirmar:

- politica interna de gestion de riesgos;
- capacidad de soporte fuera de horario;
- herramientas de analisis, QA y seguridad;
- experiencia comprobable en escenarios similares;
- postura interna sobre supuestos y exclusiones.

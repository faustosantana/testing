# 02 — EXECUTIVE SUMMARY

## Objetivo

Presentar, en un maximo de tres paginas, la vision ejecutiva de la Oferta Tecnica para la RFP No. 5801 DRC3P, demostrando comprension del problema, solucion propuesta, diferenciadores, beneficios y pendientes de informacion de Justech.

## Executive Summary

PADF e INCABIDE requieren adaptar el Sistema de Gestion de Bienes (SGB) para convertirlo en una plataforma moderna, segura y operable para la administracion de bienes incautados, decomisados y en extincion de dominio. La RFP establece que el SGB existente esta desarrollado en Django/Python, utiliza PostgreSQL 14+ con extensiones PostGIS y unaccent, y sera entregado al adjudicatario en su estado actual. Tambien identifica limitaciones que deben ser abordadas: modulos potencialmente incompletos, falta de preparacion para una infraestructura cloud moderna, necesidad de personalizacion visual y terminologica, y requerimiento de nuevos modulos para la operacion completa de INCABIDE.

La propuesta tecnica de Justech debe responder a ese contexto con una solucion que no sea simplemente una instalacion en nube, sino una transformacion controlada del SGB en una plataforma institucional de gestion, trazabilidad, seguridad, evidencia y toma de decisiones. El proyecto debe permitir que cada bien tenga un expediente digital, que cada accion relevante deje rastro, que cada cambio sea auditable y que cada hito pueda ser aprobado con evidencia verificable por PADF e INCABIDE.

La vision propuesta organiza el proyecto en las dos etapas definidas por la RFP. La **Etapa I** se enfoca en diagnosticar el codigo fuente existente, revisar dependencias, corregir incompatibilidades, refactorizar configuraciones sensibles para operacion cloud, adaptar funcionalidades afectadas por la infraestructura, aplicar identidad visual y terminologia institucional de INCABIDE, desplegar sobre Microsoft Azure, contenerizar la aplicacion, publicar el sistema en dominio institucional con TLS, entregar documentacion tecnica, capacitar al equipo tecnico, entregar accesos completos y activar soporte post-despliegue. La **Etapa II** permite evolucionar el SGB por modulos priorizados por INCABIDE, incluyendo registro e ingreso de activos, gestion de contratos y clientes, subastas/ventas, descargo de activos/donaciones, soporte multilenguaje, seguridad y control de acceso avanzado, y funciones transversales como documentacion multimedia, geolocalizacion, auditoria del personal, importacion/exportacion masiva y reportes para toma de decisiones.

La solucion se construye sobre cuatro ejes tecnicos. Primero, **modernizacion cloud-ready**, manteniendo la base Django/Python y PostgreSQL/PostGIS/unaccent, pero adaptando configuraciones, dependencias, manejo de archivos, reportes, geolocalizacion y despliegue para operar en Microsoft Azure. Segundo, **seguridad desde el diseno**, incorporando controles exigidos por la RFP: cifrado en transito y reposo, MFA para accesos administrativos, control de acceso por rol, auditoria, gestion segura de credenciales, WAF, DDoS, VPN para accesos administrativos, monitoreo, alertas, backups cifrados, DRP, escaneos y pentest de tercero independiente. Tercero, **aceptacion por evidencia**, donde cada hito y modulo se vincula con entregables, pruebas, UAT, documentacion, actas y criterios de aprobacion. Cuarto, **adopcion institucional**, mediante experiencia de usuario moderna, documentacion, capacitacion, runbooks, soporte y transferencia real de conocimiento a INCABIDE.

El ciclo de vida del bien es la narrativa central de la solucion. Desde que un bien ingresa, el sistema debe registrar su origen, caso, entidad remitente, categoria, ubicacion, identificador, documentos y evidencia multimedia. Durante la custodia, debe conservar movimientos, cambios de estado, responsables, aprobaciones, documentos y auditoria. Cuando el bien avanza hacia contrato, subasta, venta, donacion, devolucion, destruccion o cierre, el SGB debe sostener el flujo con permisos, controles, reportes y evidencia. Para la Direccion de INCABIDE, el sistema debe ofrecer una vision ejecutiva clara: cantidad de bienes, valor economico estimado, distribucion por provincia, bienes por estado, alertas, proximas subastas, procesos criticos y KPIs. Para operadores, debe simplificar el registro y seguimiento. Para auditores, debe permitir reconstruir decisiones. Para TI, debe entregar una plataforma documentada, monitoreada, respaldada y transferible.

Los diferenciadores tecnicos de la propuesta deben estar en la trazabilidad y en la madurez de ejecucion. La oferta no debe limitarse a decir que el sistema funcionara; debe demostrar como se controlaran riesgos, como se validara cada entregable, como se protegeran datos sensibles, como se documentara la operacion, como se transferira conocimiento y como se evitara aceptar funcionalidades solo porque "no fallan". El criterio de calidad de INCABIDE TITAN exige que una funcionalidad solo pueda considerarse aprobada si es usable, coherente, consistente con el producto, segura, respetuosa de permisos, libre de duplicidad y sin deuda tecnica evidente.

Los beneficios esperados se derivan directamente del alcance de la RFP. INCABIDE obtendria mayor visibilidad sobre sus bienes, mejor trazabilidad documental y operativa, una plataforma preparada para Microsoft Azure, controles de seguridad reforzados, capacidad de reporte, gestion modular de nuevas funcionalidades, soporte post-despliegue, documentacion tecnica y transferencia de conocimiento. PADF e INCABIDE tambien contarian con un modelo de aceptacion por evidencias, lo que reduce ambiguedades y facilita validar hitos, modulos y cierre.

Esta propuesta tecnica debe ser completada con informacion corporativa verificable de Justech antes de convertirse en documento final. No deben incorporarse experiencias, certificaciones, clientes, metricas, partners ni referencias que no puedan probarse documentalmente.

## Relacion con la RFP

Este resumen responde a los elementos centrales de la RFP:

- contratacion de empresa especializada para diagnostico, correccion, adaptacion tecnica, personalizacion y puesta en produccion del SGB;
- estructura por Etapa I y Etapa II;
- despliegue obligatorio sobre Microsoft Azure;
- PostgreSQL 14+ con PostGIS/unaccent como base preferida;
- API funcional del SGB;
- seguridad reforzada, evidencias de seguridad y pentest;
- documentacion tecnica, capacitacion, accesos completos y soporte por un ano;
- desarrollo modular posterior con mockups/prototipos, UAT, manuales y actas.

## Requisitos cubiertos

- TEC-001 a TEC-026: SGB actual, diagnostico, adaptacion cloud, contenerizacion y API.
- AZ-001 a AZ-015: Microsoft Azure, computo, base de datos, almacenamiento, DNS/TLS e infraestructura.
- SEC-001 a SEC-038: confidencialidad, proteccion de datos, seguridad de infraestructura y evidencias.
- QA-001 a QA-029: criterios de aceptacion, UAT, cierre y evidencias.
- CAP-001 a CAP-004: capacitacion y transferencia de conocimiento.
- SUP-001 a SUP-008: soporte post-despliegue y SLA.
- FUNC-GEN-001 a FUNC-GEN-010 y FUNC-001 a FUNC-191: evolucion modular y funciones transversales.

## Evidencias necesarias

- Matriz de cumplimiento final.
- Equipo propuesto con CVs y dedicacion.
- Certificaciones reales, si existen.
- Referencias comparables verificables.
- Arquitectura Azure final validada.
- Matriz de seguridad control-evidencia.
- Plan QA/UAT y criterios de aceptacion.
- Plan de soporte y escalamiento.
- Plan de capacitacion y transferencia.

## Dependencias

- Acceso al codigo fuente solo posterior a adjudicacion.
- Respuestas PADF/INCABIDE sobre alcance minimo de API, region Azure, tenant/suscripcion, ambientes, datos, usuarios, soporte critico y sistema de subastas existente.
- Linea grafica INCABIDE y validacion legal de terminologia.
- Confirmacion de supuestos y exclusiones por Justech.

## Informacion pendiente de Justech

- Historia corporativa breve y perfil institucional.
- Capacidades tecnicas reales.
- Equipo propuesto, dedicacion y CVs.
- Certificacion PMP del lider de proyecto.
- Certificaciones Microsoft/Azure reales, si existen.
- Referencias comparables verificables.
- Experiencia real en Python/Django, PostgreSQL/PostGIS, Azure, DevSecOps, seguridad y soporte.
- Metodologia propia de implementacion, QA, DevSecOps, soporte y capacitacion.
- Politicas internas de seguridad, calidad, continuidad y gestion de incidentes.

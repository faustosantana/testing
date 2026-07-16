# 09 — SECURITY AND COMPLIANCE

## Enfoque de seguridad

El SGB administrara informacion sensible relacionada con bienes incautados, decomisados y en extincion de dominio, procesos penales, personas y documentacion institucional. Por esta razon, la seguridad debe formar parte de la arquitectura, del desarrollo, de la operacion y de la aceptacion de hitos.

La RFP exige medidas reforzadas de proteccion de datos personales conforme a la Ley 172-13 de la Republica Dominicana, asi como salvaguardas tecnicas y contractuales para tratamiento transfronterizo de datos en Azure. La propuesta tecnica responde con un modelo de seguridad por capas, basado en identidad, red, aplicacion, datos, auditoria, monitoreo, backups y pruebas independientes.

## Controles principales

La solucion incorpora los siguientes controles:

- autenticacion multifactor para accesos administrativos;
- control de acceso por rol;
- principio de minimo privilegio;
- cifrado en transito mediante TLS/HTTPS;
- cifrado en reposo para datos y almacenamiento;
- gestion segura de credenciales mediante vault;
- WAF con proteccion contra OWASP Top 10;
- proteccion DDoS conforme al nivel aprobado;
- firewall y reglas por IP/puerto;
- segmentacion de red;
- VPN o Bastion para acceso administrativo;
- monitoreo, logs y alertas;
- escaneos de seguridad;
- backups automaticos y cifrados;
- plan de recuperacion ante desastres;
- pentest por tercero independiente posterior al despliegue en produccion.

## Evidencias de seguridad

La RFP establece que no debe solicitarse aprobacion del Hito 4 sin entregar evidencias de seguridad revisadas y aprobadas. Por ello, la propuesta contempla preparar:

- documento de arquitectura de seguridad;
- evidencias de configuracion de controles;
- informe de vulnerabilidades con CVSS y remediaciones;
- reporte TLS/HTTPS con calificacion minima requerida;
- evidencia de MFA activo;
- registro de backup operativo y restaurable;
- declaracion de ausencia de credenciales en codigo fuente o archivos versionados;
- informe de pentest tercero y plan de remediacion.

## Confidencialidad y propiedad intelectual

El codigo fuente, accesos de produccion y datos sensibles se entregan solo al adjudicatario bajo las condiciones de confidencialidad indicadas en la RFP. La solucion debe mantener controles estrictos sobre acceso, uso, almacenamiento y entrega de credenciales, asi como inventario de librerias open source con licencias compatibles.

## Auditoria

La plataforma debe conservar trazabilidad de accesos, cambios de datos, modificaciones de permisos, cargas y descargas documentales, exportaciones, aprobaciones, movimientos de custodia y acciones administrativas. La auditoria no es un reporte posterior, sino un componente transversal de confianza.

## Trazabilidad RFP

Este capitulo cubre SEC-001 a SEC-038, LEG-013 a LEG-016, PEN-012/PEN-013/PEN-018/PEN-019 y QA-015, QA-024 y criterios de cierre relacionados con seguridad.

## Informacion pendiente de Justech

Justech debe confirmar:

- politicas internas de seguridad;
- certificaciones de seguridad reales, si existen;
- herramientas de escaneo;
- procedimiento de respuesta a incidentes;
- experiencia con pentest o proveedores disponibles;
- capacidad de generar inventario de dependencias o SBOM si se requiere.

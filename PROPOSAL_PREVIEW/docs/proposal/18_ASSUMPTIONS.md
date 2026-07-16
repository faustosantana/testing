# 18 — ASSUMPTIONS

## Proposito

Esta seccion registra supuestos tecnicos necesarios para interpretar correctamente la Oferta Tecnica. Los supuestos no sustituyen respuestas oficiales de PADF/INCABIDE ni informacion verificable de Justech. Cualquier supuesto critico debe validarse antes de cerrar compromisos contractuales, tecnicos o economicos.

## Supuestos basados en la RFP

- El codigo fuente del SGB sera entregado unicamente al adjudicatario, bajo las condiciones de confidencialidad correspondientes.
- La Etapa I no incluye desarrollo de nuevas funcionalidades, sino adaptacion, personalizacion y despliegue del sistema existente.
- Microsoft Azure es plataforma obligatoria y no sustituible.
- PostgreSQL 14+ con PostGIS y unaccent es el motor preferido.
- Un motor alternativo solo seria aceptable si garantiza capacidades equivalentes y cuenta con validacion de INCABIDE.
- La API funcional del SGB es un entregable obligatorio.
- La interconexion efectiva con PGR depende de aprobacion de dicha institucion y debe cotizarse por separado.
- La infraestructura cloud y el soporte tecnico se incluyen por un ano conforme a la RFP.
- Cada hito requiere aprobacion escrita de PADF/INCABIDE para considerarse entregado.

## Supuestos pendientes de validacion PADF/INCABIDE

- Region Azure.
- Tenant y suscripcion Azure.
- Ambientes requeridos: desarrollo, QA, UAT, produccion.
- Alcance minimo de la API del SGB.
- Alcance y especificacion tecnica del sistema de subastas existente.
- Usuarios totales y concurrentes.
- Volumen de datos y documentos.
- Necesidad y alcance de migracion historica.
- RTO, RPO y retencion de backups.
- Retencion de logs.
- Nivel de WAF y DDoS.
- Modelo de VPN o Bastion.
- Proveedor o criterio para pentest.
- Catalogos oficiales de provincias, municipios, entidades remitentes y tipos de activos.
- Alcance del soporte critico fuera de horario respecto al volumen estimado de horas.

## Supuestos pendientes de Justech

- Equipo final asignado.
- Certificacion PMP del lider de proyecto.
- Certificaciones Microsoft/Azure reales, si se incluiran.
- Referencias comparables verificables.
- Capacidad de soporte fuera de horario.
- Herramientas de DevSecOps, QA, monitoreo y soporte.
- Politicas internas de seguridad, calidad y continuidad.
- Supuestos y exclusiones aceptables para la version final.

## Gestion de supuestos

Cada supuesto debe mantenerse trazable a:

- requisito RFP;
- pregunta PADF si aplica;
- decision interna Justech;
- impacto tecnico;
- impacto operativo;
- evidencia o documento que lo cierre.

## Trazabilidad RFP

Este capitulo cubre ADM-003, TEC-003, TEC-008, TEC-011, TEC-012, TEC-024 a TEC-026, AZ-001 a AZ-015, SUP-008 y brechas identificadas en la matriz de cumplimiento.

## Regla final

Ningun supuesto debe convertirse en compromiso final sin validacion oficial, evidencia suficiente o aprobacion interna de Justech.

# COMMITTEE REVIEW SIMULATION

## Proposito

Simular la revision del comite evaluador de PADF/INCABIDE antes de redactar capitulos finales. Este documento no forma parte de la entrega; sirve para anticipar preguntas, brechas, evidencias y puntos debiles.

## Preguntas probables del comite

| Tema | Pregunta probable | Donde debe responderse |
| --- | --- | --- |
| Comprension | ¿El proponente entendio que esto no es solo despliegue, sino administracion institucional de bienes sensibles? | Capitulos 3-8 |
| Etapa I | ¿Como diagnosticaran el codigo si no lo conocen antes de adjudicacion? | Capitulos 5, 9, 28, 32 |
| Cloud | ¿Por que esta arquitectura Azure es suficiente y segura? | Capitulos 18-20 |
| API | ¿Que incluye la API obligatoria y que queda separado de PGR? | Capitulos 7, 13, 18, 32, 33 |
| Seguridad | ¿Como evitan una brecha que active penalidades? | Capitulos 20, 21, 24, 28 |
| Soporte | ¿Como cumpliran SLA critico de 1 hora? | Capitulo 25 |
| Equipo | ¿El equipo cumple PMP, Python/Django y DevOps/Seguridad? | Capitulo 29 |
| Experiencia | ¿Hay al menos 3 referencias comparables verificables? | Capitulo 30 |
| Modularidad | ¿PADF puede contratar modulos por separado sin perder coherencia? | Capitulos 10-17, 31 |
| Aceptacion | ¿Como se evitara entregar algo incompleto o de baja calidad? | Capitulos 24, 31, 34 |

## Afirmaciones que necesitan evidencia

| Afirmacion | Evidencia requerida | Estado |
| --- | --- | --- |
| Justech cuenta con equipo calificado | CVs, PMP, certificaciones, roles, dedicacion | Pendiente Justech |
| Justech tiene experiencia comparable | 3 referencias con rol, periodo y resultados | Pendiente Justech |
| La arquitectura Azure es defendible | Diagramas, matriz de decisiones, controles, supuestos | Base interna lista |
| La seguridad cubre RFP | Matriz control -> evidencia; CVSS; TLS; MFA; backup; pentest futuro | Pendiente ejecucion |
| La Etapa I es controlable | Hito -> actividad -> entregable -> evidencia | Base interna lista |
| La Etapa II es modular | Modulo -> entregables -> UAT -> acta | Base interna lista |
| La transferencia sera efectiva | Plan de capacitacion, materiales, lista asistencia, runbooks | Pendiente Justech/equipo |

## Donde podemos perder puntos

| Riesgo de perdida | Criterio afectado | Mitigacion |
| --- | --- | --- |
| Equipo sin PMP verificable | Capacidad/equipo | Confirmar certificado antes de redactar. |
| Referencias debiles o no comparables | Experiencia institucional | Seleccionar referencias con similitud real. |
| Seguridad redactada genericamente | Calidad tecnica | Usar matriz de controles RFP y Azure Enterprise. |
| Azure sin decisiones pendientes claras | Calidad tecnica / valor-precio | Marcar PENDIENTE DE VALIDACION y explicar supuestos. |
| API/PGR mezclados | Calidad tecnica / costo | Separar API SGB obligatoria de PGR opcional. |
| Soporte critico ambiguo | Calidad tecnica / costo | Definir supuestos y pedir aclaracion PADF. |
| Propuesta demasiado extensa sin narrativa | Comprension/calidad | Mantener estructura por partes y lectura tipo libro. |
| Falta de evidencias visuales | Calidad tecnica | Preparar diagramas/tablas futuros antes de redaccion final. |

## Que falta

1. Informacion corporativa de Justech.
2. CVs oficiales y dedicacion cuantitativa del equipo.
3. Evidencia documental de PMP del lider de proyecto.
4. Certificaciones Microsoft reales, si existen.
5. Referencias comparables verificables.
6. Politicas de seguridad, QA, soporte y continuidad de Justech.
7. Decision de anexos externos vs internos.
8. Respuestas PADF sobre API, Azure, ambientes, datos, soporte y subastas.
9. Aprobacion de supuestos y exclusiones por Fausto/Justech.

## Que fortalece la propuesta

| Fortaleza | Como usarla |
| --- | --- |
| Matriz de 428 requisitos | Demostrar cobertura y trazabilidad. |
| Solution Blueprint | Sustentar solucion integrada. |
| UX Master | Diferenciar experiencia y adopcion. |
| Azure Enterprise | Defender arquitectura y seguridad. |
| Solution Story | Hacer visible el ciclo de vida del bien. |
| QA no conformidad | Mostrar estandar superior a "funciona". |
| Critica tecnica obligatoria | Demostrar madurez de delivery. |
| Master outline por partes | Convertir la propuesta en documento editorial profesional. |
| Team and Governance | Mostrar gobierno, responsabilidades, RACI, competencias y cobertura por especialidad. |
| Arquitectura Azure proposal-ready | Defender topologia, seguridad, HA, DR, monitoreo y supuestos de costo sin precios. |

## Preguntas que debemos poder responder verbalmente

- ¿Que pasa si el codigo fuente esta en peor estado del esperado?
- ¿Que ocurre si INCABIDE no entrega DNS o linea grafica a tiempo?
- ¿Como se protege la informacion sensible?
- ¿Como se garantiza que no queden credenciales en codigo?
- ¿Como se prueba que el sistema esta listo?
- ¿Que diferencia esta propuesta de una instalacion basica en nube?
- ¿Como se evita dependencia permanente del proveedor?
- ¿Que queda fuera de Etapa I?

## Semaforo actual

| Area | Estado | Comentario |
| --- | --- | --- |
| Comprension RFP | Verde | Artefactos de analisis completos. |
| Solucion tecnica | Verde | Blueprint y Azure Enterprise listos. |
| UX/adopcion | Verde | UX Master listo. |
| Equipo | Ambar | Equipo base confirmado e integrado; faltan CVs oficiales y dedicacion cuantitativa. |
| Experiencia/referencias | Rojo | Falta evidencia Justech. |
| Certificaciones | Rojo | Falta confirmacion. |
| Arquitectura definitiva | Verde | Arquitectura Azure y diagramas proposal-ready disponibles. |
| Demo/presentacion | Verde | Plan maestro y storyboard disponibles, sin desarrollo aun. |
| Preguntas PADF | Ambar | Borrador listo, falta envio/respuesta. |
| Supuestos/exclusiones | Ambar | Requieren decision Fausto/Justech. |

# WAR ROOM DASHBOARD — INCABIDE TITAN

Ultima actualizacion: Dia 2 - Solution Blueprint completo

## Estado general

| Indicador | Valor |
| --- | --- |
| % completado | 30% |
| Fase actual | Fase 2 — Solution Blueprint |
| Estado general | Solucion tecnica maestra disenada |
| Responsable de seguimiento | PM Bid |
| Requisitos trazables | 428 |
| Entregables identificados | 58 |
| Riesgos/brechas | 31 |
| Preguntas PADF | 75 |
| Modulos/bloques funcionales | 11 |
| Documentos Solution Blueprint | 23 |
| WOW Factors | 35 |

## Documentos pendientes

| Documento | Area | Responsable | Estado | Fecha objetivo |
| --- | --- | --- | --- | --- |
| Matriz maestra de cumplimiento | 02_REQUIREMENTS | PM Bid | Completada base | Dia 1 |
| Preguntas PADF Anexo 4 | 02_REQUIREMENTS | Bid Manager | Borrador | Dia 1 |
| Backlog profesional | 02_REQUIREMENTS | PMP | Completado base | Dia 1 |
| Solution Blueprint | SOLUTION_BLUEPRINT | CTO / Arquitectos | Completado base | Dia 2 |
| WHY_JUSTECH_SHOULD_WIN | SOLUTION_BLUEPRINT | Bid Manager / CTO | Completado base | Dia 2 |
| Oferta tecnica | 03_PROPOSAL | Lider propuesta | Pendiente | Dia 3 |
| Oferta economica | 07_COSTS | Lider comercial | Pendiente | Dia 3 |
| Paquete legal | 10_LEGAL | Responsable legal | Pendiente | Dia 4 |
| Checklist de entrega | 11_DELIVERY | Lider entrega | Pendiente | Dia 5 |

## Proximos hitos

| Hito | Fecha | Responsable | Estado |
| --- | --- | --- | --- |
| Completar Bid Center | Dia 0 | PM Bid | Completado |
| Leer RFP completo y anexos | Dia 1 | PM Bid | Completado |
| Consolidar requisitos | Dia 1 | PM Bid | Completado base |
| Aprobar preguntas PADF | Dia 1 | Bid Manager / CTO | Pendiente |
| Confirmar equipo, CVs y certificaciones | Dia 1 | PMO / CTO | Pendiente |
| Revisar Solution Blueprint | Dia 2 | CTO / Arquitectos | Pendiente |
| Seleccionar WOW Factors para propuesta | Dia 2 | Bid Manager / CTO | Pendiente |
| Ejecutar QA documental | Dia 4 | Responsable QA | Pendiente |
| Preparar entrega final | Dia 5 | Lider entrega | Pendiente |

## Problemas abiertos

| ID | Problema | Impacto | Responsable | Estado |
| --- | --- | --- | --- | --- |
| ISS-001 | Codigo fuente no disponible antes de adjudicacion | Critico | CTO | Abierto |
| ISS-002 | Alcance minimo de API no definido | Critico | Arquitecto Django | Abierto |
| ISS-003 | Region, tenant, ambientes y dimensionamiento Azure no definidos | Critico | Arquitecto Azure | Abierto |
| ISS-004 | Equipo, certificaciones y referencias reales pendientes de confirmar | Alto | PMO / Bid Manager | Abierto |
| ISS-005 | Soporte critico fuera de horario ambiguo frente a 30 horas anuales | Alto | Service Manager | Abierto |

## Decisiones tomadas

| ID | Decision | Fecha | Responsable | Evidencia |
| --- | --- | --- | --- | --- |
| DEC-001 | Usar INCABIDE TITAN como nombre interno del Bid Center | Dia 0 | PM Bid | README.md |
| DEC-002 | No redactar propuesta tecnica/economica hasta cerrar entendimiento y preguntas | Dia 1 | Bid Manager | NEXT_PHASE_READINESS.md |
| DEC-003 | Separar API base obligatoria de interconexion PGR opcional | Dia 1 | CTO | PADF_QUESTIONS_ANEXO_4_DRAFT.md |
| DEC-004 | Disenar Solution Blueprint sin redactar propuesta final ni precios | Dia 2 | CTO | SOLUTION_BLUEPRINT/README.md |

## Bloqueos

| ID | Bloqueo | Dependencia | Plan de accion | Responsable |
| --- | --- | --- | --- | --- |
| BLK-001 | Codigo fuente no disponible | Entrega solo al adjudicatario | Plantear supuestos y preguntas PADF | CTO |
| BLK-002 | Costos Azure no dimensionables aun | Faltan usuarios, ambientes, datos, region, HA | Enviar preguntas PADF | Arquitecto Azure |
| BLK-003 | Oferta legal incompleta | Faltan documentos societarios y facultades | Solicitar documentos internos | Responsable legal |

## Acciones de cierre diario

- Actualizar tareas.
- Actualizar riesgos.
- Registrar decisiones.
- Verificar documentos faltantes.
- Generar checklist actualizado.

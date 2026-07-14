# WIN STRATEGY

## Proposito

Documento interno para Justech. No forma parte de la entrega a PADF/INCABIDE.

Objetivo: definir el plan para obtener el mayor puntaje posible segun los criterios de evaluacion de la RFP, sin inventar experiencia, certificaciones, clientes, metricas ni resultados.

## Reglas

- No afirmar puntajes esperados.
- No inventar evidencia.
- No usar como anexo externo.
- Todo puntaje objetivo es una aspiracion interna de preparacion, no una prediccion de resultado.

## Estrategia por criterio de evaluacion

| Criterio | Puntaje maximo RFP | Evidencia | Documentos | Diagramas | Riesgos | Validaciones finales |
| --- | ---: | --- | --- | --- | --- | --- |
| Comprension del proyecto y calidad de la propuesta tecnica | 30 | Matriz de cumplimiento, ciclo de vida del bien, arquitectura, Azure, seguridad, QA, riesgos, entregables, supuestos/exclusiones | `MASTER_TECHNICAL_PROPOSAL_OUTLINE.md`, `MASTER_COMPLIANCE_MATRIX.md`, `SOLUTION_BLUEPRINT/`, `SOLUTION_STORY/`, `AZURE_ENTERPRISE/`, `UX_MASTER/`, `QUALITY_NON_CONFORMITY_CRITERIA.md` | Ciclo de vida del bien; arquitectura logica; arquitectura Azure; seguridad; QA; flujo Etapa I/II | Redaccion generica; no separar Etapa I/II; mezclar API con PGR; seguridad superficial; Azure sin decisiones pendientes claras | Confirmar trazabilidad de cada requisito; revisar que capitulos 3-28 y 31-35 cubren RFP; validar supuestos/exclusiones; QA editorial |
| Costo y relacion valor-precio | 30 | Estructura modular, desglose futuro por Etapa I, modulos, funciones transversales, Azure y PGR opcional | `COST_REQUIREMENTS_MAP.md`, `AZURE_COST_ASSUMPTIONS.md`, `18_ASSUMPTIONS.md`, `19_EXCLUSIONS.md`, Anexo 3 futuro | No aplica en propuesta tecnica salvo tabla de modularidad; visual economico se reserva para oferta economica | Costos no comparables; infraestructura sin variables; soporte critico ambiguo; funciones transversales duplicadas | No incluir precios en tecnica; asegurar que supuestos de alcance habiliten oferta economica clara; validar PGR opcional |
| Capacidad y experiencia del equipo propuesto | 20 | CVs, PMP, experiencia Python/Django, DevOps/Seguridad, Azure, QA, UX, dedicacion, organigrama, RACI | `MISSING_JUSTECH_INFORMATION.md`, `TEAM_REQUIREMENTS_GAP_ANALYSIS.md`, capitulo 29 futuro | Organigrama; modelo de gobierno; matriz RACI | No contar con PMP; certificaciones no verificadas; dedicacion poco clara; roles obligatorios incompletos | Validar CVs, certificados, dedicacion, roles minimos y suplentes; no incluir personas no confirmadas |
| Experiencia institucional relevante y exitosa | 20 | Minimo 3 referencias comparables con descripcion, rol, periodo y resultados verificables | `MISSING_JUSTECH_INFORMATION.md`, capitulo 30 futuro, Archivo No. 4 futuro | Tabla comparativa de referencias; mapa de similitud proyecto-RFP | Referencias no comparables; resultados no verificables; falta autorizacion; experiencia no relacionada | Validar autorizacion de uso; confirmar contactos; verificar resultados; priorizar proyectos web/cloud/seguridad/datos sensibles |

## Umbral tecnico

La RFP exige minimo 49 puntos sobre 70 tecnicos para pasar a evaluacion economica. Los criterios tecnicos son:

- Comprension/calidad tecnica: 30.
- Capacidad/equipo: 20.
- Experiencia institucional: 20.

## Plan de maximizacion tecnica

| Prioridad | Accion | Evidencia esperada | Responsable | Estado |
| --- | --- | --- | --- | --- |
| 1 | Aprobar estructura editorial por partes | `MASTER_TECHNICAL_PROPOSAL_OUTLINE.md` aprobado | Fausto / Bid Manager / CTO | Pendiente |
| 2 | Completar informacion Justech | `MISSING_JUSTECH_INFORMATION.md` resuelto | Justech | Pendiente |
| 3 | Confirmar equipo minimo obligatorio | CVs y roles | PMO / CTO | Pendiente |
| 4 | Confirmar PMP | Certificado PMP | PMO | Pendiente |
| 5 | Confirmar referencias comparables | 3 fichas verificables | Comercial / Bid | Pendiente |
| 6 | Confirmar certificaciones reales | Certificados o no incluir | CTO / PMO | Pendiente |
| 7 | Resolver preguntas PADF criticas | Respuestas o supuestos aprobados | Bid / CTO | Pendiente |
| 8 | Seleccionar diagramas y tablas futuras | Lista de visuales por capitulo | Bid / Arquitectos / UX | Pendiente |
| 9 | Validar supuestos/exclusiones | Aprobacion Legal/Comercial/CTO | Justech | Pendiente |
| 10 | Ejecutar simulacion de comite | `COMMITTEE_REVIEW_SIMULATION.md` revisado | Bid / QA / CTO | Pendiente |

## Evidencias que mas aumentan credibilidad

| Evidencia | Impacto |
| --- | --- |
| Matriz requisito -> capitulo -> evidencia | Demuestra control total del RFP. |
| CVs y PMP | Protege elegibilidad y puntaje de equipo. |
| Referencias comparables | Protege experiencia institucional. |
| Arquitectura Azure Enterprise | Eleva calidad tecnica. |
| Matriz control seguridad -> evidencia | Reduce riesgo por penalidades de seguridad. |
| Hito -> entregable -> criterio de aceptacion | Muestra gestion contractual madura. |
| UX Master / ciclo de vida del bien | Diferencia la propuesta de una respuesta tecnica generica. |

## Debilidades actuales

1. Falta informacion corporativa Justech.
2. Falta confirmar equipo nominal y dedicacion.
3. Falta PMP verificable.
4. Falta confirmar certificaciones Microsoft.
5. Falta confirmar referencias comparables.
6. Falta respuesta PADF a preguntas criticas.
7. Falta decision de supuestos/exclusiones.
8. Falta definir que visuales iran en propuesta final.

## Acciones prohibidas

- No inflar experiencia.
- No listar certificaciones no verificadas.
- No presentar clientes sin autorizacion.
- No prometer integracion PGR como entregable con fecha fija.
- No comprometer migracion historica sin alcance.
- No ocultar dependencias criticas.
- No redactar oferta economica dentro de la tecnica.

## Condicion para pasar a redaccion

No iniciar redaccion final hasta que Fausto apruebe:

1. estructura por partes;
2. nivel de extension;
3. informacion Justech minima disponible;
4. posicion sobre supuestos/exclusiones;
5. tratamiento de referencias, CVs y certificaciones;
6. visuales obligatorios por capitulo.

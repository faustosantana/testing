# MATRIZ MAESTRA DE CUMPLIMIENTO — RFP 5801 DRC3P

Estado: base de cumplimiento para construccion posterior de la propuesta.  
Regla: cada respuesta debe basarse en evidencia del PDF y no en supuestos.

## Resumen de cobertura

| Dominio | Documento de detalle | Requisitos trazables |
| --- | --- | ---: |
| Administrativos, documentales, legales, comerciales, garantias, penalidades, equipo y evaluacion | `RFP_REQUIREMENTS_ADMIN_LEGAL_COMMERCIAL.md` | 107 |
| Tecnicos, Azure, infraestructura, seguridad, QA, soporte y capacitacion | `RFP_REQUIREMENTS_TECH_AZURE_SECURITY_QA.md` | 120 |
| Modulos funcionales y funciones transversales | `RFP_REQUIREMENTS_FUNCTIONAL_MODULES.md` | 201 |
| **Total** |  | **428** |

## Criterios de cumplimiento

| Estado | Definicion |
| --- | --- |
| Cumple | Existe respuesta, evidencia o compromiso verificable para el requisito. |
| Cumple con aclaracion | El requisito puede cumplirse, pero requiere pregunta, decision o validacion PADF/INCABIDE. |
| Riesgo | El requisito tiene incertidumbre que afecta costo, plazo, alcance, aceptacion o penalidad. |
| Brecha | Falta informacion, evidencia interna o capacidad documentada para responder. |
| No iniciado | Aun no se ha preparado respuesta de propuesta. |

## Matriz de cumplimiento por bloque

| ID matriz | Bloque | Rango de requisitos | Estado actual | Accion inmediata | Evidencia |
| --- | --- | --- | --- | --- | --- |
| MCM-001 | Administracion del proceso | ADM-001 a ADM-017 | Cumple con aclaracion | Preparar checklist de envio y comunicaciones oficiales. | RFP p.1-p.13 |
| MCM-002 | Documentos de oferta | DOC-001 a DOC-013 | No iniciado | Crear carpeta de armado de archivos 1 a 5. | RFP 3.4.1, Anexos 2 y 3 |
| MCM-003 | Legal contractual | LEG-001 a LEG-019 | Riesgo | Solicitar certificados, poderes, identificaciones y declaracion de intereses. | RFP 3.4.1, 4.x, 5, 6, 7 |
| MCM-004 | Costos y pagos | COST-001 a COST-018 | Riesgo | Preparar modelo economico por Etapa I, modulos y Azure. | RFP 2.3, 4.1, Anexo 3 |
| MCM-005 | Garantias y penalidades | GAR-001 a GAR-005; PEN-001 a PEN-021 | Riesgo critico | Validar capacidad de garantias y margen por penalidades. | RFP 4.9, 11 |
| MCM-006 | Experiencia y equipo | EXP-001 a EXP-003; TEAM-001 a TEAM-005 | Brecha por validar | Confirmar perfiles, PMP, CVs y certificaciones reales. | RFP 3.4.1, 7 |
| MCM-007 | Evaluacion | EVAL-001 a EVAL-006 | No iniciado | Construir estrategia de puntaje tecnico y valor-precio. | RFP 8 |
| MCM-008 | Tecnico Etapa I | TEC-001 a TEC-026 | Riesgo | Preparar plan de diagnostico sin acceso previo a codigo. | RFP 2.2, Anexo 2 |
| MCM-009 | Azure e infraestructura | AZ-001 a AZ-015 | Riesgo critico | Definir preguntas sobre region, tenant, ambientes, HA, RTO/RPO y costos. | RFP 4.10, Anexo 2, Anexo 3 |
| MCM-010 | Seguridad | SEC-001 a SEC-038 | Riesgo critico | Mapear controles Azure y evidencias exigidas sin disenar arquitectura aun. | RFP 4.8, 4.10, Anexo 2 4.1/4.3 |
| MCM-011 | QA, aceptacion y cierre | QA-001 a QA-029 | Riesgo | Preparar modelo de aceptacion por hito/modulo. | Anexo 2 3.1, 5.3, 7 |
| MCM-012 | Soporte y capacitacion | SUP-001 a SUP-008; CAP-001 a CAP-004 | Riesgo | Aclarar alcance de soporte critico y preparar plan de transferencia. | Anexo 2 4.2, H6, H9 |
| MCM-013 | Requisitos funcionales generales | FUNC-GEN-001 a FUNC-GEN-010 | No iniciado | Definir backlog modular y criterios de validacion. | Anexo 2 5, 5.3 |
| MCM-014 | Registro e Ingreso de Activos | FUNC-001 a FUNC-021 | No iniciado | Crear epic de modulo y preguntas sobre catalogos oficiales. | Anexo 5.1 |
| MCM-015 | Gestion de Contratos y Clientes | FUNC-022 a FUNC-061 | No iniciado | Crear epic de modulo y preguntas sobre integraciones financieras. | Anexo 5.2 |
| MCM-016 | Subasta / Ventas | FUNC-062 a FUNC-083 | Riesgo | Aclarar sistema de subasta existente e integracion. | Anexo 5.3 |
| MCM-017 | Descargo / Donaciones | FUNC-084 a FUNC-115 | No iniciado | Crear epic de modulo y dependencias legales/ambientales. | Anexo 5.4 |
| MCM-018 | Multilenguaje | FUNC-116 a FUNC-129 | No iniciado | Preparar estrategia i18n posterior. | Anexo 5.5 |
| MCM-019 | Seguridad avanzada funcional | FUNC-130 a FUNC-150 | Riesgo | Separar seguridad obligatoria Etapa I vs modulo Etapa II. | Anexo 5.6 |
| MCM-020 | Funciones transversales | FUNC-151 a FUNC-191 | Riesgo | Aclarar alcance, cotizacion y aceptacion de transversales. | Anexo 5.7 |

## Respuesta inicial de cumplimiento

| Tipo | Respuesta base |
| --- | --- |
| Obligatorio claro | Debe responderse con compromiso explicito y evidencia en propuesta. |
| Condicional | Debe responderse indicando condicion del RFP y supuestos validados. |
| Muy valorado | Debe maximizarse si Justech posee evidencia real. No inventar. |
| Ambiguo | Debe convertirse en pregunta PADF antes de cerrar alcance/costos. |

## Bloqueos principales antes de redactar propuesta

1. No existe acceso al codigo fuente antes de adjudicacion.
2. No esta definido el alcance minimo de la API obligatoria.
3. No estan definidos usuarios, concurrencia, ambientes, datos ni volumen multimedia.
4. No esta definida la region Azure ni el modelo tenant/suscripcion.
5. No esta definida la frontera entre seguridad Etapa I y modulo Seguridad Avanzada Etapa II.
6. No esta definido si funciones transversales se cotizan como paquete, por modulo o ambos.
7. No esta definido el alcance del soporte critico fuera de horario respecto a las 30 horas anuales.

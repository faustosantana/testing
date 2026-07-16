# ESTRATEGIA DE EVALUACION Y PLAN PARA GANAR

Fuente: Seccion Octava del RFP No. 5801 DRC3P.  
Estado: estrategia de preparacion. No es propuesta tecnica.

## Modelo de puntuacion

| Criterio | Puntaje maximo | Evidencia PDF | Implicacion estrategica |
| --- | ---: | --- | --- |
| Comprension del proyecto y calidad de la propuesta tecnica | 30 | p.9, L351-L354 | Mayor diferenciador tecnico. Debe ser trazable, metodologico y factible. |
| Costo y relacion valor-precio | 30 | p.9, L355-L356 | Debe ser transparente, modular y alineado al Anexo 3. |
| Capacidad y experiencia del equipo propuesto | 20 | p.9, L357-L358 | Requiere perfiles obligatorios, dedicacion y certificaciones reales. |
| Experiencia institucional relevante y exitosa | 20 | p.9, L359-L362 | Requiere minimo 3 referencias verificables y resultados. |
| **Total** | **100** | p.9, L363 |  |

## Umbral tecnico

La propuesta debe alcanzar minimo **49 puntos sobre 70 tecnicos** para pasar a evaluacion de costo. Los 70 puntos tecnicos corresponden a:

- Calidad tecnica: 30.
- Equipo: 20.
- Experiencia institucional: 20.

Evidencia: p.9, L364-L367.

## Prioridad de trabajo por puntaje

| Prioridad | Frente | Por que importa | Acciones necesarias |
| --- | --- | --- | --- |
| 1 | Matriz de cumplimiento completa | Demuestra comprension y reduce riesgo de omisiones. | Usar `MASTER_COMPLIANCE_MATRIX.md` como columna vertebral. |
| 2 | Respuesta tecnica por etapas/hitos | El RFP pide Etapa I y Etapa II con alcance, actividades, entregables y cronograma. | Preparar estructura sin redactar aun solucion final. |
| 3 | Seguridad y Azure | Es obligatorio y tiene penalidades fuertes. | Responder todos los controles 4.1 y evidencias 4.3. |
| 4 | Equipo y certificaciones | 20 puntos y requisitos minimos. | Confirmar PMP, Python/Django, DevOps/Seguridad y certificaciones Microsoft reales. |
| 5 | Experiencia verificable | 20 puntos y minimo 3 referencias. | Seleccionar referencias comparables reales con resultados. |
| 6 | Valor-precio | 30 puntos; PADF puede contratar por modulo. | Separar costos por Etapa I, modulos, transversales, Azure y PGR opcional. |

## Como maximizar calidad tecnica (30 puntos)

1. Responder con la misma estructura del RFP: Etapa I, Hitos 1-9, Etapa II por modulos.
2. Incluir matriz de trazabilidad requisito -> respuesta -> entregable -> evidencia -> criterio de aceptacion.
3. Presentar un enfoque de diagnostico inicial porque el codigo se entrega "tal cual".
4. Separar claramente lo obligatorio de lo condicionado a aprobaciones externas.
5. Mostrar control de seguridad desde el inicio: MFA, WAF, DDoS, backups, vault, monitoreo, pentest.
6. Usar lenguaje de aceptacion del RFP: aprobacion escrita, UAT, actas parciales, evidencias.
7. Identificar dependencias sin trasladar indebidamente responsabilidad al cliente.

## Como maximizar valor-precio (30 puntos)

1. Usar exactamente el formato del Anexo 3.
2. Mostrar desglose por cada hito Etapa I.
3. Mostrar desglose por cada modulo Etapa II.
4. Separar funciones transversales si PADF aclara que son item independiente.
5. Cotizar PGR como item opcional separado.
6. Incluir infraestructura Azure mensual y anual.
7. Incluir soporte por 1 ano, pentest, documentacion, capacitacion y transferencia de accesos.
8. Evitar costos ocultos o paquetes no comparables.

## Como maximizar equipo (20 puntos)

| Perfil | Estado requerido | Accion |
| --- | --- | --- |
| Lider de Proyecto PMP | Obligatorio | Confirmar certificado PMP vigente y CV. |
| Backend Senior Python/Django | Obligatorio | Confirmar 3+ anos y evidencia. |
| DevOps/Seguridad | Obligatorio | Confirmar nube segura, VPN y firewalls. |
| Arquitecto Azure | Diferenciador | Adjuntar certificaciones reales si existen. |
| QA Manager | Diferenciador | Mostrar metodologia QA y UAT. |
| UX/UI Lead | Diferenciador | Relevante por mockups navegables Etapa II. |
| Consultor Gobierno Digital | Diferenciador | Relevante por INCABIDE, activos y sector publico. |

## Como maximizar experiencia institucional (20 puntos)

No inventar experiencia. Seleccionar solo referencias verificables que puedan demostrar:

- Aplicaciones web o plataformas institucionales.
- Python/Django o tecnologia comparable.
- Despliegues cloud.
- Seguridad y datos sensibles.
- Resultados medibles.
- Periodo de ejecucion y rol asumido.
- Contacto o evidencia documental disponible.

## Oportunidades de diferenciacion

| Oportunidad | Relacion con RFP | Como aprovecharla despues |
| --- | --- | --- |
| Matriz de cumplimiento exhaustiva | Evalua comprension y calidad. | Adjuntar como anexo de propuesta. |
| Plan de aceptacion por evidencia | RFP exige aprobacion escrita y evidencias. | Reducir riesgo de rechazos y penalidades. |
| DevSecOps documentado | Seguridad tiene multas y rescission. | Mostrar controles, escaneos y pentest. |
| Azure con enfoque de gobierno | Azure es obligatorio y muy valorado. | Usar certificaciones/designaciones reales. |
| Mockups navegables antes de desarrollo | Exigido para Etapa II. | Presentar metodologia UX sin disenar aun. |
| Modularidad economica | PADF puede contratar parcial. | Ofrecer claridad por modulo y paquete. |
| Transferencia real de conocimiento | Hito 6 exige autonomia INCABIDE. | Preparar plan de capacitacion medible. |

## Decision de concentracion

Para ganar, el esfuerzo debe concentrarse en:

1. Superar con margen el umbral tecnico de 49/70.
2. Demostrar dominio del riesgo del codigo fuente no disponible.
3. Cubrir seguridad/Azure con trazabilidad absoluta.
4. Presentar equipo y referencias verificables.
5. Evitar ambiguedades economicas.
6. Convertir preguntas PADF en control de alcance antes de precio final.

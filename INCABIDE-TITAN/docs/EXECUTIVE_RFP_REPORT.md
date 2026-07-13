# REPORTE EJECUTIVO — ENTENDIMIENTO RFP 5801 DRC3P

Proyecto: INCABIDE TITAN  
Cliente: PADF / INCABIDE  
Estado: fase de entendimiento completa. No se ha redactado propuesta tecnica ni economica.

## Metricas principales

| Indicador | Cantidad |
| --- | ---: |
| Requisitos trazables identificados | 428 |
| Entregables identificados | 58 |
| Riesgos, brechas, ambiguedades e inconsistencias | 31 |
| Preguntas preparadas para PADF | 75 |
| Modulos / bloques funcionales | 11 |
| Criterios de evaluacion | 4 |
| Puntaje total | 100 |
| Puntaje tecnico minimo para pasar a costo | 49 / 70 |

## Modulos y bloques funcionales

1. Registro e Ingreso de Activos.
2. Gestion de Contratos y Clientes.
3. Modulo de Subasta / Ventas.
4. Descargo de Activos / Donaciones.
5. Soporte Multilenguaje Espanol/Ingles.
6. Seguridad y Control de Acceso Avanzado.
7. Documentacion Multimedia.
8. Geolocalizacion de Activos.
9. Control y Auditoria del Personal.
10. Importacion y Exportacion Masiva de Datos.
11. Reportes y Analisis para Toma de Decisiones.

## Brechas detectadas

| Brecha | Impacto |
| --- | --- |
| Codigo fuente no disponible antes de adjudicacion. | Riesgo de precio fijo, alcance y cronograma. |
| No hay inventario tecnico del SGB actual. | Riesgo en diagnostico, dependencias y refactorizacion. |
| API obligatoria sin alcance minimo definido. | Riesgo tecnico y economico. |
| Azure obligatorio sin region, tenant, ambientes, usuarios ni dimensionamiento. | Riesgo de costo y cumplimiento. |
| Seguridad Etapa I se solapa con modulo Seguridad Avanzada Etapa II. | Riesgo de doble conteo o alcance ambiguo. |
| Soporte critico fuera de horario no queda limitado por 30 horas anuales. | Riesgo operativo y economico. |
| Interconexion con PGR es opcional, pero la API base es obligatoria. | Riesgo de confusion en oferta. |
| Subasta aparece como modulo incompleto y tambien como sistema existente a integrar. | Riesgo de alcance. |
| No hay volumen de datos, adjuntos, usuarios ni concurrencia. | Riesgo de Azure, costos y performance. |
| No hay criterios de aceptacion para GIS, multimedia, import/export ni analisis predictivo. | Riesgo de UAT y alcance. |
| Falta confirmar equipo, PMP, certificaciones Microsoft y referencias reales de Justech. | Riesgo de elegibilidad y puntaje. |
| Falta confirmar capacidad de garantias contractuales. | Riesgo comercial/legal. |

## Riesgos criticos

1. Precio fijo con codigo fuente entregado solo al adjudicatario.
2. Penalidades acumulables hasta 20% y rescision desde 15%.
3. Rescision inmediata por brecha de seguridad, confidencialidad o subcontratacion no autorizada.
4. Hito 4 en semana 8 con produccion, TLS, API, seguridad y modulos originales operables.
5. Infraestructura Azure por un ano incluida sin dimensionamiento.
6. Pentest tercero incluido dentro de 30 dias post-produccion.
7. Garantias: 10% fiel cumplimiento y 100% de anticipo.

## Decisiones que debemos tomar

| Decision | Responsable sugerido | Momento |
| --- | --- | --- |
| Aprobar preguntas PADF a enviar. | Bid Manager / CTO | Inmediato |
| Confirmar equipo minimo y PMP. | PMO | Inmediato |
| Confirmar certificaciones Microsoft reales. | CTO | Inmediato |
| Seleccionar referencias comparables reales. | Bid Manager / Comercial | Inmediato |
| Definir estrategia: paquete completo, por modulo o ambos. | Direccion / CFO | Antes de oferta economica |
| Definir postura sobre riesgos de precio fijo sin codigo. | CTO / Legal / CFO | Antes de propuesta |
| Definir si se incluira descuento por paquete completo. | CFO / Direccion | Antes de oferta economica |
| Definir estructura de equipo ampliado para maximizar puntaje. | CTO / PMO | Antes de oferta tecnica |
| Definir respuesta a garantias y flujo de caja. | CFO / Legal | Antes de oferta economica |

## Oportunidades para diferenciarnos

1. Presentar matriz de cumplimiento exhaustiva como anexo.
2. Convertir cada hito en entregables verificables con evidencia.
3. Usar un enfoque DevSecOps fuerte por las penalidades de seguridad.
4. Mostrar dominio de Azure y gobierno de datos transfronterizos.
5. Presentar modularidad economica clara para que PADF pueda contratar parcial o completo.
6. Usar UX/mockups navegables como mecanismo de reduccion de riesgo en Etapa II.
7. Proponer transferencia de conocimiento medible hacia autonomia INCABIDE.
8. Separar correctamente API base, PGR opcional y sistema de subastas existente.
9. Reforzar QA/UAT para evitar rechazos de entregables y penalidades.
10. Demostrar experiencia institucional solo con evidencia verificable.

## Plan recomendado para ganar

### Paso 1 — Cerrar preguntas criticas

Enviar preguntas PADF enfocadas en alcance, Azure, API, datos, ambientes, soporte, integraciones, aceptacion y costos. No avanzar a precio final sin estas respuestas o sin supuestos aprobados internamente.

### Paso 2 — Asegurar elegibilidad y puntaje de equipo

Confirmar PMP, Backend Python/Django, DevOps/Seguridad, CVs, dedicacion, certificaciones Microsoft reales y tres referencias comparables.

### Paso 3 — Construir propuesta sobre trazabilidad

Usar la matriz de 428 requisitos como base de la propuesta. Cada seccion debe responder al requisito, indicar entregable, evidencia y criterio de aceptacion.

### Paso 4 — Enfatizar seguridad y Azure

El RFP penaliza fuertemente seguridad. La propuesta debe demostrar control de MFA, WAF, DDoS, secretos, cifrado, monitoreo, backups, DRP, pentest y vulnerabilidades.

### Paso 5 — Modularizar valor-precio

Presentar Etapa I, cada modulo de Etapa II, funciones transversales, infraestructura Azure y PGR opcional con separacion transparente. Esto aumenta comparabilidad y reduce friccion de adjudicacion parcial.

### Paso 6 — Preparar presentacion ejecutiva opcional

PADF puede solicitar presentacion de maximo 2 horas con 48 horas de aviso. Prepararla solo despues de tener narrativa tecnica y economica aprobada.

## Estado final de esta fase

La licitacion fue convertida en un proyecto ejecutable de preparacion:

- Requisitos extraidos.
- Backlog creado.
- Matriz maestra creada.
- Riesgos y brechas registrados.
- Preguntas PADF preparadas.
- Azure analizado como requisitos y decisiones, sin arquitectura.
- Equipo y certificaciones analizados sin inventar.
- Entregables y documentos base mapeados.

Siguiente accion recomendada: **revisar y aprobar las preguntas PADF antes de redactar la propuesta tecnica o economica**.

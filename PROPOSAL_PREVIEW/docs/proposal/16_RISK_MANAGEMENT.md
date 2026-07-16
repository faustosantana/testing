# 16 — RISK MANAGEMENT

## Enfoque de gestion de riesgos

La RFP contiene riesgos tecnicos, contractuales, operativos y de seguridad que deben gestionarse de forma explicita. La propuesta tecnica debe demostrar que Justech no subestima la complejidad del proyecto y que cada riesgo relevante tiene un mecanismo de mitigacion.

## Riesgos principales y mitigacion

| Riesgo | Impacto | Mitigacion tecnica |
| --- | --- | --- |
| Codigo fuente recibido en estado desconocido | Puede afectar esfuerzo, plazo y compatibilidad | Diagnostico inicial, inventario, informe de compatibilidad y prueba de ejecucion. |
| Sistema no preparado para nube | Puede afectar despliegue Azure | Refactorizacion cloud-ready, variables de entorno, almacenamiento cloud, contenedores. |
| API sin alcance minimo definido | Puede generar sobrealcance | Separar API base obligatoria de integracion PGR opcional; validar endpoints. |
| Subasta existente sin especificacion | Puede afectar integracion | Solicitar documentacion del sistema de subastas y delimitar responsabilidades. |
| Seguridad con penalidades severas | Puede habilitar rescision o multas | Controles RFP, escaneos, pentest, WAF, MFA, cifrado, vault y auditoria. |
| Soporte critico fuera de horario ambiguo | Puede afectar operacion y costo | Aclarar alcance, canales, escalamiento y cobertura. |
| Azure sin dimensionamiento | Puede afectar costo y desempeño | Definir variables de usuarios, datos, ambientes, HA, RTO/RPO y multimedia. |
| Datos/migracion no definidos | Puede generar expectativas no controladas | Estrategia de migracion condicionada y supuestos explicitos. |

## Riesgos contractuales

La RFP establece penalidades por atraso, incumplimiento de SLA, entregables incompletos, brecha de seguridad, abandono, subcontratacion no autorizada y violacion de confidencialidad o propiedad intelectual. La mitigacion debe basarse en control de alcance, evidencia por hito, QA estricto, seguridad desde el diseno y gestion documental.

## Control de riesgos durante ejecucion

El proyecto debe mantener:

- registro de riesgos;
- responsable por riesgo;
- probabilidad e impacto;
- plan de mitigacion;
- estado;
- decisiones asociadas;
- escalamiento.

## Trazabilidad RFP

Este capitulo cubre PEN-001 a PEN-021, AZ-001 a AZ-015, SEC-001 a SEC-038, SUP-001 a SUP-008 y QA-001 a QA-029.

## Informacion pendiente de Justech

Justech debe confirmar:

- politica interna de riesgos;
- cobertura operativa;
- capacidad de garantias si aplica;
- proceso de escalamiento;
- politicas de continuidad y seguridad;
- postura sobre subcontratacion, si aplica.

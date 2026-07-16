# REGISTRO DE RIESGOS, BRECHAS, AMBIGUEDADES E INCONSISTENCIAS

Fuente: RFP No. 5801 DRC3P.  
Estado: insumo para preguntas PADF, estrategia de propuesta y control de alcance.

## Riesgos criticos y altos

| ID | Tipo | Riesgo / brecha | Prob. | Impacto | Evidencia PDF | Mitigacion requerida |
| --- | --- | --- | --- | --- | --- | --- |
| RGA-001 | Riesgo critico | Precio fijo con incertidumbre tecnica alta porque el codigo fuente se entrega solo al adjudicatario. | Alta | Critico | p.7, L243-L248; p.3, L77-L85 | Preguntar por documentacion tecnica y establecer supuestos de diagnostico. |
| RGA-002 | Riesgo critico | SGB se entrega "tal cual", no cloud-ready y con modulos potencialmente incompletos. | Alta | Critico | p.3, L77-L85 | Incluir fase fuerte de diagnostico y matriz de hallazgos. |
| RGA-003 | Riesgo critico | Hito 1 concentra 50% de Etapa I y exige diagnostico, dependencias y codigo refactorizado. | Media | Alto | p.16, L764-L773; p.17, L847-L870 | Validar alcance y criterios de aceptacion. |
| RGA-004 | Riesgo critico | Hito 4 semana 8 exige produccion, TLS, API, modulos originales operables y evidencias completas de seguridad. | Alta | Critico | p.17, L918-L946 | Aclarar alcance API, seguridad y dependencias externas. |
| RGA-005 | Riesgo critico | API funcional obligatoria sin definicion de endpoints, autenticacion, volumen o criterios funcionales. | Alta | Critico | p.16, L753-L759; p.17, L928-L943 | Pregunta PADF sobre alcance minimo API. |
| RGA-006 | Riesgo critico | Interconexion PGR opcional/separada, pero API obligatoria puede confundirse con integracion. | Alta | Alto | p.16, L753-L759; p.26, L1520-L1523 | Separar API base vs PGR. |
| RGA-007 | Riesgo critico | Seguridad Etapa I ya exige controles avanzados, mientras Etapa II incluye modulo Seguridad Avanzada. | Alta | Alto | p.19, L1060-L1084; p.21, L1247-L1264 | Preguntar frontera de alcance. |
| RGA-008 | Riesgo critico | Infraestructura Azure por 1 ano incluida representa solo 2% de pago Etapa I. | Media | Alto | p.16, L810-L816; p.18, L995-L1010 | Dimensionar cuidadosamente y preguntar ambientes. |
| RGA-009 | Riesgo critico | Soporte critico fuera de horario no queda limitado por las 30 horas anuales estimadas. | Alta | Alto | p.19, L1097-L1102 | Preguntar limite y modelo de cobertura. |
| RGA-010 | Riesgo critico | Pentest tercero incluido dentro de 30 dias post-produccion puede afectar costo y cierre. | Media | Alto | p.20, L1125-L1128 | Incluir en estimacion y validar proveedor aceptable. |
| RGA-011 | Riesgo critico | Penalidades acumulables hasta 20%, rescision desde 15% y rescision inmediata por seguridad/confidencialidad. | Media | Critico | p.10-p.12, L386-L627 | QA, DevSecOps y control contractual. |
| RGA-012 | Brecha | No hay inventario tecnico del SGB, modulos, dependencias ni defectos conocidos. | Alta | Alto | p.3, L77-L85 | Solicitar documentacion y lista de defectos. |
| RGA-013 | Brecha | No se especifica volumen de datos, archivos, usuarios ni concurrencia. | Alta | Alto | Ausente; funciones p.28-p.31 | Preguntas PADF. |
| RGA-014 | Brecha | No se especifica si existe migracion de datos ni volumen historico. | Alta | Alto | Ausente; import/export p.31, L1735-L1739 | Preguntas PADF. |
| RGA-015 | Brecha | No se definen ambientes requeridos: desarrollo, QA/UAT, staging, produccion. | Alta | Alto | Ausente; Anexo 2 menciona prueba/produccion | Preguntas PADF. |
| RGA-016 | Brecha | No se define region Azure preferida ni responsable de aprobacion legal de transferencia internacional. | Alta | Alto | p.7, L265-L270 | Preguntas PADF. |
| RGA-017 | Brecha | No se definen RTO, RPO, retencion de backups ni disponibilidad esperada. | Alta | Alto | p.19, L1083-L1084 | Preguntas PADF. |
| RGA-018 | Brecha | No se define responsable de DNS/dominio ni acceso a sgb.incabide.gob.do. | Media | Medio | p.16, L751-L752 | Preguntas PADF. |
| RGA-019 | Brecha | No se define proveedor de mapas, licencias GIS o precision requerida. | Media | Alto | p.15, L717; p.30, L1721-L1724 | Preguntas PADF. |
| RGA-020 | Brecha | Analisis predictivo y pronostico no tiene criterios de aceptacion ni datos historicos definidos. | Media | Alto | p.31, L1740-L1744 | Preguntas PADF. |
| RGA-021 | Brecha | No se define alcance de sistema de subastas existente ni su especificacion de integracion. | Alta | Alto | p.20, L1184-L1188; p.29, L1640-L1642 | Preguntas PADF. |
| RGA-022 | Brecha | No se define si funciones transversales se cotizan como modulo, por cada modulo o ambas. | Media | Alto | p.21, L1279-L1281; p.26, L1511-L1518 | Preguntas PADF. |
| RGA-023 | Brecha interna | Falta confirmar PMP, CVs, certificaciones Microsoft y referencias reales Justech. | Media | Alto | p.4, L140-L143; p.8-p.9, L316-L347 | Solicitud interna inmediata. |
| RGA-024 | Brecha interna | Falta validar capacidad financiera para garantias bancarias/aseguradoras. | Media | Critico | p.7, L249-L258 | Revision financiera/legal. |

## Inconsistencias documentales detectadas

| ID | Inconsistencia | Impacto | Evidencia PDF | Accion |
| --- | --- | --- | --- | --- |
| INC-001 | Portada indica fecha de emision 13 de julio de 2026; calendario indica publicacion 16 de julio de 2026. | Puede afectar computo y narrativa de plazos. | p.1, L8; p.3, L101-L104 | Preguntar/registrar aclaracion. |
| INC-002 | Numeracion 4.9 se usa para Garantias y luego para Cohecho privado despues de 4.10. | Riesgo de referencia contractual. | p.7, L249-L275 | Referenciar por titulo y no solo numero. |
| INC-003 | RFP usa "VPC" aunque Azure utiliza "VNet". | Riesgo de interpretacion tecnica. | p.18, L1060-L1065 | Traducir a servicio Azure equivalente posteriormente. |
| INC-004 | Descripcion de Dockerfile agrupa BD/interfaz/codigo, pero tecnicamente Dockerfile y Compose tienen responsabilidades distintas. | Riesgo de confusion en entregables. | p.15, L733-L737 | Aclarar en propuesta sin contradecir RFP. |
| INC-005 | Etapa I prohibe nuevas funcionalidades, pero exige API funcional obligatoria. | Riesgo de alcance. | p.3, L87-L90; p.16, L753-L755 | Pregunta PADF. |
| INC-006 | Subasta aparece como modulo potencialmente incompleto y tambien como sistema existente a integrar. | Riesgo de alcance y costo. | p.3, L81-L82; p.20, L1184-L1188 | Pregunta PADF. |
| INC-007 | Seguridad obligatoria Etapa I se solapa con modulo Seguridad avanzada Etapa II. | Riesgo de doble conteo o alcance duplicado. | p.19, L1060-L1084; p.21, L1247-L1264 | Pregunta PADF. |

## Informacion faltante critica

1. Documentacion tecnica actual del SGB.
2. Inventario de modulos actuales y estado real.
3. Lista de defectos conocidos.
4. Dependencias, versiones, librerias y servicios externos.
5. Volumen de base de datos y archivos.
6. Usuarios, roles actuales y concurrencia.
7. Ambientes requeridos.
8. Region Azure y tenant/suscripcion.
9. RTO, RPO, disponibilidad y retencion.
10. Politica de datos, logs, backups y residencia.
11. Alcance minimo de API.
12. Especificacion tecnica del sistema de subastas.
13. Alcance de PGR y mecanismo de aprobacion.
14. Catalogos oficiales dominicanos.
15. Proveedor/licencia de mapas.
16. Criterios de aceptacion para analisis predictivo.
17. Aprobadores UAT por modulo.
18. Limite real de soporte critico fuera de horario.
19. Proveedor aceptable de pentest.
20. Licencias prohibidas o SBOM requerido.

# BACKLOG PROFESIONAL — RFP 5801 DRC3P

Este backlog convierte la RFP en trabajo ejecutable para preparar la propuesta. No es plan de ejecucion contractual ni propuesta tecnica.

## Estados

`Pendiente` | `En analisis` | `Bloqueado` | `Listo para propuesta` | `Validado`

## Epicas

| Epic ID | Epic | Objetivo | Fuente RFP | Estado |
| --- | --- | --- | --- | --- |
| EPIC-ADM | Administracion de licitacion | Cumplir instrucciones de presentacion, comunicaciones y plazos. | Secciones 1, 3, 9, 10, Anexo 1/4 | En analisis |
| EPIC-LEGAL | Legal y cumplimiento contractual | Preparar antecedentes, declaraciones, garantias y condiciones contractuales. | Secciones 4, 5, 6, 7, 11 | En analisis |
| EPIC-EVAL | Estrategia de evaluacion | Maximizar puntaje tecnico, equipo, experiencia y valor-precio. | Seccion 8 | En analisis |
| EPIC-TECH-I | Etapa I tecnica | Preparar respuesta para diagnostico, adaptacion cloud, branding, despliegue y produccion. | Seccion 2.3, Anexo 2 | Pendiente |
| EPIC-AZURE | Azure e infraestructura | Extraer decisiones requeridas sobre Azure, region, servicios, costos y operacion. | 4.10, Anexo 2, Anexo 3 | En analisis |
| EPIC-SEC | Seguridad y DevSecOps | Cubrir controles, evidencias, pentest, backups, IAM, WAF y Zero Trust. | 4.8, 4.10, Anexo 2 4.1/4.3 | En analisis |
| EPIC-QA | QA, aceptacion y cierre | Preparar trazabilidad de hitos, UAT, actas, evidencias y cierre. | Anexo 2 3.1, 5.3, 7 | En analisis |
| EPIC-SUPPORT | Soporte y capacitacion | Cubrir soporte 1 ano, SLA, canales, capacitacion y transferencia. | Anexo 2 H6/H9, 4.2 | En analisis |
| EPIC-COST | Oferta economica base | Preparar estructura economica sin costos todavia. | 2.3, 3.3.3, Anexo 3 | Pendiente |
| EPIC-MOD-001 | Registro e Ingreso de Activos | Preparar alcance y preguntas del modulo. | Anexo 5.1 | Pendiente |
| EPIC-MOD-002 | Gestion de Contratos y Clientes | Preparar alcance y preguntas del modulo. | Anexo 5.2 | Pendiente |
| EPIC-MOD-003 | Subasta / Ventas | Preparar alcance y preguntas de integracion. | Anexo 5.3 | Bloqueado |
| EPIC-MOD-004 | Descargo / Donaciones | Preparar alcance y preguntas del modulo. | Anexo 5.4 | Pendiente |
| EPIC-MOD-005 | Multilenguaje | Preparar alcance i18n y localizacion. | Anexo 5.5 | Pendiente |
| EPIC-MOD-006 | Seguridad avanzada | Preparar alcance de roles, permisos, auditoria y MFA. | Anexo 5.6 | En analisis |
| EPIC-XMOD | Funciones transversales | Preparar alcance multimedia, GIS, auditoria, import/export y reportes. | Anexo 5.7 | En analisis |

## Backlog de tareas para propuesta

| ID | Epic | Tarea | Prioridad | Responsable sugerido | Estado | Dependencias | Fecha control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BL-001 | EPIC-ADM | Crear checklist de documentos Archivo 1 a 5. | Alta | Bid Manager | Pendiente | RFP 3.4.1 | Dia 1 |
| BL-002 | EPIC-ADM | Preparar carta de aceptacion Anexo 1 para firma. | Alta | Legal/Bid Manager | Pendiente | Datos representante | Dia 1 |
| BL-003 | EPIC-ADM | Crear formato oficial de preguntas Anexo 4. | Alta | Bid Manager | Pendiente | Preguntas aprobadas | Dia 1 |
| BL-004 | EPIC-ADM | Registrar calendario oficial: preguntas, respuestas, cierre y seleccion. | Alta | PMP | Validado | RFP 3.1 | Dia 1 |
| BL-005 | EPIC-LEGAL | Solicitar certificado de vigencia menor a 90 dias. | Critica | Legal | Pendiente | Proveedor interno | Dia 1 |
| BL-006 | EPIC-LEGAL | Solicitar poderes/facultades firmante menor a 60 dias. | Critica | Legal | Pendiente | Representante definido | Dia 1 |
| BL-007 | EPIC-LEGAL | Solicitar identificaciones tributarias empresa y representantes. | Alta | Legal | Pendiente | Datos empresa | Dia 1 |
| BL-008 | EPIC-LEGAL | Preparar declaracion de intereses/conflicto. | Alta | Legal | Pendiente | Formulario aplicable | Dia 2 |
| BL-009 | EPIC-LEGAL | Evaluar capacidad de emitir garantias 10% fiel cumplimiento y 100% anticipo. | Critica | CFO/Legal | Bloqueado | Monto contrato | Dia 2 |
| BL-010 | EPIC-EVAL | Mapear propuesta contra 4 criterios de evaluacion. | Alta | Bid Manager | Pendiente | Matriz cumplimiento | Dia 1 |
| BL-011 | EPIC-EVAL | Identificar evidencias reales para 3 referencias comparables. | Critica | CTO/Bid Manager | Pendiente | Historial Justech | Dia 1 |
| BL-012 | EPIC-EVAL | Confirmar si Justech posee certificaciones Microsoft muy valoradas. | Alta | CTO | Pendiente | Inventario certificaciones | Dia 1 |
| BL-013 | EPIC-EVAL | Confirmar Lider de Proyecto con PMP. | Critica | PMO | Pendiente | CV/certificado | Dia 1 |
| BL-014 | EPIC-TECH-I | Preparar enfoque de diagnostico de codigo sin acceso previo. | Alta | Arquitecto Django | Pendiente | Preguntas PADF | Dia 2 |
| BL-015 | EPIC-TECH-I | Preparar matriz de adaptacion cloud para dependencias, variables y archivos. | Alta | Arquitecto Django | Pendiente | RFP Anexo 2 | Dia 2 |
| BL-016 | EPIC-TECH-I | Preparar checklist de branding y terminologia INCABIDE. | Alta | UX/UI Lead | Pendiente | Linea grafica INCABIDE | Dia 2 |
| BL-017 | EPIC-TECH-I | Mapear cambios terminologicos Paraguay -> RD. | Alta | Analista funcional | Validado | Anexo 2 Fase II | Dia 2 |
| BL-018 | EPIC-AZURE | Preparar lista de decisiones Azure obligatorias. | Critica | Arquitecto Azure | Validado | RFP 4.10 / Anexo 2 | Dia 1 |
| BL-019 | EPIC-AZURE | Preguntar tenant/suscripcion Azure y region preferida. | Critica | Arquitecto Azure | Pendiente | Preguntas PADF | Dia 1 |
| BL-020 | EPIC-AZURE | Preguntar ambientes requeridos: dev, QA/UAT, staging, prod. | Critica | Arquitecto Azure | Pendiente | Preguntas PADF | Dia 1 |
| BL-021 | EPIC-AZURE | Preparar estructura de estimacion mensual/anual Azure sin costos. | Alta | Arquitecto Azure/CFO | Pendiente | Anexo 3 | Dia 2 |
| BL-022 | EPIC-SEC | Mapear controles de seguridad 4.1 a evidencias 4.3. | Critica | DevSecOps | Validado | Anexo 2 4.1/4.3 | Dia 1 |
| BL-023 | EPIC-SEC | Preparar preguntas RTO/RPO, backups, retencion y HA. | Critica | DevSecOps/Azure | Pendiente | Preguntas PADF | Dia 1 |
| BL-024 | EPIC-SEC | Confirmar alcance de pentest tercero y proveedor aceptable. | Alta | DevSecOps | Pendiente | Preguntas PADF | Dia 2 |
| BL-025 | EPIC-QA | Crear modelo de aceptacion por hito Etapa I. | Alta | QA Manager | Pendiente | Anexo 2 3.1 | Dia 2 |
| BL-026 | EPIC-QA | Crear checklist de cierre final y actas parciales. | Alta | QA Manager | Pendiente | Anexo 2 7 | Dia 2 |
| BL-027 | EPIC-QA | Definir trazabilidad requisito -> entregable -> evidencia -> aprobador. | Critica | QA Manager | Pendiente | Matriz maestra | Dia 2 |
| BL-028 | EPIC-SUPPORT | Preparar preguntas sobre soporte critico y limite de 30 horas. | Alta | Service Manager | Pendiente | Preguntas PADF | Dia 1 |
| BL-029 | EPIC-SUPPORT | Preparar estructura de adenda de soporte y SLA. | Media | Service Manager | Pendiente | Aclaraciones | Dia 3 |
| BL-030 | EPIC-SUPPORT | Preparar estructura de capacitacion tecnica minima 4 horas. | Media | Technical Writer | Pendiente | Hito 6 | Dia 3 |
| BL-031 | EPIC-COST | Crear workbook de costos segun Anexo 3 sin valores. | Critica | CFO/Bid Manager | Pendiente | Alcance validado | Dia 2 |
| BL-032 | EPIC-COST | Separar item opcional de interconexion PGR. | Alta | CFO/Arquitecto | Pendiente | Alcance API/PGR | Dia 2 |
| BL-033 | EPIC-COST | Preparar estrategia de precio global vs precio por modulo. | Alta | CFO/CTO | Pendiente | Decisiones comerciales | Dia 3 |
| BL-034 | EPIC-MOD-001 | Crear backlog funcional para Registro de Activos. | Media | Analista funcional | Validado | Anexo 5.1 | Dia 2 |
| BL-035 | EPIC-MOD-001 | Preguntar catalogos oficiales de provincias, municipios y entidades remitentes. | Alta | Analista funcional | Pendiente | Preguntas PADF | Dia 1 |
| BL-036 | EPIC-MOD-002 | Crear backlog funcional para Contratos y Clientes. | Alta | Analista funcional | Validado | Anexo 5.2 | Dia 2 |
| BL-037 | EPIC-MOD-002 | Preguntar integraciones con Finanzas, Inventario y Mantenimiento. | Critica | Arquitecto Django | Pendiente | Preguntas PADF | Dia 1 |
| BL-038 | EPIC-MOD-003 | Preguntar estado y especificacion del sistema de subastas existente. | Critica | Arquitecto Django | Pendiente | Preguntas PADF | Dia 1 |
| BL-039 | EPIC-MOD-003 | Separar alcance de gestion de subasta vs ejecucion existente. | Alta | Analista funcional | Bloqueado | Respuesta PADF | Dia 2 |
| BL-040 | EPIC-MOD-004 | Crear backlog funcional para Descargo/Donaciones. | Alta | Consultor Gobierno Digital | Validado | Anexo 5.4 | Dia 2 |
| BL-041 | EPIC-MOD-004 | Preguntar normativa ambiental/legal aplicable a destruccion y donacion. | Alta | Legal/Funcional | Pendiente | Preguntas PADF | Dia 1 |
| BL-042 | EPIC-MOD-005 | Crear backlog para multilenguaje y localizacion. | Media | UX/UI Lead | Validado | Anexo 5.5 | Dia 2 |
| BL-043 | EPIC-MOD-006 | Separar seguridad operacional Etapa I de seguridad avanzada Etapa II. | Critica | DevSecOps | Pendiente | Preguntas PADF | Dia 1 |
| BL-044 | EPIC-XMOD | Crear backlog de multimedia. | Media | Arquitecto Django | Validado | Anexo 5.7 | Dia 2 |
| BL-045 | EPIC-XMOD | Crear backlog de geolocalizacion/GIS. | Alta | Arquitecto Django/GIS | Validado | Anexo 5.7 | Dia 2 |
| BL-046 | EPIC-XMOD | Preguntar proveedor/licencia de mapas RD. | Alta | Arquitecto Azure | Pendiente | Preguntas PADF | Dia 1 |
| BL-047 | EPIC-XMOD | Crear backlog de importacion/exportacion masiva. | Alta | Arquitecto Django | Validado | Anexo 5.7 | Dia 2 |
| BL-048 | EPIC-XMOD | Crear backlog de reportes y analisis predictivo. | Alta | Analista BI | Validado | Anexo 5.7 | Dia 2 |
| BL-049 | EPIC-XMOD | Preguntar criterios de aceptacion para analisis predictivo. | Critica | Analista BI | Pendiente | Preguntas PADF | Dia 1 |
| BL-050 | EPIC-ADM | Preparar paquete de evidencias y versionado de documentos. | Alta | Bid Manager | Pendiente | Estructura repo | Dia 1 |

## Dependencias criticas

1. Codigo fuente no disponible hasta adjudicacion.
2. Linea grafica INCABIDE.
3. Validacion legal de terminologia.
4. Suscripcion/tenant Azure y region.
5. DNS y dominio INCABIDE.
6. Usuarios clave para UAT.
7. Informacion del sistema de subastas existente.
8. Definicion de API obligatoria.
9. Datos existentes y volumen de archivos.
10. Certificaciones y referencias reales de Justech.

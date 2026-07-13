# REQUISITOS TECNICOS, AZURE, SEGURIDAD, QA, SOPORTE Y CAPACITACION

Fuente: RFP No. 5801 DRC3P PADF / INCABIDE.  
Estado: extraccion base para cumplimiento. No contiene arquitectura propuesta.

## Requisitos tecnicos Etapa I

| ID | Seccion | Requisito trazable | Evidencia PDF | Entregable / respuesta requerida |
| --- | --- | --- | --- | --- |
| TEC-001 | 2.2 | SGB existente esta desarrollado en Django/Python. | p.3, L77-L80 | Mantener compatibilidad Django/Python. |
| TEC-002 | 2.2 | Base de datos actual PostgreSQL 14+ con postgis y unaccent. | p.3, L77-L80 | Mantener soporte PostgreSQL/extensiones. |
| TEC-003 | 2.2 | INCABIDE posee el codigo fuente, entregado "tal cual". | p.3, L77-L81 | Planificar diagnostico inicial. |
| TEC-004 | 2.2 | Abordar modulos potencialmente incompletos, en particular Subastas. | p.3, L81-L85 | Identificar alcance real posterior. |
| TEC-005 | 2.2 | Sistema no preparado para nube moderna. | p.3, L81-L84 | Adaptacion cloud obligatoria. |
| TEC-006 | 2.2 | Requiere personalizacion visual, terminologica e institucional. | p.3, L83-L85 | Plan de branding/nomenclatura. |
| TEC-007 | 2.2 | Carece de modulos adicionales requeridos por INCABIDE. | p.3, L84-L85 | Etapa II modular. |
| TEC-008 | 2.3 | Etapa I no incluye nuevas funcionalidades. | p.3, L87-L90 | Evitar prometer desarrollo nuevo en Etapa I. |
| TEC-009 | 2.3 | Etapa II desarrolla nuevos modulos por fases priorizadas. | p.3, L90-L91 | Backlog modular. |
| TEC-010 | Anexo 2, 1 | Servicio requerido: diagnostico, correccion, adaptacion tecnica, personalizacion y produccion. | p.14, L657-L661 | Plan por fases. |
| TEC-011 | Anexo 2, 1 | PostgreSQL es motor preferido. | p.14, L661-L667 | Usar PostgreSQL salvo aprobacion. |
| TEC-012 | Anexo 2, 1 | Motor alternativo solo si garantiza postgis/unaccent equivalentes e integridad funcional. | p.14, L663-L667 | Requiere validacion INCABIDE. |
| TEC-013 | Anexo 2, Fase I | Analisis exhaustivo del codigo fuente y dependencias. | p.14, L671-L676 | Informe de compatibilidad. |
| TEC-014 | Anexo 2, Fase I | Identificar librerias, paquetes o patrones no compatibles con cloud. | p.14, L674-L676 | Inventario tecnico. |
| TEC-015 | Anexo 2, Fase I | Reemplazar, actualizar o adaptar dependencias incompatibles. | p.14, L677-L679 | Listado dependencias actualizadas. |
| TEC-016 | Anexo 2, Fase I | Eliminar dependencia de archivos de configuracion. | p.14, L680-L681 | Refactorizacion. |
| TEC-017 | Anexo 2, Fase I | Configuraciones sensibles deben leerse desde variables de entorno. | p.14, L680-L681 | Gestion de variables. |
| TEC-018 | Anexo 2, Fase I | Adaptar manejo de archivos, reportes y geolocalizacion al nuevo entorno. | p.14, L682-L686 | Funcionalidades adaptadas. |
| TEC-019 | Anexo 2, Fase IV | Crear Dockerfile. | p.15, L733-L737 | Dockerfile en repositorio. |
| TEC-020 | Anexo 2, Fase IV | Crear Docker Compose. | p.15, L733-L737 | Compose en repositorio. |
| TEC-021 | Anexo 2, Fase IV | Orquestar aplicacion y proxy inverso, por ejemplo Nginx. | p.15, L733-L737 | Proxy configurado. |
| TEC-022 | Anexo 2, Fase IV | Construir y publicar imagenes del sistema. | p.15, L740-L742 | Imagenes publicadas. |
| TEC-023 | Anexo 2, Fase IV | Desplegar frontend, backend y base de datos. | p.16, L748-L750 | Sistema operativo. |
| TEC-024 | Anexo 2, Fase IV | Proveer API funcional del SGB para INCABIDE. | p.16, L753-L755 | API validada. |
| TEC-025 | Anexo 2, Fase IV | API debe ser interoperable con sistemas externos. | p.16, L753-L755 | Definir alcance API con PADF. |
| TEC-026 | Anexo 2, Fase IV | Interconexion con PGR depende de aprobacion PGR y no es entregable con fecha fija. | p.16, L755-L759 | Cotizar separado. |

## Requisitos Azure e infraestructura obligatoria

| ID | Seccion | Requisito trazable | Evidencia PDF | Decision pendiente |
| --- | --- | --- | --- | --- |
| AZ-001 | 4.10 | Despliegue obligatorio sobre Microsoft Azure. | p.7, L265-L270 | Ninguna: Azure es obligatorio. |
| AZ-002 | 4.10 | Azure no tiene region en Republica Dominicana. | p.7, L265-L270 | Definir region aprobada. |
| AZ-003 | 4.10 | Region debe ofrecer garantias juridicas y de desempeno. | p.7, L265-L268 | Analisis legal/rendimiento. |
| AZ-004 | 4.10 | Implementar salvaguardas contractuales y tecnicas para tratamiento transfronterizo. | p.7, L267-L270 | Definir salvaguardas. |
| AZ-005 | 7 | Azure requerido por estabilidad, escalabilidad e integracion con sistemas INCABIDE. | p.8-9, L322-L329 | Alinear narrativa posterior. |
| AZ-006 | Anexo 2, 1 | Azure es plataforma no sustituible. | p.14, L661-L664 | No proponer otra nube. |
| AZ-007 | Anexo 2, Fase III | Computo: VM o servicio gestionado para contenedores Docker. | p.15, L725-L728 | VM vs servicio gestionado. |
| AZ-008 | Anexo 2, Fase III | Base de datos PostgreSQL 14+ preferida con postgis/unaccent. | p.15, L729-L731 | Servicio gestionado vs VM. |
| AZ-009 | Anexo 2, Fase III | Almacenamiento de medios para archivos y documentos. | p.15, L732 | Seleccionar servicio. |
| AZ-010 | Anexo 2, Fase IV | Crear VM cloud con capacidad necesaria para imagen contenerizada. | p.15, L738-L739 | Dimensionamiento. |
| AZ-011 | Anexo 2, Fase IV | Sistema accesible via dominio indicado por INCABIDE. | p.15, L740-L742 | DNS/dominio/certificado. |
| AZ-012 | Anexo 2, Fase IV | Configurar dominio personalizado, ejemplo sgb.incabide.gob.do. | p.16, L751-L752 | Responsable DNS. |
| AZ-013 | Anexo 2, H3 | Computo, base de datos y almacenamiento deben estar activos, accesibles y documentados. | p.17, L907-L912 | Ambientes y accesos. |
| AZ-014 | Anexo 2, H7 | Proveedor asume infraestructura cloud por 12 meses. | p.18, L995-L1010 | Dimensionar costos. |
| AZ-015 | Anexo 3, Sec. 3 | Estimar costo mensual/anual Azure por componente y dimensionamiento. | p.26, L1530-L1545 | Cotizacion posterior. |

## Requisitos de seguridad

| ID | Seccion | Requisito trazable | Evidencia PDF | Evidencia requerida |
| --- | --- | --- | --- | --- |
| SEC-001 | 4.8 | Mantener confidencialidad sobre informacion PADF/INCABIDE. | p.7, L238-L242 | NDA y controles. |
| SEC-002 | 4.8 | Codigo fuente, produccion y datos sensibles se entregan solo al adjudicatario. | p.7, L243-L248 | Gestion de acceso posterior. |
| SEC-003 | 4.10 | Cumplir Ley 172-13 de proteccion de datos personales. | p.7, L259-L264 | Controles de datos. |
| SEC-004 | 4.10 | Aplicar cifrado en reposo. | p.7, L261-L264 | Evidencia cifrado. |
| SEC-005 | 4.10 | Aplicar cifrado en transito. | p.7, L261-L264 | TLS/HTTPS. |
| SEC-006 | 4.10 | Controles de acceso por rol. | p.7, L261-L264 | RBAC. |
| SEC-007 | 4.10 | Registros de auditoria. | p.7, L261-L264 | Logs. |
| SEC-008 | 4.10 | Minimizacion de datos. | p.7, L261-L264 | Politica de datos. |
| SEC-009 | 4.10 | Gestion segura de credenciales. | p.7, L261-L264 | Vault/secretos. |
| SEC-010 | Anexo 2, 4.1 | Aislamiento de red en VPC con subredes segmentadas. | p.18, L1060-L1065 | Evidencia red. |
| SEC-011 | Anexo 2, 4.1 | Firewall con reglas personalizables por IP o puerto. | p.19, L1070-L1071 | Evidencia firewall. |
| SEC-012 | Anexo 2, 4.1 | IAM con privilegio minimo. | p.19, L1072-L1073 | Matriz IAM. |
| SEC-013 | Anexo 2, 4.1 | MFA obligatorio para accesos administrativos. | p.19, L1074 | Evidencia MFA. |
| SEC-014 | Anexo 2, 4.1 | Cifrado TLS/HTTPS y en reposo. | p.19, L1075 | Evidencia cifrado. |
| SEC-015 | Anexo 2, 4.1 | Llaves criptograficas mediante KMS o HSM. | p.19, L1076 | Evidencia KMS/HSM. |
| SEC-016 | Anexo 2, 4.1 | WAF con proteccion OWASP Top 10. | p.19, L1077 | Evidencia WAF. |
| SEC-017 | Anexo 2, 4.1 | Proteccion DDoS. | p.19, L1078 | Evidencia DDoS. |
| SEC-018 | Anexo 2, 4.1 | Segmentacion de red y VPN para accesos administrativos. | p.19, L1079 | Evidencia VPN. |
| SEC-019 | Anexo 2, 4.1 | Secretos en vaults; nunca credenciales en codigo fuente. | p.19, L1080 | Evidencia vault. |
| SEC-020 | Anexo 2, 4.1 | Registro de accesos, monitoreo en tiempo real y alertas. | p.19, L1081 | Evidencia monitoreo. |
| SEC-021 | Anexo 2, 4.1 | Escaneos de seguridad automaticos. | p.19, L1082 | Reportes escaneo. |
| SEC-022 | Anexo 2, 4.1 | Pruebas de penetracion periodicas. | p.19, L1082 | Plan pentest. |
| SEC-023 | Anexo 2, 4.1 | Backups automaticos y cifrados. | p.19, L1083 | Registro backup. |
| SEC-024 | Anexo 2, 4.1 | Plan de Recuperacion ante Desastres. | p.19, L1083 | DRP. |
| SEC-025 | Anexo 2, 4.1 | Alta disponibilidad y redundancia. | p.19, L1084 | Evidencia arquitectura. |
| SEC-026 | Anexo 2, 4.1 | Modelo Zero Trust. | p.19, L1084 | Evidencia controles. |
| SEC-027 | Anexo 2, 4.3 | No solicitar aprobacion Hito 4 sin evidencias de seguridad aprobadas. | p.19, L1103-L1106 | Paquete seguridad. |
| SEC-028 | Anexo 2, 4.3 | Documento de arquitectura de seguridad con controles 4.1 y capturas. | p.19, L1107-L1109 | Documento seguridad. |
| SEC-029 | Anexo 2, 4.3 | Informe de vulnerabilidades con CVSS y remediaciones. | p.20, L1114-L1116 | Informe CVSS. |
| SEC-030 | Anexo 2, 4.3 | No se aceptan vulnerabilidades Alta o Critica abiertas. | p.20, L1114-L1116 | Reporte limpio. |
| SEC-031 | Anexo 2, 4.3 | Certificado TLS/HTTPS con calificacion minima A externa. | p.20, L1117-L1118 | Reporte SSL Labs o similar. |
| SEC-032 | Anexo 2, 4.3 | Informe de prueba de acceso con MFA activo. | p.20, L1119-L1120 | Evidencia MFA. |
| SEC-033 | Anexo 2, 4.3 | Evidencia de primer respaldo automatico ejecutado y restaurable. | p.20, L1121-L1122 | Prueba restore. |
| SEC-034 | Anexo 2, 4.3 | Declaracion escrita de no credenciales en codigo ni archivos versionados. | p.20, L1123-L1124 | Declaracion. |
| SEC-035 | Anexo 2, 4.3 | Pentest por tercero independiente dentro de 30 dias post-produccion. | p.20, L1125-L1128 | Informe pentest. |
| SEC-036 | Anexo 2, 7.2 | Cierre requiere evidencias de seguridad aprobadas. | p.23, L1413 | Evidencias aprobadas. |
| SEC-037 | Anexo 2, 7.2 | Cierre requiere pentest con observaciones remediadas o plan acordado. | p.23, L1414-L1415 | Informe/pplan. |
| SEC-038 | Anexo 2, 7.2 | Declaracion jurada de no retener codigo, credenciales ni datos. | p.24, L1422-L1423 | Declaracion jurada. |

## Requisitos de QA, aceptacion y cierre

| ID | Seccion | Requisito trazable | Evidencia PDF | Criterio |
| --- | --- | --- | --- | --- |
| QA-001 | Anexo 2, 3.1 | Ningun hito se considera entregado ni pagable sin aprobacion escrita. | p.17, L839-L844 | Aprobacion PADF/INCABIDE. |
| QA-002 | Anexo 2, 3.1 | PADF tiene 7 dias habiles para aprobar u objetar; silencio aprueba de pleno derecho. | p.17, L839-L844 | Control de aprobaciones. |
| QA-003 | Hito 1 | Informe de compatibilidad, dependencias actualizadas y codigo refactorizado en Git. | p.17, L847-L858 | Compila y ejecuta sin errores. |
| QA-004 | Hito 1 | Informe cubre inventario, incompatibilidades, acciones y prueba de ejecucion. | p.17, L859-L866 | Validacion lider tecnico. |
| QA-005 | Hito 2 | Sistema en prueba con logos, tipografias y terminologia dominicana. | p.17, L871-L883 | Validacion visual. |
| QA-006 | Hito 2 | Cero referencias a SENABICO o terminologia paraguaya. | p.17, L884-L889 | Revision visual/reportes. |
| QA-007 | Hito 3 | Diagrama arquitectura PDF, credenciales y evidencias de despliegue. | p.17, L895-L906 | Infraestructura activa. |
| QA-008 | Hito 3 | INCABIDE debe iniciar sesion con credenciales admin propias. | p.17, L907-L912 | Verificacion acceso. |
| QA-009 | Hito 4 | Aplicacion accesible en dominio con TLS activo. | p.17, L918-L927 | Acceso navegador externo. |
| QA-010 | Hito 4 | Dockerfile y Docker Compose en repositorio. | p.17, L924-L928 | Repositorio. |
| QA-011 | Hito 4 | API funcional validada en produccion. | p.17, L928-L943 | API responde correctamente. |
| QA-012 | Hito 4 | Todos los modulos originales visibles y operables. | p.17, L937-L940 | Cobertura 100%. |
| QA-013 | Hito 5 | Tecnico INCABIDE no involucrado debe ejecutar procedimientos sin asistencia. | p.17-18, L947-L973 | Prueba de transferencia. |
| QA-014 | Hito 6 | Capacitacion minima 4 horas. | p.18, L974-L981 | Sesion realizada. |
| QA-015 | Hito 6 | Grabacion o PDF y lista firmada con minimo 2 tecnicos. | p.18, L979-L987 | Evidencia capacitacion. |
| QA-016 | Hito 6 | INCABIDE confirma autonomia tecnica por escrito. | p.18, L988-L994 | Confirmacion escrita. |
| QA-017 | Hito 7 | Constancia firmada con desglose de servicios, cloud, costo mensual e inicio/termino. | p.18, L995-L1010 | Documento firmado. |
| QA-018 | Hito 8 | Inventario firmado de credenciales cloud, BD, SSH y tokens API. | p.18, L1012-L1026 | Entrega segura. |
| QA-019 | Hito 8 | INCABIDE verifica acceso y proveedor declara no retener copias. | p.18, L1027-L1035 | Verificacion y declaracion. |
| QA-020 | Hito 9 | Contrato/adenda soporte con canales, horario, tiempos y escalada. | p.18, L1036-L1059 | Documento firmado. |
| QA-021 | Anexo 2, 5.3 | Cada modulo Etapa II requiere UAT ejecutado y aprobado. | p.22, L1322-L1323 | Evidencia UAT. |
| QA-022 | Anexo 2, 5.3 | Cada modulo requiere acta de aceptacion parcial firmada. | p.22, L1325-L1326 | Acta firmada. |
| QA-023 | Anexo 2, 6 | Sistema desplegado debe funcionar con 100% de modulos originales visibles y accesibles. | p.23, L1375-L1384 | Cobertura funcional. |
| QA-024 | Anexo 2, 6 | Seguridad 4.1 debe subsanarse en 5 dias habiles si incumple. | p.23, L1385-L1393 | Plan remediacion. |
| QA-025 | Anexo 2, 7.1 | Proyecto se cierra solo con Acta de Cierre Final. | p.23, L1397-L1401 | Acta cierre. |
| QA-026 | Anexo 2, 7.2 | Cierre requiere todos los hitos Etapa I aprobados. | p.23, L1402-L1405 | Aprobaciones. |
| QA-027 | Anexo 2, 7.2 | Cierre requiere todos los modulos Etapa II contratados aprobados. | p.23, L1405-L1407 | Actas parciales. |
| QA-028 | Anexo 2, 7.4 | Cada modulo o etapa puede tener acta parcial para pago proporcional. | p.24, L1430-L1434 | Actas parciales. |
| QA-029 | Anexo 2, 7.5 | Garantia de 90 dias corre independiente por modulo desde su acta. | p.24, L1441-L1445 | Control de garantias. |

## Requisitos de soporte y capacitacion

| ID | Seccion | Requisito trazable | Evidencia PDF | Respuesta requerida |
| --- | --- | --- | --- | --- |
| SUP-001 | Anexo 2, H9 | Soporte tecnico por 1 ano post-despliegue. | p.16, L823-L828 | Contrato/adenda. |
| SUP-002 | Anexo 2, 4.2 | Incidente critico: respuesta maxima 1 hora. | p.19, L1085-L1088 | SLA. |
| SUP-003 | Anexo 2, 4.2 | Incidente mayor: respuesta maxima 4 horas habiles. | p.19, L1088-L1090 | SLA. |
| SUP-004 | Anexo 2, 4.2 | Incidente menor: respuesta maxima 8 horas habiles. | p.19, L1088-L1090 | SLA. |
| SUP-005 | Anexo 2, 4.2 | Horas habiles: lunes a viernes 8:00 a.m. a 5:00 p.m. GMT-4. | p.19, L1091-L1093 | Definir soporte. |
| SUP-006 | Anexo 2, 4.2 | Canales minimos: correo y telefono/WhatsApp. | p.19, L1094-L1096 | Canales activos. |
| SUP-007 | Anexo 2, 4.2 | Soporte fuera de horario para incidentes criticos o continuidad. | p.19, L1097-L1102 | Escalamiento critico. |
| SUP-008 | Anexo 2, 4.2 | Volumen estimado de soporte: aproximadamente 30 horas anuales, sin limitar criticos. | p.19, L1100-L1102 | Aclarar alcance. |
| CAP-001 | Anexo 2, H6 | Transferencia al equipo tecnico sobre arquitectura y gestion de plataforma. | p.16, L803-L809 | Capacitacion tecnica. |
| CAP-002 | Anexo 2, H6 | Sesion minima 4 horas, virtual o presencial segun acuerdo. | p.18, L974-L981 | Agenda y evidencia. |
| CAP-003 | Anexo 2, H6 | Entregar grabacion o presentacion PDF. | p.18, L979-L984 | Material capacitacion. |
| CAP-004 | Anexo 2, H6 | Lista de asistencia firmada con minimo 2 tecnicos INCABIDE. | p.18, L984-L992 | Evidencia asistencia. |

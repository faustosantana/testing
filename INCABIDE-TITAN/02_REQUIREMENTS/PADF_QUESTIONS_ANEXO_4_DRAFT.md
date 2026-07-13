# PREGUNTAS PARA PADF — BORRADOR ANEXO 4

Formato base segun Anexo 4. Estas preguntas deben revisarse internamente antes de enviarse.  
Canal oficial: correos PADF indicados en Seccion Novena del RFP.

| N° | Seccion SdP | Pregunta del Participante | Impacto |
| ---: | --- | --- | --- |
| 1 | 2.3 / Anexo 2 | ¿El plazo de 8 semanas de Etapa I inicia desde la firma del contrato, desde la entrega del codigo fuente, o desde la habilitacion de accesos a Azure/DNS? | Cronograma, penalidades |
| 2 | 2.2 / 4.8 | ¿PADF/INCABIDE entregara documentacion tecnica, manuales, backlog, issues conocidos o inventario de modulos existentes junto con el codigo fuente? | Alcance, costo |
| 3 | 2.2 | ¿Existe una lista de defectos conocidos del SGB actual? | Alcance, QA |
| 4 | Anexo 2, Hito 4 | ¿Que modulos del codigo fuente original deben considerarse obligatorios para validar "100% de modulos visibles y operables"? | Aceptacion |
| 5 | 2.3 / Anexo 2 Fase IV | ¿Que significa exactamente "sin desarrollo de nuevas funcionalidades" en Etapa I considerando que se exige una API funcional? | Alcance |
| 6 | Anexo 2 Fase IV | ¿La API de Etapa I debe exponer solo funcionalidades existentes o tambien nuevas capacidades? | API, costo |
| 7 | Anexo 2 Fase IV | ¿Cuales son los endpoints minimos requeridos para la API funcional del SGB en Etapa I? | API, alcance |
| 8 | Anexo 2 Fase IV | ¿La API debe ser REST, GraphQL u otro estandar? | API |
| 9 | Anexo 2 Fase IV | ¿Se requiere documentacion OpenAPI/Swagger y versionamiento de API? | Documentacion, API |
| 10 | Anexo 2 Fase IV / Anexo 3 | ¿La interconexion con PGR debe cotizarse como item opcional separado aun cuando la API base sea obligatoria? | Costos, alcance |
| 11 | Anexo 2 Fase IV | ¿La interconexion con PGR requiere VPN, API gateway, certificados, autenticacion especifica o aprobacion formal previa? | Integracion |
| 12 | Anexo 2 Fase III | ¿INCABIDE ya posee una suscripcion Azure o el proveedor debe crear y administrar una nueva? | Azure, costos |
| 13 | Anexo 2 Fase III | ¿La infraestructura debe quedar desde el inicio bajo tenant/suscripcion de INCABIDE? | Azure, acceso |
| 14 | 4.10 | ¿Que region Azure prefiere INCABIDE para residencia de datos, latencia y salvaguardas juridicas? | Azure, legal |
| 15 | 4.10 | ¿Quien aprobara formalmente la transferencia internacional de datos conforme a Ley 172-13? | Legal, datos |
| 16 | Anexo 2 Fase III | ¿Se aceptan servicios gestionados de Azure como Azure App Service, Azure Container Apps o Azure Database for PostgreSQL Flexible Server? | Arquitectura, costo |
| 17 | Anexo 2 Fase III/Fase IV | ¿Se requiere obligatoriamente una VM con Docker Compose o puede usarse un servicio gestionado que ejecute contenedores? | Azure |
| 18 | Anexo 2 4.1 | ¿Se requiere alta disponibilidad activa-activa, activa-pasiva o redundancia basica? | Azure, costo |
| 19 | Anexo 2 4.1 | ¿Que RTO y RPO espera INCABIDE para el SGB? | DRP, backups |
| 20 | Anexo 2 4.1 | ¿Cual es la frecuencia y retencion minima de backups? | DRP, costo |
| 21 | Anexo 2 4.1 | ¿Los backups deben replicarse a una region secundaria? | DRP, costo |
| 22 | Anexo 2 4.1 | ¿Debe usarse Azure Key Vault para secretos y llaves criptograficas? | Seguridad |
| 23 | Anexo 2 4.1 | ¿Se exige cifrado con llaves administradas por cliente? | Seguridad, costo |
| 24 | Anexo 2 4.1 | ¿Debe implementarse Azure Front Door WAF, Application Gateway WAF u otro servicio especifico? | WAF, costo |
| 25 | Anexo 2 4.1 | ¿Se requiere Azure DDoS Protection Standard o basta con proteccion basica incluida? | DDoS, costo |
| 26 | Anexo 2 4.1 | ¿La VPN administrativa debe ser site-to-site, point-to-site, Bastion u otra modalidad? | Acceso seguro |
| 27 | Anexo 2 4.1 | ¿Que herramientas de monitoreo/logging son aceptables: Azure Monitor, Log Analytics, Defender for Cloud, SIEM institucional u otras? | Operacion, costo |
| 28 | Anexo 2 Fase IV | ¿Quien administra el dominio y DNS para sgb.incabide.gob.do y en que plazo se habilitaran registros? | DNS, cronograma |
| 29 | Anexo 2 Fase IV | ¿INCABIDE proveera certificados TLS o el proveedor debe gestionarlos? | Seguridad, costo |
| 30 | Anexo 3 Sec. 3 | ¿La estimacion Azure por 1 ano debe incluir solo produccion o tambien desarrollo, QA/UAT y staging? | Costos |
| 31 | Anexo 2 | ¿Se requieren ambientes separados de desarrollo, QA/UAT, staging y produccion? | Infraestructura |
| 32 | Anexo 2 5.3 | ¿Quien aprobara UAT por cada modulo y con que disponibilidad? | QA, cronograma |
| 33 | Anexo 2 5.3 | ¿Se aceptara una matriz de trazabilidad requisito-entregable-evidencia como base de aceptacion? | QA |
| 34 | Anexo 2 4.2 | ¿El soporte de incidentes criticos fuera de horario esta limitado a las 30 horas anuales estimadas o es ilimitado? | Soporte, costo |
| 35 | Anexo 2 4.2 | ¿Cual sera el horario operativo real del sistema? | Soporte |
| 36 | Anexo 2 4.3 | ¿El pentest debe ser realizado por un proveedor previamente aprobado por PADF/INCABIDE? | Seguridad, costo |
| 37 | Anexo 2 4.3 | ¿Que severidades deben remediarse antes del cierre final ademas de Alta/Critica? | Seguridad, cierre |
| 38 | Anexo 5 | ¿Cuantos usuarios internos tendra el sistema en produccion? | Dimensionamiento |
| 39 | Anexo 5 | ¿Cuantos usuarios concurrentes se esperan? | Dimensionamiento |
| 40 | Anexo 5.6 | ¿Se requiere integracion con Microsoft Entra ID / Azure AD para usuarios internos? | Identidad |
| 41 | Anexo 5.6 | ¿Los roles Administracion, Gerente y Espectador son suficientes o existen perfiles adicionales? | Seguridad funcional |
| 42 | Anexo 5.1 | ¿INCABIDE proveera catalogos oficiales de provincias, ciudades, municipios, entidades remitentes y tipos de activos? | Datos maestros |
| 43 | Anexo 5.1 | ¿Que entidad sera responsable de mantener los catalogos maestros despues de la puesta en produccion? | Operacion |
| 44 | Anexo 5.2 | ¿Existen sistemas de Finanzas, Inventario o Mantenimiento actuales con los que deba integrarse el modulo de Contratos y Clientes? | Integraciones |
| 45 | Anexo 5.2 | ¿Existen plantillas oficiales de contratos, comprobantes, recibos y estados de cuenta? | Alcance funcional |
| 46 | Anexo 5.2 | ¿Se requiere integracion con sistemas de pago, contabilidad, correo institucional, SMS o WhatsApp? | Integraciones |
| 47 | Anexo 5.3 | ¿Existe especificacion tecnica del sistema de subastas actual de INCABIDE? | Integracion |
| 48 | Anexo 5.3 | ¿El sistema de subastas actual tiene API, base de datos accesible, exportaciones o documentacion? | Integracion |
| 49 | Anexo 5.3 | ¿Que funcionalidades de subasta ya existen y cuales deben complementarse? | Alcance |
| 50 | Anexo 5.4 | ¿Que normativa legal y ambiental especifica aplica a destruccion, donacion y devolucion de activos? | Legal, funcional |
| 51 | Anexo 5.4 | ¿INCABIDE proveera formatos oficiales para actas, protocolos y documentos legales de disposicion? | Documentacion |
| 52 | Anexo 5.5 | ¿Los manuales y recursos de ayuda deben entregarse tambien en ingles o solo la interfaz? | Multilenguaje |
| 53 | Anexo 5.7 | ¿Que proveedor de mapas, licencias GIS o fuentes cartograficas debe utilizarse para Republica Dominicana? | GIS, costo |
| 54 | Anexo 5.7 | ¿Se requiere geolocalizacion en tiempo real con dispositivos GPS o registro manual/georreferenciado de ubicacion? | GIS, alcance |
| 55 | Anexo 5.7 | ¿Cuales son los limites esperados de tamano y volumen para imagenes, videos, audio y documentos? | Multimedia, costo |
| 56 | Anexo 5.7 | ¿Se requiere antivirus o analisis de malware para archivos cargados? | Seguridad |
| 57 | Anexo 5.7 | ¿Cuales formatos de importacion masiva se usaran inicialmente: CSV, Excel, PDF u otros? | Datos |
| 58 | Anexo 5.7 | ¿Existe base de datos productiva actual del SGB que deba migrarse? | Migracion |
| 59 | Anexo 5.7 | ¿Que volumen de registros, documentos y multimedia existe actualmente? | Migracion, costo |
| 60 | Anexo 5.7 | ¿Se requiere migracion historica completa o solo configuracion inicial? | Migracion |
| 61 | Anexo 5.7 | ¿Quien sera responsable de depurar datos inconsistentes antes de la importacion? | Datos |
| 62 | Anexo 5.7 | ¿Que criterios de aceptacion aplican al analisis predictivo y pronostico? | Reportes |
| 63 | Anexo 5.7 | ¿Existen datos historicos suficientes para analisis predictivo? | Reportes |
| 64 | Anexo 5.7 | ¿Los reportes deben exportar PDF, Excel y CSV en todos los modulos o solo en reportes especificos? | Reportes |
| 65 | 5 | ¿INCABIDE tiene lista de licencias open source prohibidas, por ejemplo GPL/AGPL? | Licencias |
| 66 | 5 | ¿Se requiere SBOM formal de dependencias y vulnerabilidades? | Licencias, seguridad |
| 67 | 5 | ¿Se deben entregar resultados de analisis de vulnerabilidades de dependencias open source? | Seguridad |
| 68 | Anexo 3 | ¿Los costos de licencias, certificados, herramientas de monitoreo, WAF, backup, escaneo y pentest deben incluirse dentro del precio fijo? | Costos |
| 69 | Anexo 3 | ¿El costo de garantias bancarias/aseguradoras debe ser asumido por el proveedor? | Costos |
| 70 | Anexo 3 | ¿Los impuestos locales, retenciones o costos bancarios deben incluirse en el precio neto USD? | Costos |
| 71 | Anexo 3 | ¿Como se evaluara la propuesta economica si PADF decide contratar solo algunos modulos? | Evaluacion economica |
| 72 | Anexo 3 | ¿El descuento por paquete completo se evaluara aunque PADF pueda adjudicar parcialmente? | Evaluacion economica |
| 73 | Anexo 2 5.2 / Anexo 3 | ¿Las funciones transversales deben cotizarse como modulo independiente, distribuirse por modulo o ambas? | Costos, alcance |
| 74 | Anexo 2 7.5 | Para modulos de Etapa II que entren en produccion despues de Etapa I, ¿como se definira la cobertura de infraestructura y soporte? | Soporte, costo |
| 75 | 3.6 | Si PADF modifica plazos o alcance durante el proceso, ¿se emitira adenda formal que prevalezca sobre la SdP original? | Control de cambios |

## Datos para completar antes de envio

| Campo | Valor |
| --- | --- |
| Empresa Participante | Justech SRL |
| Fecha de envio | TBD |
| Responsable revision interna | Bid Manager |
| Estado | Borrador interno |

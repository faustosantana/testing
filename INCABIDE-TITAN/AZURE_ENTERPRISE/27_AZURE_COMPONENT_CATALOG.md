# 27 — AZURE COMPONENT CATALOG

## Objetivo

Catalogar cada componente Azure de la arquitectura objetivo, con objetivo, justificacion, dependencias, ventajas, riesgos, alternativas y criticidad.

| Componente | Objetivo | Justificacion | Dependencias | Ventajas | Riesgos | Alternativas | Criticidad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Microsoft Entra ID | Identidad, MFA, RBAC y acceso administrativo. | RFP exige IAM, MFA y minimo privilegio. | Tenant definido. | Control centralizado, Conditional Access. | Tenant no definido. | Usuarios locales SGB para app, no ideal para admin Azure. | Critica |
| Azure Virtual Network | Aislar recursos y controlar trafico. | RFP exige infraestructura aislada con subredes. | Region, CIDR. | Segmentacion y control. | CIDR mal definido. | Red plana no recomendada. | Critica |
| Subredes | Separar App Gateway, Container Apps, Private Endpoints, Management y Firewall. | Reduce superficie de ataque. | VNet. | Control granular. | Complejidad. | Subred unica no recomendada. | Alta |
| Private Endpoints | Acceso privado a PostgreSQL, Storage y Key Vault. | Evita exposicion publica de datos. | DNS privado, VNet. | Seguridad y cumplimiento. | Configuracion DNS. | Service endpoints. | Alta |
| Azure Firewall | Control de trafico centralizado. | RFP exige firewall personalizable. | Subred dedicada, rutas. | Logging y reglas centralizadas. | Costo/operacion. | NSG-only para menor alcance. | Alta |
| NSG | Control por subred. | Reglas IP/puerto. | Subredes. | Microsegmentacion. | Reglas inconsistentes. | Firewall central. | Alta |
| Azure Front Door WAF | Edge, TLS, proteccion web y entrada global. | WAF OWASP Top 10 y publicacion segura. | DNS/TLS, origin. | Performance y seguridad perimetral. | Puede ser excesivo si alcance es regional simple. | Application Gateway WAF solo. | Alta |
| Application Gateway WAF | WAF regional y enrutamiento a app interna. | Capa regional de proteccion y control. | Subred, certificados, backend. | Defensa en profundidad. | Doble WAF puede requerir afinacion. | Front Door WAF solo. | Alta |
| Azure Container Apps | Ejecutar contenedores SGB gestionados. | RFP permite VM o servicio gestionado para Docker. | ACR, VNet, identidad. | Menor operacion que VM/AKS. | Aprobacion PADF/INCABIDE pendiente. | VM Docker, App Service, AKS. | Alta |
| Azure Container Registry | Guardar imagenes SGB privadas. | Control de imagenes y releases. | CI/CD, identidad. | Versionado y seguridad. | Imagenes vulnerables si no se escanean. | Registry externo. | Media |
| Azure Database for PostgreSQL Flexible Server | Base de datos gestionada PostgreSQL. | PostgreSQL 14+ preferido con PostGIS/unaccent. | Region, red privada, version/extensiones. | Backups, HA posible, menor operacion. | Compatibilidad exacta del codigo pendiente. | PostgreSQL en VM. | Critica |
| PostGIS | Datos geoespaciales. | RFP depende de geolocalizacion. | PostgreSQL compatible. | Soporte GIS. | Version/extensiones a validar. | Motor alternativo aprobado. | Alta |
| unaccent | Busqueda sin distincion de acentos. | RFP indica dependencia funcional. | PostgreSQL compatible. | Mejor busqueda en espanol. | Compatibilidad a validar. | Funcion equivalente aprobada. | Alta |
| Azure Blob Storage | Almacenar documentos y multimedia. | RFP exige almacenamiento de medios. | Private Endpoint, RBAC. | Escalable, cifrado. | Volumen desconocido. | Azure Files, no ideal para objetos. | Alta |
| Azure Key Vault | Secretos, llaves y certificados. | RFP exige vault/KMS/HSM y no credenciales en codigo. | Entra ID, Managed Identity. | Seguridad y auditoria. | Permisos mal configurados. | Variables de entorno sin vault no recomendadas. | Critica |
| Managed Identity | Acceso sin secretos estaticos. | Reduce credenciales. | Entra ID, soporte del servicio. | Menor riesgo operacional. | Compatibilidad app a validar. | Service principal con rotacion. | Alta |
| Azure Monitor | Metricas, alertas y salud. | RFP exige monitoreo en tiempo real. | Recursos instrumentados. | Alertas nativas. | Ruido si no se ajusta. | Herramienta externa. | Alta |
| Application Insights | Telemetria de aplicacion y API. | Diagnostico y observabilidad. | Instrumentacion Django. | Trazas y errores. | Requiere integracion. | Logs basicos. | Media |
| Log Analytics | Centralizar logs y consultas. | Auditoria y seguridad. | Workspace, retencion. | Consultas y alertas. | Costos por ingesta/retencion. | SIEM externo. | Alta |
| Microsoft Defender for Cloud | Postura, recomendaciones y seguridad cloud. | Refuerza escaneos y hardening. | Suscripcion/planes. | Visibilidad de riesgos. | Planes/costo pendiente. | Escaneos terceros. | Alta |
| Backup / Recovery | Restaurar datos y continuidad. | RFP exige backups cifrados y DRP. | RPO/RTO, politicas. | Resiliencia. | Restore no probado. | Backups manuales no recomendados. | Critica |
| VPN Gateway / Bastion | Acceso administrativo seguro. | RFP exige VPN para administracion. | VNet, identidad. | Evita puertos admin publicos. | Modalidad pendiente. | Allowlist temporal, no ideal. | Alta |
| DNS | Dominio institucional. | RFP exige dominio personalizado. | Control dominio INCABIDE. | Acceso formal y confiable. | Dependencia externa. | Dominio temporal solo para pruebas. | Critica |
| TLS | Cifrado en transito. | RFP exige TLS/HTTPS. | Certificado/DNS. | Seguridad y confianza. | Renovacion/cadena certificados. | Certificado gestionado si aplica. | Critica |
| Azure Policy | Gobierno y cumplimiento. | Previene configuraciones inseguras. | Suscripcion. | Control preventivo. | Politicas demasiado restrictivas. | Revision manual. | Media |
| Tags / Resource Groups | Gobierno, costo y operacion. | Orden Enterprise. | Convencion aprobada. | Trazabilidad. | Inconsistencia. | Gestion manual sin tags. | Media |

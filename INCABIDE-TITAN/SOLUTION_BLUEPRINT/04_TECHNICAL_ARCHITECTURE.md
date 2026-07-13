# 04 — TECHNICAL ARCHITECTURE

## Base tecnologica

El SGB parte de una aplicacion web en Django/Python con PostgreSQL 14+, PostGIS y unaccent. La arquitectura tecnica debe preservar la funcionalidad existente, modernizar la operacion en nube y preparar la evolucion modular.

## Componentes tecnicos

| Componente | Funcion |
| --- | --- |
| Django Application | Aplicacion principal, modulos existentes y nuevos dominios funcionales. |
| API Layer | Exposicion controlada de servicios para INCABIDE e integraciones. |
| PostgreSQL/PostGIS | Persistencia transaccional, busquedas sin acento y datos geoespaciales. |
| Media Storage | Archivos, documentos, imagenes, videos y evidencias. |
| Reverse Proxy | Entrada HTTP/S, terminacion o encaminamiento seguro segun diseno final. |
| Background Jobs | Tareas programadas, notificaciones, reportes, imports y backups logicos. |
| Observability Agents | Logs, metricas, trazas y eventos de seguridad. |
| Secret Management | Variables sensibles y credenciales fuera del codigo. |

## Patron de aplicacion

```text
Web UI
  -> Django views / templates / frontend components
  -> Business services
  -> Domain modules
  -> ORM / data access
  -> PostgreSQL / media storage
```

## Patron API

```text
External/Internal Consumer
  -> Secure API endpoint
  -> Authentication / authorization
  -> API version
  -> Domain service
  -> Audit event
  -> Response
```

## Modulos tecnicos

| Modulo | Consideracion tecnica |
| --- | --- |
| Registro Activos | Validacion de unicidad, catalogos, QR, ubicacion y multimedia. |
| Contratos Clientes | Alertas, documentos, pagos, estados y depreciacion. |
| Subasta Ventas | Integracion con sistema existente y conciliacion. |
| Descargo Donaciones | Workflows, evidencia legal y auditoria. |
| Multilenguaje | Internacionalizacion, archivos de traduccion y localizacion. |
| Seguridad Avanzada | RBAC por modulo/accion, MFA/2FA, auditoria. |
| Reportes | Exportaciones, graficos y analisis posterior. |

## Refactorizacion cloud-ready

La adaptacion tecnica debe contemplar:

- eliminar secretos y configuraciones sensibles del codigo;
- mover configuracion a variables de entorno o vault;
- adaptar archivos y documentos a almacenamiento cloud;
- revisar dependencias y versiones;
- asegurar compatibilidad con contenedores;
- validar generacion de reportes en entorno cloud;
- validar geolocalizacion con servicios aprobados;
- preparar logging estructurado.

## Contenerizacion

La solucion debe generar:

- Dockerfile para aplicacion;
- Docker Compose para entorno orquestado cuando aplique;
- configuracion de proxy inverso;
- variables por ambiente;
- health checks;
- estrategia de build reproducible.

## Calidad tecnica

| Control | Aplicacion |
| --- | --- |
| Static analysis | Revisar calidad, vulnerabilidades y secretos. |
| Dependency scanning | Detectar dependencias vulnerables o licencias no compatibles. |
| Unit / integration tests | Validar servicios y flujos criticos. |
| UAT evidence | Evidencia funcional por modulo. |
| Code review | Control de cambios antes de despliegue. |
| SBOM | Inventario de librerias y licencias cuando se requiera. |

## Restricciones

No se define en este documento la topologia final de Azure, SKUs, capacidad, costos ni cronograma de despliegue.

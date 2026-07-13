# 08 — DATA ARCHITECTURE

## Objetivo

Definir el modelo conceptual de datos para que el SGB soporte bienes, procesos, documentos, geolocalizacion, contratos, disposicion, auditoria y reportes.

## Dominios de datos

| Dominio | Entidades conceptuales |
| --- | --- |
| Activos | Bien, categoria, subcategoria, identificador, estado, valor, seguro, mantenimiento. |
| Ubicacion | Provincia, ciudad, municipio, almacen, pasillo, seccion, referencia catastral, coordenadas. |
| Origen | Entidad remitente, caso, imputado, fiscalia remitente, tipo penal. |
| Documentos | Archivo, tipo, confidencialidad, metadata, version, relacion con activo. |
| Contratos | Cliente, contrato, condiciones, pagos, vencimientos, estados de cuenta. |
| Disposicion | Venta, subasta, donacion, destruccion, devolucion, actas, aprobaciones. |
| Seguridad | Usuario, rol, permiso, sesion, MFA, auditoria. |
| Operacion | Logs, alertas, backups, eventos, health checks. |
| Integracion | API events, imports, exports, sistemas externos. |

## Base de datos

PostgreSQL 14+ es el motor preferido por el RFP, con:

- PostGIS para datos geoespaciales;
- unaccent para busquedas sin distincion de acentos;
- integridad referencial;
- indices para busqueda y reporteria;
- auditoria de cambios relevantes;
- respaldos cifrados.

## Gobierno de datos

| Control | Aplicacion |
| --- | --- |
| Catalogos maestros | Provincias, municipios, entidades remitentes, categorias, subcategorias. |
| Calidad de datos | Validaciones, listas desplegables, unicidad y reglas de formato. |
| Trazabilidad | Auditoria de creacion, modificacion, aprobacion y disposicion. |
| Clasificacion | Niveles de confidencialidad por documento y dato sensible. |
| Retencion | Politicas por definir con INCABIDE. |
| Minimizacion | Capturar solo datos necesarios para el proceso. |

## Modelo multimedia

Los archivos multimedia deben almacenarse fuera de la base transaccional, con metadata en PostgreSQL:

- tipo de archivo;
- propietario logico;
- activo relacionado;
- fecha de carga;
- usuario;
- nivel de confidencialidad;
- hash o control de integridad;
- estado de revision;
- reglas de acceso.

## Datos geoespaciales

La solucion debe soportar:

- referencia catastral o direccion para inmuebles;
- coordenadas cuando aplique;
- catalogo de provincias/municipios;
- mapas de Republica Dominicana;
- busqueda y filtros geograficos;
- sincronizacion de ubicacion cuando se defina fuente.

## Auditoria de datos

Eventos auditables:

- creacion y edicion de activos;
- cambios de ubicacion;
- cambios de categoria;
- carga y descarga de archivos;
- cambios de permisos;
- exportaciones masivas;
- aprobaciones;
- eliminaciones logicas;
- accesos administrativos.

## Migracion e importacion

El diseno debe permitir importacion/exportacion segura en CSV, Excel, PDF cuando aplique, con:

- mapeo de columnas;
- validacion previa;
- reporte de errores;
- control de duplicados;
- auditoria;
- rollback logico;
- aprobacion antes de carga final.

## Decisiones pendientes

- volumen de base de datos;
- volumen y tamano multimedia;
- calidad de datos actuales;
- historico a migrar;
- catalogos oficiales;
- retencion legal;
- criterios de analisis predictivo.

# 12 — DATA MIGRATION

## Enfoque de datos

El SGB debe operar sobre informacion estructurada, documentos, evidencia multimedia y datos geoespaciales. La RFP identifica PostgreSQL 14+ con PostGIS y unaccent como base tecnologica del sistema, y solicita funciones de importacion/exportacion masiva, documentacion multimedia, geolocalizacion y reportes para toma de decisiones. Sin embargo, la RFP no define de forma explicita una migracion historica completa ni proporciona volumen de datos, calidad de datos, estructura de fuentes actuales o cantidad de archivos existentes.

Por esa razon, la propuesta tecnica adopta un enfoque responsable: contempla una estrategia de migracion condicionada a la confirmacion de fuentes, volumen, calidad y alcance por parte de PADF/INCABIDE. No se debe comprometer una migracion historica completa sin informacion suficiente.

## Estrategia de migracion condicionada

Si PADF/INCABIDE confirma la existencia de datos a migrar, el proceso debera ejecutarse en fases:

1. inventario de fuentes de datos;
2. perfilamiento de calidad;
3. identificacion de catalogos maestros;
4. mapeo de campos hacia el modelo del SGB;
5. reglas de transformacion y limpieza;
6. carga de prueba;
7. reporte de errores;
8. validacion funcional;
9. carga controlada;
10. reconciliacion y aprobacion.

## Gobierno de datos

La solucion debe usar catalogos controlados para provincias, municipios, entidades remitentes, categorias, subcategorias, estados, roles y otros valores estructurados. Esto reduce errores de digitacion, mejora busqueda y soporta reportes confiables.

Los datos sensibles deben gestionarse bajo principios de minimizacion, control de acceso, auditoria y confidencialidad. Los documentos y multimedia deben contar con metadatos, clasificacion, relacion con expediente, control de permisos y trazabilidad de carga o descarga.

## Importacion y exportacion

La RFP solicita compatibilidad con importacion/exportacion masiva en formatos como CSV, Excel y PDF, con validacion, mapeo, manejo de errores, transferencia segura y auditoria. La propuesta debe contemplar mecanismos para:

- validar formatos;
- detectar errores;
- controlar duplicados;
- registrar usuario y fecha;
- auditar exportaciones;
- aplicar permisos;
- generar reportes de carga.

## Geolocalizacion

La plataforma debe permitir representar ubicacion de activos en territorio dominicano, ya sea mediante provincia, municipio, referencia catastral, direccion o coordenadas, segun corresponda al tipo de bien. El proveedor de mapas, licencias, precision y fuentes oficiales deben validarse antes de comprometer una implementacion final.

## Trazabilidad RFP

Este capitulo cubre FUNC-001 a FUNC-021, FUNC-151 a FUNC-191, SEC-003 a SEC-009, DOC-009, DOC-015 y requisitos de importacion/exportacion, multimedia y geolocalizacion.

## Informacion pendiente de Justech

Justech debe confirmar:

- experiencia real en migracion de datos;
- herramientas de migracion disponibles;
- equipo responsable de datos;
- experiencia en PostgreSQL/PostGIS;
- capacidad de manejar importaciones/exportaciones seguras.

## Informacion pendiente de PADF/INCABIDE

Se requiere confirmar:

- existencia de base de datos productiva actual;
- volumen de registros;
- volumen y tipo de documentos/multimedia;
- catalogos oficiales;
- calidad de datos;
- alcance de migracion historica;
- responsables de validacion de datos.

# 12 — DATA MIGRATION

## Objetivo

Definir el enfoque de migracion o carga de datos, manteniendo como pendiente cualquier alcance no especificado por la RFP.

## Enfoque

La RFP no define explicitamente volumen ni existencia de datos historicos a migrar. Por tanto, la propuesta debe contemplar una estrategia condicionada:

1. inventario de fuentes;
2. perfilamiento de datos;
3. mapeo al modelo SGB;
4. validacion de calidad;
5. carga de prueba;
6. validacion funcional;
7. carga controlada;
8. reconciliacion;
9. evidencia de aprobacion.

## Relacion con la RFP

La RFP exige importacion/exportacion masiva, documentacion multimedia, geolocalizacion, datos de activos y almacenamiento seguro. No define migracion historica completa.

## Requisitos cubiertos

- FUNC-170 a FUNC-178.
- FUNC-151 a FUNC-160.
- FUNC-001 a FUNC-021.
- SEC-003 a SEC-009.

## Evidencias necesarias

- Inventario de datos.
- Mapeo de campos.
- Resultado de carga de prueba.
- Reporte de errores.
- Validacion INCABIDE.

## Dependencias

- Confirmacion de existencia de base actual.
- Volumen de registros y archivos.
- Calidad de datos.
- Catalogos oficiales.

## Pendientes de informacion de Justech

- Experiencia real en migraciones.
- Herramientas de migracion usadas.
- Equipo o rol responsable de datos.

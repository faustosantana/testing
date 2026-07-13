# 02 — THE PROBLEM

## Problema institucional

La RFP describe un SGB existente desarrollado en Django/Python con PostgreSQL, entregado en su estado actual, con limitaciones que deben ser abordadas:

- modulos potencialmente incompletos;
- falta de preparacion para infraestructura cloud moderna;
- necesidad de personalizacion visual, terminologica e institucional;
- necesidad de modulos adicionales para la operacion completa de INCABIDE.

## Problema operativo

La administracion de bienes incautados, decomisados o en extincion requiere control sobre:

- registro;
- clasificacion;
- ubicacion;
- documentos;
- movimientos;
- contratos;
- subastas;
- donaciones;
- devoluciones;
- destruccion;
- auditoria;
- reportes.

Sin una plataforma moderna, estos procesos pueden volverse fragmentados, dificiles de auditar y lentos para la toma de decisiones.

## Problema tecnico

El sistema actual debe adaptarse para:

- ejecutar en Microsoft Azure;
- operar con contenedores;
- manejar configuraciones sensibles fuera del codigo;
- mantener PostgreSQL/PostGIS/unaccent o equivalentes;
- exponer una API funcional;
- cumplir controles de seguridad;
- generar evidencias de aceptacion.

## Problema de confianza

La informacion del SGB esta vinculada a datos sensibles y procesos penales. Por tanto, el problema no es solo funcional: es de confianza, seguridad, trazabilidad y responsabilidad institucional.

## Problema de adopcion

El sistema debe ser comprendido por perfiles distintos: direccion, operadores, auditores, equipo tecnico y administradores. Si la experiencia es compleja, la adopcion se reduce y los errores aumentan.

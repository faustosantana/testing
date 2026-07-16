# 06 — IMPLEMENTATION APPROACH

## Enfoque de ejecucion

La implementacion propuesta se organiza para reducir incertidumbre tecnica, controlar riesgos contractuales y producir evidencias verificables por hito. El enfoque responde a la estructura de la RFP: una primera etapa orientada a adaptar y desplegar el SGB existente, y una segunda etapa orientada a desarrollar modulos priorizados por INCABIDE.

La ejecucion debe partir de un diagnostico formal del codigo fuente. Dado que el codigo se entregara al adjudicatario en su estado actual, no seria responsable asumir que la aplicacion esta lista para nube, que todas las dependencias son compatibles o que todos los modulos tienen el mismo nivel de madurez. Por ello, el primer bloque de trabajo debe producir un informe de compatibilidad, inventario de dependencias, identificacion de incompatibilidades, acciones de correccion y resultado de prueba de ejecucion.

## Etapa I: adaptacion y puesta en produccion

La Etapa I se ejecuta como una secuencia de estabilizacion, personalizacion, infraestructura, despliegue y transferencia:

1. **Analisis del codigo fuente y dependencias.** Revision del repositorio, paquetes, configuraciones, librerias, patrones de acceso a archivos, reportes, geolocalizacion y componentes que puedan afectar el despliegue cloud.
2. **Correccion y refactorizacion cloud-ready.** Ajuste de dependencias, separacion de configuraciones sensibles, uso de variables de entorno o servicios seguros, y adaptacion de funcionalidades afectadas por infraestructura.
3. **Personalizacion institucional.** Aplicacion de identidad visual, logotipos, paleta y terminologia dominicana indicada por INCABIDE, con validacion legal de terminos antes de implementacion.
4. **Implementacion Azure.** Provision conceptual de computo, base de datos, almacenamiento, red, seguridad, monitoreo y backups, de acuerdo con las decisiones validadas.
5. **Contenerizacion y produccion.** Preparacion de artefactos de contenedor, proxy inverso cuando aplique, despliegue de aplicacion, base de datos, almacenamiento, dominio personalizado y TLS.
6. **API funcional.** Habilitacion de una API del SGB para INCABIDE, separando claramente la API base de la interconexion con PGR, que depende de aprobacion externa.
7. **Documentacion y transferencia.** Entrega de arquitectura implementada, variables de entorno, procedimientos de contenedores, restauracion de respaldos, capacitacion y accesos completos.
8. **Soporte post-despliegue.** Activacion de canales de soporte, tiempos de respuesta, escalamiento y registro de incidentes.

## Etapa II: desarrollo modular

La Etapa II debe ejecutarse modulo por modulo, en funcion de prioridades de INCABIDE. Cada modulo debe iniciar con disenos o prototipos navegables validados, continuar con especificacion funcional, desarrollo, pruebas, UAT, manual de usuario y acta de aceptacion parcial. Esta secuencia permite controlar alcance, calidad y pagos proporcionales sin comprometer la aceptacion final del proyecto.

## Gobierno de calidad

Cada entregable debe ser validado contra tres criterios:

- cumplimiento del requisito RFP;
- evidencia verificable;
- criterio de no conformidad de INCABIDE TITAN: no basta con que funcione; debe ser usable, coherente, consistente, seguro, respetar permisos y no introducir duplicidad ni deuda tecnica evidente.

Despues de cada correccion se debe revalidar pantalla, flujo, modulo, regresiones y oportunidades de mejora.

## Trazabilidad RFP

Este capitulo cubre DOC-006, DOC-007, TEC-013 a TEC-026, QA-001 a QA-029, CAP-001 a CAP-004, SUP-001 a SUP-008 y FUNC-GEN-001 a FUNC-GEN-010.

## Informacion pendiente de Justech

Justech debe confirmar:

- metodologia propia de implementacion;
- roles y responsables reales;
- herramientas de gestion, QA y DevSecOps;
- capacidad de soporte;
- plantillas de entregables;
- equipo asignado y disponibilidad.

# 10 — DEVSECOPS

## Enfoque DevSecOps

El enfoque DevSecOps tiene como objetivo asegurar que cada cambio al SGB sea versionado, revisado, probado, escaneado, desplegado de forma controlada y documentado con evidencias. Dado que la RFP exige codigo fuente en repositorio Git, contenedores, seguridad, ausencia de credenciales en codigo y evidencias de despliegue, el proceso de entrega debe integrar controles tecnicos desde el inicio.

## Flujo de entrega

El flujo recomendado para cambios y releases es:

1. gestion de codigo en repositorio Git;
2. rama o unidad de trabajo controlada;
3. revision tecnica;
4. analisis de dependencias;
5. escaneo de secretos;
6. analisis de vulnerabilidades;
7. construccion de imagen de contenedor;
8. escaneo de imagen;
9. despliegue en ambiente no productivo;
10. pruebas funcionales y de seguridad;
11. aprobacion;
12. despliegue productivo controlado;
13. monitoreo y registro de evidencias.

## Control de configuracion

Las configuraciones sensibles no deben residir en el codigo fuente ni en archivos versionados. La solucion debe usar variables de entorno, vault de secretos o mecanismos equivalentes aprobados para credenciales, llaves, tokens y cadenas de conexion. Este control responde directamente al requisito de gestion segura de credenciales de la RFP.

## Seguridad de dependencias

El SGB debe mantener inventario de librerias y licencias open source. Las dependencias incompatibles o vulnerables identificadas durante el diagnostico deben actualizarse, reemplazarse o adaptarse. No deben incorporarse componentes con licencias incompatibles con los fines del proyecto.

## Evidencias DevSecOps

Las evidencias esperadas incluyen:

- historial de commits;
- registro de revisiones;
- inventario de dependencias;
- resultados de escaneos;
- evidencias de build;
- tags o versiones;
- notas de release;
- evidencias de despliegue;
- plan de rollback cuando aplique.

## Trazabilidad RFP

Este capitulo cubre TEC-019 a TEC-023, SEC-019, SEC-021, SEC-024, SEC-029, SEC-034, DOC-017 y requisitos de entrega de codigo en Git.

## Informacion pendiente de Justech

Justech debe confirmar:

- herramienta de repositorio y flujo de ramas;
- herramientas CI/CD;
- herramientas SAST/DAST/secret scan;
- herramientas de escaneo de contenedores;
- capacidad de generar SBOM;
- politicas internas de revision y aprobacion de cambios.

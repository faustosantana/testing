# 10 — DEVSECOPS

## Objetivo

Definir el enfoque DevSecOps para entregar cambios seguros, versionados, verificables y con evidencias.

## Enfoque

El enfoque DevSecOps contempla:

- control de versiones;
- revision de codigo;
- escaneo de secretos;
- analisis de dependencias;
- analisis de vulnerabilidades;
- build de imagenes;
- escaneo de contenedores;
- despliegues controlados;
- evidencias por release;
- rollback documentado.

## Relacion con la RFP

La RFP exige codigo fuente entregado en Git, Dockerfile/Docker Compose, escaneos de seguridad, ausencia de credenciales en codigo, evidencias de despliegue y documentacion tecnica.

## Requisitos cubiertos

- TEC-019 a TEC-023.
- SEC-019, SEC-021, SEC-024, SEC-029, SEC-034.
- QA-010, QA-011, QA-013.
- DOC-006/DOC-017.

## Evidencias necesarias

- Historial de commits.
- Resultados de escaneo.
- Inventario de dependencias.
- Evidencia de build/despliegue.
- Notas de version.

## Dependencias

- Repositorio Git designado por INCABIDE.
- Herramienta CI/CD aprobada.
- Acceso a infraestructura.

## Pendientes de informacion de Justech

- Plataforma DevSecOps usada.
- Politicas de ramas y revisiones.
- Herramientas SAST/DAST/secret scan.
- Capacidad de generar SBOM si se requiere.

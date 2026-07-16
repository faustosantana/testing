# 07 — DEVSECOPS

## Objetivo

Establecer un modelo de entrega seguro y repetible para adaptar, contenerizar, desplegar y evolucionar el SGB, reduciendo riesgos de calidad, seguridad y aceptacion.

## Pipeline conceptual

```text
Commit
  -> Code review
  -> Static analysis
  -> Dependency/license scan
  -> Secret scan
  -> Unit tests
  -> Build container image
  -> Container scan
  -> Deploy to QA/UAT
  -> Functional/UAT evidence
  -> Security evidence
  -> Production release approval
```

## Controles por etapa

| Etapa | Control |
| --- | --- |
| Desarrollo | Rama controlada, revision de codigo, estandares Django/Python. |
| Build | Imagen reproducible, variables externas, no secretos. |
| Seguridad | SAST, dependency scan, secret scan, container scan. |
| Pruebas | Unitarias, integracion, funcionales y UAT. |
| Despliegue | Aprobacion, version, rollback y evidencia. |
| Operacion | Monitoreo, alertas, logs y health checks. |

## Gestion de ramas

- rama principal protegida;
- ramas por feature/modulo;
- pull requests con revision;
- versionado de releases;
- tags por hito aceptado;
- historial de commits entregable a INCABIDE.

## Evidencia DevSecOps

- reporte de pruebas;
- reporte de escaneo;
- lista de dependencias;
- inventario de licencias;
- resultados de build;
- evidencias de despliegue;
- acta de aprobacion;
- notas de version.

## Gestion de configuracion

La configuracion sensible no debe estar en archivos versionados. Se debe usar:

- variables de entorno;
- vault de secretos;
- plantillas de configuracion;
- separacion por ambiente;
- rotacion de credenciales;
- auditoria de cambios.

## Release management

Cada release debe incluir:

1. version;
2. alcance;
3. requisitos cubiertos;
4. cambios de base de datos;
5. riesgos conocidos;
6. plan de rollback;
7. evidencias de pruebas;
8. aprobacion de despliegue.

## Seguridad de dependencias

- usar solo componentes open source con licencias OSI compatibles;
- documentar librerias;
- revisar vulnerabilidades;
- definir plan de remediacion;
- evitar dependencias abandonadas o no mantenidas.

## Criterio de aceptacion DevSecOps

No promover a produccion si existen vulnerabilidades abiertas de severidad Alta o Critica, o si faltan evidencias de MFA, TLS, backup restaurable y ausencia de credenciales en codigo.

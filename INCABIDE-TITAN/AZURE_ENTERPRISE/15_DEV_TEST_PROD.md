# 15 — DEV TEST PROD

## Objetivo

Definir separacion conceptual de ambientes para desarrollo, pruebas/UAT y produccion.

## Ambientes

| Ambiente | Objetivo | Criticidad |
| --- | --- | --- |
| Dev | Adaptacion, refactorizacion y pruebas internas. | Media |
| Test/QA | Validacion funcional y seguridad previa. | Alta |
| UAT | Validacion PADF/INCABIDE. | Alta |
| Prod | Operacion institucional. | Critica |

## Reglas

- secretos separados por ambiente;
- base de datos separada o aislada;
- datos productivos protegidos;
- despliegues promovidos por aprobacion;
- monitoreo minimo en todos los ambientes;
- controles de seguridad reforzados en produccion.

## Pendiente de validacion

La RFP no define ambientes requeridos. Cantidad y permanencia de ambientes es `PENDIENTE DE VALIDACION`.

## Riesgos

- mezclar datos productivos con pruebas;
- costos de ambientes no previstos;
- UAT sin usuarios disponibles;
- diferencias entre ambientes.

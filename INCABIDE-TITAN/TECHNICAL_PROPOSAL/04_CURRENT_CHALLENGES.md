# 04 — CURRENT CHALLENGES

## Objetivo

Identificar los desafios actuales del SGB y del proyecto segun la RFP, sin introducir supuestos no documentados.

## Desafios identificados

| Desafio | Fuente / relacion RFP | Implicacion tecnica |
| --- | --- | --- |
| Codigo fuente entregado "tal cual" | SGB actual descrito en RFP | Requiere diagnostico inicial robusto. |
| Sistema no preparado para nube moderna | Limitacion indicada por RFP | Requiere refactorizacion cloud-ready. |
| Modulos potencialmente incompletos | Subastas mencionado como particular | Requiere analisis de alcance posterior. |
| Personalizacion institucional | Identidad visual y terminologia INCABIDE | Requiere validacion legal/visual. |
| Azure obligatorio | RFP exige Microsoft Azure | Arquitectura debe ser Azure-native. |
| Seguridad reforzada | Datos sensibles y Ley 172-13 | Requiere controles, evidencias y pentest. |
| API obligatoria | API funcional SGB | Alcance minimo pendiente de aclaracion. |
| Soporte por un ano | RFP exige SLA y soporte | Modelo operativo formal requerido. |
| Infraestructura por un ano | Proveedor asume costo cloud 12 meses | Requiere dimensionamiento validado. |

## Relacion con la RFP

Se basa en secciones 2.2, 4.10, Anexo 2 fases I-IV, requisitos de seguridad 4.1/4.3 y soporte 4.2.

## Requisitos cubiertos

- TEC-003 a TEC-018.
- AZ-001 a AZ-015.
- SEC-003 a SEC-038.
- SUP-001 a SUP-008.

## Evidencias necesarias

- Informe de compatibilidad.
- Inventario de dependencias.
- Evidencias de seguridad.
- Evidencias de despliegue.
- Plan de soporte.

## Dependencias

- Acceso al codigo fuente.
- Respuestas PADF a preguntas tecnicas.
- Insumos visuales de INCABIDE.

## Pendientes de informacion de Justech

- Herramientas internas de diagnostico.
- Procedimientos de QA propios.
- Politicas de seguridad propias.
- Capacidad de soporte fuera de horario.

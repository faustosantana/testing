# 19 — EMPTY STATES

## Objetivo

Los estados vacios deben orientar, no solo decir que no hay datos.

## Patrones

| Contexto | Mensaje | Accion |
| --- | --- | --- |
| Sin bienes | Aun no hay bienes registrados para este filtro. | Registrar bien / limpiar filtros. |
| Sin casos | No se encontraron casos. | Crear caso / ajustar busqueda. |
| Sin documentos | Este expediente no tiene documentos cargados. | Cargar documento. |
| Sin permisos | No tienes acceso a esta informacion. | Solicitar acceso. |
| Sin reportes | No hay reportes guardados. | Crear reporte. |
| Sin resultados mapa | No hay bienes en esta zona con los filtros aplicados. | Cambiar filtros. |

## Reglas

- explicar causa probable;
- ofrecer siguiente accion;
- no culpar al usuario;
- mantener tono institucional;
- no mostrar pantallas vacias sin contexto.

## Ejemplo de tono

"No hay bienes con estado Critico en esta provincia. Puedes ajustar los filtros o volver al resumen nacional."

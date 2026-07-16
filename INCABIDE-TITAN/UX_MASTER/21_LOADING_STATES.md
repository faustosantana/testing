# 21 — LOADING STATES

## Objetivo

Los estados de carga deben comunicar progreso y mantener confianza.

## Patrones

| Contexto | Patron |
| --- | --- |
| Dashboard | Skeleton cards y graficas. |
| Tabla | Skeleton rows. |
| Expediente | Header rapido + secciones cargando. |
| Mapa | Placeholder de mapa + contador cargando. |
| Exportacion | Progreso con opcion de seguir trabajando. |
| Carga archivo | Barra de progreso y validacion. |

## Reglas

- si carga dura menos de 1 segundo, usar skeleton sutil;
- si dura mas, indicar estado;
- nunca bloquear toda la aplicacion si no es necesario;
- permitir cancelar procesos largos cuando sea seguro;
- conservar datos previos mientras se actualizan.

## Microcopy

- "Cargando bienes..."
- "Preparando reporte..."
- "Validando archivo..."
- "Sincronizando mapa..."
- "Guardando borrador..."

## Estados largos

Para importaciones, exportaciones o reportes:

- mostrar progreso;
- permitir notificacion al finalizar;
- registrar auditoria;
- mostrar errores descargables.

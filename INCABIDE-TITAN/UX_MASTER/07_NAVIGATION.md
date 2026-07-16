# 07 — NAVIGATION

## Modelo de navegacion

Navegacion lateral fija con modulos, barra superior con busqueda global y alertas, breadcrumbs para contexto y panel derecho para detalles.

## Menu principal

| Seccion | Contenido |
| --- | --- |
| Inicio | Dashboard Ejecutivo u Operativo segun rol. |
| Casos | Registro de casos, imputados, estado procesal. |
| Bienes | Expedientes de bienes, inventario, QR, ubicacion. |
| Mapa | Vista geografica por provincia/municipio. |
| Contratos | Clientes, contratos, pagos, vencimientos. |
| Subastas | Lotes, procesos, resultados, conciliacion. |
| Descargo | Donaciones, devoluciones, destrucciones. |
| Reportes | Reportes, exportaciones, dashboards. |
| Auditoria | Eventos, accesos, cambios, exportaciones. |
| Documentos | Centro documental y multimedia. |
| Usuarios | Roles, permisos, MFA, actividad. |
| Configuracion | Catalogos, parametros, integraciones. |
| Soporte | Tickets, ayuda, capacitacion. |

## Busqueda global

Debe encontrar:

- numero de caso;
- codigo de bien;
- QR;
- propietario;
- provincia;
- contrato;
- documento;
- subasta;
- usuario;
- evento de auditoria.

## Breadcrumbs

Ejemplo:

```text
Bienes > Vehiculos > INC-2026-000123 > Cadena de custodia
```

## Command palette

Para usuarios avanzados:

- buscar bien;
- crear caso;
- registrar activo;
- exportar reporte;
- abrir mapa;
- ver alertas;
- abrir soporte.

## Navegacion por permisos

El menu debe ocultar o deshabilitar funciones no permitidas, mostrando mensajes claros cuando un usuario no tiene acceso.

## Atajos contextuales

Cada expediente debe ofrecer:

- ver timeline;
- ver documentos;
- ver auditoria;
- crear alerta;
- exportar;
- solicitar aprobacion;
- abrir soporte.

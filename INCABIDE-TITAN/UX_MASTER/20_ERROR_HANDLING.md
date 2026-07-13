# 20 — ERROR HANDLING

## Objetivo

Los errores deben ser comprensibles, accionables y seguros.

## Tipos de error

| Tipo | Ejemplo | Respuesta UX |
| --- | --- | --- |
| Validacion | Campo obligatorio faltante. | Mensaje junto al campo y resumen. |
| Permisos | Usuario intenta editar sin autorizacion. | Explicar permiso requerido. |
| Seguridad | MFA requerido. | Guiar activacion o contacto admin. |
| Sistema | API no responde. | Mensaje claro, reintentar, soporte. |
| Carga archivo | Formato no permitido. | Indicar formatos validos. |
| Exportacion | Datos sensibles. | Confirmacion y auditoria. |

## Mensajes

Mal:

```text
Error 500
```

Bien:

```text
No pudimos cargar el expediente. Intenta nuevamente o contacta soporte si el problema continua.
```

## Errores criticos

Deben incluir:

- impacto;
- estado del sistema;
- proxima accion;
- identificador de incidente;
- canal de soporte;
- hora.

## Prevencion

- validacion temprana;
- autoguardado;
- confirmaciones;
- permisos visibles;
- carga progresiva;
- deshabilitar acciones no disponibles.

# 18 — NOTIFICATION SYSTEM

## Objetivo

Notificaciones accionables, priorizadas y no invasivas.

## Canales

- in-app;
- correo;
- dashboard de alertas;
- telefono/WhatsApp para soporte segun procedimiento;
- digest diario o semanal.

## Tipos

| Tipo | Ejemplo | Prioridad |
| --- | --- | --- |
| Critica | Servicio caido, brecha, vencimiento legal. | Alta |
| Aprobacion | Bien pendiente de revision. | Media/Alta |
| Vencimiento | Contrato por vencer. | Media |
| Informativa | Reporte listo. | Baja |
| Seguridad | MFA pendiente, acceso fallido. | Alta |

## Anatomia

- titulo;
- descripcion breve;
- impacto;
- accion primaria;
- fecha/hora;
- estado;
- enlace a detalle.

## Reglas

- evitar ruido;
- agrupar notificaciones similares;
- permitir marcar como leida;
- conservar historial;
- auditar notificaciones sensibles;
- escalar criticas.

## Centro de notificaciones

Debe permitir filtrar por:

- prioridad;
- modulo;
- estado;
- fecha;
- responsable;
- tipo.

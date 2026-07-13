# 12 — SUPPORT MODEL

## Objetivo

Definir el modelo conceptual de soporte para el periodo post-despliegue exigido por la RFP.

## Alcance base

- soporte tecnico por 1 ano post-despliegue;
- canales de correo y telefono/WhatsApp;
- atencion durante horario habil;
- cobertura fuera de horario para incidentes criticos;
- procedimiento de escalamiento;
- evidencias de atencion.

## Clasificacion de incidentes

| Tipo | Definicion RFP | Respuesta maxima RFP |
| --- | --- | --- |
| Critico | Servicio completamente caido. | 1 hora |
| Mayor | Funcionalidad principal degradada. | 4 horas habiles |
| Menor | Problema no bloqueante. | 8 horas habiles |

## Flujo de soporte

```text
Reporte
  -> Registro de ticket
  -> Clasificacion
  -> Asignacion
  -> Diagnostico
  -> Resolucion / workaround
  -> Validacion
  -> Cierre
  -> Leccion aprendida si aplica
```

## Canales

- correo electronico;
- telefono o WhatsApp;
- portal de soporte como diferenciador complementario;
- canal de escalamiento para incidentes criticos.

## Niveles de soporte

| Nivel | Responsabilidad |
| --- | --- |
| Nivel 1 | Registro, clasificacion, seguimiento y comunicacion. |
| Nivel 2 | Diagnostico funcional/tecnico y correcciones menores. |
| Nivel 3 | Desarrollo, DevSecOps, infraestructura y seguridad. |
| Escalamiento | CTO/Arquitecto para incidentes criticos o recurrentes. |

## Evidencias de soporte

- ticket;
- fecha/hora de reporte;
- clasificacion;
- responsable;
- diagnostico;
- acciones ejecutadas;
- evidencia de resolucion;
- validacion del usuario;
- cierre;
- causa raiz cuando aplique.

## Reportes de soporte

- volumen por tipo de incidente;
- cumplimiento SLA;
- incidentes recurrentes;
- acciones preventivas;
- salud de plataforma;
- recomendaciones de mejora.

## Ambiguedad pendiente

La RFP estima aproximadamente 30 horas anuales, pero exige atencion de incidentes criticos fuera de horario sin establecer limite claro. Esta condicion debe aclararse con PADF antes de cerrar oferta economica y modelo contractual.

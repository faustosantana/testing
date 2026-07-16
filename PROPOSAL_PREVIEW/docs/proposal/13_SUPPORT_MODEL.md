# 13 — SUPPORT MODEL

## Enfoque de soporte

La RFP exige soporte tecnico por un ano post-despliegue, con canales definidos, tiempos maximos de respuesta y atencion de incidentes criticos fuera del horario habil cuando afecten continuidad operativa. La propuesta tecnica debe presentar un modelo de soporte claro, medible y alineado con los niveles de servicio definidos por PADF/INCABIDE.

## Clasificacion de incidentes

El modelo de soporte debe contemplar la clasificacion establecida por la RFP:

- **Incidente critico:** servicio completamente caido, con tiempo maximo de respuesta de 1 hora.
- **Incidente mayor:** funcionalidad principal degradada, con tiempo maximo de respuesta de 4 horas habiles.
- **Incidente menor:** problema no bloqueante, con tiempo maximo de respuesta de 8 horas habiles.

Los horarios habiles se consideran de lunes a viernes, de 8:00 a.m. a 5:00 p.m. hora de Republica Dominicana, salvo disposicion expresa distinta. Para incidentes criticos, la RFP exige disponibilidad fuera de horario habil cuando se afecte la continuidad operativa.

## Canales y escalamiento

El soporte debe incluir como minimo correo electronico y telefono o WhatsApp. Cada incidente debe registrarse con fecha, hora, tipo, responsable, diagnostico, accion ejecutada, evidencia de resolucion y cierre. Los incidentes criticos deben contar con ruta de escalamiento tecnico y responsable de comunicacion.

## Operacion durante soporte

El soporte no debe limitarse a responder incidentes. Debe apoyarse en monitoreo, revision de logs, alertas, evidencias de backup, controles de seguridad y reportes de salud cuando aplique. Esto permite anticipar problemas, reducir reincidencias y documentar acciones.

## Ambiguedad a aclarar

La RFP menciona un volumen estimado de aproximadamente 30 horas anuales de soporte, pero tambien exige atencion de incidentes criticos fuera de horario sin establecer claramente si esos eventos quedan limitados por dicho volumen. Esta condicion debe aclararse antes de cerrar compromisos operativos y economicos.

## Trazabilidad RFP

Este capitulo cubre SUP-001 a SUP-008, QA-020 y penalidades asociadas a incumplimiento de SLA.

## Informacion pendiente de Justech

Justech debe confirmar:

- capacidad de soporte fuera de horario;
- herramienta de tickets o mesa de ayuda;
- equipo de soporte;
- modelo de escalamiento;
- canales oficiales;
- experiencia real operando servicios post-despliegue.

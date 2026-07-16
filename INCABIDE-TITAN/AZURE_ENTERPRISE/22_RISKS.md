# 22 — RISKS

## Riesgos Azure

| ID | Riesgo | Impacto | Mitigacion |
| --- | --- | --- | --- |
| AZ-RSK-001 | Region no definida. | Cumplimiento, latencia y costo. | Validar con INCABIDE. |
| AZ-RSK-002 | Tenant/suscripcion no definidos. | Operacion y propiedad. | Decision temprana. |
| AZ-RSK-003 | Usuarios/concurrencia desconocidos. | Dimensionamiento incorrecto. | Preguntas PADF. |
| AZ-RSK-004 | Volumen multimedia desconocido. | Storage y costo. | Levantamiento de datos. |
| AZ-RSK-005 | RTO/RPO no definidos. | DR/HA sub o sobredimensionado. | Definir objetivos. |
| AZ-RSK-006 | Seguridad avanzada costosa. | Presupuesto. | Separar niveles obligatorios/opcionales. |
| AZ-RSK-007 | API sin alcance minimo. | Arquitectura y seguridad. | Definir endpoints y consumo. |
| AZ-RSK-008 | DNS institucional fuera de control del proveedor. | Hito 4. | Plan de dependencia. |
| AZ-RSK-009 | Private endpoints y DNS mal configurados. | Indisponibilidad. | Pruebas y runbooks. |
| AZ-RSK-010 | Pentest con hallazgos criticos. | Aceptacion y cierre. | Escaneos tempranos. |

## Riesgos contractuales asociados

- penalidades por atraso;
- penalidades por seguridad;
- rescision por brecha;
- soporte critico fuera de horario no delimitado;
- infraestructura por 1 ano sin datos suficientes.

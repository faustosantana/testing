# 14 — GOVERNANCE

## Objetivo

Definir gobierno Azure para controlar seguridad, costos, cambios, acceso y cumplimiento.

## Controles

| Control | Objetivo |
| --- | --- |
| Resource groups | Separar ambientes y dominios. |
| Naming convention | Trazabilidad operacional. |
| Tags | Costo, ambiente, propietario, criticidad. |
| RBAC | Minimo privilegio. |
| Policies | Restringir configuraciones inseguras. |
| Locks | Proteger recursos criticos. |
| Budgets/alerts | Monitorear consumo sin precios aqui. |
| Activity logs | Auditoria de cambios. |

## Etiquetas sugeridas

- Project: INCABIDE-TITAN.
- Environment: dev/test/prod.
- Owner.
- CostCenter: PENDIENTE DE VALIDACION.
- DataClassification.
- Criticality.

## Politicas recomendadas

- no recursos publicos no autorizados;
- requerir cifrado;
- restringir regiones aprobadas;
- exigir tags;
- impedir secretos fuera de Key Vault;
- monitorear configuraciones sin backup.

## Pendiente de validacion

- Tenant/suscripcion.
- Estandares de naming INCABIDE.
- Politicas institucionales.
- Aprobadores de cambios.

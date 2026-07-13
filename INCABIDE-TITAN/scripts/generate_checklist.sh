#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_FILE="${PROJECT_ROOT}/11_DELIVERY/QA-CHECKLIST-FINAL.md"

cat > "${OUTPUT_FILE}" <<'CHECKLIST'
# QA CHECKLIST FINAL — INCABIDE TITAN

Generado por: `scripts/generate_checklist.sh`

| ID | Control | Estado | Evidencia |
| --- | --- | --- | --- |
| FIN-001 | Estructura del repositorio validada | Pendiente | TBD |
| FIN-002 | README Enterprise actualizado | Pendiente | TBD |
| FIN-003 | PROJECT_PLAN.md actualizado | Pendiente | TBD |
| FIN-004 | TASKS.md actualizado | Pendiente | TBD |
| FIN-005 | RISKS.md actualizado | Pendiente | TBD |
| FIN-006 | War Room actualizado | Pendiente | TBD |
| FIN-007 | Documentos finales versionados | Pendiente | TBD |
| FIN-008 | Evidencias almacenadas | Pendiente | TBD |
| FIN-009 | Revision legal completada | Pendiente | TBD |
| FIN-010 | Paquete final listo para entrega | Pendiente | TBD |
| FIN-011 | Criterio de no conformidad aplicado: no se acepto solo porque funciona | Pendiente | TBD |
| FIN-012 | Usabilidad, coherencia, consistencia, permisos y UX validados | Pendiente | TBD |
| FIN-013 | Duplicidad, deuda tecnica evidente y confusion de usuario revisadas | Pendiente | TBD |
| FIN-014 | Alternativas superiores dentro del alcance evaluadas/documentadas | Pendiente | TBD |

## Observaciones

- Completar durante la fase de entrega.
CHECKLIST

echo "Checklist generated: ${OUTPUT_FILE}"

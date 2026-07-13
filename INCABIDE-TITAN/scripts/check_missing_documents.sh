#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

expected_documents=(
  "01_RFP/RFP-ORIGINAL.md"
  "02_REQUIREMENTS/RFP-MATRIZ-REQUISITOS.md"
  "02_REQUIREMENTS/RFP-MATRIZ-CUMPLIMIENTO.md"
  "03_PROPOSAL/TEC-OFERTA-TECNICA.md"
  "07_COSTS/ECO-OFERTA-ECONOMICA.md"
  "09_TEAM/EQP-MATRIZ-RACI.md"
  "10_LEGAL/LEG-CHECKLIST.md"
  "11_DELIVERY/QA-CHECKLIST-FINAL.md"
)

echo "Checking expected bid documents..."

missing_count=0
for document in "${expected_documents[@]}"; do
  if [[ -e "${PROJECT_ROOT}/${document}" ]]; then
    echo "OK ${document}"
  else
    echo "PENDING ${document}"
    missing_count=$((missing_count + 1))
  fi
done

echo "Pending documents: ${missing_count}"

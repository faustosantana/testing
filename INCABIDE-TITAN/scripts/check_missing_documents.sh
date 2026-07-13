#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

expected_documents=(
  "02_REQUIREMENTS/MASTER_COMPLIANCE_MATRIX.md"
  "02_REQUIREMENTS/RFP_REQUIREMENTS_ADMIN_LEGAL_COMMERCIAL.md"
  "02_REQUIREMENTS/RFP_REQUIREMENTS_TECH_AZURE_SECURITY_QA.md"
  "02_REQUIREMENTS/RFP_REQUIREMENTS_FUNCTIONAL_MODULES.md"
  "02_REQUIREMENTS/PROJECT_BACKLOG_RFP_5801_DRC3P.md"
  "02_REQUIREMENTS/RISK_GAP_AMBIGUITY_REGISTER.md"
  "02_REQUIREMENTS/PADF_QUESTIONS_ANEXO_4_DRAFT.md"
  "03_PROPOSAL/PROPOSAL_DOCUMENT_MAP.md"
  "04_AZURE/AZURE_REQUIREMENTS_AND_DECISIONS.md"
  "07_COSTS/COST_REQUIREMENTS_MAP.md"
  "09_TEAM/TEAM_REQUIREMENTS_GAP_ANALYSIS.md"
  "docs/EVALUATION_WIN_STRATEGY.md"
  "docs/EXECUTIVE_RFP_REPORT.md"
  "docs/NEXT_PHASE_READINESS.md"
  "99_EVIDENCE/RFP_EXTRACTION_EVIDENCE.md"
  "11_DELIVERY/QA-CHECKLIST-FINAL.md"
)

future_documents=(
  "01_RFP/RFP-ORIGINAL.md"
  "03_PROPOSAL/TEC-OFERTA-TECNICA.md"
  "07_COSTS/ECO-OFERTA-ECONOMICA.md"
  "09_TEAM/EQP-MATRIZ-RACI.md"
  "10_LEGAL/LEG-CHECKLIST.md"
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

echo "Checking future phase documents..."
future_count=0
for document in "${future_documents[@]}"; do
  if [[ -e "${PROJECT_ROOT}/${document}" ]]; then
    echo "OK ${document}"
  else
    echo "FUTURE ${document}"
    future_count=$((future_count + 1))
  fi
done

echo "Future phase documents not created by design: ${future_count}"

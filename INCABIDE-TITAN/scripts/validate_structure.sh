#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
missing=0

required_paths=(
  "00_WAR_ROOM"
  "00_WAR_ROOM/DASHBOARD.md"
  "01_RFP"
  "02_REQUIREMENTS"
  "03_PROPOSAL"
  "04_AZURE"
  "05_DEMO"
  "06_PRESENTATION"
  "07_COSTS"
  "08_REFERENCES"
  "09_TEAM"
  "10_LEGAL"
  "11_DELIVERY"
  "12_VIDEO"
  "13_WEBSITE"
  "99_EVIDENCE"
  "docs"
  "docs/STANDARDS.md"
  "docs/EVALUATION_WIN_STRATEGY.md"
  "docs/EXECUTIVE_RFP_REPORT.md"
  "docs/NEXT_PHASE_READINESS.md"
  "scripts"
  "templates"
  "assets"
  "README.md"
  "LICENSE"
  ".gitignore"
  "CHANGELOG.md"
  "PROJECT_PLAN.md"
  "TASKS.md"
  "RISKS.md"
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
  "12_VIDEO/README.md"
  "13_WEBSITE/README.md"
  "99_EVIDENCE/RFP_EXTRACTION_EVIDENCE.md"
  "templates/OFERTA_TECNICA.md"
  "templates/OFERTA_ECONOMICA.md"
  "templates/CRONOGRAMA.md"
  "templates/PLAN_QA.md"
  "templates/PLAN_SEGURIDAD.md"
  "templates/PLAN_INFRAESTRUCTURA.md"
  "templates/PLAN_MIGRACION.md"
  "templates/PLAN_CAPACITACION.md"
  "templates/ACTA_REUNION.md"
  "templates/CONTROL_CAMBIOS.md"
  "templates/CHECKLIST_FINAL.md"
)

echo "Validating INCABIDE TITAN structure..."

for path in "${required_paths[@]}"; do
  if [[ -e "${PROJECT_ROOT}/${path}" ]]; then
    echo "OK ${path}"
  else
    echo "MISSING ${path}"
    missing=1
  fi
done

if [[ "${missing}" -ne 0 ]]; then
  echo "Validation failed: missing required paths."
  exit 1
fi

echo "Validation passed."

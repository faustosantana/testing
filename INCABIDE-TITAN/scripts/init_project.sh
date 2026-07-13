#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

directories=(
  "00_WAR_ROOM"
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
  "AZURE_ENTERPRISE"
  "SOLUTION_BLUEPRINT"
  "SOLUTION_STORY"
  "UX_MASTER"
  "docs"
  "scripts"
  "templates"
  "assets/images"
  "assets/diagrams"
)

echo "Initializing INCABIDE TITAN Bid Center at: ${PROJECT_ROOT}"

for directory in "${directories[@]}"; do
  mkdir -p "${PROJECT_ROOT}/${directory}"
  echo "OK directory: ${directory}"
done

echo "Initialization completed."

#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "INCABIDE-TITAN" / "TECHNICAL_PROPOSAL"
DEST = ROOT / "PROPOSAL_PREVIEW" / "docs"
PROPOSAL_DEST = DEST / "proposal"
REF_DEST = DEST / "references"

PROPOSAL_FILES = [
    "01_COVER.md",
    "02_EXECUTIVE_SUMMARY.md",
    "03_UNDERSTANDING_OF_THE_PROJECT.md",
    "04_CURRENT_CHALLENGES.md",
    "05_PROPOSED_SOLUTION.md",
    "06_IMPLEMENTATION_APPROACH.md",
    "07_TECHNICAL_ARCHITECTURE_SUMMARY.md",
    "08_AZURE_STRATEGY.md",
    "09_SECURITY_AND_COMPLIANCE.md",
    "10_DEVSECOPS.md",
    "11_TESTING_AND_QA.md",
    "12_DATA_MIGRATION.md",
    "13_SUPPORT_MODEL.md",
    "14_TRAINING.md",
    "15_CHANGE_MANAGEMENT.md",
    "15_TEAM_AND_GOVERNANCE.md",
    "16_RISK_MANAGEMENT.md",
    "17_DELIVERABLES.md",
    "18_ASSUMPTIONS.md",
    "19_EXCLUSIONS.md",
    "20_APPENDIX_MAP.md",
    "21_PROJECT_EXECUTION_MODEL.md",
    "22_DEFINITIVE_TECHNICAL_ARCHITECTURE.md",
    "23_QUALITY_SECURITY_OPERATION.md",
]

SUPPORT_FILES = [
    "MASTER_TECHNICAL_PROPOSAL.md",
    "MASTER_TECHNICAL_PROPOSAL_OUTLINE.md",
    "COMMITTEE_REVIEW_SIMULATION.md",
    "WIN_STRATEGY.md",
    "COMPANY_PROFILE.md",
    "CORPORATE_CAPABILITIES.md",
    "RELEVANT_EXPERIENCE.md",
    "PARTNERS_AND_CERTIFICATIONS.md",
    "PROJECT_TEAM.md",
    "MISSING_JUSTECH_INFORMATION.md",
]

STATUS = {
    "01_COVER.md": "Listo con datos formales pendientes",
    "02_EXECUTIVE_SUMMARY.md": "Listo",
    "03_UNDERSTANDING_OF_THE_PROJECT.md": "Listo",
    "04_CURRENT_CHALLENGES.md": "Listo",
    "05_PROPOSED_SOLUTION.md": "Listo",
    "06_IMPLEMENTATION_APPROACH.md": "Listo",
    "07_TECHNICAL_ARCHITECTURE_SUMMARY.md": "Listo",
    "08_AZURE_STRATEGY.md": "Listo",
    "09_SECURITY_AND_COMPLIANCE.md": "Listo",
    "10_DEVSECOPS.md": "Listo",
    "11_TESTING_AND_QA.md": "Listo",
    "12_DATA_MIGRATION.md": "Listo",
    "13_SUPPORT_MODEL.md": "Listo",
    "14_TRAINING.md": "Listo",
    "15_CHANGE_MANAGEMENT.md": "Listo",
    "15_TEAM_AND_GOVERNANCE.md": "Listo; CVs oficiales pendientes",
    "16_RISK_MANAGEMENT.md": "Listo",
    "17_DELIVERABLES.md": "Listo",
    "18_ASSUMPTIONS.md": "Listo; decisiones PADF/INCABIDE pendientes",
    "19_EXCLUSIONS.md": "Pendiente revision final",
    "20_APPENDIX_MAP.md": "Pendiente revision final",
    "21_PROJECT_EXECUTION_MODEL.md": "Listo",
    "22_DEFINITIVE_TECHNICAL_ARCHITECTURE.md": "Listo",
    "23_QUALITY_SECURITY_OPERATION.md": "Listo",
}


def clean_markdown(text: str) -> str:
    """Remove accidental line-number artifacts from copied preview docs."""
    text = re.sub(r"(?m)^\s*\d+\|", "", text)
    text = re.sub(r"(?m)(^|\n)\s+\d+\|", r"\1", text)
    return text


def copy_doc(name: str) -> None:
    source = SOURCE / name
    target = PROPOSAL_DEST / name
    if not source.exists():
        raise FileNotFoundError(source)
    target.write_text(clean_markdown(source.read_text(encoding="utf-8")), encoding="utf-8")


def write_assets() -> None:
    (DEST / "assets").mkdir(parents=True, exist_ok=True)
    (DEST / "stylesheets").mkdir(parents=True, exist_ok=True)
    (DEST / "assets" / "justech-temp-logo.svg").write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" role="img" aria-label="Justech temporary logo">
<rect width="96" height="96" rx="20" fill="#0f172a"/>
<path d="M23 58c6 9 14 14 25 14 15 0 25-10 25-25V22H59v25c0 7-4 11-11 11-5 0-9-2-12-7L23 58z" fill="#38bdf8"/>
<path d="M24 24h30v13H24V24z" fill="#e2e8f0"/>
</svg>
""",
        encoding="utf-8",
    )
    (DEST / "stylesheets" / "extra.css").write_text(
        """
:root {
  --md-primary-fg-color: #0f172a;
  --md-accent-fg-color: #0284c7;
}
.md-typeset h1 {
  font-weight: 750;
}
.md-typeset table:not([class]) {
  font-size: 0.72rem;
}
.md-content {
  counter-reset: h2;
}
.md-typeset h2 {
  counter-reset: h3;
}
.md-typeset h2::before {
  counter-increment: h2;
  content: counter(h2) ". ";
  color: #64748b;
}
.md-typeset h3::before {
  counter-increment: h3;
  content: counter(h2) "." counter(h3) " ";
  color: #64748b;
}
@media print {
  .md-sidebar, .md-header, .md-tabs {
    display: none !important;
  }
}
""",
        encoding="utf-8",
    )


def write_index() -> None:
    rows = "\n".join(
        f"| [{name.replace('.md', '').replace('_', ' ')}](proposal/{name}) | {STATUS.get(name, 'Soporte')} |"
        for name in PROPOSAL_FILES
    )
    (DEST / "index.md").write_text(
        f"""# INCABIDE TITAN — Technical Proposal Preview

Vista navegable local de la propuesta tecnica para la RFP No. 5801 DRC3P.

!!! note "Uso"
    Esta vista es para revision editorial y tecnica. La fuente de verdad sigue siendo `INCABIDE-TITAN/TECHNICAL_PROPOSAL/`.

## Estado de capitulos

| Capitulo | Estado |
| --- | --- |
{rows}

## Exportacion a PDF

Usar la opcion **Exportar / imprimir PDF** del menu lateral generada por el plugin de impresion, o imprimir desde el navegador usando la ruta `/print_page/`.
""",
        encoding="utf-8",
    )


def write_references() -> None:
    REF_DEST.mkdir(parents=True, exist_ok=True)
    (REF_DEST / "chapter_status.md").write_text(
        "# Estado de capitulos\n\n"
        + "\n".join(
            f"- **{name.replace('.md', '').replace('_', ' ')}:** {STATUS.get(name, 'Soporte')}"
            for name in PROPOSAL_FILES
        )
        + "\n",
        encoding="utf-8",
    )
    (REF_DEST / "cross_references.md").write_text(
        """# Matriz de navegacion y referencias cruzadas

| Tema | Capitulos | Soporte |
| --- | --- | --- |
| Comprension RFP | 03, 04, 05 | Matriz de cumplimiento, RFP Intelligence |
| Azure | 08, 22 | Azure Enterprise, diagramas Mermaid |
| Seguridad | 09, 22, 23 | Security Architecture, QA criteria |
| DevSecOps | 10, 21, 23 | DevSecOps, Azure Architecture |
| QA / UAT | 11, 23 | Non-conformity criteria, continuous improvement |
| Datos / Migracion | 12, 22 | Data Architecture |
| Soporte / Operacion | 13, 21, 23 | Operation Model |
| Equipo | 15B | Project Team, Missing Justech Information |
| Demo | Demo Master Plan | 05_DEMO/DEMO_MASTER_PLAN.md |
| Presentacion | Presentation Storyboard | 06_PRESENTATION/PRESENTATION_MASTER_STORYBOARD.md |
""",
        encoding="utf-8",
    )


def main() -> None:
    if DEST.exists():
        shutil.rmtree(DEST)
    PROPOSAL_DEST.mkdir(parents=True, exist_ok=True)
    write_assets()
    for name in PROPOSAL_FILES + SUPPORT_FILES:
        copy_doc(name)
    write_index()
    write_references()


if __name__ == "__main__":
    main()

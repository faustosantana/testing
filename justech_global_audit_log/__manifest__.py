{
    "name": "Justech Global Audit Log",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Auditoría global multiempresa configurable por modelo",
    "description": """
Auditoría global para entornos multiempresa de Justech.
Registra creación, modificación y eliminación de registros según reglas
configurables por el administrador.
    """,
    "author": "Justech",
    "website": "https://www.justech.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "mail",
        "sale",
        "purchase",
        "account",
        "stock",
        "product",
        "crm",
        "project",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/audit_log_views.xml",
        "views/audit_rule_views.xml",
        "data/audit_rule_data.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

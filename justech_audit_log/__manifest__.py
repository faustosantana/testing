{
    "name": "Justech Audit Log",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Auditoría interna de cambios críticos en documentos multiempresa",
    "description": """
Registra cambios críticos en cotizaciones, compras, facturas y albaranes
para detectar inconsistencias multiempresa (secuencia vs company_id).
    """,
    "author": "Justech",
    "website": "https://www.justech.com",
    "license": "LGPL-3",
    "depends": [
        "base",
        "sale",
        "purchase",
        "account",
        "stock",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/audit_log_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}

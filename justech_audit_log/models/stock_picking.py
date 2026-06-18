from odoo import models


class StockPicking(models.Model):
    _inherit = ["stock.picking", "justech.audit.mixin"]

    JUSTECH_AUDIT_FIELDS = [
        "company_id",
        "partner_id",
        "state",
        "origin",
        "picking_type_id",
    ]

from odoo import models


class AccountMove(models.Model):
    _inherit = ["account.move", "justech.audit.mixin"]

    JUSTECH_AUDIT_FIELDS = [
        "company_id",
        "partner_id",
        "state",
        "amount_total",
        "move_type",
    ]

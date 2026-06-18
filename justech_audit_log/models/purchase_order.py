from odoo import models


class PurchaseOrder(models.Model):
    _inherit = ["purchase.order", "justech.audit.mixin"]

    JUSTECH_AUDIT_FIELDS = [
        "company_id",
        "partner_id",
        "state",
        "amount_total",
        "user_id",
    ]

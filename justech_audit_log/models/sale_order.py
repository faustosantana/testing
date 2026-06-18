from odoo import models


class SaleOrder(models.Model):
    _inherit = ["sale.order", "justech.audit.mixin"]

    JUSTECH_AUDIT_FIELDS = [
        "company_id",
        "partner_id",
        "state",
        "amount_total",
        "user_id",
        "pricelist_id",
    ]

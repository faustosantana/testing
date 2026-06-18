from odoo.exceptions import ValidationError
from odoo import api, fields, models


class JustechAuditRule(models.Model):
    _name = "justech.audit.rule"
    _description = "Justech Audit Rule"
    _order = "model_description, name"

    name = fields.Char(required=True)
    model_id = fields.Many2one(
        "ir.model",
        string="Modelo",
        required=True,
        ondelete="cascade",
        domain="[('transient', '=', False)]",
    )
    model_name = fields.Char(related="model_id.model", store=True, index=True)
    model_description = fields.Char(related="model_id.name", store=True)
    active = fields.Boolean(default=True)

    EXCLUDED_MODELS = {
        "justech.audit.log",
        "justech.audit.rule",
        "bus.bus",
        "mail.message",
        "mail.followers",
        "ir.logging",
    }

    _sql_constraints = [
        (
            "model_unique",
            "unique(model_id)",
            "Ya existe una regla para este modelo.",
        ),
    ]

    @api.model
    def _justech_get_audited_model_names(self):
        return set(
            self.sudo()
            .search([("active", "=", True)])
            .mapped("model_name")
        )

    @api.model
    def _justech_is_model_audited(self, model_name):
        if model_name in self.EXCLUDED_MODELS:
            return False
        return model_name in self._justech_get_audited_model_names()

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        self.env.registry.clear_cache()
        return records

    def write(self, vals):
        result = super().write(vals)
        if {"active", "model_id"} & set(vals.keys()):
            self.env.registry.clear_cache()
        return result

    def unlink(self):
        result = super().unlink()
        self.env.registry.clear_cache()
        return result

    @api.constrains("model_id")
    def _check_model_not_excluded(self):
        for rule in self:
            if rule.model_name in self.EXCLUDED_MODELS:
                raise ValidationError(
                    "Este modelo está excluido de la auditoría por diseño."
                )

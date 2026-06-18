import json

from odoo import api, fields, models


class JustechAuditLog(models.Model):
    _name = "justech.audit.log"
    _description = "Justech Audit Log"
    _order = "change_date desc, id desc"
    _rec_name = "record_name"

    model_name = fields.Char(required=True, index=True)
    record_id = fields.Integer(required=True, index=True)
    record_name = fields.Char(index=True)
    field_name = fields.Char(string="Campo", required=True)
    old_value = fields.Text(string="Valor anterior")
    new_value = fields.Text(string="Valor nuevo")
    user_id = fields.Many2one("res.users", string="Usuario", index=True)
    company_id = fields.Many2one("res.company", string="Empresa", index=True)
    change_date = fields.Datetime(
        string="Fecha de cambio",
        default=fields.Datetime.now,
        required=True,
        index=True,
    )
    operation_type = fields.Selection(
        selection=[
            ("create", "Creación"),
            ("update", "Actualización"),
        ],
        string="Tipo de operación",
        required=True,
        index=True,
    )
    technical_field_name = fields.Char(string="Campo técnico", index=True)


class JustechAuditMixin(models.AbstractModel):
    _name = "justech.audit.mixin"
    _description = "Justech Audit Mixin"

    JUSTECH_AUDIT_FIELDS = []

    def _justech_get_audit_fields(self):
        return list(self.JUSTECH_AUDIT_FIELDS)

    def _justech_get_field_label(self, field_name):
        field = self._fields.get(field_name)
        return field.string if field else field_name

    def _justech_format_value(self, field_name, value):
        if value is False or value is None:
            return ""
        field = self._fields.get(field_name)
        if not field:
            return str(value)
        if field.type == "many2one":
            return value.display_name if value else ""
        if field.type == "selection":
            selection = dict(field.selection or [])
            return selection.get(value, value)
        if field.type == "monetary":
            return f"{value:.2f}"
        if field.type == "float":
            return f"{value:.2f}"
        return str(value)

    def _justech_get_record_company(self, record):
        if "company_id" in record._fields and record.company_id:
            return record.company_id
        return self.env.company

    def _justech_create_log(self, values):
        self.env["justech.audit.log"].sudo().create(values)

    def _justech_log_create(self, record):
        tracked = self._justech_get_audit_fields()
        snapshot = {
            field: self._justech_format_value(field, record[field])
            for field in tracked
            if field in record._fields
        }
        self._justech_create_log(
            {
                "model_name": record._name,
                "record_id": record.id,
                "record_name": record.display_name,
                "field_name": "Creación",
                "technical_field_name": "__create__",
                "old_value": "",
                "new_value": json.dumps(snapshot, ensure_ascii=False, sort_keys=True),
                "user_id": self.env.uid,
                "company_id": self._justech_get_record_company(record).id,
                "change_date": fields.Datetime.now(),
                "operation_type": "create",
            }
        )

    def _justech_log_update(self, record, field_name, old_value, new_value):
        if old_value == new_value:
            return
        self._justech_create_log(
            {
                "model_name": record._name,
                "record_id": record.id,
                "record_name": record.display_name,
                "field_name": self._justech_get_field_label(field_name),
                "technical_field_name": field_name,
                "old_value": self._justech_format_value(field_name, old_value),
                "new_value": self._justech_format_value(field_name, new_value),
                "user_id": self.env.uid,
                "company_id": self._justech_get_record_company(record).id,
                "change_date": fields.Datetime.now(),
                "operation_type": "update",
            }
        )

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        if not self.env.context.get("justech_skip_audit"):
            for record in records:
                record._justech_log_create(record)
        return records

    def write(self, vals):
        if self.env.context.get("justech_skip_audit"):
            return super().write(vals)

        tracked_fields = set(self._justech_get_audit_fields())
        fields_to_check = tracked_fields & set(vals.keys())
        if not fields_to_check:
            return super().write(vals)

        previous_values = {
            record.id: {field: record[field] for field in fields_to_check}
            for record in self
        }
        result = super().write(vals)

        for record in self:
            for field_name in fields_to_check:
                record._justech_log_update(
                    record,
                    field_name,
                    previous_values[record.id][field_name],
                    record[field_name],
                )
        return result

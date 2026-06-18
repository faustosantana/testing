import json

from odoo import api, fields, models
from odoo.http import request


class JustechAuditLog(models.Model):
    _name = "justech.audit.log"
    _description = "Justech Global Audit Log"
    _order = "change_date desc, id desc"
    _rec_name = "record_name"

    operation_type = fields.Selection(
        selection=[
            ("create", "Creación"),
            ("write", "Modificación"),
            ("unlink", "Eliminación"),
        ],
        required=True,
        index=True,
    )
    model_name = fields.Char(required=True, index=True)
    model_description = fields.Char(string="Modelo", index=True)
    record_id = fields.Integer(required=True, index=True)
    record_name = fields.Char(index=True)
    field_name = fields.Char(string="Campo técnico", index=True)
    field_description = fields.Char(string="Campo", index=True)
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
    ip_address = fields.Char(string="Dirección IP", index=True)
    active = fields.Boolean(default=True)

    @api.model
    def _justech_get_ip_address(self):
        try:
            if request and request.httprequest:
                return request.httprequest.remote_addr
        except RuntimeError:
            pass
        return False

    @api.model
    def _justech_get_model_description(self, model_name):
        model = self.env["ir.model"].sudo().search([("model", "=", model_name)], limit=1)
        return model.name or model_name

    @api.model
    def _justech_get_field_description(self, model_name, field_name):
        if field_name in ("__create__", "__unlink__"):
            return field_name
        field = self.env[model_name]._fields.get(field_name)
        return field.string if field else field_name

    @api.model
    def _justech_format_value(self, model_name, field_name, value):
        if value is False or value is None:
            return ""
        if field_name in ("__create__", "__unlink__"):
            return str(value)
        model = self.env[model_name]
        field = model._fields.get(field_name)
        if not field:
            return str(value)
        if field.type == "many2one":
            return value.display_name if value else ""
        if field.type == "many2many" or field.type == "one2many":
            return ", ".join(value.mapped("display_name"))
        if field.type == "selection":
            selection = dict(field.selection or [])
            return selection.get(value, value)
        if field.type in ("monetary", "float"):
            return f"{value:.2f}"
        return str(value)

    @api.model
    def _justech_get_record_company_id(self, record):
        if "company_id" in record._fields and record.company_id:
            return record.company_id.id
        return self.env.company.id

    @api.model
    def _justech_create_entries(self, entries):
        if not entries:
            return
        self.sudo().create(entries)

    @api.model
    def _justech_build_entry(
        self,
        record,
        operation_type,
        field_name,
        old_value,
        new_value,
    ):
        model_name = record._name
        return {
            "operation_type": operation_type,
            "model_name": model_name,
            "model_description": self._justech_get_model_description(model_name),
            "record_id": record.id,
            "record_name": record.display_name,
            "field_name": field_name,
            "field_description": self._justech_get_field_description(model_name, field_name),
            "old_value": old_value,
            "new_value": new_value,
            "user_id": self.env.uid,
            "company_id": self._justech_get_record_company_id(record),
            "change_date": fields.Datetime.now(),
            "ip_address": self._justech_get_ip_address(),
            "active": True,
        }

    @api.model
    def _justech_log_create(self, records):
        entries = []
        for record in records:
            snapshot = {}
            for field_name, field in record._fields.items():
                if field_name in record._justech_excluded_fields():
                    continue
                if field.type in ("one2many", "many2many", "binary", "html"):
                    continue
                if not field.store and not field.related:
                    continue
                snapshot[field_name] = self._justech_format_value(
                    record._name, field_name, record[field_name]
                )
            entries.append(
                self._justech_build_entry(
                    record,
                    "create",
                    "__create__",
                    "",
                    json.dumps(snapshot, ensure_ascii=False, sort_keys=True),
                )
            )
        self._justech_create_entries(entries)

    @api.model
    def _justech_log_write(self, records, previous_values, changed_fields):
        entries = []
        for record in records:
            for field_name in changed_fields:
                old_raw = previous_values[record.id][field_name]
                new_raw = record[field_name]
                old_text = self._justech_format_value(record._name, field_name, old_raw)
                new_text = self._justech_format_value(record._name, field_name, new_raw)
                if old_text == new_text:
                    continue
                entries.append(
                    self._justech_build_entry(
                        record,
                        "write",
                        field_name,
                        old_text,
                        new_text,
                    )
                )
        self._justech_create_entries(entries)

    @api.model
    def _justech_log_unlink(self, records_data):
        entries = []
        for data in records_data:
            entries.append(
                {
                    "operation_type": "unlink",
                    "model_name": data["model_name"],
                    "model_description": self._justech_get_model_description(data["model_name"]),
                    "record_id": data["record_id"],
                    "record_name": data["record_name"],
                    "field_name": "__unlink__",
                    "field_description": "Eliminación",
                    "old_value": data["snapshot"],
                    "new_value": "",
                    "user_id": self.env.uid,
                    "company_id": data["company_id"],
                    "change_date": fields.Datetime.now(),
                    "ip_address": self._justech_get_ip_address(),
                    "active": True,
                }
            )
        self._justech_create_entries(entries)

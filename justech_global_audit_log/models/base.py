import json

from odoo import api, models, tools


class Base(models.AbstractModel):
    _inherit = "base"

    JUSTECH_EXCLUDED_FIELDS = {
        "write_date",
        "write_uid",
        "create_date",
        "create_uid",
        "message_ids",
        "activity_ids",
        "__last_update",
        "message_follower_ids",
        "message_partner_ids",
        "message_main_attachment_id",
        "website_message_ids",
        "access_token",
    }

    @api.model
    def _justech_excluded_fields(self):
        return self.JUSTECH_EXCLUDED_FIELDS

    @api.model
    def _justech_is_audited_model(self):
        return self.env["justech.audit.rule"]._justech_is_model_audited(self._name)

    @api.model
    @tools.ormcache()
    def _justech_cached_audited_models(self):
        return frozenset(self.env["justech.audit.rule"]._justech_get_audited_model_names())

    @api.model
    def _justech_should_audit(self):
        if self._name in self.env["justech.audit.rule"].EXCLUDED_MODELS:
            return False
        return self._name in self._justech_cached_audited_models()

    def _justech_capture_unlink_data(self):
        AuditLog = self.env["justech.audit.log"]
        data = []
        for record in self:
            snapshot = {}
            for field_name, field in record._fields.items():
                if field_name in self._justech_excluded_fields():
                    continue
                if field.type in ("one2many", "many2many", "binary", "html"):
                    continue
                snapshot[field_name] = AuditLog._justech_format_value(
                    record._name, field_name, record[field_name]
                )
            data.append(
                {
                    "model_name": record._name,
                    "record_id": record.id,
                    "record_name": record.display_name,
                    "company_id": AuditLog._justech_get_record_company_id(record),
                    "snapshot": json.dumps(snapshot, ensure_ascii=False, sort_keys=True),
                }
            )
        return data

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        if not self.env.context.get("justech_skip_audit") and records._justech_should_audit():
            self.env["justech.audit.log"]._justech_log_create(records)
        return records

    def write(self, vals):
        if self.env.context.get("justech_skip_audit") or not self._justech_should_audit():
            return super().write(vals)

        fields_to_check = set(vals.keys()) - self._justech_excluded_fields()
        if not fields_to_check:
            return super().write(vals)

        previous_values = {
            record.id: {field: record[field] for field in fields_to_check}
            for record in self
        }
        result = super().write(vals)
        self.env["justech.audit.log"]._justech_log_write(self, previous_values, fields_to_check)
        return result

    def unlink(self):
        if self.env.context.get("justech_skip_audit") or not self._justech_should_audit():
            return super().unlink()

        records_data = self._justech_capture_unlink_data()
        result = super().unlink()
        self.env["justech.audit.log"]._justech_log_unlink(records_data)
        return result

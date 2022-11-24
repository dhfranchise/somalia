from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    auto_check_invoice = fields.Boolean(string="Invoice Auto Check")

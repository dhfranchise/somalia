from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    enable_manual_discount_selection = fields.Boolean(string="Enable Manual Discount Selection")

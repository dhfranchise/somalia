from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    email = fields.Char(string="Email")

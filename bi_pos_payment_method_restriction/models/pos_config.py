from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    pwd_payment_method = fields.Char(string="Password to Allow selecting payment method for credit note")

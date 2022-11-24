from odoo import models, fields


class PosConfig(models.Model):
    _inherit = "pos.config"

    restrict_line_discount = fields.Boolean(string="Restrict Line Discount", default=False)
    pw_allow_discount = fields.Char(string="Password to Allow Line Discount")
    pos_deny_order = fields.Boolean(string="Deny POS Order", default=False)
    pos_deny_qty = fields.Integer(string="Deny POS Order When Product Qty is goes down to", default=0)
    pw_allow_order = fields.Char(string="Password to Allow POS Order When Product is less than deny quantity")

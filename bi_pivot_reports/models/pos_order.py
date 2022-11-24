from odoo import fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    margin = fields.Monetary(store=True)
    margin_percent = fields.Float(store=True)

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    reference = fields.Char(string="Reference", related="pos_order_id.name")

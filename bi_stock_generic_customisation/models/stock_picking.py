from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    total_value = fields.Float(string="Total Value", compute="_compute_total_value")

    @api.depends("move_lines")
    def _compute_total_value(self):
        for rec in self:
            rec.total_value = sum(rec.move_lines.mapped("total_value"))


class StockMove(models.Model):
    _inherit = "stock.move"

    total_value = fields.Float(string="Total Value", compute="_compute_total_value")

    @api.depends("product_uom_qty", "product_id")
    def _compute_total_value(self):
        for rec in self:
            rec.total_value = rec.product_uom_qty * rec.product_id.standard_price

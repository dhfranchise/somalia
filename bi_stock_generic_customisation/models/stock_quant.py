from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    group_code_id = fields.Many2one(related="product_tmpl_id.group_code_id", store=True, index=True)
    sub_group_code_id = fields.Many2one(related="product_tmpl_id.sub_group_code_id", store=True, index=True)
    brand_code_id = fields.Many2one(related="product_tmpl_id.brand_code_id", store=True, index=True)
    color_code_id = fields.Many2one(related="product_tmpl_id.color_code_id", store=True, index=True)

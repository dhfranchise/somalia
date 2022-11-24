from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    price_quoted = fields.Char(string="Price Quoted")
    delivery = fields.Char(string="Delivery")
    quote = fields.Char(string="Quote")
    warranty = fields.Char(string="Warranty")

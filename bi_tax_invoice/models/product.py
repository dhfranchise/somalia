from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    other_charges = fields.Boolean(string="Other Charges")


class ProductProduct(models.Model):
    _inherit = "product.product"

    other_charges = fields.Boolean(string="Other Charges")

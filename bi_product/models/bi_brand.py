from odoo import fields, models


class BiBrandCode(models.Model):
    _name = "bi.brand.code"
    _description = "Brand Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

from odoo import fields, models


class BiGroupCode(models.Model):
    _name = "bi.group.code"
    _description = "group Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

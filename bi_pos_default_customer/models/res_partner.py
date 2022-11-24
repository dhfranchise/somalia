from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    cash_customer = fields.Boolean(string="Cash Customer")

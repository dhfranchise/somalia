from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_sales_person_id = fields.Many2one("hr.employee", string="Custom Salesperson")

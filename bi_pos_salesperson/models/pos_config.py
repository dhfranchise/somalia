from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    is_salesperson_enabled = fields.Boolean(
        string="Enable Salesperson",
        help="Enable salesperson in POS",
    )
    salesperson_ids = fields.Many2many(
        "hr.employee",
        "pos_config_salesperson_rel",
        string="Salespersons",
        help="Salespersons assigned to this POS.",
    )

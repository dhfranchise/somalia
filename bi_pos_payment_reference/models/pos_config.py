from odoo import models, fields


class PosConfig(models.Model):
    _inherit = "pos.config"

    is_provide_payment_ref = fields.Boolean(
        string="Provide Payment Reference?",
        help="Provide Payment Reference for selected Payment Types?",
        default=False,
    )

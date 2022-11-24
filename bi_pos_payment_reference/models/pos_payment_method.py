from odoo import models, fields


class PosPaymentMethod(models.Model):
    _inherit = "pos.payment.method"

    is_provide_payment_ref = fields.Boolean(
        string="Provide Payment Reference?",
        help="Check this if you want to provide payment reference in Payment Screen",
        default=False,
    )

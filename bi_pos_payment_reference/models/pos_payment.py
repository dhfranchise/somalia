from odoo import models, fields


class PosPayment(models.Model):
    _inherit = "pos.payment"

    payment_reference = fields.Char(
        string="Payment Reference",
        copy=False,
    )

    def _export_for_ui(self, payment):
        fields = super(PosPayment, self)._export_for_ui(payment)
        fields.update(
            {
                "payment_reference": payment.payment_reference,
            }
        )
        return fields

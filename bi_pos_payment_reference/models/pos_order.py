from odoo import models, api


class PosOrder(models.Model):
    _inherit = "pos.order"

    @api.model
    def _payment_fields(self, order, ui_paymentline):
        fields = super(PosOrder, self)._payment_fields(order, ui_paymentline)
        fields.update(
            {
                "payment_reference": ui_paymentline.get("payment_reference", False),
            }
        )
        return fields

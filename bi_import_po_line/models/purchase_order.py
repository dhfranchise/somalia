from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def bi_import_po_line(self):
        if self:
            action = self.env.ref("bi_import_po_line.import_pol_action").read()[0]
            return action

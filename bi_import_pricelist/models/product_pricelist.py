from odoo import models


class ProductPricelist(models.Model):
    _inherit = "product.pricelist"

    def action_open_import_pricelist(self):
        action_ref = "bi_import_pricelist.action_import_product_pricelist_wizard"
        action = self.env["ir.actions.act_window"]._for_xml_id(action_ref)
        return action

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    location_wise_qty = fields.Float(string="Quantity")

    @api.model
    def get_location_qty(self, picking_type_id):
        product_list = []
        products = self.env["product.product"].search([("available_in_pos", "=", True)])
        picking_type = self.env["stock.picking.type"].search([("id", "=", picking_type_id)])
        for product_id in products:
            product_list.append(
                {
                    "id": product_id.id,
                    "location_wise_qty": product_id.with_context({"location": picking_type.default_location_src_id.id})
                    .sudo()
                    .qty_available,
                }
            )
        return product_list

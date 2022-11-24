from odoo import fields, models, api


class PosOrder(models.Model):
    _inherit = "pos.order"

    custom_salesperson_id = fields.Many2one("hr.employee", string="Salesperson")

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        if ui_order.get("salesperson", False):
            res["custom_salesperson_id"] = ui_order.get("salesperson", False)["id"]
        return res

    def _export_for_ui(self, order):
        result = super(PosOrder, self)._export_for_ui(order)
        result.update(
            {
                "salesperson": order.custom_salesperson_id.id,
            }
        )
        return result

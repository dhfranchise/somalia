from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    discount_amount = fields.Float(string="Discount Amount", digits="Discount", default=0.0)

    @api.onchange("discount")
    def _onchange_discount_amount(self):
        for line in self:
            if line.discount:
                discount_amount = ((line.price_unit * line.product_uom_qty) * line.discount) / 100
                line.discount_amount = discount_amount

    @api.depends("product_uom_qty", "discount", "discount_amount", "price_unit", "tax_id")
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            quantity = line.product_uom_qty
            if line.discount_amount:
                price = (line.price_unit * line.product_uom_qty) - line.discount_amount
                quantity = 1
            taxes = line.tax_id.compute_all(
                price,
                line.order_id.currency_id,
                quantity,
                product=line.product_id,
                partner=line.order_id.partner_shipping_id,
            )
            line.update(
                {
                    "price_tax": sum(t.get("amount", 0.0) for t in taxes.get("taxes", [])),
                    "price_total": taxes["total_included"],
                    "price_subtotal": taxes["total_excluded"],
                }
            )
            if self.env.context.get("import_file", False) and not self.env.user.user_has_groups(
                "account.group_account_manager"
            ):
                line.tax_id.invalidate_cache(["invoice_repartition_line_ids"], [line.tax_id.id])

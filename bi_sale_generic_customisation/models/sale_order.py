from odoo import api, fields, models

# import json


class SaleOrderUpdate(models.Model):
    _inherit = "sale.order"

    balance_to_pay = fields.Monetary(string="Balance Amount to Pay", compute="_compute_balance_to_pay", store=True)
    invoiced_amount = fields.Monetary(string="Invoiced Amount", compute="_compute_balance_to_pay", store=True)

    @api.depends("pos_order_line_ids", "invoice_ids")
    def _compute_balance_to_pay(self):
        # ToDo: balance to pay other than pos order
        for order in self:
            # invoice_ids = order.mapped('invoice_ids')
            # paid_amount = 0.0
            # for invoice in invoice_ids:
            # 	if invoice.payment_state in ['paid', 'in_payment', 'partial']:
            # 		widget_val = json.loads(invoice.invoice_payments_widget)
            # 		current_amounts = {vals['amount'] for vals in widget_val['content']}
            # 		paid_amount += sum(current_amounts)
            # order.balance_to_pay = order.amount_total - paid_amount
            if len(order.pos_order_line_ids) > 0:
                order.balance_to_pay = order.amount_total - sum(
                    order.pos_order_line_ids.mapped("order_id").mapped("amount_paid")
                )
                order.invoiced_amount = sum(
                    order.pos_order_line_ids.mapped("order_id").mapped("account_move").mapped("amount_total")
                )

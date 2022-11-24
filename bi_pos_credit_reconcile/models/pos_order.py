from odoo import api, fields, models
import ast


class PosOrder(models.Model):
    _inherit = "pos.order"

    amount_due = fields.Float("Amount Due", compute="_compute_get_amount_due")
    use_advance_amount = fields.Boolean("Use Advance Amount", default=False)
    advance_total = fields.Float("Advance Total to User")
    advance_list = fields.Char(string="Advance List")
    credit_total = fields.Float("Credit Total to User")
    credit_list = fields.Char(string="Credit List")
    advance_credit_total = fields.Float(string="Advance-Credit Total")

    @api.depends("amount_total", "amount_paid")
    def _compute_get_amount_due(self):
        for order in self:
            if order.amount_paid - order.amount_total >= 0:
                order.amount_due = 0
            else:
                order.amount_due = order.amount_total - order.amount_paid

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        res["advance_total"] = ui_order.get("advance_total", False)
        res["advance_list"] = ui_order.get("advance_list", False)
        res["credit_total"] = ui_order.get("credit_total", False)
        res["credit_list"] = ui_order.get("credit_list", False)
        res["advance_credit_total"] = ui_order.get("advance_credit_total", False)
        res["use_advance_amount"] = ui_order.get("use_advance_amount", False)
        return res

    @api.model
    def get_tender_amount(self, partner_id, advance_details_entered, credit_details_entered):
        partner_id = self.env["res.partner"].search([("id", "=", partner_id)])
        advance_list = []
        advance_total = 0
        if "," in advance_details_entered:
            advance_numbers = advance_details_entered.split(",")
        else:
            advance_numbers = [advance_details_entered]
        if advance_details_entered == "":
            advance_numbers = []
        for each_advance in advance_numbers:
            payment_id = self.env["account.payment"].search(
                [
                    ("name", "=", each_advance),
                    ("partner_id", "=", partner_id.id),
                    ("payment_type", "=", "inbound"),
                    ("pos_order_id", "=", False),
                ]
            )
            if not payment_id:
                return {
                    "status": False,
                    "issue_model": "advance",
                    "advance_record": each_advance,
                    "advance_issue": "notfound",
                }
            elif payment_id and payment_id.is_reconciled:
                return {
                    "status": False,
                    "issue_model": "advance",
                    "advance_record": each_advance,
                    "advance_issue": "reconciled",
                }
            else:
                partner_debit = self.debit_payment_partner_get(payment_id.id)
                advance_list.append(
                    {
                        each_advance: partner_debit,
                    }
                )
                advance_total += partner_debit
        credit_list = []
        credit_total = 0
        if "," in credit_details_entered:
            credit_numbers = credit_details_entered.split(",")
        else:
            credit_numbers = [credit_details_entered]
        for each_credit in credit_numbers:
            move_id = self.env["account.move"].search([("name", "=", each_credit), ("partner_id", "=", partner_id.id)])
            if not move_id and advance_total == 0:
                return {
                    "status": False,
                    "issue_model": "credit",
                    "advance_record": each_credit,
                    "credit_issue": "notfound",
                }
            elif move_id and move_id.amount_residual <= 0 and advance_total == 0:
                return {
                    "status": False,
                    "issue_model": "credit",
                    "advance_record": each_credit,
                    "credit_issue": "reconciled",
                }
            elif move_id and move_id.invoice_date_due < fields.Date.today():
                return {
                    "status": False,
                    "issue_model": "credit",
                    "advance_record": each_credit,
                    "credit_issue": "overdue",
                }
            else:
                credit_list.append(
                    {
                        each_credit: move_id.amount_residual,
                    }
                )
                credit_total += move_id.amount_residual
        advance_credit_total = credit_total + advance_total
        if advance_list or credit_list:
            return {
                "status": True,
                "advance_array": advance_list,
                "advance_total": advance_total,
                "credit_array": credit_list,
                "credit_total": credit_total,
                "advance_credit_total": advance_credit_total,
            }
        else:
            return {"status": False, "issue_model": "ignore"}

    @api.model
    def _process_order(self, order, draft, existing_order):
        res = super(PosOrder, self)._process_order(order, draft, existing_order)
        order = self.browse(res)
        if order.use_advance_amount:
            moves = self.env["account.move"]
            move_vals = order._prepare_invoice_vals()
            new_move = (
                moves.sudo()
                .with_company(order.company_id)
                .with_context(default_move_type=move_vals["move_type"])
                .create(move_vals)
            )
            order_credit_list = ast.literal_eval(order.credit_list)
            all_names = list(set().union(*(d.keys() for d in order_credit_list)))
            pending_credit_notes = self.env["account.move"].search(
                [
                    ("partner_id", "=", order.partner_id.id),
                    ("move_type", "=", "out_refund"),
                    ("name", "in", all_names),
                ]
            )
            order.write({"state": "paid"})
            order.write({"account_move": new_move.id, "state": "invoiced"})
            new_move.sudo().with_company(order.company_id)._post()
            for each_credit_note in pending_credit_notes:
                credit_line_id = each_credit_note.line_ids.filtered(
                    lambda line: line.account_id.user_type_id.type in ("receivable", "payable")
                )
                if credit_line_id.reconciled:
                    continue
                credit_amount_residual = each_credit_note.amount_residual
                new_move.js_assign_outstanding_line(credit_line_id.id)
                order.amount_paid += credit_amount_residual
                order._compute_get_amount_due()
                if new_move.amount_residual == 0:
                    break

            order_advance_list = ast.literal_eval(order.advance_list)
            all_names = list(set().union(*(d.keys() for d in order_advance_list)))
            pending_payments = self.env["account.payment"].search(
                [
                    ("partner_id", "=", order.partner_id.id),
                    ("payment_type", "=", "inbound"),
                    ("name", "in", all_names),
                    ("pos_order_id", "=", order.id),
                ]
            )
            for each_payment in pending_payments:
                payment_line_id = each_payment.move_id.line_ids.filtered(
                    lambda line: line.account_id.user_type_id.type in ("receivable", "payable")
                )
                if payment_line_id.reconciled:
                    continue
                new_move.js_assign_outstanding_line(payment_line_id.id)
                order.amount_paid = order.amount_total - order.account_move.amount_residual
                order._compute_get_amount_due()
                if new_move.amount_residual == 0:
                    break
        return res

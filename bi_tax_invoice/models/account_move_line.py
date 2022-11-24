from odoo import api, fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    is_delivery = fields.Boolean(string="Is a Delivery", compute="_compute_is_delivery")
    is_other_charges = fields.Boolean(string="Is other charges", related="product_id.other_charges")

    def _compute_is_delivery(self):
        for rec in self:
            rec.is_delivery = False
            if rec.move_id.pos_order_ids:
                pos_order = rec.move_id.pos_order_ids.lines
                for pos_obj in pos_order:
                    linked_sale_order_lines = pos_obj.sale_order_origin_id.order_line
                    delivery = linked_sale_order_lines.filtered(lambda x: x.is_delivery)
                    if delivery.product_id == rec.product_id:
                        rec.is_delivery = True
                    else:
                        rec.is_delivery = False


class AccountMove(models.Model):
    _inherit = "account.move"

    declaration = fields.Text(string="Declaration")
    other_terms = fields.Html(string="Other Terms")
    invoice_sales_person_id = fields.Many2one(
        "hr.employee", string="Invoice Salesperson", compute="_compute_invoice_sales_person_id", store="True"
    )

    @api.depends("invoice_origin")
    def _compute_invoice_sales_person_id(self):
        for rec in self:
            if rec.pos_order_ids:
                rec.invoice_sales_person_id = rec.pos_order_ids.custom_salesperson_id.id
            else:
                sale_obj = self.env["sale.order"].search([])
                sale_id = sale_obj.filtered(lambda x: x.invoice_ids == rec)
                rec.invoice_sales_person_id = sale_id.custom_sales_person_id.id

    @api.model
    def default_get(self, vals):
        res = super(AccountMove, self).default_get(vals)
        res.update(
            {
                "declaration": "We decalare that this invoice shows the actual price of the goods described \
                    and that all particulars are true and correct."
            }
        )
        res.update(
            {
                "other_terms": """<p><span style="font-weight: bolder;">SUBJECT TO LILONGWE JURISDICTION</span>\
                    </p><p><span style="font-size: 14px;">We have attached Withholding Tax Exemption Certificate.\
                    Please do not deduct 3%. This is a computer generated invoice.</span><br></p><p><br></p>"""
            }
        )
        return res

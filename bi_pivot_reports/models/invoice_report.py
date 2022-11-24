from odoo import models, fields


class AccountInvoiceReport(models.Model):

    _inherit = "account.invoice.report"

    price_total = fields.Float(readonly=True, string="Total")
    group_code_id = fields.Many2one("bi.group.code", string="Group Code", readonly=True)
    sub_group_code_id = fields.Many2one("bi.sub.group.code", string="Sub Group Code", readonly=True)
    brand_code_id = fields.Many2one("bi.brand.code", string="Brand Code", readonly=True)
    invoice_sales_person_id = fields.Many2one("hr.employee", string="Invoice Salesperson", readonly=True)

    _depends = {
        "account.move": ["invoice_sales_person_id"],
        "account.move.line": ["price_total"],
        "product.template": ["group_code_id", "sub_group_code_id", "brand_code_id"],
    }

    def _select(self):
        return (
            super()._select()
            + ",move.invoice_sales_person_id as invoice_sales_person_id, line.price_total as price_total, \
                template.group_code_id as group_code_id, template.sub_group_code_id as sub_group_code_id,\
                template.brand_code_id as brand_code_id "
        )

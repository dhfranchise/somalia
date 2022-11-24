from odoo import api, models


class TaxInvoice(models.AbstractModel):
    _name = "report.bi_tax_invoice.bi_tax_invoice_template"
    _description = "Tax Invoice"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["account.move"].browse(docids)
        val = []
        num_word = str(docs.currency_id.amount_to_text(docs.amount_total))
        delivery = docs.invoice_line_ids.filtered(lambda x: x.is_delivery).mapped("price_unit")
        other_charges = docs.invoice_line_ids.filtered(
            lambda x: x.product_id.other_charges and x.product_id.detailed_type == "service"
        ).mapped("price_unit")
        delivery_note_num = 0
        quotation_num = 0
        location = 0
        reference = 0
        if not docs.pos_order_ids:
            sale_obj = self.env["sale.order"].search([("invoice_ids", "=", docs.ids)])
            for rec in sale_obj:
                picking_obj = rec.picking_ids
                for obj in picking_obj:
                    delivery_note_num = obj.name
                    quotation_num = rec.name
                    location = rec.picking_ids.location_id.location_id.name
                    reference = rec.picking_ids.name

        values = {
            "num_word": num_word,
            "delivery": delivery[0] if delivery else "",
            "delivery_note_num": delivery_note_num,
            "quotation_num": quotation_num,
            "location": location,
            "reference": reference,
            "other_charges": other_charges[0] if other_charges else "",
        }
        val.append(values)

        return {"doc_ids": docs.ids, "doc_model": "sale.order", "data": data, "docs": docs, "vals": val}

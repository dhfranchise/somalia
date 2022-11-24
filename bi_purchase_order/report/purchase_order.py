from odoo import api, models


class PurchaseOrder(models.AbstractModel):
    _name = "report.bi_purchase_order.bi_purchase_order_template"
    _description = "Purchase Order"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["purchase.order"].browse(docids)
        val = []
        num_word = str(docs.currency_id.amount_to_text(docs.amount_total))
        values = {"num_word": num_word}
        val.append(values)

        return {"doc_ids": docs.ids, "doc_model": "purchase.order", "data": data, "docs": docs, "vals": val}

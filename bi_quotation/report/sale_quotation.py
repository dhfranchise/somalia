from odoo import api, models


class SaleQuotation(models.AbstractModel):
    _name = "report.bi_quotation.bi_quotation_template"
    _description = "Sale Quotation"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["sale.order"].browse(docids)
        val = []
        num_word = str(docs.currency_id.amount_to_text(docs.amount_total))
        color = []
        delivery = 0
        for record in docs:
            for lines in record.order_line:
                delivery = lines.filtered(lambda x: x.is_delivery).mapped("price_unit")
                attr_obj = lines.product_id.attribute_line_ids.attribute_id.filtered(
                    lambda x: x.display_type == "color"
                ).mapped("value_ids")
                for obj in attr_obj:
                    color.append(obj.name)
                color_obj = ",".join(color)
                values = {
                    "num_word": num_word,
                    "color": color_obj if color_obj else "",
                    "delivery": delivery[0] if delivery else "",
                }
                val.append(values)

        return {
            "doc_ids": docs.ids,
            "doc_model": "sale.order",
            "data": data,
            "docs": docs,
            "vals": val,
            "num_word": num_word,
            "delivery": delivery[0] if delivery else "",
        }

from odoo import api, models


class PosOrderLine(models.AbstractModel):
    _name = "report.bi_delivery_note_printout.bi_delivery_note_template"
    _description = "Pos Order Line"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["stock.picking"].browse(docids)
        val = []
        if docs.pos_order_id:

            pos_id = self.env["pos.order"].search([])
            pos_obj = pos_id.filtered(lambda x: x.id == docs.pos_order_id.id)
            sales_person = pos_obj.custom_salesperson_id.name
            invoice_num = pos_obj.account_move.name
            quotation_num = pos_obj.lines.sale_order_origin_id.name
            order_num = pos_obj.lines.sale_order_origin_id.name
            bill_to_name = pos_obj.account_move.partner_id.name
            bill_to_street = pos_obj.account_move.partner_id.street
            bill_to_street2 = pos_obj.account_move.partner_id.street2
            bill_to_city = pos_obj.account_move.partner_id.city
            bill_to_zip = pos_obj.account_move.partner_id.zip
            bill_to_state = pos_obj.account_move.partner_id.state_id.name
            bill_to_country = pos_obj.account_move.partner_id.country_id.name
            bill_to_phone = pos_obj.account_move.partner_id.phone
            values = {
                "sales_person": sales_person,
                "invoice_num": invoice_num,
                "quotation_num": quotation_num,
                "order_num": order_num,
                "bill_to_name": bill_to_name,
                "bill_to_street": bill_to_street,
                "bill_to_street2": bill_to_street2,
                "bill_to_city": bill_to_city,
                "bill_to_zip": bill_to_zip,
                "bill_to_state": bill_to_state,
                "bill_to_country": bill_to_country,
                "bill_to_phone": bill_to_phone,
            }
            val.append(values)

        return {"doc_ids": docs.ids, "doc_model": "pos.order.line", "data": data, "docs": docs, "vals": val}

from datetime import datetime
import string
from odoo import models, fields


class BestSellerReportxlsx(models.AbstractModel):
    _name = "report.bi_best_seller_report.best_seller_report_xlsx"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, lines):
        sheet = workbook.add_worksheet("Best Seller Report")
        num_fmt = workbook.add_format({"num_format": "#,###"})
        bold = workbook.add_format({"bold": True, "text_wrap": True})
        text = workbook.add_format({"text_wrap": True})
        start_date = data["form"]["start_date"]
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = data["form"]["end_date"]
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        today_date = fields.Date.today()
        m = list(string.ascii_uppercase)
        n = 14
        warehouse_id = self.env["stock.warehouse"].search([])

        row = 4
        sheet.write("A%s" % row, "Product", bold)
        sheet.write("B%s" % row, "Description", bold)
        sheet.write("C%s" % row, "Color Code", bold)
        sheet.write("D%s" % row, "Brand Code", bold)
        sheet.write("E%s" % row, "Category", bold)
        sheet.write("F%s" % row, "Model No", bold)
        sheet.write("G%s" % row, "Last Sell Price", bold)
        sheet.write("H%s" % row, "Sell Price", bold)
        sheet.write("I%s" % row, "Group Code", bold)
        sheet.write("J%s" % row, "Sub Group Code", bold)
        sheet.write("K%s" % row, "Cost Price", bold)
        sheet.write("L%s" % row, "SELL MGN %", bold)
        sheet.write("M%s" % row, "Total Sale Qty", bold)
        sheet.write("N%s" % row, "Last Received Date", bold)
        for warehouse in warehouse_id:
            sheet.write("%s%s" % (m[n], row), warehouse.name, bold)
            n += 1
        sheet.set_column("A:A", 15)
        sheet.set_column("B:B", 18)
        sheet.set_column("C:C", 13)
        sheet.set_column("D:D", 15)
        sheet.set_column("E:E", 15)
        sheet.set_column("F:F", 15)
        sheet.set_column("G:G", 15)
        sheet.set_column("H:H", 15)
        sheet.set_column("I:I", 15)
        sheet.set_column("J:J", 15)
        sheet.set_column("K:K", 15)
        sheet.set_column("L:L", 15)
        sheet.set_column("M:M", 15)
        sheet.set_column("N:N", 15)
        sheet.set_column("O:O", 15)
        sheet.set_column("P:P", 15)
        domain = []
        if start_date:
            domain.append(["move_id.invoice_date", ">=", start_date])
        if end_date:
            domain.append(["move_id.invoice_date", "<=", end_date])
            invoice_obj = self.env["account.move.line"].search(domain)
            product_ids = invoice_obj.mapped("product_id")
            row = row + 1
            total_sale_qty = 0
            for product in product_ids:
                sheet.write("A%s" % row, product.name if product.name else "", text)
                sheet.write("B%s" % row, product.name if product.name else "", text)
                sheet.write("C%s" % row, product.color_code_id.code if product.color_code_id.code else "", text)
                sheet.write("D%s" % row, product.brand_code_id.code if product.brand_code_id.code else "", text)
                sheet.write("E%s" % row, product.categ_id.name if product.categ_id.name else "", text)
                sheet.write("F%s" % row, product.default_code if product.default_code else "", text)
                invoice = self.env["account.move"].search([])
                invoice_obj_date = invoice.filtered(lambda x: x.invoice_date)
                record = invoice_obj_date.filtered(lambda x: x.state == "posted").sorted(key=lambda x: x.invoice_date)
                last_sell_price = record.invoice_line_ids.filtered(lambda x: x.product_id == product).mapped(
                    "price_unit"
                )
                if last_sell_price:
                    sheet.write("G%s" % row, round(last_sell_price[-1], 2) if last_sell_price else "", num_fmt)
                for rec in invoice_obj:
                    sell_price = rec.company_id.partner_id.property_product_pricelist.item_ids.filtered(
                        lambda x: x.product_tmpl_id == product.product_tmpl_id
                    ).mapped("fixed_price")
                if sell_price:
                    sheet.write("H%s" % row, round(sell_price[0], 2) if sell_price else "", num_fmt)
                sheet.write("I%s" % row, product.group_code_id.code if product.group_code_id.code else "", text)
                sheet.write("J%s" % row, product.sub_group_code_id.code if product.sub_group_code_id.code else "", text)
                sheet.write("K%s" % row, round(product.standard_price, 2) if product.standard_price else "", num_fmt)
                total_sales_price = 0
                if last_sell_price:
                    total_sales_price = (last_sell_price[0]) * (rec.quantity)
                total_cost_price = (product.standard_price) * (rec.quantity)
                product_margin = 0
                if total_sales_price != 0:
                    product_margin = ((total_sales_price - total_cost_price) / total_sales_price) * 100.0
                sheet.write("L%s" % row, round(product_margin, 2) if product_margin else "", num_fmt)
                total_sale_qty = product.sales_count
                sheet.write("M%s" % row, round(total_sale_qty, 2) if total_sale_qty else "", num_fmt)
                purchase_obj = self.env["purchase.order.line"].search([("product_id", "=", product.id)])
                last_received_date = 0
                if purchase_obj:
                    last_received_date = purchase_obj.order_id.picking_ids.filtered(
                        lambda x: x.move_ids_without_package.product_id == product
                    ).mapped("date_done")
                    last_received_date[0] = last_received_date[0].strftime("%d/%m/%Y")
                sheet.write("N%s" % row, last_received_date[0] if last_received_date else "", text)
                n = 14
                for warehouse in warehouse_id:
                    product_available_qty = product.with_context(
                        {"warehouse": warehouse.id}, {"to_date": today_date}
                    ).qty_available
                    sheet.write(
                        "%s%s" % (m[n], row), round(product_available_qty, 2) if product_available_qty else "", num_fmt
                    )
                    n += 1
                row += 1

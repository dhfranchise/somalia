from odoo import fields, models
import base64
import xlrd
import os


class SalePriceUpdateWizard(models.TransientModel):
    _name = "sale.price.update.wizard"
    _description = "Sale Price Update Wizard"

    filename = fields.Char(string="File name")
    csv_file = fields.Binary("Upload File", attachment=True)
    # line_ids = fields.One2many('sale.price.lines', 'top_id', string='Products')

    def generate_update(self):
        if self.csv_file:
            file_value = self.csv_file.decode("utf-8")
            filename, FileExtension = os.path.splitext(self.filename)
            if FileExtension == ".csv":
                input_file = base64.b64decode(file_value)
                lst = []
                for loop in input_file.decode("utf-8"):
                    lst.append(loop)
                lsts = input_file.decode("utf-8").split("\n")
                lsts.pop(0)
                # print (sdf)
                for rec in lsts:
                    if rec:
                        code = rec.split(",")
                        product_id = self.env["product.product"].search([("barcode", "=", code[0])])
                        product_id.write(
                            {
                                "lst_price": code[1],
                            }
                        )
            else:
                wb = xlrd.open_workbook(file_contents=base64.decodestring(self.csv_file))
                product_id_rno = 0
                lst_price_rno = 1
                for sheet in wb.sheets():
                    for row in range(1, sheet.nrows):
                        barcode = str(sheet.cell(row, product_id_rno).value).split(".")[0]
                        product_id = self.env["product.product"].search([("barcode", "=", barcode)])
                        lst_price = sheet.cell(row, lst_price_rno).value
                        product_id.write(
                            {
                                "lst_price": lst_price,
                            }
                        )

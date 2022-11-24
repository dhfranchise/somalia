import logging
import tempfile
import binascii
import xlrd
import io
import math
from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, fields, exceptions, _

_logger = logging.getLogger(__name__)

try:
    import csv
except ImportError:
    _logger.debug("Cannot `import csv`.")
try:
    pass
except ImportError:
    _logger.debug("Cannot `import xlwt`.")
try:
    pass
except ImportError:
    _logger.debug("Cannot `import cStringIO`.")
try:
    import base64
except ImportError:
    _logger.debug("Cannot `import base64`.")


class ProductPricelist(models.TransientModel):
    _name = "import.product.pricelist"
    _description = "Import Product Pricelist"

    file = fields.Binary("File")
    import_option = fields.Selection([("csv", "CSV File"), ("xls", "XLS File")], string="Select", default="csv")
    import_prod_option = fields.Selection(
        [("name", "Name"), ("code", "Internal Reference"), ("barcode", "Barcode")],
        string="Select Product By",
        default="name",
    )

    def make_product_pricelist(self, values):
        prod_pricelist_obj = self.env["product.pricelist"]
        product_templ_obj = self.env["product.template"]
        DATETIME_FORMAT = "%Y-%m-%d"
        product = math.trunc(int(float(values["product"]))) if type(values["product"]) == "int" else values["product"]
        product = str(product)
        pricelist = values["pricelist"].lower()
        price = values["price"].lower()
        min_qty = values["min_qty"] or 1
        datetime.now().strftime("%Y-%m-%d")
        st_dt = False
        ed_dt = False
        if values.get("start_dt"):
            st_dt = datetime.strptime(values.get("start_dt"), DATETIME_FORMAT)
        if values.get("end_dt"):
            ed_dt = datetime.strptime(values.get("end_dt"), DATETIME_FORMAT)
        find_product = False
        company_obj = self.env["res.company"].search([("name", "=", values.get("company"))], limit=1)
        if company_obj:
            company_id = company_obj.id
        else:
            company_id = False
        currency_obj = self.env["res.currency"].search([("name", "=", values.get("currency"))], limit=1)
        if currency_obj:
            currency_id = currency_obj.id
        else:
            currency_id = False
        if values.get("company"):
            if not company_obj:
                raise ValidationError(_(' "%s" Company is not available.') % values.get("company"))
        if values.get("currency"):
            if not currency_obj:
                raise ValidationError(_(' "%s" Currency is not available.') % values.get("currency"))
        if pricelist and price:
            if self.import_prod_option == "barcode":
                find_product = product_templ_obj.search([("barcode", "=", product)])
            elif self.import_prod_option == "code":
                find_product = product_templ_obj.search([("default_code", "=", product)])
            else:
                find_product = product_templ_obj.search([("name", "=ilike", product.lower())])
            if find_product:
                if not pricelist:
                    raise ValidationError(_("Please fill the pricelist column.") % pricelist)
                else:
                    get_pricelist = False
                    pricelist_exist = prod_pricelist_obj.search(
                        [
                            ("name", "=ilike", pricelist),
                            ("company_id", "=", company_id),
                            ("currency_id", "=", currency_id),
                        ]
                    )
                    if pricelist_exist:
                        product_ids = pricelist_exist.item_ids.mapped("product_tmpl_id")
                        if find_product in product_ids:
                            for item in pricelist_exist.item_ids:
                                if item.product_tmpl_id.id == find_product.id:
                                    item.write(
                                        {
                                            "fixed_price": price,
                                            "min_quantity": min_qty,
                                            "date_start": st_dt,
                                            "date_end": ed_dt,
                                            "applied_on": "1_product",
                                        }
                                    )
                        else:
                            item_list = {
                                "pricelist_id": pricelist_exist.id,
                                "fixed_price": price,
                                "min_quantity": min_qty,
                                "date_start": st_dt,
                                "date_end": ed_dt,
                                "name": find_product.name,
                                "applied_on": "1_product",
                                "product_tmpl_id": find_product.id,
                            }
                            self.env["product.pricelist.item"].create(item_list)
                    else:
                        product_pricelist = {
                            "name": values["pricelist"],
                            "company_id": company_id,
                            "currency_id": currency_id,
                        }

                        get_pricelist = prod_pricelist_obj.create(product_pricelist)

                        item_list = {
                            "pricelist_id": get_pricelist.id,
                            "fixed_price": price,
                            "min_quantity": min_qty,
                            "date_start": st_dt,
                            "date_end": ed_dt,
                            "name": find_product.name,
                            "applied_on": "1_product",
                            "product_tmpl_id": find_product.id,
                        }
                        self.env["product.pricelist.item"].create(item_list)
        else:
            raise ValidationError(_("Pricelist or price are required."))

    def find_date(self, date):
        DATETIME_FORMAT = "%Y-%m-%d"
        try:
            i_date = datetime.strptime(date, DATETIME_FORMAT).date()
        except Exception:
            raise ValidationError(_("Wrong Date Format. Date Should be in format YYYY-MM-DD."))
        return i_date

    def import_product_pricelist(self):
        if self.import_option == "csv":
            if self.file:
                keys = ["product", "pricelist", "price", "min_qty", "start_dt", "end_dt", "company", "currency"]
                try:
                    csv_data = base64.b64decode(self.file)
                    data_file = io.StringIO(csv_data.decode("utf-8"))
                    data_file.seek(0)
                    file_reader = []
                    csv_reader = csv.reader(data_file, delimiter=",")
                    file_reader.extend(csv_reader)
                except Exception:
                    raise exceptions.ValidationError(_("Invalid file!"))
                values = {}
                for i in range(len(file_reader)):
                    field = list(map(str, file_reader[i]))
                    values = dict(zip(keys, field))
                    if values:
                        if i == 0:
                            continue
                        else:
                            self.find_date(values.get("start_dt"))
                            self.find_date(values.get("end_dt"))

                            values.update({"option": self.import_option})
                            self.make_product_pricelist(values)
            else:
                raise ValidationError(_("Please Seelect a file."))
        else:
            if self.file:
                try:
                    fp = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
                    fp.write(binascii.a2b_base64(self.file))
                    fp.seek(0)
                    values = {}
                    workbook = xlrd.open_workbook(fp.name)
                    sheet = workbook.sheet_by_index(0)
                except Exception:
                    raise exceptions.ValidationError(_("Invalid file!"))
                for row_no in range(sheet.nrows):
                    if row_no <= 0:
                        pass
                    else:
                        line = list(
                            map(
                                lambda row: isinstance(row.value, bytes)
                                and row.value.encode("utf-8")
                                or str(row.value),
                                sheet.row(row_no),
                            )
                        )
                        start_date_string = False
                        end_dt_string = False

                        if line[4]:
                            start_dt = int(float(line[4]))
                            start_dt_datetime = datetime(*xlrd.xldate_as_tuple(start_dt, workbook.datemode))
                            start_date_string = start_dt_datetime.date().strftime("%Y-%m-%d")
                        if line[5]:
                            end_dt = int(float(line[5]))
                            end_dt_datetime = datetime(*xlrd.xldate_as_tuple(end_dt, workbook.datemode))
                            end_dt_string = end_dt_datetime.date().strftime("%Y-%m-%d")
                        min_qty = 1
                        if line[3]:
                            min_qty = int(float(line[3]))
                        values.update(
                            {
                                "product": line[0],
                                "pricelist": line[1],
                                "price": line[2],
                                "min_qty": min_qty,
                                "start_dt": start_date_string,
                                "end_dt": end_dt_string,
                                "company": line[6],
                                "currency": line[7],
                            }
                        )
                        self.make_product_pricelist(values)
            else:
                raise ValidationError(_("Please Seelect a file."))

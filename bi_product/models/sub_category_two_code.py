import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiSubCategoryTwoCode(models.Model):
    _name = "bi.sub.category.two.code"
    _description = "Sub Category Two Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

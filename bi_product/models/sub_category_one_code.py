import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiSubCategoryOneCode(models.Model):
    _name = "bi.sub.category.one.code"
    _description = "Sub Category One Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

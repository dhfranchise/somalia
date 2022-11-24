import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiSubCategoryThreeCode(models.Model):
    _name = "bi.sub.category.three.code"
    _description = "Sub Category Three Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

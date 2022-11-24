import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiColorCode(models.Model):
    _name = "bi.color.code"
    _description = "Color Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

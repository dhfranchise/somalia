import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiSizeCode(models.Model):
    _name = "bi.size.code"
    _description = "Size Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiDivisionCode(models.Model):
    _name = "bi.division.code"
    _description = "Division Code"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

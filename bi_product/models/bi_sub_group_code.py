import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiSubGroupCode(models.Model):
    _name = "bi.sub.group.code"
    _description = "Sub Group COde"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

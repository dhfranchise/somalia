import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class BiBudgetCategory(models.Model):
    _name = "bi.budget.category"
    _description = "Budget Category"
    _rec_name = "code"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

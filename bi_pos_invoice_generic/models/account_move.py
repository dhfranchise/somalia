from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    session_id = fields.Many2one("pos.session", string="Session", readonly=True, copy=False)
    efg_no = fields.Char(string="EFG No", copy=False)

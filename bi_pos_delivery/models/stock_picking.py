import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    driver_name = fields.Char(string="Name of the Driver")
    vehicle_no = fields.Char(string="Vehicle No")
    mobile_no = fields.Char(string="Mobile No")
    transporter = fields.Char(string="Transporter")
    route = fields.Char(string="Route")
    carpentry_name = fields.Char(string="Carpentry Person Name")
    carpentry_phone = fields.Char(string="Carpentry Person Phone")

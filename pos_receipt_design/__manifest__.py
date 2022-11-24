#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
    "name": "POS Receipt Design",
    "summary": """This module allows to make custom POS Receipt.""",
    "category": "Point Of Sale",
    "version": "1.0.2",
    "author": "Webkul Software Pvt. Ltd.",
    "license": "OPL-1",
    "website": "https://store.webkul.com",
    "description": """Odoo POS Receipt Design
  Custom Receipt
  Design Receipt
  Custom XML Receipt
  POS Receipt
  POS Ticket""",
    "live_test_url": "http://odoodemo.webkul.com/?module=pos_receipt_design&custom_url=/pos/auto",
    "depends": ["point_of_sale"],
    "data": [
        "security/ir.model.access.csv",
        "demo/demo.xml",
        "views/pos_config_view.xml",
        "views/receipt_design_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "/pos_receipt_design/static/src/js/pos_export_printing.js",
            "/pos_receipt_design/static/src/js/models.js",
        ],
    },
    "qweb": ["static/src/xml/pos.xml"],
    "images": ["static/description/Odoo_POS-Receipt-Design_POS-Receipt-Design-Banner.png"],
    "application": True,
    "installable": True,
    "auto_install": False,
    "price": 79,
    "currency": "USD",
    "pre_init_hook": "pre_init_check",
}

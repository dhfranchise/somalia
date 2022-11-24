{
    "name": "Delivery note report",
    "version": "15.0.1.0.0",
    "category": "account",
    "summary": "Delivery note Pdf report ",
    "license": "AGPL-3",
    "description": """
        This module will generate a delivery note printout .
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://www.bassaminfotech.com",
    "depends": ["stock", "account", "sale", "purchase", "bi_pos_salesperson", "bi_tax_invoice"],
    "data": [
        "report/paperformat.xml",
        "report/header.xml",
        "report/delivery_note.xml",
        "report/report.xml",
        "views/stock_picking.xml",
    ],
    "installable": True,
    "auto_install": False,
}

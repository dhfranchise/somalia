{
    "name": "POS Invoice Print",
    "summary": """
        Point of sale invoice print.""",
    "description": """
        Point of sale invoice print.
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale", "bi_tax_invoice"],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_invoice_print/static/src/js/model.js",
            "bi_pos_invoice_print/static/src/js/receipt_screen.js",
            "bi_pos_invoice_print/static/src/js/TicketScreen/InvoiceButton.js",
        ],
        "web.assets_qweb": [
            "bi_pos_invoice_print/static/src/xml/**/*",
        ],
    },
    "pre_init_hook": "pre_init_check",
}

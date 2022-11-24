{
    "name": "Tax Invoice Report",
    "summary": """
        Generate Tax Invoice Report""",
    "description": """
       Generate Pdf of Tax Invoice Report
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Reports",
    "version": "15.0.1.0.0",
    "depends": ["account", "point_of_sale", "delivery", "sale", "bi_pos_invoice_generic"],
    "data": [
        "reports/paperformat.xml",
        "reports/report.xml",
        "reports/tax_invoice.xml",
        "views/product.xml",
        "views/account_move.xml",
        "views/sale_order.xml",
    ],
}

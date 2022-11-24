{
    "name": "Point of Sale Auto Invoice Check",
    "summary": """
        Point of Sale Auto Invoice Check.""",
    "description": """
        Point of Sale Auto Invoice Check.
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale"],
    "data": [
        "views/pos_config_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_auto_invoice/static/src/js/PaymentScreen.js",
        ],
    },
}

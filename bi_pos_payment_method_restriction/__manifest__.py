{
    "name": "POS Payment Method Restriction",
    "summary": """
        POS Payment Method Restriction.""",
    "description": """
        POS Payment Method Restriction.
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
            "bi_pos_payment_method_restriction/static/src/js/PaymentScreen.js",
        ],
    },
}

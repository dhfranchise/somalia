{
    "name": "POS Salesperson",
    "summary": """POS Salesperson""",
    "description": """POS Salesperson""",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale", "pos_hr"],
    "data": [
        "views/pos_config.xml",
        "views/pos_order.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_salesperson/static/src/js/models.js",
            "bi_pos_salesperson/static/src/js/PaymentScreen.js",
            "bi_pos_salesperson/static/src/js/SalePerson.js",
        ],
        "web.assets_qweb": [
            "bi_pos_salesperson/static/src/xml/**/*",
        ],
    },
}

{
    "name": "POS Button",
    "summary": """Button in POS""",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_button/static/src/js/pos_button.js",
        ],
        "web.assets_qweb": [
            "bi_pos_button/static/src/xml/**/*",
        ],
    },
}

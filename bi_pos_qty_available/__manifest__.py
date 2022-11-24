{
    "name": "POS Product Available",
    "summary": """
        Helps to see the stock on hand in product.""",
    "description": """
        Helps to see the stock on hand in product.""",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "installable": True,
    "auto_install": False,
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "/bi_pos_qty_available/static/src/css/qty_available.css",
            "/bi_pos_qty_available/static/src/js/qty_available.js",
        ],
        "web.assets_qweb": [
            "bi_pos_qty_available/static/src/xml/**/*",
        ],
    },
    "pre_init_hook": "pre_init_check",
}

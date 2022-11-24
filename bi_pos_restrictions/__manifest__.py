{
    "name": "Point of Sale Restrictions",
    "summary": """
        Point of Sale Restrictions.""",
    "description": """
        Point of Sale Restrictions.
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["bi_pos_qty_available"],
    "data": [
        "views/pos_config_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_restrictions/static/src/js/NumpadWidget.js",
            "bi_pos_restrictions/static/src/js/ProductScreen.js",
        ],
    },
}

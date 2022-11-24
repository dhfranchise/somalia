{
    "name": "POS Line Discount Selection",
    "summary": """
        POS Line Discount Selection.""",
    "description": """
        POS Line Discount Selection.
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
            "bi_pos_line_discount_selection/static/src/css/discount_popup.css",
            "bi_pos_line_discount_selection/static/src/js/models.js",
            "bi_pos_line_discount_selection/static/src/js/DiscountSelectionPopup.js",
            "bi_pos_line_discount_selection/static/src/js/NumpadWidget.js",
            "bi_pos_line_discount_selection/static/src/js/ProductScreen.js",
            "bi_pos_line_discount_selection/static/src/js/ClearDiscount.js",
        ],
        "web.assets_qweb": [
            "bi_pos_line_discount_selection/static/src/xml/**/*",
        ],
    },
}

{
    "name": "POS Credit Reconcile",
    "summary": """
        POS Credit Reconcile""",
    "description": """
        POS Credit Reconcile
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale"],
    "data": [
        # "views/pos_order_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_credit_reconcile/static/src/js/credit_reconcile.js",
            "bi_pos_credit_reconcile/static/src/js/receipt_confirmation_popup.js",
        ],
        "web.assets_qweb": [
            "bi_pos_credit_reconcile/static/src/xml/**/*",
        ],
    },
}

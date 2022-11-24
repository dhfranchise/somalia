{
    "name": "POS Payment Pivot",
    "summary": """
        POS Payment Pivot.""",
    "description": """
        POS Payment Pivot.
    """,
    "version": "15.0.1.0.0",
    "category": "Point of Sale",
    "author": "BassamInfotech",
    "license": "OPL-1",
    "depends": ["point_of_sale", "account", "bi_tax_invoice"],
    "website": "https://www.bassaminfotech.in",
    "data": [
        "views/pos_payment_view.xml",
        "views/pos_order_view.xml",
        "views/account_invoice_report.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "bi_pivot_reports/static/src/js/dates.js",
            ("replace", "web/static/lib/luxon/luxon.js", "bi_pivot_reports/static/src/js/luxon.js"),
        ],
    },
    "post_load": "post_load_hook",
}

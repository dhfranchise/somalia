{
    "name": "POS Payment Reference",
    "summary": """
        POS Payment Reference""",
    "description": """
        POS Payment Reference
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_payment_reference/static/src/css/payment_reference.css",
            "bi_pos_payment_reference/static/src/js/models.js",
            "bi_pos_payment_reference/static/src/js/Popups/ReferencePopup.js",
            "bi_pos_payment_reference/static/src/js/PaymentScreen/PaymentScreen.js",
            "bi_pos_payment_reference/static/src/js/TicketScreen/TicketScreen.js",
            "bi_pos_payment_reference/static/src/js/ReceiptScreen/OrderReceipt.js",
        ],
        "web.assets_qweb": [
            "bi_pos_payment_reference/static/src/xml/**/*",
        ],
    },
    "data": [
        "views/pos_config.xml",
        "views/pos_order.xml",
        "views/pos_payment_method.xml",
        "views/pos_payment.xml",
    ],
}

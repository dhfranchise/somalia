{
    "name": "POS Default Customer",
    "summary": "Set Default Customer in POS",
    "description": "Set Default Customer in POS",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Point of Sale",
    "version": "15.0.1.0.0",
    "depends": ["point_of_sale"],
    "data": [
        "views/pos_config_view.xml",
        "views/res_partner_view.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "bi_pos_default_customer/static/src/js/models.js",
        ],
    },
}

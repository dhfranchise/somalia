{
    "name": "bi_barcode",
    "summary": "",
    "description": "",
    "author": "Bassam Infotech LLP",
    "website": "http://www.bassaminfotech.com",
    "category": "Uncategorized",
    "version": "15.0.1.0.0",
    "depends": ["base", "product", "stock"],
    "license": "OPL-1",
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/views.xml",
        "views/sequence.xml",
        "wizards/sale_price_update_wizard_views.xml",
    ],
    "external_dependencies": {"python": ["xlrd"]},
}

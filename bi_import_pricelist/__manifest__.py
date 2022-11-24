{
    "name": "Import Product Pricelist from Excel or CSV File",
    "summary": "Import Product pricelist from Excel or CSV File",
    "description": """Import pricelist from Excel or CSV File""",
    "version": "15.0.1.0.0",
    "author": "Bassam Infotech LLP",
    "website": "https://www.bassaminfotech.com",
    "license": "OPL-1",
    "category": "stock",
    "depends": ["stock", "web"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/product_pricelist_wizard.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "bi_import_pricelist/static/src/js/import_pricelist_list.js",
        ],
        "web.assets_qweb": [
            "bi_import_pricelist/static/src/xml/import_pricelist_list.xml",
        ],
    },
    "external_dependencies": {"python": ["xlrd"]},
}

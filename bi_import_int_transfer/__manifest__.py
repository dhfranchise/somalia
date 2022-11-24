{
    "name": "Import Internal Transfer from CSV/Excel file",
    "summary": "Import internal transfer app, internal transfer from csv, internal transfer from excel.",
    "description": """This module useful to import internal transfer from csv/excel.""",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Warehouse",
    "version": "15.0.1.0.0",
    "depends": ["sh_message", "stock"],
    "data": [
        "security/import_int_transfer_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_int_transfer_wizard.xml",
        "views/stock_view.xml",
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
}

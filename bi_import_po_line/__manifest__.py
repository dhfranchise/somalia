{
    "name": "Import Purchase Order Lines from CSV/Excel file",
    "summary": "Import Purchase Order Lines from CSV/Excel file.",
    "description": """Import Purchase Order Lines from CSV/Excel file.""",
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Purchase",
    "version": "15.0.1.0.0",
    "depends": ["purchase", "sh_message"],
    "data": [
        "security/import_pol_security.xml",
        "security/ir.model.access.csv",
        "wizard/import_pol_wizard.xml",
        "views/purchase_order_view.xml",
    ],
    "external_dependencies": {
        "python": ["xlrd"],
    },
}

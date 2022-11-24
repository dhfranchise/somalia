{
    "name": "bi_best_seller_report",
    "summary": """
        Generate Best Seller Report from a wizard""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Reports",
    "version": "0.1",
    "depends": ["base", "account", "report_xlsx"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/best_seller_wizard.xml",
        "report/best_seller_report.xml",
    ],
}

{
    "name": "bi_quotation",
    "summary": """
        Generate Sales quotation""",
    "description": """
        Long description of module's purpose
    """,
    "author": "Bassam Infotech LLP",
    "website": "https://bassaminfotech.com",
    "support": "sales@bassaminfotech.com",
    "license": "OPL-1",
    "category": "Reporting",
    "version": "15.0.0.1",
    "depends": ["base", "sale", "delivery", "bi_delivery_note_printout"],
    "data": [
        "report/header.xml",
        "report/quot_paperformat.xml",
        "report/quotation_template.xml",
        "report/report_action_quotation.xml",
        "views/sale.xml",
    ],
}

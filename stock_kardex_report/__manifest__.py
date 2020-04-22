# Copyright 2020, Jarsa Sistemas, S.A. de C.V.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lpgl.html).

{
    "name": "Stock Kardex Report",
    "summary": "Generate Kardex Report",
    "version": "13.0.1.0.0",
    "category": "Reports",
    "author": "Jarsa Sistemas, S.A. de C.V.," "Odoo Community Association (OCA)",
    "website": "https://www.jarsa.com.mx",
    "license": "LGPL-3",
    "depends": ["stock"],
    "data": [
        "views/stock_kardex_report_views.xml",
        "wizard/stock_kardex_report_wizard_view.xml",
        "security/ir.model.access.csv",
    ],
}

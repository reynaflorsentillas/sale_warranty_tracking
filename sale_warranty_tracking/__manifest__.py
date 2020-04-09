# -*- coding: utf-8 -*-
{
    'name': "sale_warranty_tracking",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "OmniTechnical Global Solutions, Inc",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','sales_team','stock','sale_management'],

    # always loaded
    'data': [
        'reports/warranty_analysis.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/warranty_period.xml',                
        'views/sale_warranty_views.xml',
        'views/product_warranty_period.xml',
        'views/product_template.xml',
        'views/sale_order_views.xml',
        'wizard/sale_warranty_add_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "m.tan",

    'summary': """
        intern test 2""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/security.xml',
        'views/product_product_view.xml',
        #'views/sale_order_view.xml',
        'views/templates.xml',
        'wizard/update_product_warranty_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}

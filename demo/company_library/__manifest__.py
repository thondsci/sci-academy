# -*- coding: utf-8 -*-
{
    'name': "company_library_2",

    'summary': """
        Thư viện của công ty X""",

    'description': """
        Thư viện của công ty X, nơi các nhân viên có thể mượn và đọc sách
    """,

    'author': "Đỗ Duy CHiến",
    'website': "http://www.X.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Application',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/BookCategory.xml',
        'views/Books.xml',
        'views/tickets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
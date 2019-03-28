# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """Quản lý thư viện""",

    'description': """
        Thư viện nơi các nhân viên có thể mượn và đọc sách
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        'views/book_category_view.xml',
        'views/books_view.xml',
        'views/tickets_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

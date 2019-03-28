# -*- coding: utf-8 -*-
{
    'name': "quanlythuvien",

    'summary': """Thư viện của công ty""",

    'description': """
        Nơi các nhân viên có thể mượn và đọc sách
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views_tv.xml',
        'views/views_sach.xml',
        'views/views_loaisach.xml',
        'views/views_ngonngu.xml',
        'views/views_phieumuon.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
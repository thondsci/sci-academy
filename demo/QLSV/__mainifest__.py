# -*- coding: utf-8 -*-
{
    'name': "Quản lý điểm sinh viên",

    'summary': """Quản lý sinh viên""",

    'description': """
        Thông tin về sinh viên 
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
       'views/Lop.xml',
       'views/MonHoc.xml',
        'views/PhieuDiem.xml',
        'views/SinhVien.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
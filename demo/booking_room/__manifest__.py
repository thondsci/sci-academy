# -*- coding: utf-8 -*-
{
    'name': "booking_room",

    'summary': """
       Module quản lý khách sạn, nhà nghỉ vừa và nhỏ""",

    'description': """
        Quản lý phòng nhà nghỉ, khách sạn vừa và nhỏ
    """,

    'author': "Đỗ Duy Chiến",
    'website': "------",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Quản lý',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',

        # 'views/templates.xml',
        'views/views.xml',
        'views/guest_room.xml',
        'views/service.xml',
        'views/bills.xml',
        # 'views/service_use.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

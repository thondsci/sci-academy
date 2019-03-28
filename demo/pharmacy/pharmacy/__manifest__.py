# -*- coding: utf-8 -*-
{
    'name' : "pharmacy",
    'summary' : """ Lịch phòng khám  """,
    'description': """Quản lý lịch khám bệnh của bác sĩ """,
    'author': "Đỗ Duy Chiến",
    'website': "http://www.DDC.com",
    'category': 'Application',
    'version': '0.9',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/category_view.xml',
        'views/products.xml',
        'views/productDetail.xml',
        'views/employee.xml',
        'views/phieu_nhapkho.xml',
        'views/bills.xml',
    ],
    'demo' : [],

}

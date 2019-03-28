# -*- coding: utf-8 -*-
{
    'name' : "hospital_management",
    'summary' : """ Lịch phòng khám  """,
    'description': """Quản lý lịch khám bệnh của bác sĩ """,
    'author': "Đỗ Duy Chiến",
    'website': "http://www.DDC.com",
    'category': 'Application',
    'version': '0.9',
    'depends': ['base'],
    'data' : [
        'views/doctor.xml',
        'views/patient.xml',
        'views/service.xml',
        'views/drug.xml',
        'views/bill.xml',
        'views/bill_drug.xml',
        'views/rv.xml',
        #'views/purchase.xml',
        #'views/print.xml',
    ],
    'demo' : [],

}
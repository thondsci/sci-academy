# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import datetime

class bill(models.Model):
    _name = 'bill'
    name_patient = fields.Many2one('patient', string="Tên bệnh nhân")
   # field.Integer(string="SST", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field')
    name = fields.Integer(string = "Phiếu khám bệnh số :",default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    date = fields.Datetime(string='thời gian khám : ',default =datetime.now())
    TSB = fields.Char('Tiền sử bệnh : ')
    height = fields.Integer('Chiều cao : ')
    weight = fields.Integer('Cân nặng : ')
    blood_pressure = fields.Char('Huyết áp : ')
    name_doctor = fields.Many2one('doctor',string="Tên bác sĩ : ")
    diagnose = fields.Char('chuẩn đoán bệnh : ')
    service_use = fields.One2many('suggestion','line','Yêu cầu ')
    bill_drug = fields.Many2one('bill_purchase_all',string="Hóa đơn thuốc")
    nv = fields.Boolean('Yêu cầu nhập viện: ')
    rv = fields.Many2one('ravien',string="nhập viện")
    ttt = fields.Integer(compute="get_total",string="Viện phí")
    BHYT = fields.Boolean('Yêu cầu thanh toán bằng BHYT : ')
    code_BHYT = fields.Char('Mã bảo hiểm y tế : ')
    tt_BHYT = fields.Integer(compute="get_total_2",string='Bảo hiểm y tế thanh toán : ')
    tt = fields.Integer(compute="get_total_2",string='Số tiền bệnh nhân cần thanh toán:')

    # tinh tien vien phi
    @api.depends('service_use','bill_drug')
    def get_total(self):
        for record in self:
            a =0
            if record.service_use:
                for i in record.service_use:
                    a += i.name.price_service

            if record.bill_drug:
                for j in record.bill_drug:
                    a += j.t2
            if record.rv:
                for g in record.rv:
                    a += g.total

            record.ttt = a

    @api.depends('BHYT','tt_BHYT','tt','ttt','name_patient')
    def get_total_2(self):
        for record in self:
            if record.BHYT == True:
                for i in record.name_patient:
                    if i.age <= 6:
                          record.tt_BHYT = record.ttt
                    elif i.age >= 60:
                          record.tt_BHYT = record.ttt*0.95
                    else:
                          record.tt_BHYT = record.ttt*0.8
            record.tt = record.ttt-record.tt_BHYT

class suggest(models.Model):
    _name = 'suggestion'
    line = fields.Many2one('bill')
    name = fields.Many2one('service','Yêu cầu')


# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Patient(models.Model):
    _name = 'patient'

    code_pt = fields.Char('Mã bệnh nhân : ')
    name = fields.Char('Tên bệnh nhân : ')
    age = fields.Integer('Tuổi bệnh nhân : ')
    address = fields.Char('Địa chỉ : ')
    job = fields.Char('Nghề nghiệp : ')
    phone = fields.Char('Số điện thoại : ')
    #pkb = fields.Char(string='phieu kham benh : ',compute='apt')







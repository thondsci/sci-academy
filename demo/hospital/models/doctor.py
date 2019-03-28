# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Doctor(models.Model):
    _name = 'doctor'

    pst = [('1','Bác sĩ'),('2','Y tá')]
    lct = [('1','Ngoại tổng hợp'),('2','Hồi phục chấn thương'),('3','Hồi sức cấp cứu'),('4','Nội')]

    code_dt = fields.Char('Mã nhân viên : ')
    name = fields.Char('Tên nhân viên : ')
    position = fields.Selection(selection=pst,string='Chức vụ ')
    Faculty = fields.Selection(selection=lct,string='Khoa : ')


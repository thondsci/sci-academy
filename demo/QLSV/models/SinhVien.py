# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class SinhVien(models.Model):
    _name = 'sinhvien'

    MSV = fields.Char('Mã sinh viên và tên sinh viên')
    NS = fields.Char('Ngày sinh')
    GT = fields.Char('Giới tính')
    EM = fields.Char('Email ')
    DT = fields.Char('Số điện thoại')
    QQ = fields.Char('Quê quán')
    LOP = fields.Many2one(comodel_name='Lop',string='tên lớp')
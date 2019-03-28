# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from . import MonHoc

class PhieuDiem(models.Model):
    _name = 'phieudiem'

    MSV = fields.One2many(comodel_name='sinhvien',string='Mã sinh viên')
    HK = fields.Char('Học Kỳ')
    NH = fields.Char('Năm học ')
    MH = fields.Selection(selection=MonHoc.MonHoc.TMH,string=' Tên môn học')
    DIEM = fields.Float(string='Điểm môn học')
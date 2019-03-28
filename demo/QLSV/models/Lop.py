# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


nganhhoc = [('1', 'Kinh Tế'), ('2', 'Công nghệ thông tin'),('3','Ngoại Ngữ')]

class Lop(models.Model):
    _name = 'Lop'

    # code = fields.Char('Mã loại Sách')
    TN = fields.Selection(selection=nganhhoc,string='Tên ngành học')
    TL = fields.Char('Tên lớp')
    GC = fields.Char('Ghi chú')

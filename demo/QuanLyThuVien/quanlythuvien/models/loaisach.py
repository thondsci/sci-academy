# -*- coding:utf-8 -*-
from odoo import models,fields,api

class Loai(models.Model):
    _name = 'categorys'

    _maloaisach = fields.Char('Mã loại sách', required = True)
    _theloai = fields.Char('Thể Loại', required = True)
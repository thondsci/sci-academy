# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

AREA = [('1', 'Khu vực 1 - Tầng 1'), ('2', 'Khu vực 2 - Tầng 2')]


class Books(models.Model):
    _name = 'books'

    name_book = fields.Char('Tên Sách')
    author = fields.Char('Tác Giả')
    number_page = fields.Integer('Số Trang')
    category = fields.Many2one(comodel_name='book.ctg', string='Thể loại')
    area = fields.Selection(selection=AREA, string='Khu vực sách')
    # num_in = fields.Integer('Số lượng nhập')
    # num_remain = fields.Integer('Số lượng còn lại')
    # emp_borrow = fields.Many2one('tickets', 'Nhân viên mượn')

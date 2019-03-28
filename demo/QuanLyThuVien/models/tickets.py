# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class Ticket(models.Model):
    _name = 'tickets'

    code_emp = fields.Char('Mã Nhân Viên')
    name_emp = fields.Char('Tên Nhân Viên')
    sdt = fields.Char('Số Điện Thoại')
    date_borrow = fields.Date('Thời gian mượn sách')
    date_pay = fields.Date('Thời gian trả sách')
    line_ids = fields.Many2many(comodel_name='books', relation='tickets', string='Sách Mượn')

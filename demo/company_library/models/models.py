# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookCategory(models.Model):
    _name = 'bookcategory'

    _rec_name = 'name_category'
    name_category = fields.Char('Thể loại sách', size=40)
    description = fields.Html('Mô tả')

class Book(models.Model):
    _name = 'book'

    name = fields.Char('Tên sách', size=70)
    author = fields.Char('Tên tác giả', size=25)
    page = fields.Integer('Số trang')
    category = fields.Many2one('bookcategory', string='Thể loại')
    input_amount = fields.Integer('Số lượng nhập vào thư viện')
    remain_amount = fields.Integer('Số lượng còn lại')
    #remain_amount = fields.Integer(compute='_get_number', string='Số lượng còn lại')
    employee_borrow = fields.Many2one('ticket.book', 'Danh sách nhân viên mượn')

    #def _get_number(self):
    #    remain_amount = input_amount
    #    for record in self:
    #        if record.employee_borrow:
    #            for book in record.employee_borrow:
    #                remain_amount -= input_amount



class ticket(models.Model):
    _name = 'ticket.book'

    _rec_name = 'ma_nv'
    ma_nv = fields.Char('Mã nhân viên', size=6)
    name_nv = fields.Char('Tên nhân viên', size=40)
    sdt = fields.Char('Số điện thoại')
    book_borrow = fields.One2many('tickets_book', 'line', 'Sách đang mượn')
    time_borrow = fields.Datetime('Thời gian mượn')
    time_pay = fields.Datetime('Thời gian trả')


class ticketline(models.Model):
    _name = 'tickets_book'

    line = fields.Many2one('ticket.book', 'Mã nhân viên')
    sach = fields.Many2one('book', 'Sách mượn')
    author1 = fields.Char(compute='_get_author', string='Tên tác giả')

    @api.onchange
    def _get_author(self):
        if self.sach != None:
            self.author1 = self.sach.author
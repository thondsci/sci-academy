# -*- coding:utf-8 -*-

from odoo import models,fields,api
from datetime import datetime

class Tickets(models.Model):
    _name = 'tickets'

    _maphieu = fields.Char('Mã Phiếu Mượn', required = True)
    _nguoimuon = fields.Many2one('tttv', string='Tên Người Mượn', required = True)
    _sach = fields.One2many('muon', '_sachmuon',string='Sách mượn', required = True)
    _date_borrow = fields.Date('Ngày mượn', required = True)
    _date_pay = fields.Date('Ngày trả', required = True)
    _tienmuon = fields.Integer('Tiền Mượn')
    _tientra = fields.Integer('Tiền Đã Trả')

class Muon(models.Model):
    _name = 'muon'

    _phieu = fields.Many2one('tickets')
    _sachmuon = fields.Many2one('books','Tên Sách')
    author1 = fields.Char('Tên giác giả')
    language1 = fields.Char('Ngôn Ngữ')
    category1 = fields.Char('Thể loại')

    @api.onchange
    def onchane_book(self):
        if self._sachmuon != None:
            self.author1 = self._sachmuon.author2
            self.language1 = self._sachmuon.language2
            self.category2 = self._sachmuon.category1
# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Books(models.Model):
    _name = 'books'

    masach = fields.Char("Mã Sách", required = True)
    name_book = fields.Char('Tên sách', required = True)
    author2 = fields.Char('Tác giả', required = True)
    number_page = fields.Integer('Số trang', required = True)
    category2 = fields.Many2one('categorys','Thể Loại', required = True)
    language2 = fields.Many2one('language',string='Ngôn Ngữ', required = True)
    num_in = fields.Integer('Số lượng nhập', required = True)
    num_remain = fields.Integer('Số lượng còn lại', required = True)
    _phieumuon = fields.One2many('muon', '_phieu',string='Mượn ở phiếu')
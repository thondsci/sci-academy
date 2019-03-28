# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime



class BookCategory(models.Model):
    _name = 'book.ctg'

    # code = fields.Char('Mã loại Sách')
    name = fields.Char('Tên loại sách')

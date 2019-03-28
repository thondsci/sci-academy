# -*- coding:utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class MonHoc(models.Model):
    _name = 'monhoc'

    TMH = fields.Char('Tên môn học')
    GC  = fields.Char('Ghi chú')
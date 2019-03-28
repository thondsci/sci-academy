# -*- coding:utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class Signup(models.Model):
    _name = 'tttv'

    _matv = fields.Char('Mã Thành Viên', required = True)
    _ngaydk = fields.Date('Ngày đăng ký', required = True)
    _ngayhethan = fields.Date('Ngày hết hạn', required = True)
    _hoten = fields.Char('Họ và Tên', required = True)
    _ngaysinh = fields.Date('Ngày sinh',)
    _diachi = fields.Char('Địa chỉ')
    _sdt = fields.Char('Số điện thoại', required = True)

# -*- coding: utf-8 -*-
from odoo import models,fields,api
class service(models.Model):
    _name = 'service'
    name = fields.Char('Tên dịch vụ : ')
    price_service = fields.Integer('Giá dịch vụ : ')
    code_service = fields.Char('Mã dịch vụ : ')

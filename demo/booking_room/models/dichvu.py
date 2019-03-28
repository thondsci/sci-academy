# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Service(models.Model):
    _name = 'service'

    name = fields.Char(string="Tên dịch vụ", required=True)
    code_service = fields.Char(string="Mã dịch vụ", required=True)
    price_service = fields.Integer(string="Giá dịch vụ", required=True)
    # price_service = fields.Reference
    # ‘contact’: fields.reference(‘Contact’, [res.partner’, ’Partner’), res.partner.contact’, ’Contact’)], 128)
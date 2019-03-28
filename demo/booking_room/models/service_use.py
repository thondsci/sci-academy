# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Service_use(models.Model):
    _name = 'service_use'

    # roomthue = fields.Many2one('room', string="Phòng thuê")
    # servicesudung = fields.Many2one('service', string="Dịch vụ đã dùng")
    hotennguoimuon = fields.One2many('guest','name', string="Họ tên người dùng")
    price = fields.Char('tổng')



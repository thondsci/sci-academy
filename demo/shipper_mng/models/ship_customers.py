# -*- coding: utf-8 -*-

from odoo import models, fields


class ShipCustomers(models.Model):
    _name = "ship.customers"

    id = fields.Integer(string="Mã khách hàng", Required=True)
    name = fields.Char(string="Tên khách hàng", Required=True)
    phone = fields.Char(string="Số điện thoại", Required=True)
    address = fields.Char(string="Địa chỉ", Required=True)
    distance = fields.Selection([(1, 'Dưới 10km'), (2, '10 - 20km'), (3, '20 - 30km'), (4, 'Trên 30km')],
                                string='Khoảng cách', Required=True)




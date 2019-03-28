# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShipItems(models.Model):
    _name = "ship.items"

    id = fields.Integer(string="Mã hàng", Required=True)
    name = fields.Char(string="Tên mặt hàng", Required=True)
    unit = fields.Char(string="Đơn vị", Required=True)
    price = fields.Integer(string="Giá bán (vnđ)", Required=True)
    weight = fields.Float(string="Khối lượng (kg)", Required=True)
    height = fields.Float(string="Chiều cao đóng gói (cm)", Required=True)
    width = fields.Float(string="Chiều rộng đóng gói (cm)", Required=True)
    length = fields.Float(string="Chiều dài đóng gói (cm)", Required=True)
    volume = fields.Float(compute="_get_volume", string="Thể tích đóng gói (cm3)")
    description = fields.Html(string="Mô tả sản phẩm", size=1000)

    @api.depends("height", "width", "length")
    def _get_volume(self):
        for _ in self:
            _.volume = _.height * _.width * _.length

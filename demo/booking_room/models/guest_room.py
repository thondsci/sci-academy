# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class guest_room(models.Model):
    _name = 'guest'

    name = fields.Char(string="Họ tên", required=True, size=50)
    cmnd = fields.Char(string="Số CMND", required=True, size=12)
    sdt = fields.Char(string="SĐT", required=True, size=10)
    time_in = fields.Datetime(string="Ngày đến")
    time_out = fields.Datetime(string="Ngày trả")
    description = fields.Html("Ghi chú", size=1000)
    # servicesd = fields.One2many('service', string=" Tên dịch vụ")
    servicesd_ids = fields.One2many('room.line', 'line', 'Dịch vụ')
    roomsd = fields.Many2one('room', string="Phòng thuê")

#
class RoomLine(models.Model):
    _name = 'room.line'

    line = fields.Many2one('guest')
    name = fields.Many2one('service', 'Dịch vụ')

    # @api.multi
    # def _get_time_out(self):
    #     t = dt.t().strptime()



# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date as dt


class booking_room(models.Model):
    _name = 'room'

    name = fields.Char(string="Mã phòng", required=True)
    status = fields.Selection([('trống', 'Trống'), ('bận', 'Bận')], string="Trạng thái",
                              compute="_get_status", default="Trống"
                              )
    kind = fields.Selection([('a', 'A'), ('b', 'B'), ('5', 'C'), ('6', 'Vip')],
                            string="Loại phòng", required=True
                            )
    price = fields.Integer(string="Giá phòng", required=True)
    description = fields.Html("Ghi chú")
    guestsd = fields.Many2one('guest', 'Khách thuê')

    @api.multi
    def _get_status(self):
        # Lấy datetime hiện tại theo định dạng mà các trường time được lưu trữ trong cơ sở dữ liệu
        now = dt.now().strftime('%d-%m-%y %H:%M:%S')
       # for room in self:
            # tìm những khách đã đặt phòng ngay bây giờ và có id phòng là hiện tại
       #     guest_in_room = len(
#
         #     self.env['guest'].search([('time_out', '>=', now), ('time_in', '<=', now), ('roomsd', '=', room.name)]))

         #   if guest_in_room:
         #       room.status = 'trống'
         #   else:
          #      room.status = 'bận'
#

# @api.multi
# def roomallocationandfree(self):
#     if self.status == 1:
#         self.status = 2
#     else:
#         self.status = 1

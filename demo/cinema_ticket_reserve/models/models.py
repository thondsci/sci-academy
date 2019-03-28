# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class Movie(models.Model):
    """Danh sách phim"""
    _name = "reserve.movie"

    name = fields.Char("Tên phim")
    description = fields.Text("Nội dung")
    duration = fields.Integer("Độ dài (phút)")


#
#
class ReserveSeat(models.Model):
    """Tạo danh sách ghế, giá vé ghế cho từng lịch chiếu"""
    _name = "reserve.seat"

    schedule_id = fields.Many2one("reserve.schedule", string="Chọn buổi chiếu")
    date = fields.Date("Ngày chiếu")
    time = fields.Char("Buổi chiếu")
    movie = fields.Char("Tên phim")
    @api.onchange("schedule_id")
    def onchange_id(self):
        if self.schedule_id:
            self.date = self.schedule_id.date
            self.time = self.schedule_id.time
            self.movie = self.schedule_id.movie


class ReseveSchedule(models.Model):
    """Tạo lịch chiếu"""
    _name = "reserve.schedule"
    movie = fields.Many2one("reserve.movie", string='Tên phim')
    date = fields.Date("Ngày chiếu")
    time = fields.Selection([("1", "Sáng"), ("2", "Chiều")])
    seat_ids = fields.One2many("reserve.seat", "schedule_id", string="Ghế", readonly=True)

# class ReserveBooking(models.Model):
#     """Tạo phương thức đặt vé"""
#     _name = "reserve.booking"
#     seat_id = fields.Many2many("reserve.seat", "booking_id", string="Id buổi chiếu")
#     movie = fields.Char("Phim")
#     time = fields.Char(related="seat_id.time", string="Suất chiếu")
#     date = fields.Date("Phim")
#     seat = fields.Integer("Số ghế")
#     booking = fields.Integer("Số vé đặt")
#     price = fields.Integer(related="seat_id.price", string="Giá vé")
#     pay = fields.Integer("Giá vé phải trả", compute='total_pay')

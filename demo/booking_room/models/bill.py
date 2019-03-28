# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Bill(models.Model):
    _name = 'bills'

    so_phong = fields.Many2one('room', 'Mã phòng')
    gia_phong = fields.Integer('giá')
    # gia_phong = fields.Many2one('room', string='giá phòng')
    dich_vu = fields.Many2one('service', 'dịch vụ')
    gia_dv = fields.Integer(string='Giá dịch vụ')
    # ng_thue = fields.Many2one('guest', 'người thuê')
    solgdv = fields.Integer('số dịch vụ dùng')
    total = fields.Integer(compute="_get_total", string='tổng cộng')

    @api.multi
    @api.depends("gia_phong",
                 "solgdv")  # kích hoạt cuộc gọi đến chức năng được trang trí nếu bất kỳ trường nào được chỉ định
    def _get_total(self):
        for gia in self:
            if gia.gia_phong or gia.gia_dv:
                gia.total = gia.gia_phong + (gia.gia_dv * gia.solgdv)



            # elif gia.gia_dv:
            #     gia.total += (gia.gia_dv * gia.solgdv)
    # @api.multi
    # def _get_kh(self):
    #     for kh in self:
    #         if kh.so_phong != None:
    #             self.kh = self.name
    # name_guest = fields.Many2many('guest', string='Khách hàng')
    # total = fields.Float(compute='_get_total', string='Tổng tiền')
    #
    #
    # @api.multi
    # @api.depends("price", "price_server")
    # def _get_total(self):

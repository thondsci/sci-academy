# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Bill(models.Model):
    _name = 'bills'

    kh_thue = fields.Many2one('guest', 'Khách hàng')
    total = fields.Integer(compute="_get_total", string='Tổng')

    # @api.multi
    # @api.depends("kh_thue")
    # def _get_total(self):
    #     self.total = self.kh_thue.roomsd.price + self.kh_thue.servicesd_ids.name.price_service


    @api.depends('kh_thue')
    def _get_total(self):
        for record in self:
            total = 0
            if record.kh_thue:
                for servicesd_id in record.kh_thue.servicesd_ids:
                    total += servicesd_id.name.price_service
                total += record.kh_thue.roomsd.price
                record.total = total


# record là từng bản ghi trong model, self là chính nó trong model
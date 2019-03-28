# -*- coding: utf-8 -*-
from odoo import api,fields,models
from datetime import datetime
class bill_purchase(models.Model):
    _name = 'bill_purchase'

    line = fields.Many2one('bill_purchase_all')
    name = fields.Many2one('drug',string="Tên thuốc: ")
    price_drug = fields.Integer(string='Giá sản phẩm :')
    amount_drug = fields.Integer('Số lượng mua : ')
    _into_money = fields.Integer(compute = 'money',string='thành tiền')
    @api.onchange('name')
    def money(self):
        for i in self:
            if i:
                i._into_money = i.price_drug * i.amount_drug







class bill_purchase_all(models.Model):
    _name = 'bill_purchase_all'
    name = fields.Char('Mã đơn thuốc: ')
    #name = fields.Integer(string="Hóa đơn thuốc số :",default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    date = fields.Datetime(string='thời gian bán : ', default=datetime.now())
    name_doctor = fields.Many2one('doctor',string="Người bán : ")
    t2 = fields.Integer(compute='_get_total',string="Tiền thuốc : ")
    list_drug = fields.One2many('bill_purchase', 'line', string="Danh sách thuốc : ")

    def _get_total(self):
        total = 0
        for record in self:
            if record.list_drug:
                for i in record.list_drug:
                    total += i._into_money

                record.t2 = total

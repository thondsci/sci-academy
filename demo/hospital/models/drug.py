# -*- coding: utf-8 -*-
from odoo import models,fields,api

class drug(models.Model):
    _name = 'drug'
    #AREA = [('1', 'Kháng sinh'), ('2', 'Giải độc'),('3','An thần'),('4','Kháng nấm'),('5','Giảm đau'),('6','Thuốc bổ')]
    name = fields.Char('Tên thuốc')
    code_drug = fields.Char('Mã thuốc')
    category = fields.Char('Loại thuốc:')
    producer = fields.Char('Nhà sản xuất : ')
    expiry_date = fields.Date('Hạn sử dụng : ')
    amount = fields.Integer('Số lượng hiện có : ')
   # price = fields.Integer('Giá thuốc : ')
 #   amount2 = fields.Integer(compute='_get_update',string='số lượng còn lại :')


  #  line = fields.Many2many('bill_purchase')


   # @api.depends('line')

   # def _get_update(self):
     #   for record in self:
    #        a = record.amount
       #     if record.line:
      #          for i in record.line:
         #           a -= i.amount_drug
        #        record.amount2 = a




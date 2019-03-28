# -*- coding: utf-8 -*-

from odoo import models,fields
from datetime import datetime
class PlayerCategory(models.Model):
    _name = "player.category"
    # your_field = field.Integer(string="SST", default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field')
    your_field = fields.Integer(string="SST",default=lambda self: self.env['ir.sequence'].next_by_code('increment_your_field'))
    TCT = fields.Char("Tên Cầu thủ ")
    NS = fields.Date("Ngày sinh ")
    CC = fields.Char("Chiều cao ")
    CN = fields.Char(" Cân nặng ")
    CLB = fields.Char("Tên câu lạc bộ đang thi đấu ")
    SACLB = fields.Char("Số áo tại câu lạc bộ ")
    VTTD = fields.Char(" Vị trí thi đấu sở trường")
    DTQG = fields.Char(" Tên đội tuyển quốc gia đang thi đấu")
    SADTQG = fields.Char("  Số áo tại quốc gia")
   # description = fields.Char()
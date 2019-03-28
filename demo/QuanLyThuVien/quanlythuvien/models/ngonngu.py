# -*- coding:utf-8 -*-
from odoo import models,fields,api

class Language(models.Model):
    _name = 'language'

    _mangonngu = fields.Char('Mã Ngôn Ngữ', required = True)
    _ngonngu = fields.Char('Ngôn Ngữ', required = True)
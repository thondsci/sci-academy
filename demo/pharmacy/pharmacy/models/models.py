# -*- coding: utf-8 -*-

from odoo import models, fields, api

unit = [('1', 'Hộp'), ('2', 'Vỉ'), ('3', 'Lọ'), ('4', 'Chai'), ('5', 'Viên'), ('6', 'Liều')]

class Category(models.Model):
    _name = 'category.pharmacy'
    cate = fields.Selection(selection=[('1', 'Thuốc'), ('2', 'Dụng cụ y tế')], string='Danh mục')
    name = fields.Char('Tên', size=60, required=True)
    note = fields.Html('Ghi chú')


class employees(models.Model):
    _name = 'employee.pharmacy'

    _rec_name = 'ma_nv'
    ma_nv = fields.Char('Mã nhân viên', size=6, required=True)
    name_nv = fields.Char('Họ tên', size=25, required=True)
    birth_day = fields.Date('Ngày sinh')
    sex = fields.Selection([('1', 'Nam'), ('2', 'Nữ')], 'Giới tính')
    email = fields.Char('Email', size=40, required=True)
    sdt = fields.Char('Số điện thoại', size=10,required=True)
    addr = fields.Text('Địa chỉ', required=True)
    note = fields.Html('Ghi chú')


class products(models.Model):
    _name = 'product.pharmacy'

    _rec_name = 'ma_sp'

    ma_sp = fields.Char('Mã sản phẩm', size=8, required=True)
    name_sp = fields.Char('Tên sản phẩm', size=25, required=True)
    nha_sx = fields.Char('Nhà sản xuất', size=70, required=True)
    type_sp = fields.Many2one('category.pharmacy', 'Loại sản phẩm', required=True)
    note = fields.Html('Ghi chú')

class ticket_input(models.Model):
    _name = 'ticket.pharmacy'

    code_order = fields.Char('Mã đơn hàng', size=8, required=True) #tự nhập
    in_date = fields.Datetime('Ngày nhập', required=True)
    in_emp = fields.Many2one('employee.pharmacy', 'Nhân viên nhập kho')
    total_pay = fields.Float(compute='_getTotal', string='Tổng tiền thanh toán')
    in_ticket = fields.One2many('in_ticket.pharmacy', 'in_ticket', 'Danh sách sản phẩm nhập vào')
    note = fields.Html('Ghi chú')

    # Tính tổng tiền thanh toán

    def _getTotal(self):
        total_pay = 0
        for record in self:
            if record.in_ticket:
                for items in record.in_ticket:
                    total_pay += items.pay_sp
                record.total_pay = total_pay

class in_ticket(models.Model):
    _name = 'in_ticket.pharmacy'

    in_ticket = fields.Many2one('ticket.pharmacy')
    code_sp = fields.Many2one('product.pharmacy', 'Mã sản phẩm')
    ten_sp = fields.Char(compute='_get_namesp', string='Tên sản phẩm')  #
    in_num = fields.Integer('Số lượng nhập', required=True)
    price_in = fields.Float('Giá nhập', required=True)
    tax_vat = fields.Float('Thuế VAT')
    pay_sp = fields.Float(compute='_getMoney', string='Thành tiền')

    @api.onchange('code_sp')
    def _get_namesp(self):
        for record in self:
            if record.code_sp:
                record.ten_sp = record.code_sp.name_sp

    #tính tổng tiền từng loại sản phẩm pay_sp = in_num*price_in + (in_num*price_in)*tax_vat
    #@api.one
    @api.depends('in_num','code_sp','price_in', 'tax_vat')
    def _getMoney(self):
        for items in self:
            if items.in_num:
                items.pay_sp = items.in_num*items.price_in + (items.in_num*items.price_in)*items.tax_vat






class productsDetail(models.Model):
    _name = 'productdetail.pharmacy'

    id_sp = fields.Many2one('ticket.pharmacy')
    ma_sp = fields.Char(compute='_getInfo',string='Mã sản phẩm', required=True)
    ten_sp = fields.Char(compute='_getInfo',string='Tên Thuốc', required=True) #lấy từ products
    manu_facture = fields.Char(compute='_getInfo', string='Nhà sản xuất', required=True) #lấy từ products
    price_sale = fields.Float('Giá bán', required=True, default=0) #nhập từ bản phím
    type_sp = fields.Many2one(compute='_getInfo', string='Loại thuốc') #lấy từ products
    in_time = fields.Many2one(compute='_getInfo', string='Thời gian nhập', required=True) #thời gian nhập là thời gian ở phiếu nhập kho
    status = fields.Selection([('1', 'Còn'), ('2', 'Hết')]) #viết hàm tự động nhảy hết khi số lượng =0
    amount = fields.Integer('Số lượng còn lại') #viết hàm lấy số lượng từ nhập hàng
    note = fields.Html('Ghi chú')

    @api.onchange('id_sp.code_order')
    def _getInfo(self):
        if self.id_sp.code_order:
            self.ma_sp = self.id_sp.in_ticket.code_sp
            self.ten_sp = self.id_sp.in_ticket.ten_sp
            self.manu_facture = self.id_sp.in_ticket.code_sp.nha_sx
            self.type_sp = self.id_sp.in_ticket.code_sp.type_sp
            self.in_time = self.id_sp.in_date






class ticket_sale(models.Model):
    _name = 'ticket_sale.pharmacy'

    ma_sale = fields.Char('Mã hóa đơn', size=6, required=True)
    out_time = fields.Datetime('Thời gian bán', required=True)
    emp_sale = fields.Many2one('employee.pharmacy', 'Nhân viên bán', required=True)
    total_sale = fields.Float(compute='_getTotal', string='Tổng tiền thanh toán')
    ticket = fields.One2many('ticketline.pharmacy', 'lineTicket', 'Danh sách mua')
    note = fields.Html('Ghi chú')

    def _getTotal(self):
        total_sale = 0
        for record in self:
            if record.ticket:
                for item in record.ticket:
                    total_sale += item.pay_sp
                record.total_sale = total_sale

class ticketLine(models.Model):
    _name = 'ticketline.pharmacy'

    lineTicket = fields.Many2one('ticket_sale.pharmacy')
    ma_sp = fields.Many2one('product.pharmacy', 'Mã sản phẩm')
    ten_sp = fields.Char(compute='_get_namesp', string='Tên sản phẩm')
    price_sale = fields.Float('Giá bán', required=True)
    sale_num = fields.Integer('Số lượng', required=True)
    units = fields.Selection(selection=unit, string='Đơn vị', required=True)
    pay_sp = fields.Float(compute='_cal_money', string='Thành tiền')

    @api.onchange('ma_sp')
    def _get_namesp(self):
        for record in self:
            if record.ma_sp:
                record.ten_sp = record.ma_sp.name_sp
    @api.onchange('ma_sp', 'sale_num')
    def _cal_money(self):
        for items in self:
            if items:
                items.pay_sp = items.price_sale*items.sale_num



# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class ShipInvoices(models.Model):
    _name = "ship.invoices"

    _rec_name = "customer_address"
    id = fields.Integer(string="Mã đơn hàng", Required=True)
    customer_name = fields.Many2one("ship.customers", "Tên khách hàng", Required=True)
    customer_address = fields.Char(string="Địa chỉ khách hàng")

    date = fields.Date(string="Ngày nhận hàng", Required=True)
    time = fields.Selection([(1, 'Sáng'), (2, 'Chiều')], string="Thời gian", Required=True)

    status = fields.Selection(
        selection=[(1, 'Ở công ty'), (2, 'Đang ship'), (3, 'Đã giao'), (4, 'Khách trả về')],
        string="Trạng Thái",
        default=1)

    shipper = fields.Char(string="Shipper")

    total_bill_b4ship = fields.Integer(compute="_get_total_bill_b4ship", string="Giá trị các mặt hàng")
    ship_fee = fields.Integer(compute="_get_ship_fee", string="Phí ship")
    total_bill = fields.Integer(compute="_get_total_bill", string="Giá trị hóa đơn")

    total_weight = fields.Float(compute="_get_total_weight", string="Tổng khối lượng (kg)")
    total_volume = fields.Float(compute="_get_total_volume", string="Tổng thể tích (cm3)")

    line_ids = fields.One2many("item.line", "line", "Các mặt hàng")

    @api.onchange("customer_name")
    def onchange_customer_name(self):
        if self.customer_name is not None:
            self.customer_address = self.customer_name.address
            self.date = datetime.today()  # Set ngày nhận hàng là hôm nay khi điền khách hàng

    # @api.multi
    # @api.depends("shipper.invoice_ids.invoice_status")
    # def _get_status(self):
    #     for _ in self:
    #         if _.shipper is None:
    #             _.status = 1
    #         elif _.shipper.invoice_ids.invoice_id == _.id:
    #             _.status = _.shipper.invoice_ids.invoice_status

    @api.multi
    @api.depends("line_ids.total_price")
    def _get_total_bill_b4ship(self):
        for _ in self:
            _.total_bill_b4ship = sum(line.total_price for line in _.line_ids)

    @api.multi
    @api.depends("line_ids.quantity")
    def _get_total_volume(self):
        for _ in self:
            for line in _.line_ids:
               _.total_volume += line.quantity * line.item.volume

    @api.multi
    @api.depends("line_ids.quantity")
    def _get_total_weight(self):
        for _ in self:
            for line in _.line_ids:
                _.total_weight += line.quantity * line.item.weight

    @api.multi
    @api.depends("total_weight", "total_bill_b4ship")
    def _get_ship_fee(self):
        free_ship_amount = 1000000  # Miễn phí ship với đơn hàng giá trị hơn 1000000
        distance_price = {0: 0, 1: 10000, 2: 20000, 3: 30000, 4: 35000}  # Giá ship đối với từng lựa chọn khoảng cách của khách hàng
        weight_change = 15  # Giá ship tăng sau mỗi 15 kg
        weight_weighted_price = 0.1  # Tỷ trọng cân nặng / giá ship
        for _ in self:
            if _.total_bill_b4ship < free_ship_amount:
                #  Giá ship tính theo khoảng cách & cân nặng
                _.ship_fee = distance_price[_.customer_name.distance] * (1 + _.total_weight // weight_change * weight_weighted_price)
            else:
                _.ship_fee = 0

    @api.multi
    @api.depends("ship_fee", "total_bill_b4ship")
    def _get_total_bill(self):
        for _ in self:
            _.total_bill = _.ship_fee + _.total_bill_b4ship


class ItemLine(models.Model):
    _name = "item.line"

    line = fields.Many2one("ship.invoices")
    item = fields.Many2one("ship.items", string="Mặt hàng")
    unit = fields.Char(string="Đơn vị")
    item_price = fields.Integer(string="Giá bán", compute="_get_item_price")
    quantity = fields.Integer(string="Số lượng", Required=True)
    total_price = fields.Integer(compute="_get_total_price", string="Tổng giá trị")

    @api.onchange("item")
    def onchange_item(self):
        if self.item is not None:
            self.unit = self.item.unit

    @api.depends("item")
    def _get_item_price(self):
        for _ in self:
            if _.item is not None:
                _.item_price = _.item.price

    @api.depends("item_price", "quantity")
    def _get_total_price(self):
        for _ in self:
            _.total_price = _.item_price * _.quantity



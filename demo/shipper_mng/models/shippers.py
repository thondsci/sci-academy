# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Shippers(models.Model):
    _name = "shippers"

    id = fields.Integer(string="Mã shipper", Required=True)
    name = fields.Char(string="Tên shipper", Required=True)
    shipper_phone = fields.Char(string="Số điện thoại", Required=True)

    shipper_status = fields.Char(compute="_get_invoice_num", string="Số đơn hàng đang giao")

    current_weight = fields.Float(compute="_get_current_weight", string="Khối lượng đang giao")
    current_volume = fields.Float(compute="_get_current_volume", string="Thể tích đang giao (m3)")

    total_weight = fields.Float(compute="_get_total_weight", string="Khối lượng đã giao")
    total_volume = fields.Float(compute="_get_total_volume", string="Thể tích đã giao (m3)")

    invoice_ids = fields.One2many("invoice.line", "invoice_line", "Hóa đơn")

    @api.multi
    @api.depends("invoice_ids.invoice_weight", "invoice_ids.invoice_status")
    #  Tính tổng khối lượng các đơn hàng shipper đang giao
    def _get_current_weight(self):
        for _ in self:
            for invoice in _.invoice_ids:
                if invoice.invoice_status == 2:
                    _.current_weight += invoice.invoice_weight

    @api.multi
    @api.depends("invoice_ids.invoice_volume", "invoice_ids.invoice_status")
    #  Tính tổng thể tích các đơn hàng shipper đang giao, quy về m3
    def _get_current_volume(self):
        for _ in self:
            for invoice in _.invoice_ids:
                if invoice.invoice_status == 2:
                    _.current_volume += invoice.invoice_volume/1000000

    @api.multi
    @api.depends("invoice_ids.invoice_weight", "invoice_ids.invoice_status")
    #  Tính tổng khối lượng các đơn hàng shipper đã giao
    def _get_total_weight(self):
        for _ in self:
            for invoice in _.invoice_ids:
                if invoice.invoice_status == 3:
                    _.total_weight += invoice.invoice_weight

    @api.multi
    @api.depends("invoice_ids.invoice_volume", "invoice_ids.invoice_status")
    #  Tính tổng thể tích các đơn hàng shipper đã giao, quy về m3
    def _get_total_volume(self):
        for _ in self:
            for invoice in _.invoice_ids:
                if invoice.invoice_status == 3:
                    _.total_volume += invoice.invoice_volume/1000000

    @api.depends("invoice_ids.invoice_status")
    #  Tính số lượng đơn hàng shipper đang giao
    def _get_invoice_num(self):
        for _ in self:
            num_invoice = 0
            for invoice in _.invoice_ids:
                if invoice.invoice_status == 2:
                    num_invoice += 1
                _.shipper_status = str(num_invoice) + " Đơn hàng"

    @api.onchange("current_weight")
    # Cảnh báo khi khối lượng đơn hàng vượt quá ngưỡng weight_limit
    def onchange_weight(self):
        weight_limit = 70
        if self.current_weight > weight_limit:
            warning = {
                'title': _('Cảnh báo!'),
                'message': _('Khối lượng vượt quá ngưỡng quy định (%s kg)') % weight_limit,
            }
            return {'warning': warning}

    @api.onchange("current_volume")
    # Cảnh báo khi thể tích đơn hàng vượt quá ngưỡng quy định (0.216 m3 = 60cm3 ^3)
    def onchange_volume(self):
        volume_limit = 0.216
        if self.current_volume > volume_limit:
            warning = {
                'title': _('Cảnh báo!'),
                'message': _('Thể tích vượt quá ngưỡng quy định (%s m3)') % volume_limit,
            }
            return {'warning': warning}


class InvoiceLine(models.Model):
    _name = "invoice.line"

    invoice_line = fields.Many2one("shippers")
    invoice_id = fields.Integer(string="Mã đơn hàng")
    invoice_customer = fields.Char(string="Tên khách hàng")

    # Chọn đơn hàng cho shipper theo địa chỉ; lọc theo các đơn hàng có trạng thái "Ở công ty"
    invoice_address = fields.Many2one("ship.invoices", string="Địa chỉ", domain="[('status', '=', 1)]")

    invoice_date = fields.Date(string="Ngày nhận hàng")
    invoice_time = fields.Char(string="Thời gian nhận hàng")
    invoice_status = fields.Selection(
        selection=[(1, 'Ở công ty'), (2, 'Đang ship'), (3, 'Đã giao'), (4, 'Khách trả về')],
        string="Trạng Thái",)

    invoice_weight = fields.Float(string="Khối lượng đơn hàng (kg)",)
    invoice_volume = fields.Float(string="Thể tích đơn hàng (cm3)",)

    # Báo lỗi khi nhập một đơn hàng hơn 1 lần
    _sql_constraints = [('invoice_address', 'UNIQUE (invoice_line, invoice_id)', 'Không thể nhập một hóa đơn nhiều lần')]

    @api.multi
    @api.onchange("invoice_address")
    def onchange_address(self):
        if self.invoice_address is not None:
            self.invoice_id = self.invoice_address.id
            self.invoice_customer = self.invoice_address.customer_name.name
            self.invoice_date = self.invoice_address.date
            self.invoice_status = 2
            self.invoice_weight = self.invoice_address.total_weight
            self.invoice_volume = self.invoice_address.total_volume
            # Cập nhật trạng thái và shipper cho đơn hàng
            invoices = self.env['ship.invoices'].search([('id', '=', self.invoice_id)])
            for invoice in invoices:
                invoice.write({'status': self.invoice_status, 'shipper': self.invoice_line.name})

    @api.multi
    @api.onchange("invoice_status")
    # Cập nhật trạng thái của đơn hàng ở model ship_invoices theo trạng thái của invoice.line
    def update_status(self):
        invoices = self.env['ship.invoices'].search([('id', '=', self.invoice_id)])
        for invoice in invoices:
            invoice.write({'status': self.invoice_status})

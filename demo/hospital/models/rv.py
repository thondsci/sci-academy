from odoo import fields,api,models
from datetime import datetime
class rv(models.Model):
    _name = 'ravien'
    #fmt = '%Y-%m-%d'
   # lct = [('1', 'Ngoại tổng hợp'), ('2', 'Hồi phục chấn thương'), ('3', 'Hồi sức cấp cứu'), ('4', 'Nội')]

    name = fields.Char('Mã phiếu nhập viện : ')
    name_2 = fields.Many2one('patient',string="tên người bệnh :")
   # age = fields.Integer('Tuổi :')
   # address = fields.Char('Địa chỉ : ')
    time_in = fields.Date('Ngày nhập viện: ')
    time_out = fields.Date('Ngày xuất viện : ')
    total_days = fields.Char(compute="calculate_date",string='số ngày nhập viện : ')
    treatments = fields.Char('Phương pháp điều trị : ')
    room = fields.Selection([(1,'Loại 1 '),(2,'Loại 2'),(3,'loại 3')],string='Phòng bệnh: ')
    price_room = fields.Integer('Giá phòng : ')
    total = fields.Integer(compute="calculate",string='Tổng tiền phòng : ')
    #b = fields.Many2one('bill')

    @api.onchange('time_in','time_out','total_days')
    #@api.depends('time_in','time_out','total_days')
    def calculate_date(self):
        for record in self:
            if record.time_out and record.time_in:
                  date1 = datetime.strptime(record.time_in,"%Y-%m-%d")
                  date2 = datetime.strptime(record.time_out,"%Y-%m-%d")
                  date = (date2-date1).days
                  record.total_days = date

    @api.depends('price_room','total_days','total')
    def calculate(self):
        a = 0
        for record in self:
            if record.price_room:
               a += int(record.total_days)*record.price_room

            record.total += a
    #@api.onchange('b')
    #def extend(self):
     #   for i in self:
      #      if i.b:
      #          i.name_2 = i.b.name_patient






     #   a = 0
      #  d1 = str(self.time_in)
      #  d2 = str(self.time_out)
      #  d3 = datetime.strptime(d1,"%Y-%m-%d")
      #  d4 = datetime.strptime(d2,"%Y-%m-%d")
      #  a +=abs((d4 - d3).days)

      #  self.total_days = a


  #  d1 = datetime.strftime(time_in,fmt)
  #  d2 = datetime.strftime(time_out,fmt)
  #  count_day = str((d2-d1).days +1)
  # number = fields.Char(string='số ngày nhập viện: ',default =count_day)




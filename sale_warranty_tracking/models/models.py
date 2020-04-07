# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class sale_warranty_tracking(models.Model):
#     _name = 'sale_warranty_tracking.sale_warranty_tracking'
#     _description = 'sale_warranty_tracking.sale_warranty_tracking'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class ProductWarrantyPeriod(models.Model):
    _name = 'product.warranty.period'

    name = fields.Char(string= 'Period Name')
    days = fields.Integer(string="Days")

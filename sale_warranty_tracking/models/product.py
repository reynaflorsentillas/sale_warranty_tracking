# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_allowWarranty = fields.Boolean(string="Allow Warranty")
    is_alloweRenewal = fields.Boolean(string="Allow Renewal")
    terms_and_cond = fields.Text(string="Terms and Condition")
    warranty_cond = fields.Text(string="Notes")
    warranty_period = fields.Many2one('product.warranty.period', string= "Warranty Period")

    

#class ProductProduct(models.Model):
#    _inherit = 'product.product'
#
#    is_allowWarranty = fields.Boolean(string="Allow Warranty")
#    is_alloweRenewal = fields.Boolean(string="Allow Renewal")
#    terms_and_cond = fields.Text(string="Terms and Condition")
#    warranty_cond = fields.Text(string="Notes")
#    warranty_period = fields.Many2one('product.warranty.period', string= "Warranty Period")

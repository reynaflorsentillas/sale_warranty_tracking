# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_allowWarranty = fields.Boolean(string="Allow Warranty")
    is_alloweRenewal = fields.Boolean(string="Allow Renewal")
    terms_and_cond = fields.Text(string="Terms and Condition")
    warranty_cond = fields.Text(string="Notes")
    warranty_period = fields.Many2one('product.warranty.period', string= "Warranty Period")


    @api.model
    def ProductAllowedWarranty(self, product_tmpl_id = False):
        if product_tmpl_id:
            product_template = self.env['product.template'].search([('id', '=', product_tmpl_id)])
            return product_template and product_template.is_allowWarranty or False                
        return False

    

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def ProductAllowedWarranty(self):
        self.ensure_one()
        for rec in self:
            return rec.product_tmpl_id.ProductAllowedWarranty(rec.product_tmpl_id.id)

#
#    is_allowWarranty = fields.Boolean(string="Allow Warranty")
#    is_alloweRenewal = fields.Boolean(string="Allow Renewal")
#    terms_and_cond = fields.Text(string="Terms and Condition")
#    warranty_cond = fields.Text(string="Notes")
#    warranty_period = fields.Many2one('product.warranty.period', string= "Warranty Period")

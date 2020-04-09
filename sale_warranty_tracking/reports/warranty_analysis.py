# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import tools
from odoo import api, fields, models
from odoo import fields as fields_as_date_converter

import logging

_logger = logging.getLogger(__name__)

class WarrantyAnalysis(models.Model):
    _name = "warranty.analysis.report"
    _auto = False
    _description = "Warranty Analysis Report"

    name = fields.Char(string='Warranty Reference', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    product_id = fields.Many2one('product.product', string='Product', readonly=True)
    total_expiration_in_days = fields.Integer(string='Days Expiration', readonly=True)
    expiration_days = fields.Integer(string='Remaining Expiration Days', readonly=True)
    nbr = fields.Integer('# of Warranty', readonly=True)
    #state = fields.Selection([
    #    ('draft', 'Draft'),
    #    ('warranty', 'In Warranty'),
    #    ('expired', 'Expired'),
    #], readonly=True)    

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        date_now = fields_as_date_converter.Datetime.now().date().strftime('%Y-%m-%d')
        select_ = """
            min(id) as id,
            product_id,
            partner_id,
            DATE_PART('day', (expiry_date::timestamp) - (purchase_date::timestamp)) as total_expiration_in_days,
            DATE_PART('day', (expiry_date::timestamp) - ('%s'::timestamp)) as expiration_days,
            count(*) as nbr            
        """ % date_now

        from_ = """ sale_warranty
            %s
        """ % from_clause

        groupby_ = """
            product_id,
            partner_id,
            expiry_date,
            purchase_date
            
            %s
        """ % (groupby)
        _logger.info('%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)) 
        return '%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)
   
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))






from odoo import models, fields, api, _
from dateutil import relativedelta

from odoo.exceptions import UserError

import logging
_logger = logging.getLogger('models')

class SaleWarrantyAdd(models.TransientModel):
    _name = 'sale.warranty.add'
    _description = 'Add sales warranty to sales order'

    @api.model
    def _default_order(self):
        order_line = self.env['sale.order.line'].browse(self._context.get('active_id'))
        return order_line.order_id

    @api.model
    def _default_order_line(self):
        order_line = self.env['sale.order.line'].browse(self._context.get('active_id'))
        return order_line

    @api.model
    def _default_partner(self):
        order_line = self.env['sale.order.line'].browse(self._context.get('active_id'))
        return order_line.order_id.partner_id

    @api.model
    def _default_product(self):
        order_line = self.env['sale.order.line'].browse(self._context.get('active_id'))
        return order_line.product_id

    @api.model
    def _default_purchase_date(self):
        order_line = self.env['sale.order.line'].browse(self._context.get('active_id'))
        return order_line.order_id.date_order

    sale_id = fields.Many2one('sale.order', string='Sales Order', required=True, default=_default_order)
    sale_line_id = fields.Many2one('sale.order.line', string='Sale Order Line', default=_default_order_line)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, default=_default_partner)
    product_id = fields.Many2one('product.product', string='Product', required=True, default=_default_product)
    serial_no = fields.Char(string='Lot/Serial')
    note = fields.Text()
    purchase_date = fields.Date(required=True, default=_default_purchase_date)
    expiry_date = fields.Date(string='Expiration Date', required=True)
    warranty_period = fields.Integer(required=True)

    @api.onchange('product_id')
    def onchange_product_id(self):
        self.warranty_period = self.product_id.warranty_period.days

    @api.onchange('warranty_period')
    def onchange_warranty_period(self):
        purchase_date = self.purchase_date
        warranty_period = self.warranty_period
        expiry_date = (purchase_date + relativedelta.relativedelta(months=warranty_period))
        self.expiry_date = expiry_date

    def confirm_warranty(self):
        # if self.product_id and self.product_id.is_allowWarranty != True:
        #     raise UserError(_('Product is not configured for warranty!'))
        warranty_id = self.env['sale.warranty'].sudo().create({
            'sale_id': self.sale_id.id,
            'sale_line_id': self.sale_line_id.id,
            'product_id': self.product_id.id,
            'partner_id': self.partner_id.id,
            'serial_no': self.serial_no,
            'note': self.note,
            'purchase_date': self.purchase_date,
            'expiry_date': self.expiry_date,
            'warranty_period': self.warranty_period,
            'is_confirmed': True,
        })
        self.sale_line_id.write({'warranty_ids':[(6, 0, warranty_id.ids)]})
    
    def add_warranty(self):
        # if self.product_id and self.product_id.is_allowWarranty != True:
        #     raise UserError(_('Product is not configured for warranty!'))
        warranty_id = self.env['sale.warranty'].sudo().create({
            'sale_id': self.sale_id.id,
            'sale_line_id': self.sale_line_id.id,
            'product_id': self.product_id.id,
            'partner_id': self.partner_id.id,
            'serial_no': self.serial_no,
            'note': self.note,
            'purchase_date': self.purchase_date,
            'expiry_date': self.expiry_date,
            'warranty_period': self.warranty_period,
        })
        self.sale_line_id.write({'warranty_ids':[(6, 0, warranty_id.ids)]})
    
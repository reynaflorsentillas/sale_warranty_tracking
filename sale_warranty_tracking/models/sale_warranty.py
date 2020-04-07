from odoo import models, fields, api, _
from dateutil import relativedelta

class SaleWarranty(models.Model):
    _name = 'sale.warranty'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Sale Warranty'

    name = fields.Char(string='Warranty Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
    sale_id = fields.Many2one('sale.order', string='Sales Order', readonly=True, states={'draft': [('readonly', False)]})
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, readonly=True, states={'draft': [('readonly', False)]})
    product_id = fields.Many2one('product.product', string='Product', required=True, readonly=True, states={'draft': [('readonly', False)]})
    serial_no = fields.Char(string='Lot/Serial', readonly=True, states={'draft': [('readonly', False)]})
    note = fields.Text()
    purchase_date = fields.Date(required=True, default=fields.Datetime.now, readonly=True, states={'draft': [('readonly', False)]})
    expiry_date = fields.Date(string='Expiration Date', required=True, default=fields.Datetime.now, readonly=True, states={'draft': [('readonly', False)]})
    warranty_period = fields.Integer(required=True, readonly=True, states={'draft': [('readonly', False)]})
    is_confirmed = fields.Boolean(default=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('warranty', 'In Warranty'),
        ('expired', 'Expired'),
    ], default='draft', string='Status', readonly=True, copy=False, index=True, tracking=3, compute='_compute_state')

    @api.depends('purchase_date', 'expiry_date', 'warranty_period')
    def _compute_state(self):
        for record in self:
            if record.is_confirmed == True and record.expiry_date == fields.Datetime.now().date():
                record.state = 'expired'
            elif record.is_confirmed == True and record.expiry_date > fields.Datetime.now().date():
                record.state = 'warranty'
            else:
                record.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.warranty') or _('New')

        result = super(SaleWarranty, self).create(vals)
        return result

    @api.onchange('warranty_period')
    def onchange_warranty_period(self):
        purchase_date = self.purchase_date
        warranty_period = self.warranty_period
        expiry_date = (purchase_date + relativedelta.relativedelta(months=warranty_period))
        self.expiry_date = expiry_date

    def action_confirm(self):
        for record in self:
            record.is_confirmed = True
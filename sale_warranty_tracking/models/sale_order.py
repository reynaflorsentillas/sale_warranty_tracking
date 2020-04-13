from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    warranty_ids = fields.Many2many('sale.warranty', string='Waranties', compute="_get_warranty", readonly=True, copy=False)
    warranty_count = fields.Integer(string='Warranty Count', compute='_get_warranty', readonly=True)

    @api.depends('order_line.warranty_ids')
    def _get_warranty(self):
        for order in self:
            warranty_ids = order.order_line.mapped('warranty_ids')
            order.warranty_ids = warranty_ids
            order.warranty_count = len(warranty_ids)

    def action_view_warranty(self):
        warranty_ids = self.mapped('warranty_ids')
        action = self.env.ref('sale_warranty_tracking.action_all_warranty').read()[0]
        if len(warranty_ids) > 1:
            action['domain'] = [('id', 'in', warranty_ids.ids)]
        elif len(warranty_ids) == 1:
            form_view = [(self.env.ref('sale_warranty_tracking.sale_warranty_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = warranty_ids.id
        else:
            action = {'type': 'ir.actions.act_window_close'}

        return action

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    warranty_ids = fields.Many2many('sale.warranty', string='Sales Warranty')

    def action_add_warranty(self):
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.warranty.add',
            'target': 'new',
        }
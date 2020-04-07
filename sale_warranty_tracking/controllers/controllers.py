# -*- coding: utf-8 -*-
# from odoo import http


# class SaleWarrantyTracking(http.Controller):
#     @http.route('/sale_warranty_tracking/sale_warranty_tracking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_warranty_tracking/sale_warranty_tracking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_warranty_tracking.listing', {
#             'root': '/sale_warranty_tracking/sale_warranty_tracking',
#             'objects': http.request.env['sale_warranty_tracking.sale_warranty_tracking'].search([]),
#         })

#     @http.route('/sale_warranty_tracking/sale_warranty_tracking/objects/<model("sale_warranty_tracking.sale_warranty_tracking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_warranty_tracking.object', {
#             'object': obj
#         })

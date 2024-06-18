# -*- coding: utf-8 -*-
# from odoo import http


# class LsdSale(http.Controller):
#     @http.route('/lsd_sale/lsd_sale', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lsd_sale/lsd_sale/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lsd_sale.listing', {
#             'root': '/lsd_sale/lsd_sale',
#             'objects': http.request.env['lsd_sale.lsd_sale'].search([]),
#         })

#     @http.route('/lsd_sale/lsd_sale/objects/<model("lsd_sale.lsd_sale"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lsd_sale.object', {
#             'object': obj
#         })


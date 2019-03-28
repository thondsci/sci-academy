# -*- coding: utf-8 -*-
from odoo import http

# class CompanyLibrary(http.Controller):
#     @http.route('/company_library/company_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/company_library/company_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('company_library.listing', {
#             'root': '/company_library/company_library',
#             'objects': http.request.env['company_library.company_library'].search([]),
#         })

#     @http.route('/company_library/company_library/objects/<model("company_library.company_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('company_library.object', {
#             'object': obj
#         })
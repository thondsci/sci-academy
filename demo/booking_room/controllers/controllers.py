# -*- coding: utf-8 -*-
from odoo import http

# class BookingRoom(http.Controller):
#     @http.route('/booking_room/booking_room/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_room/booking_room/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_room.listing', {
#             'root': '/booking_room/booking_room',
#             'objects': http.request.env['booking_room.booking_room'].search([]),
#         })

#     @http.route('/booking_room/booking_room/objects/<model("booking_room.booking_room"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_room.object', {
#             'object': obj
#         })
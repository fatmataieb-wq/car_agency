# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request, route


class CarAgencyCustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'car_count' in counters:
            values['car_count'] = request.env['car.car'].search_count(
                [('customer_id', '=', request.env.user.partner_id.id)]
            )
        return values

    @route(['/my/cars'], type='http', auth='user', website=True)
    def portal_my_cars(self, **kw):
        partner = request.env.user.partner_id
        cars = request.env['car.car'].search([('customer_id', '=', partner.id)])
        values = self._prepare_portal_layout_values()
        values.update({'cars': cars, 'page_name': 'car'})
        return request.render('car_agency.portal_my_cars', values)
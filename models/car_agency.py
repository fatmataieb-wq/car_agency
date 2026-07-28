# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CarAgency(models.Model):
    """A car rental agency.

    Specification:
        - responsible_id (res.partner) is mandatory.
        - the agency exposes the list of cars available through its
          brands ("list of cars which will be present at the agency").
        - agencies can be grouped by their responsible person.
        - (requirement 3) a smart button on the form shows the car
          brands that belong ONLY to the current agency.
    """
    _name = 'car.agency'
    _description = 'Car Rental Agency'

    # The specification does not define a dedicated 'name' field for
    # the agency, so we use the responsible person as the record's
    # display name (res.partner.name is used automatically by Odoo's
    # default name_get for a Many2one _rec_name).
    _rec_name = 'responsible_id'

    responsible_id = fields.Many2one(
        comodel_name='res.partner',
        string='Responsible',
        required=True,
        help="Person in charge of the agency.",
    )

    # Real One2many: reverse of car.brand.agency_id.
    # Used for requirement 3 (smart button).
    brand_ids = fields.One2many(
        comodel_name='car.brand',
        inverse_name='agency_id',
        string='Car Brands',
    )
    brand_count = fields.Integer(
        string='Brand Count',
        compute='_compute_brand_count',
    )

    # A car is NOT directly linked to an agency: it is linked to a
    # brand, and a brand is linked to an agency. So "the list of cars
    # present at the agency" is a computed (read-only) aggregation
    # through the brands, not a stored field.
    car_ids = fields.One2many(
        comodel_name='car.car',
        string='Cars',
        compute='_compute_car_ids',
    )
    car_count = fields.Integer(
        string='Total Cars',
        compute='_compute_car_ids',
    )

    @api.depends('brand_ids')
    def _compute_brand_count(self):
        for agency in self:
            agency.brand_count = len(agency.brand_ids)

    @api.depends('brand_ids.car_ids')
    def _compute_car_ids(self):
        for agency in self:
            cars = agency.brand_ids.mapped('car_ids')
            agency.car_ids = cars
            agency.car_count = len(cars)

    def action_view_brands(self):
        """Smart button action (requirement 3): open only the brands
        that belong to the current agency."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Car Brands',
            'res_model': 'car.brand',
            'view_mode': 'list,form',
            'domain': [('agency_id', '=', self.id)],
            'context': {'default_agency_id': self.id},
        }

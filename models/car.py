# -*- coding: utf-8 -*-
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class Car(models.Model):
    _name = 'car.car'
    _description = 'Car'
    # mail.thread/mail.activity.mixin give us a chatter for free, so
    # every status/damage change is logged and auditable.
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'registration_number'
    _order = 'registration_number'

    registration_number = fields.Integer(
        string='Registration Number',
        required=True,
        copy=False,
        tracking=True,
        help="Unique 8-digit positive registration number of the car. "
             "NOTE: because this is an Integer (as required by the "
             "specification) a leading zero would not survive storage "
             "(e.g. 01234567 -> 1234567). If leading zeros must be kept, "
             "switch this field to Char with a regex constraint instead.",
    )
    brand_id = fields.Many2one(
        comodel_name='car.brand',
        string='Car Model',
        required=True,
        ondelete='restrict',
        tracking=True,
        help="Brand/model of the car (e.g. Toyota Corolla).",
    )
    # Convenience related field: the agency is not stored directly on
    # the car, it is derived from the car's brand.
    agency_id = fields.Many2one(
        comodel_name='car.agency',
        string='Agency',
        related='brand_id.agency_id',
        store=True,
        readonly=True,
    )
    mileage = fields.Float(
        string='Mileage (km)',
    )
    state = fields.Selection(
        selection=[
            ('available', 'Available'),
            ('rented', 'Rented'),
            ('damaged', 'Damaged'),
        ],
        string='Status',
        required=True,
        default='available',
        tracking=True,
    )
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    # Requirement 2: the customer renting the car.
    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        help="Person currently renting the car.",
    )

    # Requirement 4: filled by the 'Damaged' wizard.
    note = fields.Text(
        string='Damage Note',
        help="Description of the damage, filled from the 'Damaged' wizard.",
    )

    # NOTE: Odoo 19 replaced the old `_sql_constraints = [(...)]` list
    # with individual `models.Constraint` class attributes.
    _registration_number_unique = models.Constraint(
        'unique(registration_number)',
        'The registration number must be unique!',
    )
    _registration_number_positive = models.Constraint(
        'CHECK(registration_number > 0)',
        'The registration number must be strictly positive!',
    )

    @api.constrains('registration_number')
    def _check_registration_number_length(self):
        """Registration number must contain exactly 8 digits."""
        for car in self:
            if car.registration_number and len(str(car.registration_number)) != 8:
                raise ValidationError(
                    _('The registration number "%s" must contain exactly 8 digits.')
                    % car.registration_number
                )

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Basic consistency check between the rental dates."""
        for car in self:
            if car.start_date and car.end_date and car.end_date < car.start_date:
                raise ValidationError(_('The end date cannot be earlier than the start date.'))

    def action_open_damage_wizard(self):
        """Open the 'Damaged' wizard (requirement 4)."""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Report Damage'),
            'res_model': 'car.damage.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_car_id': self.id},
        }

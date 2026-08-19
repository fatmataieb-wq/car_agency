from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
class Car(models.Model):
    _name = 'car.car'
    _description = 'Car'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'registration_number'
    _order = 'registration_number'

    registration_number = fields.Integer(
        string='Registration Number',
        required=True,
        copy=False,
    )
    brand_id = fields.Many2one(
        comodel_name='car.brand',
        string='Car Model',
        required=True,
        ondelete='restrict',
        tracking=True,
    )
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
    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        help="Person currently renting the car.",
    )
    note = fields.Text(
        string='Damage Note',
        help="Description of the damage, filled from the 'Damaged' wizard.",
    )
    _registration_number_unique = models.Constraint(
        'unique(registration_number)',
        'The registration number must be unique!',
    )
    _registration_number_positive = models.Constraint(
        'CHECK(registration_number > 0)',
        'The registration number must be strictly positive!',
    )
    @api.constrains('registration_number')
    def _check_registration_number(self):
        for car in self:
            if not car.registration_number:
                continue
            if len(str(car.registration_number)) != 8:
                raise ValidationError(
                    _('The registration number must contain exactly 8 digits.')
            )
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for car in self:
            if car.start_date and car.end_date and car.end_date < car.start_date:
                raise ValidationError(_('The end date cannot be earlier than the start date.'))

    def action_open_damage_wizard(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Report Damage'),
            'res_model': 'car.damage.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_car_id': self.id},
        }

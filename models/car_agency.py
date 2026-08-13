from odoo import api, fields, models
class CarAgency(models.Model):
    _name = 'car.agency'
    _description = 'Car Rental Agency'
    _rec_name = 'responsible_id'

    responsible_id = fields.Many2one(
        comodel_name='res.partner',
        string='Responsible',
        required=True,
        help="Person in charge of the agency.",
    )

    brand_ids = fields.One2many(
        comodel_name='car.brand',
        inverse_name='agency_id',
        string='Car Brands',
    )
    brand_count = fields.Integer(
        string='Brand Count',
        compute='_compute_brand_count',
    )

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
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Car Brands',
            'res_model': 'car.brand',
            'view_mode': 'list,form',
            'domain': [('agency_id', '=', self.id)],
            'context': {'default_agency_id': self.id},
        }

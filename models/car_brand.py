from odoo import api, fields, models
class CarBrand(models.Model):
    _name = 'car.brand'
    _description = 'Car Brand'
    _order = 'name'

    name = fields.Char(
        string='Brand Name',
        required=True,
        help="Commercial name of the brand, e.g. Toyota, Fiat.",
    )
    image = fields.Image(
        string='Brand Logo',
        max_width=1024,
        max_height=1024,
    )
    description = fields.Text(
        string='Description',
    )
    agency_id = fields.Many2one(
        comodel_name='car.agency',
        string='Agency',
        required=True,
        ondelete='cascade',
        index=True,
        help="Agency that manages cars of this brand.",
    )
    car_ids = fields.One2many(
        comodel_name='car.car',
        inverse_name='brand_id',
        string='Cars',
    )
    car_count = fields.Integer(
        string='Car Count',
        compute='_compute_car_count',
    )

    @api.depends('car_ids')
    def _compute_car_count(self):
        for brand in self:
            brand.car_count = len(brand.car_ids)
    _name_agency_uniq = models.Constraint(
        'unique(name, agency_id)',
        'A brand with this name already exists for this agency.',
    )

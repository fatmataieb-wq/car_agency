from odoo import fields, models


class CarDamageWizard(models.TransientModel):
    _name = 'car.damage.wizard'
    _description = 'Report Car Damage'

    car_id = fields.Many2one(
        comodel_name='car.car',
        string='Car',
        required=True,
        readonly=True,
    )
    description = fields.Text(
        string='Damage Description',
        required=True,
        help="Explain what happened to the car.",
    )

    def action_confirm_damage(self):
        self.ensure_one()
        self.car_id.write({
            'state': 'damaged',
            'note': self.description,
        })
        return {'type': 'ir.actions.act_window_close'}

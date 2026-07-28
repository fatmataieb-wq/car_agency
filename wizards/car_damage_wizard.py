# -*- coding: utf-8 -*-
from odoo import fields, models


class CarDamageWizard(models.TransientModel):
    """Wizard opened by the 'Damaged' button on the car form.

    The user types a description of the damage; on confirmation the
    car is switched to state 'damaged' and the description is stored
    on car.car.note (requirement 4).
    """
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
        """Mark the related car as damaged and store the note."""
        self.ensure_one()
        self.car_id.write({
            'state': 'damaged',
            'note': self.description,
        })
        return {'type': 'ir.actions.act_window_close'}

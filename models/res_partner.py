from odoo import fields, models
class ResPartner(models.Model):
    _inherit = 'res.partner'

    cin = fields.Char(
        string='CIN Number',
        help="Customer's National Identity Card number.",
        copy=False,
    )

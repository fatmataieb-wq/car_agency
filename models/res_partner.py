# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """Extends res.partner to add the customer's national ID (CIN).

    Requirement 2 asks for a 'customer' characterized by
    name / cin number / phone / email. name, phone and email already
    exist on res.partner, so only 'cin' needs to be added here.
    """
    _inherit = 'res.partner'

    cin = fields.Char(
        string='CIN Number',
        help="Customer's National Identity Card number.",
        copy=False,
    )

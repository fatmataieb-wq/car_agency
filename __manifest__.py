# -*- coding: utf-8 -*-
{
    'name': 'Car Agency',
    'version': '19.0.1.0.0',
    'category': 'Services/Car Rental',
    'summary': 'Manage car rental agencies, brands, cars and damage reports',
    'description': """
Car Agency Management
======================
This module implements a small car-rental business case:

* **Agencies** — each managed by a responsible person (res.partner).
* **Car Brands** — each attached to exactly one agency.
* **Cars** — each attached to a brand, rentable to a customer, and
  trackable through 3 states: Available / Rented / Damaged.
* A **"Damaged"** wizard lets a user record the reason a car is taken
  out of service.

Extends ``res.partner`` with a CIN (national ID) field so that a
customer is fully described by name / CIN / phone / email, all of
which are supported natively by ``res.partner``.
""",
    'author': 'Fatma Taieb',
    'license': 'LGPL-3',
    # 'mail' is required for the chatter (mail.thread) on car.car,
    # used to keep an audit trail of status/damage changes.
    'depends': ['base', 'mail'],
    'data': [
        # security must be loaded first
        'security/car_agency_security.xml',
        'security/ir.model.access.csv',
        # wizard view must exist before it is referenced by python actions
        'wizards/car_damage_wizard_views.xml',
        # business views (order matters: actions must exist before menus)
        'views/car_brand_views.xml',
        'views/car_views.xml',
        'views/car_agency_views.xml',
        'views/res_partner_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

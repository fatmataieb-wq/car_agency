{
    'name': 'Car Agency',
    'version': '19.0.1.0.0',
    'category': 'Car Rental',
    'summary': 'Manage car rental agencies, brands, cars and damage reports',
    'description': """Car Agency Management""",
    'author': 'Fatma Taieb',
    'license': 'LGPL-3',
    # 'mail' is required for the chatter (mail.thread) on car.car,
    # used to keep an audit trail of status/damage changes.
    # 'portal' is required for the "My Cars" customer portal page.
    'depends': ['base', 'mail', 'portal'],
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
        'views/portal_templates.xml',
        'reports/car_contract_report.xml',
        'reports/car_contract_action.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
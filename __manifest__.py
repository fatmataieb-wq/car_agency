{
    'name': 'Car Agency',
    'version': '19.0.1.0.0',
    'category': 'Services/Car Rental',
    'summary': 'Manage car rental agencies, brands, cars and damage reports',
    'description': """
Car Agency Management
""",
    'author': 'Fatma Taieb',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/car_agency_security.xml',
        'security/ir.model.access.csv',
        'wizards/car_damage_wizard_views.xml',
        'views/car_brand_views.xml',
        'views/car_views.xml',
        'views/car_agency_views.xml',
        'views/res_partner_views.xml',
        'views/menu_views.xml',
        'reports/car_contract_report.xml',
        'reports/car_contract_action.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

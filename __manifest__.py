{
    'name': 'Car Agency',
    'version': '19.0.1.0.0',
    'category': 'Car Rental',
    'summary': 'Manage car rental agencies, brands, cars and damage reports',
    'description': """Car Agency Management""",
    'author': 'Fatma Taieb',
    'license': 'LGPL-3',
    'depends': ['base', 'mail', 'portal'],
    # base give us res.partner, mail gives us chatter and portal gives us the customer portal 
    'data': [
        # security must be loaded first
        'security/car_agency_security.xml',
        'security/ir.model.access.csv',
        # wizard view must exist before it is referenced by python actions
        'wizards/car_damage_wizard_views.xml',
        #  views (actions must exist before menus)
        'views/car_brand_views.xml',
        'views/car_views.xml',
        'views/car_agency_views.xml',
        'views/res_partner_views.xml',
        'views/menu_views.xml',
        'views/portal_templates.xml',
        'reports/car_contract_report.xml',
        'reports/car_contract_action.xml',
        'views/car_rental_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
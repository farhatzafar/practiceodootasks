{
    'name': "Practice Module",
    'description': "A module for practice",
    'version': '18.0.0.1',
    'application': True,
    'depends': ['base', 'account', 'sale', 'contacts'],
    'data': [
        'views/account_views.xml',
        'views/invoice_views.xml',
        'views/partner_parent_views.xml',
    ],
}

{
    "name": "Account Currency Custom",
    "summary": "Allows CAD currency on invoices, regardless of company currency",
    "version": "18.0.1.0.0",
    "depends": ['sale', 'account'],
    "data": ['views/sale_order_views.xml',
             'views/res_config_settings_view.xml',
             'views/account_move_views.xml'],
    "installable": True,
}
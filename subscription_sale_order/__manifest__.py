{
    "name": "Subscription Custom Sale Order",
    "summary": "Custom fields on sale order of Subscription module",
    "version": "18.0.1.0.0",
    "depends": ['sale', 'sale_subscription'],
    "data": ['security/ir.model.access.csv', 'views/subscriptions_views.xml', 'views/account_move_views.xml'],
    "installable": True,
}
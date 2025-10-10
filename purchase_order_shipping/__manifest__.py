{
    'name': "Purchase Order Shipping Date",
    'description': "Adds a shipping date field to the purchase order",
    'version': '18.0.1.0.0',
    'application': True,
    'depends': ['purchase'],
    'data': ['views/purchase_views.xml', 'reports/purchase_order_report.xml'],
}

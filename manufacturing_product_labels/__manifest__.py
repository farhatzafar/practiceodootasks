{
    "name": "Manufacturing Product Labels",
    "version": "18.0.1.0.0",
    "summary": "Adds new report with product labels containing barcodes",
    "depends": ['base', 'mrp', 'stock'],
    "data": ['data/report_paperformat_data.xml',
             'report/product_label_template.xml',
             'report/product_label_views.xml'],
    "installable": True
}
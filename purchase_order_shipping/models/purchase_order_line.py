from odoo import fields, models

class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    shipping_date = fields.Date(string="Shipping Date")
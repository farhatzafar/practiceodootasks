from odoo import fields, models

class PurchaseOrder(models.Model):

    _inherit = "purchase.order"

    shipping_date = fields.Date(string="Shipping Date")
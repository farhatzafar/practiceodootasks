from odoo import models, fields

class ProductPricelistItem(models.Model):

    _inherit = "product.pricelist.item"

    min_limit = fields.Integer()
    max_limit = fields.Integer()
    remove_customer_limit_after = fields.Integer()

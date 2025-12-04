from odoo import models, fields

class SaleMaterialLine(models.Model):

    _name = 'sale.material.line'
    _description = "Materials Used Line"

    order_id = fields.Many2one('sale.order')

    product_id = fields.Many2one('product.product')

    quantity = fields.Float()
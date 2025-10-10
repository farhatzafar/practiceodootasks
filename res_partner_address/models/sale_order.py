from odoo import fields, models, api

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    @api.depends('partner_id')
    def _compute_partner_shipping_id(self):
        super()._compute_partner_shipping_id()

        for order in self:
            order.partner_shipping_id = order.partner_id
from odoo import models, fields, api

class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _prepare_invoice(self):
        self.ensure_one()
        values = super()._prepare_invoice()

        values['recipient_id'] = self.partner_id.id

        return values


    @api.depends('partner_id')
    def _compute_partner_invoice_id(self):
        super()._compute_partner_invoice_id()
        for order in self:
            partner = order.partner_id
            while partner.parent_id:
                partner = partner.parent_id
            order.partner_invoice_id = partner
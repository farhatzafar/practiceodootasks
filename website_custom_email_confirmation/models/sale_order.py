from odoo import fields, models

class SaleOrder(models.Model):

    _inherit = "sale.order"

    def _find_mail_template(self):
        self.ensure_one()
        if self.website_id and self.website_id.sale_confirmation_email_template_id:
            if self.state == 'sale' and not self.env.context.get('proforma', False):
                return self.website_id.sale_confirmation_email_template_id
        return super()._find_mail_template()


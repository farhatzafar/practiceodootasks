from odoo import fields, models

class Website(models.Model):

    _inherit = "website"

    sale_confirmation_email_template_id = fields.Many2one(
        "mail.template",
        string="Sale Confirmation Email Template",
        domain=[("model", "=", "sale.order")],
    )
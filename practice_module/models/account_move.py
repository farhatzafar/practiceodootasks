from odoo import models, fields

class AccountMove(models.Model):
    _inherit = "account.move"

    recipient_id = fields.Many2one("res.partner", string="Recipient")
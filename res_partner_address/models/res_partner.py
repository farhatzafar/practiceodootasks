from odoo import fields, models

class ResPartner(models.Model):

    _inherit = "res.partner"

    state_id = fields.Many2one(required=True)

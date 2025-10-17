from odoo import fields, models

class AccountMove(models.Model):

    _inherit = 'account.move'

    prime_previous = fields.Float('Prime Previous')
    prime_current = fields.Float('Prime Current')
    gap_previous = fields.Float('GAP Previous')
    gap_current = fields.Float('GAP Current')
    life_comm_previous = fields.Float('Life Comm. Previous')
    life_comm_current = fields.Float('Life Comm. Current')
    credits_previous = fields.Char('Credits Previous')
    credits_current = fields.Char('Credits Current')
    mutual_funds_previous = fields.Float('Mutual Funds Previous')
    mutual_funds_current = fields.Float('Mutual Funds Current')
    life_agent_previous = fields.Float('Life Agent Previous')
    life_agent_current = fields.Float('Life Agent Current')
    amf_previous = fields.Float('AMF Previous')
    amf_current = fields.Float('AMF Current')

    per_claim = fields.Float('Per Claim')
    per_period = fields.Float('Per Period')
    deductible = fields.Float('Deductible')
    deductible_per_year = fields.Float('Deductible Per Year')
    notes = fields.Text('Notes')

    designated_insured_ids = fields.One2many('account.move.designated.insured', 'move_id', string='Designated Insured')

    mutual_funds_ids = fields.One2many('account.move.mutual.funds', 'move_id', string='Mutual Funds')
    life_group_ids = fields.One2many('account.move.life.group', 'move_id', string='Life and/or Group Insurance')
    financial_plan_ids = fields.One2many('account.move.financial.plan', 'move_id', string='Financial Plan')
    add_ins_ids = fields.One2many('account.move.add.ins', 'move_id', string='ADD Insurance')
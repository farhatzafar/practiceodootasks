from odoo import fields, models

class SaleOrder(models.Model):

    _inherit = 'sale.order'

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


    designated_insured_ids = fields.One2many('sale.order.designated.insured', 'order_id', string='Designated Insured')

    mutual_funds_ids = fields.One2many('sale.order.mutual.funds', 'order_id', string='Mutual Funds')
    life_group_ids = fields.One2many('sale.order.life.group', 'order_id', string='Life and/or Group Insurance')
    financial_plan_ids = fields.One2many('sale.order.financial.plan', 'order_id', string='Financial Plan')
    add_ins_ids = fields.One2many('sale.order.add.ins', 'order_id', string='ADD Insurance')

    def _prepare_invoice(self):
        self.ensure_one()
        values = super()._prepare_invoice()

        values.update({

            'prime_previous': self.prime_previous,
            'prime_current': self.prime_current,
            'gap_previous': self.gap_previous,
            'gap_current': self.gap_current,
            'life_comm_previous': self.life_comm_previous,
            'life_comm_current': self.life_comm_current,
            'credits_previous': self.credits_previous,
            'credits_current': self.credits_current,
            'mutual_funds_previous': self.mutual_funds_previous,
            'mutual_funds_current': self.mutual_funds_current,
            'life_agent_previous': self.life_agent_previous,
            'life_agent_current': self.life_agent_current,
            'amf_previous': self.amf_previous,
            'amf_current': self.amf_current,
            'per_claim': self.per_claim,
            'per_period': self.per_period,
            'deductible': self.deductible,
            'deductible_per_year': self.deductible_per_year,
            'notes': self.notes,
        })

        return values
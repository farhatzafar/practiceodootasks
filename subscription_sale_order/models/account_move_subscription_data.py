from odoo import fields, models

class AccountMoveAddIns(models.Model):
    _name = 'account.move.add.ins'

    move_id = fields.Many2one('account.move', string='Account Move')
    name = fields.Char('Name')

class AccountMoveDesignatedInsured(models.Model):
    _name = 'account.move.designated.insured'

    move_id = fields.Many2one('account.move', string='Account Move')
    name = fields.Char('Name')

class AccountMoveFinancialPlan(models.Model):
    _name = 'account.move.financial.plan'

    move_id = fields.Many2one('account.move', string='Account Move')
    name = fields.Char('Name')

class AccountMoveLifeGroup(models.Model):
    _name = 'account.move.life.group'

    move_id = fields.Many2one('account.move', string='Account Move')
    name = fields.Char('Name')

class AccountMoveMutualFunds(models.Model):
    _name = 'account.move.mutual.funds'

    move_id = fields.Many2one('account.move', string='Account Move')
    name = fields.Char('Name')
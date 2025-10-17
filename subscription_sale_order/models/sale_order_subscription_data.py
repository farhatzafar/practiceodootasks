from odoo import models, fields

class SaleOrderDesignatedInsured(models.Model):
    _name = 'sale.order.designated.insured'
    _description = 'Sale Order Designated Insured'

    order_id = fields.Many2one('sale.order', string='Order')
    name = fields.Char('Name')


class SaleOrderMutualFunds(models.Model):
    _name = 'sale.order.mutual.funds'
    _description = 'Sale Order Mutual Funds'

    order_id = fields.Many2one('sale.order', string='Order')
    name = fields.Char('Name')


class SaleOrderAddIns(models.Model):
    _name = 'sale.order.add.ins'
    _description = 'Sale Order Additional Insurance'

    order_id = fields.Many2one('sale.order', string='Order')
    name = fields.Char('Name')


class SaleOrderLifeGroup(models.Model):
    _name = 'sale.order.life.group'
    _description = 'Sale Order Life and/or Group Insurance'

    order_id = fields.Many2one('sale.order', string='Order')
    name = fields.Char('Name')


class SaleOrderFinancialPlan(models.Model):
    _name = 'sale.order.financial.plan'
    _description = 'Sale Order Financial Plan'

    order_id = fields.Many2one('sale.order', string='Order')
    name = fields.Char('Name')
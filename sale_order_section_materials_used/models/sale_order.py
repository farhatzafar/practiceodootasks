from odoo import fields, models

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    material_line_ids = fields.One2many('sale.material.line', 'order_id', string = "Materials Used")

    def action_confirm(self):
        res = super().action_confirm()

        for order in self:
            pickings = order.picking_ids.filtered(lambda p: p.state not in ['cancel', 'done'])
            if not pickings:
                continue

            for material in order.material_line_ids:
                for picking in pickings:
                    move_vals = {
                        'name': material.product_id.name,
                        'product_id': material.product_id.id,
                        'product_uom': material.product_id.uom_id.id,
                        'product_uom_qty': material.quantity,
                        'location_id': picking.location_id.id,
                        'location_dest_id': picking.location_dest_id.id,
                        'picking_id': picking.id,
                        'company_id': picking.company_id.id,
                        'origin': order.name,
                        'group_id': order.procurement_group_id.id,
                        'propagate_cancel': False,
                    }
                    move = self.env['stock.move'].create(move_vals)

                    move._action_confirm()

                    move._action_assign()

        return res
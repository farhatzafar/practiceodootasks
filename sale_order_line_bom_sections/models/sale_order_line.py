from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    bom_auto_created = fields.Boolean(default=False)

    @api.model_create_multi
    def create(self, vals_list):
        lines = super().create(vals_list)

        for line, vals in zip(lines, vals_list):

            if vals.get('display_type'):
                continue

            if vals.get('bom_auto_created'):
                continue

            product = line.product_id
            if not product:
                continue

            products_to_find = self.env['product.product'].browse([product.id])
            bom_find_result = self.env['mrp.bom']._bom_find(products_to_find)
            bom = bom_find_result.get(product)
            if bom:
                line._expand_bom(bom, product, line.product_uom_qty)

        return lines

    def _expand_bom(self, bom, root_product, root_qty, parent_section=None, ancestors=None):

        if ancestors is None:
            ancestors = set()

        order = self.order_id

        if root_product in ancestors:
            raise UserError(_("BoM cycle detected for %s") % root_product.display_name)
        ancestors = ancestors | {root_product}

        if parent_section is None:
            section_sequence = self.sequence - 10
        else:
            section_sequence = parent_section.sequence + 0.0001

        section = self.create({
            'order_id': order.id,
            'display_type': 'line_section',
            'name': root_product.display_name,
            'sequence': section_sequence,
            'bom_auto_created': True,
        })

        components = bom.bom_line_ids

        products_to_find = self.env['product.product'].browse([line.product_id.id for line in components])
        bom_find_map = self.env['mrp.bom']._bom_find(products_to_find)

        for bom_line in components:
            comp_product = bom_line.product_id
            effective_qty = bom_line.product_qty * root_qty

            so_line = self.create({
                'order_id': order.id,
                'product_id': comp_product.id,
                'name': comp_product.get_product_multiline_description_sale(),
                'product_uom_qty': effective_qty,
                'price_unit': comp_product.lst_price,
                'sequence': section.sequence + 0.0001,
                'bom_auto_created': True,
            })

            child_bom = bom_find_map.get(comp_product)
            if child_bom:
                so_line._expand_bom(
                    bom=child_bom,
                    root_product=comp_product,
                    root_qty=effective_qty,
                    parent_section=so_line,
                    ancestors=ancestors,
                )

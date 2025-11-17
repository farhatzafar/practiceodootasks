from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sale_total_company_id = fields.Many2one(
        "res.company",
        string="Company of Total Sale Amount",
        config_parameter="%s.%s"
                         % ("account_currency_custom", "sale_total_company_id"),
        help=(
            "From this company, its currency will be taken to display the"
            " total amount.\n"
            "Make sure you have currency rates linked to this company."
        ),
    )

    sale_total_company_currency = fields.Many2one(
        "res.currency",
        string="Currency of Total Sale Amount",
        related="sale_total_company_id.currency_id",
        readonly=True,
    )


    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for vals in vals_list:
            if vals.get("sale_total_company_id"):
                self.env["sale.order"].search([]).write(
                    {"total_company_id": vals["sale_total_company_id"]}
                )
        return res

    def write(self, vals):
        res = super().write(vals)
        if "sale_total_company_id" in vals:
            self.env["sale.order"].search([]).write(
                {"total_company_id": vals["sale_total_company_id"]}
            )
        return res

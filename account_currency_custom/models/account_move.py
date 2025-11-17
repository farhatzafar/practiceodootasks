from ast import literal_eval
from lxml import etree
from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        """
        Set the correct label for `total amount`, depending on the currency
        """
        result = super().fields_view_get(
            view_id=view_id,
            view_type=view_type,
            toolbar=toolbar,
            submenu=submenu,
        )
        result["arch"] = self._apply_total_currency_label(
            result["arch"], view_type=view_type
        )
        return result

    @api.model
    def _apply_total_currency_label(self, view_arch, view_type="form"):
        doc = etree.XML(view_arch)

        sale_total_company_id = literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "account_currency_custom.sale_total_company_id",
                "False",
            )
        )
        total_company = self.env["res.company"].browse(sale_total_company_id)

        for node in doc.xpath(
            "//field[@name='amount_total_curr']"
        ):
            node.set(
                "string",
                _("Total (%s)") % (total_company.currency_id.name or ""),
            )
        return etree.tostring(doc, encoding="unicode")

    def _default_total_company(self):
        sale_total_company_id = literal_eval(
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "account_currency_custom.sale_total_company_id",
                "False",
            )
        )
        return self.env["res.company"].browse(int(sale_total_company_id))

    total_company_id = fields.Many2one(
        "res.company",
        string="Company (its currency) for the Total Amount",
        help=(
            "From this company, its currency will be taken to display the"
            " total amount."
        ),
        default=_default_total_company,
    )
    total_currency = fields.Many2one(
        "res.currency",
        related="total_company_id.currency_id",
        string="Currency for Total Amount",
        readonly=True,
    )
    amount_total_curr = fields.Monetary(
        string="Total Amount (Specific Currency)",
        readonly=True,
        compute="_compute_amount_company",
        currency_field="total_currency",
        store=True,
    )

    @api.depends("amount_total", "currency_id", "total_company_id")
    def _compute_amount_company(self):
        for move in self:
            if not move.total_company_id or not move.total_company_id.currency_id:
                move.amount_total_curr = 0.0
                continue

            invoice_date = move.invoice_date or fields.Date.today()

            move.amount_total_curr = move.currency_id._convert(
                move.amount_total,
                move.total_company_id.currency_id,
                move.total_company_id,
                invoice_date,
            )







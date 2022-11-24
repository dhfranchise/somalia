from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    terms = fields.Char(string="Terms Of Payment")
    price_quoted = fields.Char(string="Price Quoted")
    delivery = fields.Char(string="Delivery")
    quote = fields.Char(string="Quote")
    warranty = fields.Char(string="Warranty")

    @api.model
    def default_get(self, vals):
        res = super(SaleOrder, self).default_get(vals)
        res.update({"terms": "By Cheque/Cash before delivery. Cheque to be cleared before delivery is made."})
        res.update({"price_quoted": "Final pricing is inclusive VAT (Grand Total)"})
        res.update(
            {
                "delivery": "2-3 days after receipt of confirmed LPO or signed Proforma Invoice. \
                    Subject to availability of goods."
            }
        )
        res.update({"quote": "Validiy .. Days"})
        res.update(
            {
                "warranty": """1 year on Desks and Cabinets against manufacturers defects \
                                under normal usage.
                                1 year on all mechanical componenets of Chairs against \
                                    manufacturing defects under normal usage .
                                No warrenty on fabric and leather upholstery pf the chairs"""
            }
        )
        return res

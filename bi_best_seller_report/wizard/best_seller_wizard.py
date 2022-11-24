from odoo import fields, models


class BestSellerReport(models.TransientModel):
    _name = "best.seller.report"

    start_date = fields.Date("Start Date", required="1")
    end_date = fields.Date("End Date", required="1")

    def button_print(self):
        data = {
            "ids": self.ids,
            "model": self._name,
            "form": {
                "start_date": self.start_date,
                "end_date": self.end_date,
            },
        }
        return self.env.ref("bi_best_seller_report.action_view_best_seller_report1").report_action(
            self, data=data, config=False
        )

odoo.define('pos_receipt_design.pos_receipt_design', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    var OrderSuper = models.Order.prototype;
    models.Order = models.Order.extend({

        export_for_printing: function () {
            var receipt = OrderSuper.export_for_printing.bind(this)();

            receipt = _.extend(receipt, {
                'company': _.extend(receipt.company, {
                'street': this.pos.company.street,
                'city': this.pos.company.city,
                'state': this.pos.company.state_id[1],
                'zip': this.pos.company.zip,
                'mobile': this.pos.company.mobile,
                })
            });

            return receipt;
        },
    });
});

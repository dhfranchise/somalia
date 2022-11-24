odoo.define('bi_pos_payment_reference.models', function(require) {
    'use strict';

    var models = require('point_of_sale.models');

    models.load_fields("pos.payment.method", ["is_provide_payment_ref"]);

    models.load_fields("pos.payment", ["payment_reference"]);

    var _super_paymentline = models.Paymentline.prototype;
    models.Paymentline = models.Paymentline.extend({
        initialize: function(attr, options) {
            _super_paymentline.initialize.apply(this, arguments);
            this.payment_reference = this.payment_reference || '';
        },
        init_from_JSON: function(json) {
            _super_paymentline.init_from_JSON.apply(this, arguments);
            this.payment_reference = json.payment_reference;
        },
        export_as_JSON: function () {
            var json = _super_paymentline.export_as_JSON.call(this);
            json.payment_reference = this.payment_reference || "";
            return json;
        },
    });

    models.Order = models.Order.extend({
        get_payment_reference: function () {
            var reference_payment_line = this.paymentlines.find(pl => pl.payment_reference !== "");
            return reference_payment_line ? reference_payment_line.payment_reference : "";
        }
    });

});

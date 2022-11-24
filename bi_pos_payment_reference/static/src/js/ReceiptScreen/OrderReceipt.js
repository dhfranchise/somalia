odoo.define('bi_pos_payment_reference.OrderReceiptExt', function(require) {
    'use strict';

    const OrderReceipt = require('point_of_sale.OrderReceipt');
    const Registries = require('point_of_sale.Registries');

    const OrderReceiptExt = (OrderReceipt) =>
        class extends OrderReceipt {

            get payment_references() {
                let refs = [];
                _.each(this.receiptEnv.paymentlines, function (l) {
                    if (l.payment_reference) {
                        refs.push(l.payment_reference);
                    }
                });
                return refs;
            }
        };

    Registries.Component.extend(OrderReceipt, OrderReceiptExt);

    return OrderReceiptExt;
});

odoo.define('bi_pos_auto_invoice.PaymentScreen', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const PaymentScreenAutoInvoice = PaymentScreen =>
        class extends PaymentScreen {
            constructor() {
                super(...arguments);
                if(this.env.pos.config.auto_check_invoice){
                    this.currentOrder.set_to_invoice(true);
                }
            }

        }

    Registries.Component.extend(PaymentScreen, PaymentScreenAutoInvoice);

    return PaymentScreen;

});

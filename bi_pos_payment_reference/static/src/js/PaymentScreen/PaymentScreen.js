odoo.define('bi_pos_payment_reference.PaymentScreen', function(require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const PaymentScreen = require('point_of_sale.PaymentScreen');

    const PaymentScreenReference = PaymentScreen => class extends PaymentScreen {
        async addNewPaymentLine({ detail: paymentMethod }) {
            if (paymentMethod.is_provide_payment_ref) {
                let { confirmed, payload } = await this.showPopup('ReferencePopup', {
                    title: this.env._t('Payment Reference'),
                    startingValue: null,
                });
                if (!confirmed) return false;
                super.addNewPaymentLine(...arguments);
                if (confirmed) {
                    if (payload) {
                        this.currentOrder.selected_paymentline.payment_reference = payload;
                    }else {
                        return false;
                    }
                }
            }else
                super.addNewPaymentLine(...arguments);
        }
    };

    Registries.Component.extend(PaymentScreen, PaymentScreenReference);

    return PaymentScreen;

});

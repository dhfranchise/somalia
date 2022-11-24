odoo.define('bi_pos_payment_method_restriction.PaymentScreen', function(require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const NumberBuffer = require('point_of_sale.NumberBuffer');

    const PaymentScreenRestriction = PaymentScreen => class extends PaymentScreen {
        async addNewPaymentLine({ detail: paymentMethod }) {
            if (paymentMethod.call_super) {
                paymentMethod.call_super = false;
                return super.addNewPaymentLine(...arguments);
            }
            if (this.currentOrder.get_selected_orderline()) {
                let refund_qty = this.currentOrder.get_selected_orderline().quantity;
                if (refund_qty < 0 && paymentMethod.split_transactions === false) {
                    let title = 'Please enter password for selecting the payment method';
                    await this.show_password_prompt(paymentMethod, 1, title);
                }else
                    return super.addNewPaymentLine(...arguments);
            }else
                return super.addNewPaymentLine(...arguments);
        }

        async show_password_prompt (val, try_count, title) {
            if (!try_count)
                try_count = 1;
            if (try_count > 1)
                title = "Incorrect password provided, please try again";
            let { confirmed, payload } = await this.showPopup('TextInputPopup', {
                title: title
            });

            if (confirmed) {
                let pwd_payment_method = this.env.pos.config.pwd_payment_method;
                if (payload && payload == pwd_payment_method) {
                    val.call_super = true;
                    await this.addNewPaymentLine({ detail: val });
                    this.trigger('close-popup');
                }
                else {
                    try_count += 1;
                    this.show_password_prompt(val, try_count);
                }
            } else {
                return;
            }
        }
    };

    Registries.Component.extend(PaymentScreen, PaymentScreenRestriction);

    return PaymentScreen;

});

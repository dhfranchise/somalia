odoo.define('bi_pos_payment_reference.TicketScreen', function(require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const TicketScreen = require('point_of_sale.TicketScreen');

    const TicketScreenPaymentSearch = TicketScreen =>
        class extends TicketScreen {

            _getSearchFields() {
                const fields = super._getSearchFields();
                 fields.PAYMENT_REFERENCE = {
                    repr: (order) => order.get_payment_reference(),
                    displayName: this.env._t('Payment Reference'),
                    modelField: 'payment_ids.payment_reference',
                 }
                return fields;
            }

            getPaymentReference(order) {
                return order.get_payment_reference();
            }

        };
        Registries.Component.extend(TicketScreen, TicketScreenPaymentSearch);

    return TicketScreenPaymentSearch;
});

odoo.define('bi_pos_invoice_print.InvoiceButton', function (require) {
    'use strict';

    const InvoiceButton = require('point_of_sale.InvoiceButton');
    const Registries = require('point_of_sale.Registries');

    const ChangeInvoiceButton = (InvoiceButton) =>
        class extends InvoiceButton {

            async _downloadInvoice(orderId) {
                try {
                    const [orderWithInvoice] = await this.rpc({
                        method: 'read',
                        model: 'pos.order',
                        args: [orderId, ['account_move']],
                        kwargs: { load: false },
                    });
                    if (orderWithInvoice && orderWithInvoice.account_move) {
                        await this.env.pos.do_action('bi_tax_invoice.tax_invoice_pdf', {
                            additional_context: {
                                active_ids: [orderWithInvoice.account_move],
                            },
                        });
                    }
                } catch (error) {
                    if (error instanceof Error) {
                        throw error;
                    } else {
                        // NOTE: error here is most probably undefined
                        this.showPopup('ErrorPopup', {
                            title: this.env._t('Network Error'),
                            body: this.env._t('Unable to download invoice.'),
                        });
                    }
                }
            }
        };

    Registries.Component.extend(InvoiceButton, ChangeInvoiceButton);
    return ChangeInvoiceButton;

});

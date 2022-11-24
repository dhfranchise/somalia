odoo.define('pos_invoice_print.receipt_screen', function (require) {
    'use strict';

    var  Registries = require('point_of_sale.Registries');
    var  ReceiptScreen = require('point_of_sale.ReceiptScreen');

    var ReceiptScreenInvoicePrint = (ReceiptScreen) =>
        class ReceiptScreenInvoicePrint extends ReceiptScreen {

            async printInvoicePdf() {
                var self =this;
                const order = this.currentOrder;
                return new Promise((resolve, reject) => {
                    if (order.invoice_id) {
                        self.env.pos.flush_mutex.exec(async () => {
                            try {
                                await self.env.pos.do_action('bi_tax_invoice.tax_invoice_pdf', {
                                        additional_context: {
                                            active_ids: [order.invoice_id],
                                        },
                                    })
                                    .catch(() => {
                                        reject({ code: 401, message: 'Backend Invoice', data: { order: order } });
                                    });
                                resolve(true);
                            } catch (error) {
                                reject(error);
                            }
                        });
                    }
                });
            }
        }

    Registries.Component.extend(ReceiptScreen, ReceiptScreenInvoicePrint);

});

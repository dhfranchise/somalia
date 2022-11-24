odoo.define('bi_pos_credit_reconcile.ReceiptConfirmationPopup', function(require) {
    'use strict';

    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');
    var _t = require('web.core')._t;

    class ReceiptConfirmationPopup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
        }

        async do_calculate_tender_amount(){
            var self = this;
            let advance_details_entered = '';
            let partner_id = self.props.order.get_client().id;
            let credit_details_entered = '';
            let advance_class = $('.advance-receipt-details');
            let credit_class = $('.credit-note-details');
            $.each(advance_class, function(index, value) {
                let entered_details_advance = $(value).find('input');
                let entered_advance_details = entered_details_advance.val();
                advance_details_entered = entered_advance_details;
            });
            $.each(credit_class, function(index, value) {
                let entered_details_credit = $(value).find('input');
                let entered_credit_details = entered_details_credit.val();
                credit_details_entered = entered_credit_details;
            });
            await this.rpc({
                model: 'pos.order',
                method: 'get_tender_amount',
                args: [partner_id, advance_details_entered, credit_details_entered],
            }).then(function(return_value) {
                if (!return_value['status']) {
                    if(return_value['issue_model'] == 'advance') {
                        if (return_value['advance_issue'] == 'notfound') {
                            alert(_t("Following Advance Number Not Found! \r\n") + return_value['advance_record']);
                            // self.showPopup('ErrorPopup',{
                            //     'title': 'Following Advance Number Not Found!',
                            //     'body':  return_value['advance_record'],
                            // });
                        }else if (return_value['advance_issue'] == 'due_date') {
                            alert(_t("Following Advance Number is Not Valid! \r\n") + return_value['advance_record']);
                            // self.showPopup('ErrorPopup',{
                            //     'title': 'Following Advance Number is Not Valid!',
                            //     'body':  return_value['advance_record'],
                            // });
                        }else {
                            alert(_t("Following Advance Is Already Reconciled! \r\n") + return_value['advance_record']);
                            // self.showPopup('ErrorPopup',{
                            //     'title': 'Following Advance Is Already Reconciled!',
                            //     'body':  return_value['advance_record'],
                            // });
                        }
                    }else if (return_value['issue_model'] == 'credit') {
                        if (return_value['credit_issue'] == 'notfound') {
                            alert(_t("Following Credit Note Number Not Found! \r\n") + return_value['advance_record']);
                            // self.showPopup('ErrorPopup',{
                            //     'title': 'Following Credit Note Number Not Found!',
                            //     'body':  return_value['credit_record'],
                            // });
                        }else if (return_value['credit_issue'] == 'overdue') {
                            alert(_t("Following Credit Note Number is Not Valid! \r\n") + return_value['advance_record']);
                            // self.showPopup('ErrorPopup',{
                            //     'title': 'Following Credit Note Number is Not Valid!',
                            //     'body':  return_value['credit_record'],
                            // });
                        }else {
                            alert(_t("Following Credit Note Is Already Reconciled! \r\n") + return_value['advance_record']);
                            // self.showPopup('ErrorPopup',{
                            //     'title': 'Following Credit Note Is Already Reconciled!',
                            //     'body':  return_value['credit_record'],
                            // });
                        }
                    }
                } else {
                    var current_order = self.props.order;
                    current_order.advance_total = return_value['advance_total'];
                    current_order.advance_list = return_value['advance_array'];
                    current_order.credit_total = return_value['credit_total'];
                    current_order.credit_list = return_value['credit_array'];
                    current_order.advance_credit_total = return_value['advance_credit_total'];
                    current_order.set_to_use_advance_amount();
                }
            });

            self.trigger('close-popup');
        }
    }

    ReceiptConfirmationPopup.template = 'ReceiptConfirmationPopup';
    Registries.Component.add(ReceiptConfirmationPopup);
    return ReceiptConfirmationPopup;
});

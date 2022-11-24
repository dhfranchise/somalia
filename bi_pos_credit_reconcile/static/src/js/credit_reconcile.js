odoo.define('bi_pos_credit_reconcile.credit_reconcile', function (require) {
    "use strict";

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    var models = require('point_of_sale.models');
    const { useListener } = require('web.custom_hooks');
    var utils = require('web.utils');
    var round_pr = utils.round_precision;

    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function(attr, options) {
            this.use_advance_amount = false;
            this.advance_total = false;
            this.advance_list = [];
            this.credit_total = false;
            this.credit_list = [];
            this.advance_credit_total = false;
            _super_order.initialize.call(this,attr,options);
        },
        export_as_JSON: function() {
            var self = this;
            var loaded = _super_order.export_as_JSON.call(this);
            loaded.amount_paid = ((this.use_advance_amount) ? (self.get_total_paid() - self.get_change() + self.advance_total) : (self.get_total_paid() - self.get_change())),
            loaded.use_advance_amount = self.use_advance_amount || false;
            loaded.advance_total = self.advance_total || false;
            loaded.advance_list = self.advance_list || [];
            loaded.credit_total = self.credit_total || false;
            loaded.credit_list = self.credit_list || [];
            loaded.advance_credit_total = self.advance_credit_total || false;
            return loaded;
        },
        init_from_JSON: function(json){
            _super_order.init_from_JSON.apply(this,arguments);
            this.use_advance_amount = json.use_advance_amount || false;
            this.advance_total = json.advance_total || false;
            this.advance_list = json.advance_list || [];
            this.credit_total = json.credit_total || false;
            this.credit_list = json.credit_list || [];
            this.advance_credit_total = json.advance_credit_total || false;
        },
        set_to_use_advance_amount: function() {
            if (this.get_client()) {
                let current_value = !this.is_to_use_advance_amount();
                this.use_advance_amount = current_value;
            }
        },
        remove_to_use_advance_amount: function() {
            let current_value = this.set_advance_amout();
            this.use_advance_amount = current_value;
        },
        is_to_use_advance_amount: function() {
            if (!this.get_client()) {
                this.use_advance_amount = false;
                this.advance_total = false;
                this.advance_list = [];
                this.credit_total = false;
                this.credit_list = [];
                this.advance_credit_total = false;
            }
            return this.use_advance_amount;
        },
        set_advance_amout: function(){
            this.use_advance_amount = false;
            this.advance_total = false;
            this.advance_list = [];
            this.credit_total = false;
            this.credit_list = [];
            this.advance_credit_total = false;
            return this.use_advance_amount;
        },
        get_change: function(paymentline) {
            if (this.use_advance_amount){
                if (!paymentline) {
                    var change = this.get_total_paid() - this.get_total_with_tax() - this.get_rounding_applied() + this.advance_credit_total;
                } else {
                    var change = -this.get_total_with_tax() + this.advance_credit_total;
                    var lines  = this.paymentlines.models;
                    for (var i = 0; i < lines.length; i++) {
                        change += lines[i].get_amount();
                        if (lines[i] === paymentline) {
                            break;
                        }
                    }
                }
            } else {
                if (!paymentline) {
                    var change = this.get_total_paid() - this.get_total_with_tax() - this.get_rounding_applied();
                } else {
                    var change = -this.get_total_with_tax();
                    var lines  = this.paymentlines.models;
                    for (var i = 0; i < lines.length; i++) {
                        change += lines[i].get_amount();
                        if (lines[i] === paymentline) {
                            break;
                        }
                    }
                }
            }
            return round_pr(Math.max(0,change), this.pos.currency.rounding);
        },
        get_due: function(paymentline) {
            if (this.use_advance_amount && (this.get_total_with_tax() > 0)){
                if (!paymentline) {
                    var due = this.get_total_with_tax() - this.get_total_paid() + this.get_rounding_applied() - this.advance_credit_total;
                } else {
                    var due = this.get_total_with_tax();
                    var lines = this.paymentlines.models;
                    for (var i = 0; i < lines.length; i++) {
                        if (lines[i] === paymentline) {
                            break;
                        } else {
                            due -= lines[i].get_amount();
                        }
                    }
                }
            } else {
                if (!paymentline) {
                    var due = this.get_total_with_tax() - this.get_total_paid() + this.get_rounding_applied();
                } else {
                    var due = this.get_total_with_tax();
                    var lines = this.paymentlines.models;
                    for (var i = 0; i < lines.length; i++) {
                        if (lines[i] === paymentline) {
                            break;
                        } else {
                            due -= lines[i].get_amount();
                        }
                    }
                }
            }
            return round_pr(due, this.pos.currency.rounding);
        },

        });


    const PosPartialPaymentScreen = PaymentScreen =>
        class extends PaymentScreen {
            constructor() {
                super(...arguments);
                this.use_advance_amount = false;
                useListener('click-tenderAmountDetails', this.clickTenderAmountDetails);
            }
            clickTenderAmountDetails (event) {
                let self = this;
                if (!self.env.pos.get_order().use_advance_amount){
                    self.showPopup('ReceiptConfirmationPopup', {
                        'order': this.env.pos.get_order(),
                    });
                    return;
                } else {
                    this.env.pos.get_order().remove_to_use_advance_amount();
                    this.render();
                }
            }
    }

    Registries.Component.extend(PaymentScreen, PosPartialPaymentScreen);
});

odoo.define("bi_pos_line_discount_selection.DiscountSelectionPopup", function (require) {

    const Registries = require("point_of_sale.Registries");
    const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");

    class DiscountSelectionPopup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
        }
        async confirm() {
            var self = this;
            this.props.resolve({ confirmed: true, payload: await this.getPayload() });

            if (!$(".discount_value").val()) {
                alert("Enter amount of discount.");
                $(".discount_value").addClass("invalid_number");
            } else if (
                ($(".discount_value").val() && parseFloat($(".discount_value").val()) > 100 && document.getElementById("discount_percentage_radio") && document.getElementById("discount_percentage_radio").checked) ||
                ($(".discount_value").val() && parseFloat($(".discount_value").val()) < 0) ||
                !/^\d*\.?\d*$/.test(parseFloat($(".discount_value").val()))
            ) {
                $(".discount_value").addClass("invalid_number");
                $(".discount_value").val(" ");
                $(".discount_value").focus();
            } else {
                var value = $(".discount_value").val();
                if (document.getElementById("discount_fixed_radio") && document.getElementById("discount_fixed_radio").checked) {
                    var selected_orderline = self.env.pos.get_order().get_selected_orderline();
                    if (selected_orderline) {
                        if (selected_orderline.get_discount()) {
                            var price = selected_orderline.get_display_price();
                            var current_price = price - value;
                            var discount = ((selected_orderline.price * selected_orderline.quantity - current_price) / (selected_orderline.price * selected_orderline.quantity)) * 100;
                            if (selected_orderline.get_fix_discount()) {
                                selected_orderline.set_fix_discount(selected_orderline.get_fix_discount() + parseFloat(value));
                            } else {
                                selected_orderline.set_fix_discount(parseFloat(value));
                            }
                            selected_orderline.set_discount(discount);
                        } else {
                            var apply_disc_percen = (value * 100) / selected_orderline.get_display_price();
                            selected_orderline.set_fix_discount(parseFloat(value));
                            selected_orderline.set_discount(apply_disc_percen);
                        }
                    }
                }
                if (document.getElementById("discount_percentage_radio") && document.getElementById("discount_percentage_radio").checked) {
                    var selected_orderline = self.env.pos.get_order().get_selected_orderline();
                    if (selected_orderline) {
                        if (selected_orderline.get_discount()) {
                            var price = selected_orderline.get_display_price();

                            var current_price = price - (price * value) / 100;
                            var discount = ((selected_orderline.price * selected_orderline.quantity - current_price) / (selected_orderline.price * selected_orderline.quantity)) * 100;

                            selected_orderline.set_discount(discount);
                        } else {
                            selected_orderline.set_discount(parseFloat(value));
                        }
                    }

                }
                self.trigger("close-popup");
            }
        }
    }

    DiscountSelectionPopup.template = "DiscountSelectionPopup";

    Registries.Component.add(DiscountSelectionPopup);
});

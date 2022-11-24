odoo.define("bi_pos_line_discount_selection.RemoveDiscountButton", function (require) {

    const PosComponent = require("point_of_sale.PosComponent");
    const Registries = require('point_of_sale.Registries');
    const { useListener } = require("web.custom_hooks");
    const ProductScreen = require('point_of_sale.ProductScreen');

    class RemoveDiscountButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener("click-remove-discount-button", this.onClickRemoveDiscount);
        }

        onClickRemoveDiscount() {
            var self = this;
            var order = self.env.pos.get_order();
            var orderlines = self.env.pos.get_order().get_orderlines();
            if (orderlines) {
                _.each(orderlines, function (each_orderline) {
                    each_orderline.set_discount(0);
                    each_orderline.set_fix_discount(0);
                    if (self.env.pos.config.discount_product_id) {
                        var product  = self.env.pos.db.get_product_by_id(self.env.pos.config.discount_product_id[0]);
                        if (each_orderline.product.id == product.id) {
                            order.remove_orderline(each_orderline);
                        }
                    }
                });
            }
        }
    }

    RemoveDiscountButton.template = "RemoveDiscountButton";

    ProductScreen.addControlButton({
        component: RemoveDiscountButton,
        condition: function() {
            return this.env.pos.config.enable_manual_discount_selection;
        }
    });

    Registries.Component.add(RemoveDiscountButton);

    return RemoveDiscountButton;
});

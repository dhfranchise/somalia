odoo.define("bi_pos_line_discount_selection.ProductScreen", function (require) {
    "use strict";

    const Registries = require("point_of_sale.Registries");
    const ProductScreen = require("point_of_sale.ProductScreen");

    const ProductScreenDiscountSelection = (ProductScreen) =>
        class extends ProductScreen {
            _setValue(val) {
                super._setValue(val);
                var mode = this.state.numpadMode;
                var order = this.env.pos.get_order();
                if(order.get_selected_orderline() && this.env.pos.config.discount_product_id){
                    var product  = this.env.pos.db.get_product_by_id(this.env.pos.config.discount_product_id[0]);
                    if(order.get_selected_orderline().product.id == product.id){
                        if(mode == "discount" && val != "remove"){
                            this.showPopup('ErrorPopup', {
                                title: this.env._t('Discount is already applied'),
                                body: this.env._t('You can not apply discount on the global discount product'),
                            });
                        }
                    }else if(mode == "discount" && order.get_selected_orderline().get_fix_discount() > 0) {
                        var discount = (val/100) * (order.get_selected_orderline().price * order.get_selected_orderline().quantity);
                        order.get_selected_orderline().set_fix_discount(discount);
                    }
                }
            }
        };

    Registries.Component.extend(ProductScreen, ProductScreenDiscountSelection);
});

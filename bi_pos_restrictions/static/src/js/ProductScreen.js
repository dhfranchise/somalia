odoo.define('bi_pos_restrictions.productScreen', function(require) {
    "use strict";

    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');

    const ProductScreenDenyOrder = (ProductScreen) =>
        class extends ProductScreen {

            async _clickProduct(event, return_super = false) {
                let self = this;
                let order = self.env.pos.get_order();
                let lines = order.get_orderlines();
                const product = event.detail;
                let deny_order = self.env.pos.config.pos_deny_order;
                let deny_qty = self.env.pos.config.pos_deny_qty;
                let call_super = true;
                if (product.type == 'product'){
                    if (deny_order && product.location_wise_qty <= deny_qty)
                    {
                        call_super = false;
                        let title = self.env._t('Denied Order, Please enter the password for order products');
                        this.show_password_prompt(event, 1, title);
                    }
                    else if (lines)
                    {
                        for (let i = 0; i < lines.length; i++)
                        {
                            if (lines[i].product.type == 'product')
                            {
                                if (deny_order && (lines[i].product.location_wise_qty + (- lines[i].quantity)) <= deny_qty){
                                    call_super = false;
                                    let title = self.env._t('Ordered qty of One or more product(s) is more than available qty.');
                                    this.show_password_prompt(event, 1, title);
                                }
                            }
                        }
                    }
                }

                if(call_super){
                    super._clickProduct(event);
                }
                if(return_super){
                    super._clickProduct(event);
                }
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
                    let pw_allow_order = this.env.pos.config.pw_allow_order;
                    if (payload && payload == pw_allow_order) {
                        await this._clickProduct(val, true);
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

    Registries.Component.extend(ProductScreen, ProductScreenDenyOrder);

    return ProductScreen;

});

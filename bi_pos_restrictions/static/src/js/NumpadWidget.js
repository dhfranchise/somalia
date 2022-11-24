odoo.define('bi_pos_restrictions.NumpadWidget', function (require) {
    'use strict';

    const Registries = require("point_of_sale.Registries");
    const NumpadWidget = require("point_of_sale.NumpadWidget");

    const NumpadWidgetDiscount = (NumpadWidget) =>
        class extends NumpadWidget {
            changeMode(mode) {
                var self = this;
                var call_super = true
                if (mode && mode == "discount" && self.env.pos.config.restrict_line_discount && self.env.pos.config.enable_manual_discount_selection) {
                    let title = self.env._t('Please enter the password for apply discount');
                    this.show_password_prompt(1, title);
                    call_super = false;
                }else if (mode && mode == "discount" && !self.env.pos.config.restrict_line_discount && self.env.pos.config.enable_manual_discount_selection) {
                    call_super = false;
                    super.changeMode("discount_selection");
                }
                if (call_super)
                    super.changeMode(mode);
            }

            async show_password_prompt (try_count, title) {
                if (!try_count)
                    try_count = 1;
                if (try_count > 1)
                    title = "Incorrect password provided, please try again";
                let { confirmed, payload } = await this.showPopup('TextInputPopup', {
                    title: title
                });

                if (confirmed) {
                    let pw_allow_discount = this.env.pos.config.pw_allow_discount;
                    if (payload && payload == pw_allow_discount) {
                        this.trigger('close-popup');
                        super.changeMode("discount_selection");
                    }
                    else {
                        try_count += 1;
                        this.show_password_prompt(try_count);
                    }
                } else {
                    return;
                }
            }
        };


    Registries.Component.extend(NumpadWidget, NumpadWidgetDiscount);

    return NumpadWidgetDiscount;
});

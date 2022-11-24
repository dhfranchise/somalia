odoo.define("bi_pos_line_discount_selection.NumpadWidget", function (require) {
    "use strict";

    const Registries = require("point_of_sale.Registries");
    const NumpadWidget = require("point_of_sale.NumpadWidget");

    const PosNumpadWidget = (NumpadWidget) =>
        class extends NumpadWidget {
            changeMode(mode) {
                super.changeMode(mode);
                var self = this;
                if (mode && mode == "discount_selection" && self.env.pos.config.enable_manual_discount_selection) {
                    this.showPopup("DiscountSelectionPopup");
                }
            }
        };

    Registries.Component.extend(NumpadWidget, PosNumpadWidget);
});

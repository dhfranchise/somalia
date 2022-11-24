odoo.define('bi_pos_button.PosNewButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class PosNewButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        async onClick() {
            var settings = {
                    "url": "http://localhost:8001/printers/02mw601892/xreport",
                    "method": "POST",
                    "timeout": 0,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                };

                $.ajax(settings).done(function (response) {
                console.log(response);
            });
        }
    }

    PosNewButton.template = 'PosNewButton';
    ProductScreen.addControlButton({
        component: PosNewButton,
        condition: function() {
            return this.env.pos;
        },
    });
    Registries.Component.add(PosNewButton);
    return PosNewButton;

});

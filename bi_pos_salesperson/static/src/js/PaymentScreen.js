odoo.define('bi_pos_salesperson.PaymentScreen', function(require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const PaymentCustomScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            async toggleSelectSalesperson() {
                if (!this.env.pos.config.is_salesperson_enabled) return;

                const posSalespersonList = [];
                const salesPersonIds = await this.rpc({
                    model: 'hr.employee',
                    method: 'read',
                    args: [this.env.pos.config.salesperson_ids, ['name', 'id']],
                });
                for (let salesperson of salesPersonIds) {

                    posSalespersonList.push({
                        id: salesperson.id,
                        label: salesperson.name,
                        item: salesperson,
                    });
                }

                const { confirmed, payload: selectedSalespersonId } = await this.showPopup(
                    'SelectionPopup',
                    {
                        title: 'Select Salesperson',
                        list: posSalespersonList,
                    }
                );

                if (confirmed) {
                    if (this.env.pos){
                        this.env.pos.get_order().set_salesperson(selectedSalespersonId);
                    }
                }
            }

            async validateOrder(isForceValidate) {
                if (this.env.pos.config.is_salesperson_enabled && !this.env.pos.get_order().get_salesperson()) {
                    const { confirmed } = await this.showPopup('ConfirmPopup', {
                        title: this.env._t('Please select the Salesperson'),
                        body: this.env._t(
                            'You need to select the salesperson before you can invoice or ship an order.'
                        ),
                    });
                    if (confirmed) {
                        this.toggleSelectSalesperson();
                    }
                    return false;
                }
                await super.validateOrder(...arguments);
            }
        };

    Registries.Component.extend(PaymentScreen, PaymentCustomScreen);
    return PaymentScreen;

});

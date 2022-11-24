odoo.define('bi_pos_salesperson.SalesPerson', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen');

    // Previously UsernameWidget
    class SalesPerson extends PosComponent {

        async selectCashier() {
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

    }
    SalesPerson.template = 'SalesPerson';

    ProductScreen.addControlButton({
        component: SalesPerson,
        condition: function() {
            return this.env.pos.config.is_salesperson_enabled;
        }
    });

    Registries.Component.add(SalesPerson);

    return SalesPerson;
});

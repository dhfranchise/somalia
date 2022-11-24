odoo.define('bi_import_pricelist.ImportPricelist', function (require) {
    "use strict";

    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var viewRegistry = require('web.view_registry');

    var ImportPricelistListController = ListController.extend({
        buttons_template: 'ImportPricelist.Buttons',

        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            this.$buttons.on('click', '.o_button_import_pricelist', this._onOpenImportWizard.bind(this));
        },

        _onOpenImportWizard: function () {
            var context = {
                active_model: this.modelName,
            };
            this.do_action({
                res_model: 'import.product.pricelist',
                views: [[false, 'form']],
                target: 'new',
                type: 'ir.actions.act_window',
                context: context,
            });
        },
    });

    var PricelistListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: ImportPricelistListController,
        }),
    });

    viewRegistry.add('import_pricelist_tree', PricelistListView);
});

odoo.define('bi_pos_salesperson.models', function(require) {
    "use strict";

    var models = require('point_of_sale.models');

    var posorder_super = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function(attr, options) {
            this.salesperson = this.salesperson || false;
            posorder_super.initialize.call(this,attr,options);
        },

        set_salesperson: function(salesperson) {
            this.salesperson = salesperson;
        },

        get_salesperson: function() {
            return this.salesperson;
        },

        export_as_JSON: function() {
            var self = this;
            var loaded = posorder_super.export_as_JSON.call(this);
            loaded.salesperson = self.salesperson  || false;
            return loaded;
        },

        init_from_JSON: function(json){
            posorder_super.init_from_JSON.apply(this,arguments);
            this.salesperson = json.salesperson || false;
        },

    });

});

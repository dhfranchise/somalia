odoo.define("bi_pos_line_discount_selection.models", function (require) {

    const OrderWidget = require("point_of_sale.OrderWidget");
    const Registries = require("point_of_sale.Registries");

    var models = require("point_of_sale.models");

    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        initialize: function (attr, options) {
            this.fix_discount = 0.00;
            _super_orderline.initialize.call(this, attr, options);
        },
        init_from_JSON: function(json) {
            _super_orderline.init_from_JSON.call(this, json);
            this.set_fix_discount(json.fix_discount);
        },
        clone: function(){
            var orderline = _super_orderline.clone.call(this);
            orderline.fix_discount = this.fix_discount;
            return orderline;
        },
        export_as_JSON: function() {
            var json = _super_orderline.export_as_JSON.call(this);
            json.fix_discount = this.fix_discount;
            return json;
        },
        set_fix_discount: function (discount) {
            this.fix_discount = discount;
        },
        get_fix_discount: function () {
            return this.fix_discount;
        },
    });
});

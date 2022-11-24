odoo.define('bi_pos_payment_pivot.DateFilterPivot', function (require) {
  'use strict';

  var core = require('web.core');
  var _lt = core._lt;

  const { INTERVAL_OPTIONS } = require('@web/search/utils/dates');
  Object.assign(INTERVAL_OPTIONS, {
    'hour': {
      description: _lt("Hour"),
      id: 'hour',
      groupNumber: 1,
    },
  });

});

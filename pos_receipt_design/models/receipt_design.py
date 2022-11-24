#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
#
#################################################################################
from odoo import api, fields, models


class ReceiptDesign(models.Model):
    _name = "receipt.design"
    _rec_name = "name"

    name = fields.Char(string="Name")
    receipt_design = fields.Text(string="Description", required=True)

    @api.model
    def _create_receipt_design_1(self):
        record_data = {}
        record_data["name"] = "Receipt Design 1"
        record_data[
            "receipt_design"
        ] = """
            <div class="pos-receipt">
            <t t-if='receipt.company.logo'>
                <img style="width: 30%;display: block;margin: auto;text-align:left;"
                t-att-src='receipt.company.logo' alt="Logo"/>
            </t>
            <br/>
            <div style="font-size: 80%; text-align:center;">
                <t t-if='receipt.company.name'>
                    <h2>
                    <t t-esc='receipt.company.name' />
                    </h2>
                </t>
                <t t-if='receipt.company.zip'>
                    <div>P.O BOX
                    <t t-esc='receipt.company.zip'/>,
                    </div>
                </t>
                <t t-if='receipt.company.state'>
                    <div><t t-esc='receipt.company.state'/>,</div>
                </t>
                <t t-if='receipt.company.street'>
                    <div>
                    <t t-esc="receipt.company.street"/>
                    </div>
                </t>
                <t t-if='receipt.company.city'>
                    <div><t t-esc='receipt.company.city'/></div>
                </t>
                <t t-if='receipt.company.mobile'>
                  <div>Tel:<t t-esc='receipt.company.mobile' /></div>
                </t>
                <t t-if='receipt.company.phone'>
                    <div>PHONE<t t-esc='receipt.company.phone' /></div>
                </t>
                <t t-if='receipt.company.vat'>
                    <b><div>TIN: <t t-esc='receipt.company.vat' /></div></b>
                </t>
                <div><b>*VAT REGISTERED*</b></div>
                <br/>
                <div>DEFAULT TAX OFFICE</div>
                <br/>
                <t t-if='receipt.header_html'>
                    <t t-raw='receipt.header_html' />
                </t>
                <t t-if='!receipt.header_html and receipt.header'>
                    <div><t t-esc='receipt.header' /></div>
                </t>
            </div>
            <div style="font-size:70%; text-align:left;">
                <div>
                    BUYER'S NAME:
                    <t t-if='receipt.client'>
                    <t t-esc='receipt.client.name' />
                    </t>
                </div>

                <div>
                    RECEIPT NUMBER :
                    <t t-if='receipt.name'>
                    <span t-esc='receipt.name' />
                    </t>
                </div>
            </div>
            <table style="width: 100%;">
              <tr t-foreach="receipt.orderlines" t-as="line"
                style="border-top: 1px dashed black;font-size:14px;font-family: initial;">
                <td style="padding-top:8px;padding-bottom:8px;">
                  <div>
                    <span t-esc="line.quantity"/> X
                    <span t-esc='widget.pos.format_currency_no_symbol(line.price)'/>
                  </div>
                  <div>
                    <span t-esc='line.product_name_wrapped[0]'/>
                  </div>
                </td>
                <td class="pos-receipt-right-align"
                    style="padding-top:8px;padding-bottom:8px;">
                  <div>
                      <span t-esc='widget.pos.format_currency_no_symbol(line.price)'/>
                  </div>

                </td>
              </tr>
              <t t-foreach="order.get_tax_details()" t-as="taxdetail">
                <tr  style="border-top: 1px dashed black;font-size:12px;font-family: initial;">
                  <td style="padding-top:8px;padding-bottom:8px;">
                    <t t-esc="taxdetail.name" />
                  </td>
                  <td class="pos-receipt-right-align" style="padding-top:8px;padding-bottom:8px;">
                      <span t-esc='widget.pos.format_currency_no_symbol(taxdetail.amount)'/>
                  </td>
                </tr>
              </t>
              <tr  style="font-size:12px;font-family: initial;">
                  <td>
                   <b>TOTAL VAT</b>
                  </td>
                  <td class="pos-receipt-right-align">
                    <span t-esc='widget.pos.format_currency_no_symbol(receipt.total_tax)'/>
                  </td>
              </tr>
              <tr  style="border-top: 1px dashed black;font-size:15px;font-family: initial;">
                  <td style="padding-top:8px;padding-bottom:8px;">
                   <b>TOTAL</b>
                  </td>
                  <td class="pos-receipt-right-align" style="padding-top:8px;padding-bottom:8px;">
                    <span t-esc='widget.pos.format_currency_no_symbol(receipt.total_with_tax)'/>
                  </td>
              </tr>
              <tr t-foreach='paymentlines' t-as='line'>
                <td style="font-size:12px;">
                  <t t-esc='line.name'/>
                </td>
                <td style="font-size:12px;">
                  <span t-esc='widget.pos.format_currency_no_symbol(line.get_amount())'
                    class="pos-receipt-right-align"/>
                </td>
              </tr>

          </table>
          <br/>
          <table style="width: 100%;">
            <tr>
                <td style="font-size:14px;">
                    <div>
                      DATE : <t t-esc="receipt.date.localestring.split(' ')[0]"/>
                    </div>
                </td>
                <td style="font-size:14px;float:right;" class="pos-receipt-right-align">
                    <div class="pos-receipt-right-align">
                      TIME : <t t-esc="receipt.date.localestring.split(' ')[1]"/>
                    </div>
                </td>
            </tr>
          </table>
        </div>
        """
        record_id = self.create(record_data)
        pos_config_id = self.env.ref("point_of_sale.pos_config_main")
        if record_id and pos_config_id:
            pos_config_id.use_custom_receipt = True
            pos_config_id.receipt_design_id = record_id.id

    @api.model
    def _create_receipt_design_2(self):
        record_data = {}
        record_data["name"] = "Receipt Design 2"
        record_data[
            "receipt_design"
        ] = """
        <div class="pos-receipt" style="font-family: monospace;">
            <div class="pos-center-align" style="font-size: 12px;">
                <t t-if="order.formatted_validation_date">
                    <t t-esc="order.formatted_validation_date"/>
                </t>
                <t t-else="">
                    <t t-esc="order.validation_date"/>
                </t>
                <br/><t t-esc="order.name"/></div>
            <br />
            <t t-esc="widget.pos.company.name"/><br />
            <div style="font-size:13px">
                Phone: <t t-esc="widget.pos.company.phone || ''"/><br />
            </div>
            <div style="font-size:13px">
                User: <t t-esc="widget.pos.cashier ? widget.pos.cashier.name : widget.pos.user.name"/><br />
            </div>
            <br />
            <t t-if="receipt.header">
                <div style='text-align:center; font-size:13px'>
                    <t t-esc="receipt.header" />
                </div>
                <br />
            </t>
            <table class='receipt-orderlines' style="font-size:13px;">
                <colgroup>
                    <col width='45%' />
                    <col width='25%' />
                    <col width='30%' />
                </colgroup>
                <tr t-foreach="orderlines" t-as="orderline">
                    <td><div style="padding-top: 5px;padding-bottom: 5px;">
                          <t t-esc="orderline.get_product().display_name"/>
                           <t t-if="orderline.get_discount() > 0">
                              <div style="font-size: 12px;font-style: italic;color: #808080;">
                                  <t t-esc="orderline.get_discount()"/>% discount
                              </div>
                          </t>
                        </div>
                    </td>
                    <td class="pos-right-align">
                        <div>
                          <t t-esc="orderline.get_quantity_str_with_unit()"/>
                        </div>
                    </td>
                    <td class="pos-right-align">
                        <div>
                          <t t-esc="widget.pos.format_currency(orderline.get_display_price())"/>
                        </div>
                    </td>
                </tr>
            </table>
            <br />
            <!-- Subtotal -->
            <t t-set='taxincluded' t-value='Math.abs(receipt.subtotal - receipt.total_with_tax) &lt;= 0.000001' />
            <t t-if='!taxincluded'>
                <br/>
                <div style="font-weight: 700; font-size: 14px;">
                    Subtotal
                    <span t-esc='widget.pos.format_currency(receipt.subtotal)' class="pos-receipt-right-align"/>
                </div>
                <t t-foreach='receipt.tax_details' t-as='tax'>
                    <div style="font-weight: 700; font-size: 14px;">
                        <t t-esc='tax.name' />
                        <span t-esc='widget.pos.format_currency_no_symbol(tax.amount)' class="pos-receipt-right-align"/>
                    </div>
                </t>
            </t>
            <!-- Total -->
            <br/>
            <div style="font-weight: 700; font-size: 14px;">
                TOTAL
                <span t-esc='widget.pos.format_currency(receipt.total_with_tax)' class="pos-receipt-right-align"/>
            </div>
            <br/><br/>
            <!-- Payment Lines -->
            <t t-foreach='paymentlines' t-as='line'>
                <div style="font-size: 14px;">
                    <t t-esc='line.name' />
                    <span t-esc='widget.pos.format_currency_no_symbol(line.get_amount())'
                    class="pos-receipt-right-align"/>
                </div>
            </t>
            <br/>
            <div class="receipt-change" style="font-size: 14px;">
                CHANGE
                <span t-esc='widget.pos.format_currency(receipt.change)' class="pos-receipt-right-align"/>
            </div>
            <br/>
            <!-- Extra Payment Info -->
            <t t-if='receipt.total_discount'>
                <div style="font-size: 14px;">
                    Discounts
                    <span t-esc='widget.pos.format_currency(receipt.total_discount)' class="pos-receipt-right-align"/>
                </div>
            </t>
            <t t-if='taxincluded'>
                <t t-foreach='receipt.tax_details' t-as='tax'>
                    <div style="font-size: 14px;">
                        <t t-esc='tax.name' />
                        <span t-esc='widget.pos.format_currency_no_symbol(tax.amount)' class="pos-receipt-right-align"/>
                    </div>
                </t>
                <div style="font-size: 14px;">
                    Total Taxes
                    <span t-esc='widget.pos.format_currency(receipt.total_tax)' class="pos-receipt-right-align"/>
                </div>
            </t>
            <div class='before-footer' />
            <!-- Footer -->
            <div t-if='receipt.footer_html' style="text-align: center; font-size: 14px;">
                <t t-raw='receipt.footer_html'/>
            </div>
            <div t-if='!receipt.footer_html and receipt.footer' style="text-align: center;font-size: 14px;">
                <br/>
                <t t-esc='receipt.footer'/>
                <br/><br/>
            </div>
            <div class='after-footer' style="font-size: 14px;">
                <t t-foreach='paymentlines' t-as='line'>
                    <t t-if='line.ticket'>
                        <br />
                        <div class="pos-payment-terminal-receipt">
                            <t t-raw='line.ticket'/>
                        </div>
                    </t>
                </t>
            </div>
            <br/><br/>
            <div style="text-align:center;border-top: 2px dotted black;padding-top: 15px;">
                <t t-if='receipt.cashier'>
                    <div class='cashier' style="text-align:center;">
                        <div>Served by <t t-esc='receipt.cashier' /></div>
                    </div>
                </t>
                <br/>
                Thank You. Please Visit Again !!
            </div>
        </div>"""
        self.create(record_data)

    @api.model
    def _create_receipt_design_3(self):
        record_data = {}
        record_data["name"] = "Receipt Design 3"
        record_data[
            "receipt_design"
        ] = """
        <div class="pos-receipt">
            <t t-esc="widget.pos.company.name"/><br />
            <div style="font-size:13px">
                Phone: <t t-esc="widget.pos.company.phone || ''"/><br />
            </div>
            <div style="font-size:13px">
                User : <t t-esc="widget.pos.cashier ? widget.pos.cashier.name : widget.pos.user.name"/><br />
            </div>
            <br/>
            <div style="font-size:13px">
                Date :
                <t t-if="order.formatted_validation_date">
                    <t t-esc="order.formatted_validation_date"/>
                </t>
                <t t-else="">
                    <t t-esc="order.validation_date"/>
                </t>
                <br />
            </div>
            <div style="font-size:13px">
                Order : <t t-esc="order.name"/><br />
            </div>
            <br />
            <div style="font-size:13px">
                Cashier :  <t t-esc='receipt.cashier' /><br />
            </div>
            <br/>
            <t t-if="receipt.header">
                <div style='text-align:center; font-size:13px'>
                    <t t-esc="receipt.header" />
                </div>
                <br />
            </t>
            <div>
                <table class='receipt-orderlines' style="font-size:15px; border-style: double;
            border-left: none;border-right: none;border-bottom: none;width: 100%;">
                <colgroup>
                    <col width='40%' />
                    <col width='30%' />
                    <col width='30%' />
                </colgroup>
                <tr style="border-bottom: 1px dashed black;">
                    <th style="text-align:left;">Product</th>
                    <th style="text-align:center;">Qty</th>
                    <th style="text-align:center;">Amount</th>
                </tr>
                <tr t-foreach="orderlines" t-as="orderline">
                    <td style="padding-top: 1%;padding-bottom: 1%;">
                        <t t-esc="orderline.get_product().display_name"/>
                        <t t-if="orderline.get_discount() > 0">
                            <div style="font-size: 12px;font-style: italic;color: #808080;">
                                <t t-esc="orderline.get_discount()"/>% discount
                            </div>
                        </t>
                    </td>
                    <td class="pos-center-align">
                        <t t-esc="orderline.get_quantity_str_with_unit()"/>
                    </td>
                    <td class="pos-center-align">
                        <t t-esc="widget.pos.format_currency(orderline.get_display_price())"/>
                    </td>
                </tr>
                </table>
            </div>
            <br />
            <div style="padding-top: 6px;">
                <!-- Subtotal -->
                <t t-set='taxincluded' t-value='Math.abs(receipt.subtotal - receipt.total_with_tax) &lt;= 0.000001' />
                <t t-if='!taxincluded'>
                    <br/>
                    <div style="font-weight: 700; font-size: 14px; border-top:1px dashed;">
                    <span style="margin-left: 40%;">
                    Subtotal : </span>
                    <span t-esc='widget.pos.format_currency(receipt.subtotal)' class="pos-receipt-right-align"/></div>
                    <t t-foreach='receipt.tax_details' t-as='tax'>
                        <div style="font-weight: 700; font-size: 14px;">
                            <span style="margin-left: 40%;"><t t-esc='tax.name' /></span>
                            <span t-esc='widget.pos.format_currency_no_symbol(tax.amount)'
                            class="pos-receipt-right-align"/>
                        </div>
                    </t>
                </t>
                <!-- Total -->
                <br/>
                <div style="font-weight: 700; font-size: 14px;">
                    <span style="margin-left: 40%;">TOTAL : </span>
                    <span t-esc='widget.pos.format_currency(receipt.total_with_tax)' class="pos-receipt-right-align"/>
                </div>
                <br/><br/>
            </div>
            <!-- Payment Lines -->
            <t t-foreach='paymentlines' t-as='line'>
                <div style="font-size: 14px;border-top:1px dashed;padding-top: 5px;">
                    <span style="margin-left: 40%;"><t t-esc='line.name' /></span>
                    <span t-esc='widget.pos.format_currency_no_symbol(line.get_amount())'
                    class="pos-receipt-right-align"/>
                </div>
            </t>
            <br/>
            <div class="receipt-change" style="font-size: 14px;">
            <span style="margin-left: 40%;">CHANGE : </span>
                <span t-esc='widget.pos.format_currency(receipt.change)' class="pos-receipt-right-align"/>
            </div>
            <br/>
            <!-- Extra Payment Info -->
            <t t-if='receipt.total_discount'>
                <div style="font-size: 14px; border-top:1px dashed;padding-top: 5px;">
                    <span style="margin-left: 40%;">Discounts : </span>
                    <span t-esc='widget.pos.format_currency(receipt.total_discount)' class="pos-receipt-right-align"/>
                </div>
            </t>
            <t t-if='taxincluded'>
                <t t-foreach='receipt.tax_details' t-as='tax'>
                    <div style="font-size: 14px;">
                        <span style="margin-left: 40%;"><t t-esc='tax.name' /></span>
                        <span t-esc='widget.pos.format_currency_no_symbol(tax.amount)' class="pos-receipt-right-align"/>
                    </div>
                </t>
                <div style="font-size: 14px;">
                    <span style="margin-left: 40%;">Total Taxes : </span>
                    <span t-esc='widget.pos.format_currency(receipt.total_tax)' class="pos-receipt-right-align"/>
                </div>
            </t>
            <div class='before-footer' />
            <!-- Footer -->
            <div t-if='receipt.footer_html' style="text-align: center; font-size: 14px;">
                <t t-raw='receipt.footer_html'/>
            </div>
            <div t-if='!receipt.footer_html and receipt.footer' style="text-align: center;font-size: 14px;">
                <br/>
                <t t-esc='receipt.footer'/>
                <br/><br/>
            </div>
            <div class='after-footer' style="font-size: 14px;">
                <t t-foreach='paymentlines' t-as='line'>
                    <t t-if='line.ticket'>
                        <br />
                        <div class="pos-payment-terminal-receipt">
                            <t t-raw='line.ticket'/>
                        </div>
                    </t>
                </t>
            </div>
            <br/><br/>
            <div>
                Thank You. Please Visit Again !!
            </div>
        </div>"""
        self.create(record_data)

    @api.model
    def _create_receipt_design_4(self):
        record_data = {}
        record_data["name"] = "Receipt Design 4"
        record_data[
            "receipt_design"
        ] = """
        <div class="pos-receipt" style="font-family: 'Inconsolata';">
            <div class="pos-receipt-order-data" style="font-size: 14px;">
                <t t-if="order.formatted_validation_date">
                    <t t-esc="order.formatted_validation_date"/>
                </t>
                <t t-else="">
                    <t t-esc="order.validation_date"/>
                </t>
                <t t-esc="order.name"/></div>
            <br />
            <div class="pos-receipt-contact" style="font-size: 14px; font-family: 'Inconsolata'; text-align:left;">
                <div style="font-size:15px;">
                <t t-esc="widget.pos.company.name"/><br />
                </div>
                <div>
                    Phone: <t t-esc="widget.pos.company.phone || ''"/><br />
                </div>
                <div class='cashier'>
                    User: <t t-esc="widget.pos.cashier ? widget.pos.cashier.name : widget.pos.user.name"/><br />
                </div>
                <br />
                <t t-if="receipt.header">
                    <div style='text-align:center;'>
                        <t t-esc="receipt.header" />
                    </div>
                    <br />
                </t>
            </div>
            <table class='orderlines'>
                <colgroup>
                    <col width='40%' />
                    <col width='30%' />
                    <col width='30%' />
                </colgroup>
                <tr t-foreach="orderlines" t-as="orderline">
                    <td><div style="padding-top: 5px;padding-bottom: 5px;">
                        <t t-esc="orderline.get_product().display_name"/>
                        <t t-if="orderline.get_discount() > 0">
                            <div style="font-size: 12px;font-style: italic;color: #808080;">
                                <t t-esc="orderline.get_discount()"/>% discount
                            </div>
                        </t>
                        </div>
                    </td>
                    <td style="text-align:right;">
                        <div>
                        <t t-esc="orderline.get_quantity_str_with_unit()"/>
                        </div>
                    </td>
                    <td style="text-align:right;">
                        <div>
                        <t t-esc="widget.pos.format_currency(orderline.get_display_price())"/>
                        </div>
                    </td>
                </tr>
            </table>
            <br />
            <table style="width: 100%;">
                <tr>
                    <td>Subtotal:</td>
                    <td class="pos-receipt-right-align">
                        <t t-esc="widget.pos.format_currency(order.get_total_without_tax())"/>
                    </td>
                </tr>
                <t t-foreach="order.get_tax_details()" t-as="taxdetail">
                    <tr>
                        <td><t t-esc="taxdetail.name" /></td>
                        <td class="pos-receipt-right-align">
                            <t t-esc="widget.pos.format_currency(taxdetail.amount)" />
                        </td>
                    </tr>
                </t>
                <tr>
                    <t t-if="order.get_total_discount() > 0">
                        <td>Discount:</td>
                        <td class="pos-receipt-right-align">
                            <t t-esc="widget.pos.format_currency(order.get_total_discount())"/>
                        </td>
                    </t>
                </tr>
                <tr style="font-size: 20px;margin: 5px;">
                    <td>Total:</td>
                    <td class="pos-receipt-right-align">
                        <t t-esc="widget.pos.format_currency(order.get_total_with_tax())"/>
                    </td>
                </tr>
            </table>
            <br />
            <table style="width: 100%;">
                <t t-foreach="paymentlines" t-as="line">
                    <tr>
                        <td>
                            <t t-esc="line.name"/>
                        </td>
                        <td class="pos-receipt-right-align">
                            <t t-esc="widget.pos.format_currency(line.get_amount())"/>
                        </td>
                    </tr>
                </t>
            </table>
            <br />
            <table style="width: 100%;">
                <tr><td>Change:</td><td class="pos-receipt-right-align">
                    <t t-esc="widget.pos.format_currency(order.get_change())"/>
                    </td></tr>
            </table>
            <t t-if="receipt.footer">
                <br />
                <div style='text-align:center'>
                    <t t-esc="receipt.footer" />
                </div>
            </t>
        </div>"""
        self.create(record_data)

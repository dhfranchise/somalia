from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    orion_item_no = fields.Char(string="Orion Item No")
    no = fields.Char(string="No")
    budget_category_id = fields.Many2one("bi.budget.category", string="Budget Category code")
    division_code_id = fields.Many2one("bi.division.code", string="Division code")
    group_code_id = fields.Many2one("bi.group.code", string="Group Code")
    sub_group_code_id = fields.Many2one("bi.sub.group.code", string="Sub Group Code")
    sub_category_one_code = fields.Many2one("bi.sub.category.one.code", string="Sub Category 1 Code")
    sub_category_two_code = fields.Many2one("bi.sub.category.two.code", string="Sub Category 2 Code")
    sub_category_three_code = fields.Many2one("bi.sub.category.three.code", string="Sub Category 3 Code")
    brand_code_id = fields.Many2one("bi.brand.code", string="Brand Code")
    sub_sub_code_id = fields.Many2one("bi.sub.sub.group.code", string="Sub Sub Group Code")
    warranty_date = fields.Char(string="Warranty Date")
    acp_category_code = fields.Char(string="ACP Category Code")
    obc = fields.Char(string="OBC")
    item_classification = fields.Char(string="Item Classification")
    no_of_boxes_cartons = fields.Char(string="No of Boxes /Cartons")
    item_status = fields.Selection(
        [("import", "Import"), ("local", "Local"), ("mix", "Mix")], string="Item Status", default="import"
    )
    status_type = fields.Selection([("general", "General")], string="Status Type", default="general")
    blind_curtain_type = fields.Char(string="Blind Curtain Type")
    model_no = fields.Char(string="Name / Model No.")
    shape_finish = fields.Char(string="Shape/Finish")
    size_code_id = fields.Many2one("bi.size.code", string="Size Code")
    color_code_id = fields.Many2one("bi.color.code", string="Color Code")
    material = fields.Char(string="Material")
    width_of_fabric = fields.Float(string="Width Of Fabric(mts)")
    height_of_fabric = fields.Float(string="height Of Fabric(mts)")
    blind_addition = fields.Float(string="Blind Default Addition")
    valance_pelmet_style = fields.Char(string="Valance/Pelmet Style")
    estimated_panel_default = fields.Float(string="Estimated No.of Panel Default")
    cbm = fields.Char(string="CBM")
    fixing_time = fields.Char(string="Fixing Time")
    po_number = fields.Char(string="Po Number")

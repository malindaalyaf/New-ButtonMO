from odoo import models


class Sales_MO(models.Model):
    _inherit = 'sale.order'

    def mo_button(self):
        for record in self.order_line:
            for k in record.product_id.bom_ids:
                bom = record.env['mrp.bom'].search([('id', '=', k.id)]).read()
                if bool(bom) == True:
                    record.env['mrp.production'].create(
                        {'product_id': record.product_id.id, 
                        'product_uom_id': record.product_id.bom_ids.product_uom_id.id, 
                        'bom_id': k.id, 
                        'product_qty': record.product_uom_qty})
               
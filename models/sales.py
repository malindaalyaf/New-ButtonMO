from odoo import models


class Sales_MO(models.Model):
    _inherit = 'sale.order'

    def mo_button(self):
        mo = []
        mo_auto_target = self.env['mrp.bom'].search(self.product_id.id)
        
        if self.order_line.product_id.bom_ids.harga_bom > 0:
            self.env['mrp.production'].create(
                {'product_id': self.order_line.product_id.id, 
                "product_uom_id": self.order_line.product_uom_id.id, 
                "bom_id": self.order_line.product_id.bom_ids.id, 
                "product_qty": self.order_line.product_uom_qty})
        else:
            pass
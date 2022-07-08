from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
import base64
from datetime import date,datetime
import csv
import json
from odoo.tools.safe_eval import safe_eval

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        self.action_done()
        return res

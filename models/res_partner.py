# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def write(self, vals):
        raise Exception('Save exception')
        res = super(Partner, self).write(vals)

        return res
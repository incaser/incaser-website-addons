# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models


class SlideCategory(models.Model):
    _inherit = 'slide.category'

    notice_level = fields.Selection([
        ('alert-success', 'Success'),
        ('alert-info', 'Info'),
        ('alert-warning', 'Warning'),
        ('alert-danger', 'Danger'),
    ], default='alert-info', string='Level Notice')
    notice = fields.Html(string='Notice', translate=True)

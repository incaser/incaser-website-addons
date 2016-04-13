# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import api, fields, models, SUPERUSER_ID, _


class SlideCategory(models.Model):
    _inherit = 'slide.category'

    notice = fields.Html(string='Notice', translate=True)

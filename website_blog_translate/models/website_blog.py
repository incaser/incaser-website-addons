# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import fields, models


class BlogPost(models.Model):
    _inherit = 'blog.blog'

    name = fields.Char(translate=True)
    subtitle = fields.Char(translate=True)

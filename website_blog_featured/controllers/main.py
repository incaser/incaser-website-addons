# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp import tools
from openerp.addons.web import http
from openerp.addons.web.http import request

from openerp.addons.website_blog.controllers.main import WebsiteBlog


class WebsiteBlogFeatured(WebsiteBlog):
    _blog_post_per_page = 6

# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from openerp.addons.website_slides.controllers.main import WebsiteSlides


class NoticeWebsiteSlides(WebsiteSlides):

    def _get_slide_detail(self, slide):
        res = super(NoticeWebsiteSlides, self)._get_slide_detail(slide)
        if slide.category_id.notice:
            res.update({'notice': slide.category_id.notice})
        return res

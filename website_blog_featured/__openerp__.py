# -*- coding: utf-8 -*-
# (c) 2015 Incaser Informatica S.L. - Sergio Teruel
# (c) 2015 Incaser Informatica S.L. - Carlos Dauden
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Website Blog Featured',
    'summary': 'Show blog post with featured view',
    'version': '8.0.1.0.0',
    'category': 'website',
    'author': 'Incaser Informatica S.L., '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'website_blog',
    ],
    'data': [
        'views/website_blog_view.xml',
        'views/website_blog_templates.xml',
    ],
    'images': [],
    'installable': True,
}

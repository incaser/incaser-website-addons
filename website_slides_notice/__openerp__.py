# -*- coding: utf-8 -*-
# © 2016 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Website Slides Notice',
    'summary': 'Show notices in channels and slides',
    'version': '8.0.1.0.0',
    'category': 'website',
    'author': 'Tecnativa, '
              'Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'depends': [
        'website_slides',
    ],
    'data': [
        'views/website_slides.xml',
        'views/website_slides_backend.xml',
    ],
    'images': [],
    'installable': True,
}

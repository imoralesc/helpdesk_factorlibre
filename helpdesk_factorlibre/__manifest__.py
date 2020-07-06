# -*- coding: utf-8 -*-
# © 2020 Nacho Morales(Camptocamp SA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Helpdesk Factor Libre',
    'summary': "Helpdesk curso odoo factor libre",
    'version': '11.0.1.0.1',
    'author': "Nacho Morales",
    'license': "AGPL-3",
    'maintainer': 'Camptocamp, Acsone',
    'category': 'HelpDesk',
    'website': 'https://odoo-community.org/',
    'depends': ['mail'],
    'data' :[
        'views/helpdesk_ticket_views.xml',
        'views/helpdesk_ticket_tag_views.xml',
        'views/inherit_res_partners_views.xml',
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv'  ],
    'installable': True,
}
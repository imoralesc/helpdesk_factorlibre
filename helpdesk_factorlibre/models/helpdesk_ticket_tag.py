 # -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, _

class HelpdeskTicketTag(models.Model):
    _name = 'helpdesk.ticket.tag'
    
    
    name = fields.Char(
        string='Tittle',
    )
    
    description = fields.Text(
        string='Description',
    )
    
    color = fields.Integer(string='Color Index')
    
    active = fields.Boolean(default=True)
    
    
    
    
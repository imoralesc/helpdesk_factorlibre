 # -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import api, fields, models


class HelpdeskTeam(models.Model):

    _name = 'helpdesk.ticket.team'
    _description = 'Helpdesk Ticket Team'

    name = fields.Char(
        string='Name',
    )
    
    team_id = fields.Integer(
        string='Team Id'
    )
    
    color = fields.Integer("Color Index", default=0)
    
    user_ids = fields.Many2many(comodel_name='res.users', string='Members')
    
    active = fields.Boolean(default=True)
    
    
    
    
        
    
    
    
    
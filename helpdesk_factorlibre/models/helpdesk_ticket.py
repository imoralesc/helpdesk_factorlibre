 # -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, _, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    """Aqui se meten los metodos Default que vaya a utilizar, antes de los campos de la clase"""
    
    numero_ticket = fields.Integer(
        string='Numero de ticket',
        required=True,
    )
    
    name = fields.Char(
        string='Tittle',
        required=True,
    )
    
    description = fields.Html(
        string='Description',
    )
    
    fecha_asignada = fields.Datetime(
        string='Assigned Date',
        compute='_compute_fecha_asignada',
        store=True,
    )
    
    fecha_cierre = fields.Datetime(string='Closed Date')
    
    prioridad = fields.Selection(selection=[
        ('0', _('Baja')),
        ('1', _('Media')),
        ('2', _('Alta')),
        ], 
        string='Priority',
        default='1',
    )
    
    customer_name = fields.Char(
        string='Customemer name'
    )
    
    customer_email = fields.Char(
        string='Customemer email'
    )
    
    user_id = fields.Many2one(
        string='Assigned to',
        comodel_name='res.users',
        ondelete='restrict', 
    )
    
    partner_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
        ondelete='restrict',
    )
    
    
    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='helpdesk.ticket.tag',
    )
    
    @api.multi
    def assign_to_me(self):
        self.write({
            'user_id': self.env.user.id
        })
        
    @api.onchange('partner_id')
    def onchange_partner_id(self):
        for record in self:
            partner = record.partner_id
            record.update({
                'customer_name' : partner.name,
                'customer_email' : partner.email,
            })
                
    
    @api.depends('user_id')
    def _compute_fecha_asignada(self):
        self.fecha_asignada = fields.Datetime.now()
        
    
    
    
    
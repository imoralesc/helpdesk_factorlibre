 # -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, _, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    """Aqui se meten los metodos Default que vaya a utilizar, antes de los campos de la clase"""
    
    def _get_default_priority(self):
        return "1"
    
    def _get_default_stage_id(self):
        return self.env['helpdesk.ticket.stage'].search([], limit=1).id
    
    ticket_number = fields.Integer(
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
    
    assigned_date = fields.Datetime(
        string='Assigned Date',
        compute='_compute_assigned_date',
        store=True,
    )
    
    closed_date = fields.Datetime(string='Closed Date')
    
    priority = fields.Selection(selection=[
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
    
    user_ids = fields.Many2many(
        comodel_name='res.users',
        related='team_id.user_ids',
        string='Users')
    
    partner_id = fields.Many2one(
        string='Customer',
        comodel_name='res.partner',
        ondelete='restrict',
    )
    
    
    tag_ids = fields.Many2many(
        string='Tags',
        comodel_name='helpdesk.ticket.tag',
    )
    
    stage_id = fields.Many2one(
        'helpdesk.ticket.stage',
        string='Stage',
        group_expand='_read_group_stage_ids',
        default=_get_default_stage_id,
        track_visibility='onchange',
    )
    
    color = fields.Integer(
        string='Color Index'
    )
    
    kanban_state = fields.Selection([
        ('normal', 'Default'),
        ('done', 'Ready for next stage'),
        ('blocked', 'Blocked')], 
        string='Kanban State'
    )
    
    team_id = fields.Many2one(
        'helpdesk.ticket.team'
    )
    
    closed = fields.Boolean(
        related='stage_id.closed'
    )
    
    unattended = fields.Boolean(
        related='stage_id.unattended'
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
    def _compute_assigned_date(self):
        self.assigned_date = fields.Datetime.now()
        
    @api.model
    def create(self,vals):
        if vals.get("partner_id") and ("partner_name" not in vals or "partner_mail" not in vals):
            partner = self.env["res.partner"].browse(vals["partner_id"])
            vals.setdefault("customer_name", partner.name)
            vals.setdefault("customer_email", partner.email)
            
        res = super().create(vals)
        return res
    
    @api.multi
    @api.onchange('team_id', 'user_id')
    def _onchange_dominion_user_id(self):
        if self.user_id:
            if self.user_id and self.user_ids and \
                    self.user_id not in self.user_ids:
                self.update({
                    'user_id': False
                })
                return {'domain': {'user_id': []}}
        if self.team_id:
            return {'domain': {'user_id': [('id', 'in', self.user_ids.ids)]}}
        else:
            return {'domain': {'user_id': []}}
        
    
    
        
    
    
    
    
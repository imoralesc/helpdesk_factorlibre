 # -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import models, fields, _, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    
    helpdesk_ticket_ids = fields.One2many(
        string='Tickets',
        comodel_name='helpdesk.ticket',
        inverse_name='partner_id',
    )
    
    count_tickets = fields.Integer(
        string='Number of tickets',
        compute='_compute_count_tickets'
    )
    
    @api.multi
    def _compute_count_tickets(self):
        for record in self:
            #Codigo mas eficiente: record.count_tickets = len(record.helpdesk_ticket_ids)
            tickets = self.env['helpdesk.ticket'].search([
                ('partner_id', '=', record.id)
                ])
            record.count_tickets = len(tickets)
            
    @api.model
    def create(self, vals):
        if vals.get("partner_id") and (
            "customer_name" not in vals or "customer_email" not in vals
        ):
            partner = self.env["res.partner"].browse(vals["partner_id"])
            vals.setdefault("customer_name", partner.name)
            vals.setdefault("customer_email", partner.email)
        
        res = super().create(vals)
        return res
    
    
    
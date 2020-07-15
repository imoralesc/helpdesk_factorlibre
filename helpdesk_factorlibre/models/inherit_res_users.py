# -*- coding: utf-8 -*-
# © 2020 Nacho Morales
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    helpdesk_ticket_ids = fields.One2many(
        string='Tickets',
        comodel_name='helpdesk.ticket',
        inverse_name='user_id'
    )

    team_ids = fields.Many2many(
        string='Team',
        comodel_name='helpdesk.ticket.team',
    )

    count_open_tickets = fields.Integer(
        string='Number of tickets',
        compute='_compute_count_tickets'
    )

    def _compute_count_tickets(self):
        for record in self:
            tickets = self.env['helpdesk.ticket'].search(
                [('user_id', '=', record.id)])
            record.count_open_tickets = len(
                tickets.filtered(lambda ticket: ticket.stage_id.closed == False))
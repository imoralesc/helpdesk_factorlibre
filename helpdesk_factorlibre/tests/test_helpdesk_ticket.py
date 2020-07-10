from odoo.tests import common

class TestHelpdeskTicket(common.SavepointCase):
    
    @classmethod
    def setUpClass(cls):
        super(TestHelpdeskTicket, cls).setUpClass()
        
        helpdesk_ticket = cls.env['helpdesk.ticket']
        user_admin = cls.env.ref('base.admin')
        user_demo = cls.env.ref('base.admin')

        tickets = cls.env['res.users']
        cls.ticket_test = tickets.create({
            'name': 'Test 1',
            'description': 'Ticket test',
        })


    def test_helpdesk_ticket_number(self):
        self.assertNotEquals(self.ticket.number, '/',
                             'Helpdesk Ticket: A ticket should have '
                             'a number.')

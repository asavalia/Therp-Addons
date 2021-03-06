# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import SUPERUSER_ID, api


def post_init_hook(cr, pool):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['ir.cron'].with_context(active_test=False).search([]).write({
        'email_template_id':
        env.ref('scheduler_error_mailer.scheduler_error_mailer').id,
    })

# -*- coding: utf-8 -*-
# A prdouct of DX-8, module resricted as per the license.

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    enable_idle = fields.Boolean(string="Enable Idle Time", default=True,
                                 help="Check if the user is enable with idle timer auto logout ")
    idle_time = fields.Integer(string="Idle Time (Minutes)", default=120,
                               help="User's idle time in minutes")

    _sql_constraints = [
        ('check_idle_time', 'CHECK(idle_time >= 1)',
         'Idle Time must be a positive number.'),
    ]

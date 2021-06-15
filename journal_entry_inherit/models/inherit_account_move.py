# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class AccountMoveChatter(models.Model):
    _inherit = 'account.move'
    name = fields.Char(tracking=True)


class AccountMoveChatterAdd(models.Model):
    _name = 'account.move'
    _inherit = ['account.move', 'mail.thread', 'mail.activity.mixin']
# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class AccountTaxChatter(models.Model):
    _inherit = 'account.tax'
    hire_date = fields.Date(string='Hire Date', readonly=False, tracking=True)
    name = fields.Char(tracking=True)

class AccountTaxChatterAdd(models.Model):
    _name = 'account.tax'
    _inherit = ['account.tax', 'mail.thread', 'mail.activity.mixin']
#   _inherit = ['mail.thread', 'mail.activity.mixin']


# class EmployeeInherit(models.Model):
#     _inherit = 'hr.employee'
#     permission_responsible = fields.Many2one('hr.employee', string='Permission Responsible')
#     hire_date = fields.Date(string='Hire Date', readonly=False, tracking=True)

# class AccountTaxChatter(models.Model):
#    _name = 'account.tax'
#    _inherit = ['account.tax', 'mail.thread']

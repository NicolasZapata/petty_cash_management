from odoo import _, api, fields, models
from odoo.exceptions import ValidationError, UserError


class PettyCashManagement(models.Model):
      _name = 'petty.cash.management'
      _description = 'PettyCash'
      
      name=fields.Char(string='Petty Cash Management')
      responsable_id = fields.Many2one('hr.employee', string='responsable')
      cash_amount = fields.Float(string='cash_amount')
      cash_notes = fields.Html(string='cash_notes')
      date_closed = fields.Date(string='date_closed')
      date_opened = fields.Date(string='date opened')
      refund_account_id = fields.Many2one('account.account', string='refund_account')
      expense_ids = fields.One2many('hr.expense','petty_cash_management_id', string='Expenses')
      expense_to_report = fields.Float(string='Expense to Report', compute='_compute_expense_to_report', readonly='True', store='True')
      validation_expenses = fields.Float(string='Validation Expenses')
      expenses_to_reimburse = fields.Float(string='Expenses to reimburse')
      cash_on_hand = fields.Float(string='Cash on hand')
      total = fields.Float(string='total', compute="total_cash_amount", store=True)

      @api.depends('validation_expenses', 'expenses_to_reimburse')
      def _compute_expense_to_report(self):
            for record in self:
                  draft_expenses = (record.expense_ids.filtered(lambda expense: expense.state == 'draft'))
                  record.expense_to_report = sum(draft_expenses.mapped('total_amount'))

      @api.depends('expense_to_report', 'validation_expenses')
      def total_cash_amount(self):
            self.total = self.expense_to_report + self.validation_expenses
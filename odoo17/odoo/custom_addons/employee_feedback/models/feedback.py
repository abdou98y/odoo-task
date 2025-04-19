from odoo import models, fields,api
from odoo.exceptions import ValidationError


class Feedback(models.Model):
    _name = 'feedback'
    _description = 'Employee Feedback'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True,default = lambda self: self._default_employee_id())
    feedback = fields.Text(string='Feedback Text',required=True)
    date_submitted = fields.Date(string='Feedback Date', default=fields.Date.today)
    status = fields.Selection([
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('action_taken', 'Action Taken')
    ], string='Status', default='pending')
    
    
    def _default_employee_id(self):
        # Get the current user's employee ID
        user = self.env.user
        employee = self.env['hr.employee'].search([('user_id', '=', user.id)], limit=1)
        return employee.id if employee else False

    @api.constrains('feedback')
    def _check_feedback_not_empty(self):
        for record in self:
            if not record.feedback or record.feedback.isspace():
                raise ValidationError("Feedback cannot be empty or just whitespace!")

    
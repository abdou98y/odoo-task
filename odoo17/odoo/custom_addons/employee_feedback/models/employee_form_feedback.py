from  odoo import models, fields



class Employee(models.Model):
    _inherit = 'hr.employee'

    feedback_ids = fields.One2many('feedback', 'employee_id', string='Feedbacks')
    user_id = fields.Many2one('res.users', string='Related User')
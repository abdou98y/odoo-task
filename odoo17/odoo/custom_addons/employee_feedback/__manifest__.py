{
    'name': 'Employee Feedback',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Module to manage employee feedback and performance reviews',
    'depends': [
        'base',
        'hr',
        
        ],
    'data': [
        'security/ir.model.access.csv',
        'security/feedback_security.xml',
        'views/base_menu.xml',
        'views/feedback_view.xml',
        'views/employee_form_feedback.xml',
        ],
    'application': True,
}
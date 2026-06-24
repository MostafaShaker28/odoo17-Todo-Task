from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(required=True)
    assign_to = fields.Many2one('res.users', string='Assign To')
    description = fields.Text()
    due_date = fields.Date()
    status = fields.Selection([
    ('new', 'New'),
    ('in_progress','In Progress'),
    ('completed', 'Completed')
    ],
    default = 'new')


    def action_new(self):
        for rec in self:
            print("inside new action")
            rec.status = 'new'

    def action_in_progress(self):
        for rec in self:
            print("inside In Progress action")
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            print('inside completed action')
            rec.status = 'completed'
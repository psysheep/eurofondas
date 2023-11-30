from odoo import fields, models


class CreateReportWizard(models.TransientModel):
    _name = 'create.library_report.wizard'
    _description = 'Create library report by date'

    start = fields.Date(string='From:', required=True)
    finish = fields.Date(string='To:', required=True)

    def action_generate_report(self):
        start_date = self.start
        end_date = self.finish
        library_tools = self.env['library.tool'].search([
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date),
        ])
        tool_ids = library_tools.ids
        return {
            'name': 'Library Report',
            'type': 'ir.actions.act_window',
            'res_model': 'library.tool',
            'view_mode': 'tree,form',
            'view_id': False,
            'target': 'current',
            'domain': [('id', 'in', tool_ids)],
        }

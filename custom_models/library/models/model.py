from odoo import models, fields


class LibraryModel(models.Model):
    _name = 'library.tool'
    _description = 'Library management tool'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', required=True)


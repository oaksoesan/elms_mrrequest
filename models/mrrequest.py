from openerp import fields, models, api
from openerp.exceptions import ValidationError
from datetime import datetime, timedelta, date
import time
from openerp.tools.translate import _

class MRrequest(models.Model):
    _name = 'mrrequest'
    _description = 'MR request model'

    name = fields.Char('Name')
    mrdate = fields.Date('Date')
    department = fields.Many2one("hr.department",string="Department",store=True)
    location_id = fields.Many2one('stock.location',string="Location")
    prob = fields.Char('Problem Detail')
    priority = fields.Selection([('0','High'),('1','Medium'),('2','Low')],track_visibility='onchange')
    action_plan = fields.Char('Action Plan For the Problem')
    to_assign = fields.Selection([('0','Own Staff'),('1','Outside Contractor')],track_visibility='onchange')
    Estimate_cost = fields.Char('Estimate Cost')
    Estimate_time = fields.Char('Estimate Time')
    
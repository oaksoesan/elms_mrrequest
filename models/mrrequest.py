from openerp import fields, models, api
from datetime import datetime

class MrRequest(models.Model):
    _name = 'mrrequest'
    _inherit = ['mail.thread']
    _description = 'MR request model'

    # Left Panel (User)
    name = fields.Char('Name', compute='_compute_name')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('cancel', 'Canceled'),
        ('requested', 'Requested'),
        ('assigned', 'Assigned'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
    ], string='State', default="draft", track_visibility='onchange')
    res_user_id = fields.Many2one('res.users', required=True,
                                     string='Requested By', track_visibility='onchange')
    department = fields.Many2one('hr.department', string="Department",
                                 store=True, track_visibility='onchange')
    priority = fields.Selection(
        [
            ('0', 'Very Low'),
            ('1', 'Low'),
            ('2', 'Normal'),
            ('3', 'High'),
            ('4', 'Serious'),
            ('5', 'Urgent'),
        ],
        'Priority', track_visibility='onchange')
    date_time = fields.Datetime(string='Request Date & Time', required=True, track_visibility='onchange')
    mr_location_id = fields.Many2one('mrrequest.location', string='Location', track_visibility='onchange')
    job_section = fields.Selection([
        ('electrical', 'Electrical'),
        ('plumbing', 'Plumbing'),
        ('acmv', 'ACMV'),
        ('civil', 'Civil'),
        ('general', 'General'),
    ], track_visibility='onchange', string='Job Section')
    problem_detail = fields.Text('Problem Detail', track_visibility='onchange')

    # Right Panel (MR Admin)
    hr_employee_id = fields.Many2one('hr.employee', string='Assign To',
                                     track_visibility='onchange')
    estimate_cost = fields.Char('Estimated Cost', track_visibility='onchange')
    estimate_start_time = fields.Datetime(string='Estimate Start At', track_visibility='onchange')
    estimate_end_time = fields.Datetime(string='Estimate End At', track_visibility='onchange')
    actual_start_time = fields.Datetime(string='Actual Start At', track_visibility='onchange')
    actual_end_time = fields.Datetime(string='Actual End At', track_visibility='onchange')
    job_status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], track_visibility='onchange', string='Job Status')
    maintenance_detail = fields.Text('Maintenance Detail', track_visibility='onchange')

    # Receiving Panel
    received_status = fields.Selection([
        ('satisfied', 'Satisfied'),
        ('unsatisfied', 'Unsatisfied')
    ],
        string='Received Status', track_visibility='onchange')
    received_date_time = fields.Datetime(string='Received At', track_visibility='onchange')
    received_note = fields.Text('Received Note', track_visibility='onchange')
    approver_comment = fields.Text('Approver Comment', track_visibility='onchange')

    @api.multi
    def to_draft(self):
        self.state = 'draft'

    @api.multi
    def to_cancel(self):
        self.state = 'cancel'

    @api.multi
    def to_assign(self):
        self.state = 'assigned'

    @api.multi
    def to_approve(self):
        self.state = 'approved'

    @api.multi
    def to_complete(self):
        self.state = 'completed'

    @api.multi
    def to_draft(self):
        self.state = 'draft'

    @api.multi
    def to_request(self):
        self.state = 'requested'

    @api.depends('date_time')
    def _compute_name(self):
        for record in self:
            join_datetime = datetime.strptime(record.date_time,
                                              '%Y-%m-%d %H:%M:%S')
            record.name = "MR/{}/{:02d}{:02d}{:02d}".format(
                join_datetime.strftime('%Y%m%d'), join_datetime.hour,
                join_datetime.minute, join_datetime.second)


class MrLocation(models.Model):
    _name = 'mrrequest.location'
    _description = 'Locations for MR requests'
    name = fields.Char(string='Location Name')

#TODO: Change admin info to maintenanace information
#TODO: Wider feedback session
#TODO: Track visibility
#TODO: Request Users to users
#TODO: Security Group

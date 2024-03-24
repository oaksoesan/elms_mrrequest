from openerp import fields, models, api

class MrRequest(models.Model):
    _name = 'mrrequest'
    _description = 'MR request model'

    # Left Panel (User)
    name = fields.Char('Name')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('requested', 'Requested'),
        ('assigned', 'Assigned'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
    ])
    res_partner_id = fields.Many2one('res.partner', required=True,
                                     string='Requested By')
    department = fields.Many2one('hr.department', string="Department",
                                 store=True)
    priority = fields.Selection(
        [
            ('0', 'Very Low'),
            ('1', 'Low'),
            ('2', 'Normal'),
            ('3', 'High'),
            ('4', 'Serious'),
            ('5', 'Urgent'),
        ],
        'Priority')
    date_time = fields.Datetime(string='Request Date & Time', required=True)
    mr_location_id = fields.Many2one('mrrequest.location', string='Location')
    job_section = fields.Selection([
        ('electrical', 'Electrical'),
        ('plumbing', 'Plumbing'),
        ('acmv', 'ACMV'),
        ('civil', 'Civil'),
        ('general', 'General'),
    ])
    problem_detail = fields.Text('Problem Detail')

    # Right Panel (MR Admin)
    hr_employee_id = fields.Many2one('hr.employee', string='Assign To',
                                     track_visibility='onchange')
    estimate_cost = fields.Char('Estimated Cost')
    estimate_start_time = fields.Datetime(string='Estimate Start at')
    estimate_end_time = fields.Datetime(string='Estimate End at')
    actual_start_time = fields.Datetime(string='Actual Start at')
    actual_end_time = fields.Datetime(string='Actual End at')
    job_status = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ])
    maintenance_detail = fields.Text('Maintenance Detail')

    # Receiving Panel
    received_status = fields.Selection([
        ('satisfied', 'Satisfied'),
        ('unsatisfied', 'Unsatisfied')
    ],
        string='Received Status')
    received_date_time = fields.Datetime(string='Received At')
    received_note = fields.Text('Received Note')
    approver_comment = fields.Text('Approver Comment')


class MrLocation(models.Model):
    _name = 'mrrequest.location'
    _description = 'Locations for MR requests'
    name = fields.Char(string='Location Name')

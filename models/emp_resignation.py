# -*- coding:utf-8 -*-

from flectra import api, fields, models, SUPERUSER_ID, _
from flectra.exceptions import UserError, AccessError, ValidationError

class HrResignation(models.Model):
  
    _inherit = 'hr.resignation'

    @api.model
    def create(self, vals):

        
        employee =vals['employee_id']
        

        employee = self.env['hr.employee'].search([('id','=',employee)])

        
        Error = False
        
        for rec in employee.hr_details:
            if rec.sorted_id == False:
                 Error  = True
            

        if  Error == True:
            raise ValidationError(_("You cannot Resign from the company due to the Legal Issues."))
    
        result = super(HrResignation, self).create(vals)
        return result
# -*- coding: utf-8 -*-

from flectra import models,fields,api, _

class EmployeeTable(models.Model):
    _name ='hr.employee.line'
    
    issue= fields.Char(string='Issue')
    status= fields.Char(string='Status')
    date = fields.Date(string="Date")
    sorted_id = fields.Boolean('Sorted')
    emp_id = fields.Many2one('hr.employee', string='Employee')

class HREmployee(models.Model):
    
    _inherit ='hr.employee'
    _description = 'Legal Issues'
    hr_details = fields.One2many('hr.employee.line','emp_id' ,string='Legal Issues')
    
 

    
    
    
                          
    

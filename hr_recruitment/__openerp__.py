# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Recruitment Process',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 24,
    'summary': 'Jobs, Recruitment, Applications, Job Interviews',
    'description': """
Manage job positions and the recruitment process
=================================================
This application allows you to easily keep track of jobs, vacancies, applications, interviews etc.

It is integrated with the mail gateway to automatically fetch email sent to <jobs@yourcompany.com> in list of applications. It's also integrated with the document management system to store and search in CV base and find required candidate. It is also integrated with the survey module to allow you to define interview for different jobs.
You can define different phases of interview and easily rate applicant from kanban view.
    """,
    'author': 'OpenERP SA',
    'website': 'http://www.openerp.com',
    'images': ['images/hr_recruitment_analysis.jpeg','images/hr_recruitment_applicants.jpeg'],
    'depends': [
        'base_status',
        'decimal_precision',
        'hr',
        'survey',
        'base_calendar',
        'fetchmail',
    ],
    'data': [
        'wizard/hr_recruitment_employee_hired.xml',
        'wizard/hr_recruitment_create_partner_job_view.xml',
        'hr_recruitment_view.xml',
        'hr_recruitment_menu.xml',
        'security/hr_recruitment_security.xml',
        'security/ir.model.access.csv',
        'report/hr_recruitment_report_view.xml',
        'board_hr_recruitment_statistical_view.xml',
        'hr_recruitment_installer_view.xml',
        'res_config_view.xml',
        'hr_recruitment_data.xml'
    ],
    'demo': ['hr_recruitment_demo.yml'],
    'js': ['static/src/js/hr_recruitment.js'],
    'test': ['test/recruitment_process.yml'],
    'installable': True,
    'auto_install': False,
    'certificate': '001073437025460275621',
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

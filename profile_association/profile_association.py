# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

from osv import fields, osv
import pooler


class profile_association_config_install_modules_wizard(osv.osv_memory):
    _name='profile.association.config.install_modules_wizard'
    _inherit = 'res.config.installer'

    _columns = {
        'hr_expense':fields.boolean('Expenses Tracking', help="Tracks the personal expenses process, from the employee expense encoding, to the reimbursement of the employee up to the reinvoicing to the final customer."),
        'project':fields.boolean('Project Management'),
        'board_document':fields.boolean('Document Management', help= "The Document Management System of Open ERP allows you to store, browse, automatically index, search and preview all kind of documents (internal documents, printed reports, calendar system). It opens an FTP access for the users to easily browse association's document."),
        'segmentation':fields.boolean('Segmentation'),
        'crm_configuration' : fields.boolean('Partner Relation & Calendars'),
        'project_gtd':fields.boolean('Getting Things Done',
            help="GTD is a methodology to efficiently organise yourself and your tasks. This module fully integrates GTD principle with OpenERP's project management."),
        'wiki': fields.boolean('Wiki', 
            help="An integrated wiki content management system. This is really usefull to manage FAQ, quality manuals, etc.")
    }
profile_association_config_install_modules_wizard()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

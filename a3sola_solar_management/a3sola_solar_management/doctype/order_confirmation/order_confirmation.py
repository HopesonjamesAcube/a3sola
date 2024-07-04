# Copyright (c) 2024, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OrderConfirmation(Document):
	pass

@frappe.whitelist(allow_guest=True)
def get_project(pro):
    project = frappe.get_doc('Project', pro)
    d = {'email': "", 'phone': ""}

    if project.email:
        d['email'] = project.email

    if project.contact_list:
        for i in project.contact_list:
            if i.is_primary == 1 and i.contact_number:
                d['phone'] = i.contact_number
                break
            elif i.contact_number:
                d['phone'] = i.contact_number

    return d

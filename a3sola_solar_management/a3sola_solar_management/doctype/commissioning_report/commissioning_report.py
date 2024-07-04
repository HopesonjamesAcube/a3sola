# Copyright (c) 2024, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CommissioningReport(Document):
	pass


@frappe.whitelist(allow_guest=True)
def test(doc, pro):
    project = frappe.get_doc('Project', pro)
    if project.address:
        d = {'cadd': project.address}
    else:
        d = {'cadd': ""}
    return d
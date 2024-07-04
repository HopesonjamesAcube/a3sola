# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MNREAgreement(Document):
	pass



@frappe.whitelist(allow_guest=True)
def test(doc,pro):

	project = frappe.get_doc('Project',pro)

	print(project.address)
	print(project.customer)


	d={'cadd':project.address,'opp':project.oppertunity,'consno':project.consumer_number}
	
	# ebexist=frappe.db.exists("EB Information",{"project_id":pro})
	# siteexist=frappe.db.exists("Site Information",{"project_id":pro})
	# # if not ebexist and not siteexist:
	# # 	frappe.throw("Please Complete EB information and Site Information")
	# # if not ebexist:
	# # 	frappe.throw("Please Complete EB information")
	# # if not siteexist:
	# # 	frappe.throw("Please Complete Site information")

	# if  ebexist and  siteexist:
	# 	eb=frappe.get_doc("EB Information",{"project_id":pro})
	# 	site=frappe.get_doc("Site Information",{"project_id":pro})
	# 	print(eb.customer)
	# 	if eb:
	# 		if eb.customer:
	# 			d['cu']=eb.customer
	# 		else:
	# 			d['cu']=""
	# 		if eb.consumer_number:
	# 			d['consu']=eb.consumer_number
	# 		else:
	# 			d['consu']=""

	# 	print(d)
	return d

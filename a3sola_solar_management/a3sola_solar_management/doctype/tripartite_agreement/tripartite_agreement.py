# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class TripartiteAgreement(Document):
	pass




@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)
		price=0
		discount=0
		rate=0
		
		print(project.primary_address)
		print(project.customer)
		if frappe.db.exists("Quotation",{"project_id":pro}):
			quotation=frappe.get_doc("Quotation",{"project_id":pro})

			for row in quotation.items:

				if frappe.db.exists("Product Bundle",row.item_code):
					price=row.price_list_rate
					discount=row.discount_amount
					rate=row.rate
		# else:
		# 	frappe.throw("No Quotation Created For this Project")


		d={'cadd':project.primary_address,'customer':project.customer,'opp':project.oppertunity,'consno':project.consumer_number,'price':price,"discount_amount":discount,"rate":rate,"item":project.item_name,"capacity":project.panel_capacity}
		if frappe.db.exists("Site Survey",{"project_id":pro}):
			site=frappe.get_doc("Site Survey",{"project_id":pro})
			if site.name_of_electrical_station:
				d['sta']=site.name_of_electrical_station
			else:

				d['sta']=""
		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

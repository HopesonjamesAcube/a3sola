# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class JointInspectionReport(Document):
	def validate(doc):
		project = frappe.get_doc('Project',doc.project_id)
		if project.panel_capacity:
			doc.solar_pv_capacity=project.panel_capacity
		if project.inverter_capacity:
			doc.inverter_capacity=project.inverter_capacity



@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.consumer_number)
		if frappe.db.exists("Quotation",{"project_id":pro}):
			quotation=frappe.get_doc("Quotation",{"project_id":pro})

			price=0
			discount=0
			rate=0

			for row in quotation.items:

				price=price+row.price_list_rate
				discount=discount+row.discount_amount
				rate=rate+row.rate
			rate=quotation.rounded_total
		else:
			price=0
			discount=0
			rate=0



		d={'cadd':project.primary_address,'customer':project.customer,'opp':project.oppertunity,'consno':project.consumer_number,'price':price,"discount_amount":discount,"rate":rate,"item":project.item_name}

		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

		# d={'cadd':project.primary_address,'customer':project.customer,'consno':project.consumer_number}


		# print(d)
		# return d

# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ANERTAGREEMENT(Document):
	def validate(doc):
		if doc.project_id:
			project = frappe.get_doc('Project',doc.project_id)
			project.work_order_number=doc.work_order_no
			project.save()


@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.customer)
		

		

		price=0
		discount=0
		amount=0
		if frappe.db.exists("Quotation",{"project_id":pro}):
			quotation=frappe.get_doc("Quotation",{"project_id":pro})
			

			for row in quotation.items:
				

				price=price+row.price_list_rate
				if row.discount_amount:
					discount=discount+row.discount_amount
				amount=amount+row.amount
		# else:
		# 	frappe.throw("No Quotation Created For this Project")

	

		d={'cadd':project.primary_address,'customer':project.customer,'price':price,"discount_amount":discount,"amount":amount,"item":project.item_name}
		

		print(d)
		return d

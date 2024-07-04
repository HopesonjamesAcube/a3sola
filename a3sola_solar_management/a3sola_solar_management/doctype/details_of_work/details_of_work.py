import frappe
from frappe.model.document import Document

class DetailsofWork(Document):
	def validate(doc):
		completion_report=frappe.db.exists("Completion Report",{"project_id":doc.project_id})

		if completion_report:

			cr=frappe.get_doc("Completion Report",{"project_id":doc.project_id})
			doc.actual_date_of_completion=cr.work_completion_date
			print("helooo")
			print(doc.actual_date_of_completion)

			


		site_survey=frappe.db.exists("Site Survey",{"project_id":doc.project_id})

		if site_survey:

			ss=frappe.get_doc("Site Survey",{"project_id":doc.project_id})
			if ss.circle_name:
				doc.circle=ss.circle_name
			if ss.name_of_electrical_station:
				doc.section=ss.name_of_electrical_station
				
		pr=frappe.get_doc("Project",doc.project_id)
		if pr.consumer_number and pr.consumer_number!="Please Fill":
				doc.consumer_number=pr.consumer_number
		if pr.section:
			doc.section=pr.section
		if pr.circle:
			doc.circle=pr.circle

		if frappe.db.exists("Performance Ratio Test",{"project_id":doc.project_id}):
			pr=frappe.get_doc("Performance Ratio Test",{"project_id":doc.project_id})
			doc.pr=pr.pr_ac



		project = frappe.get_doc('Project',doc.project_id)
		if project.number_of_panels:
			doc.no_of_panels=project.number_of_panels
		if project.panel_capacity:
			doc.installed_capacity=project.panel_capacity
		if project.capacity_in_watts:
			doc.panel_capacity=project.capacity_in_watts
		if project.inverter_capacity:
			doc.inverter_capacity=project.inverter_capacity
		if project.total_capacity:
			doc.total_capacity=project.total_capacity
		
		





@frappe.whitelist(allow_guest=True)
def test(doc,pro):

		project = frappe.get_doc('Project',pro)

		d={'customer':project.customer,'consumer':project.consumer_number}
		if frappe.db.exists("Site Survey",{"project_id":pro}):
			site=frappe.get_doc("Site Survey",{"project_id":pro})
			if site.circle_name:
				d['cir']=site.circle_name
			else:
				d['cir']=""
			if site.name_of_electrical_station:
				d['sta']=site.name_of_electrical_station
			else:

				d['sta']=""
		if frappe.db.exists("Quotation",{"project_id":pro}):
			quotation=frappe.get_doc("Quotation",{"project_id":pro})
			discount=0
			for row in quotation.items:
				if row.discount_amount:
				# d['price']=row.price_list_rate
					discount=discount+row.discount_amount

				# rate=row.rate
			if discount!=0:
				d['discount']=discount
			else:
				d['discount']=""
		# else:
		# 	frappe.throw("No Quotation Created For this Project")

		if frappe.db.exists("Performance Ratio Test",{"project_id":pro}):
			pr=frappe.get_doc("Performance Ratio Test",{"project_id":pro})
			if pr.pr_ac:
				d['pr']=pr.pr_ac

		else:
			d['pr']=''


		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

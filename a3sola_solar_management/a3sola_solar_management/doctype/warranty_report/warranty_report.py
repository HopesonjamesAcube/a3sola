# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

class WarrantyReport(Document):
	def validate(doc):
		
		
	
		pr=frappe.get_doc("Project",doc.project_id)
		if pr.item_name:
			doc.item_name=pr.item_name
		if pr.panel_capacity:
			doc.capacity=pr.panel_capacity

		if pr.panel_make:
			doc.pv_module_make=pr.panel_make

		if pr.number_of_panels:
			doc.pv_module_quantity=pr.number_of_panels

		if pr.capacity_in_watts:
			doc.pv_module_capacity=pr.capacity_in_watts

		if pr.serial_no:
			
			if doc.pv_sl_no:
			
				doc.pv_sl_no.clear()
			for i in pr.serial_no:
				doc.append("pv_sl_no",{"serial_number":i.spv_serial_no})
		
		if pr.inverter_serial_no:
			if doc.inverter_sl_no:
				doc.inverter_sl_no.clear()
			count=1
			for i in pr.inverter_serial_no:
				doc.append("inverter_sl_no",{"serial_number":i.inverter_serial_no})
				if count==1:
					doc.inverter_make=i.make
					
				count=count+1
				
		if pr.inverter_capacity:
			doc.inverter_capacity=pr.inverter_capacity
			
		# if doc.date:
		# 	datetime_string = str(doc.date)
		# 	format_string = "%Y-%m-%d"

		# 	date_obj = datetime.strptime(datetime_string, format_string).date()
		# 	future_date = date_obj + relativedelta(years=5)
		# 	future_date = future_date - timedelta(days=1)
		# 	doc.warranty_closed_date=future_date.strftime('%Y-%m-%d')


		




@frappe.whitelist(allow_guest=True)
def test(doc,pro):

		project = frappe.get_doc('Project',pro)



		d={'customer':project.customer,'it':project.item_name}

		if frappe.db.exists("Sales Invoice",{"project":pro}):
			si=frappe.get_doc("Sales Invoice",{"project":pro})


			# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
			print(d)
			print(si.name)

			d['si']=si.name
		else:
			d['si']=""



		return d

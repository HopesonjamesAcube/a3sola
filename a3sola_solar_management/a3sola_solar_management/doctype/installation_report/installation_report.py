# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class InstallationReport(Document):
	def validate(doc):
		
		pr=frappe.get_doc("Project",doc.project_id)
		if pr.base_document!='Installation Report':
		
			if pr.serial_no and pr.inverter_serial_no:    
				print("Hello")
			
				
				doc.solar_module_series_numbers.clear()
				for i in pr.serial_no:
						doc.append("solar_module_series_numbers",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
				if pr.inverter_serial_no:
					doc.inverter_details.clear()
					for i in pr.inverter_serial_no:
						doc.append("inverter_details",{"make":i.make,"capacity_of_inverter":i.capacity_of_inverter,"inverter_serial_no":i.inverter_serial_no})






@frappe.whitelist(allow_guest=True)
def test(doc,pro):

		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.customer)
		



		d={'cadd':project.address,'customer':project.customer,'consumer':project.consumer_number,'con':project.contact_number,'em':project.email,'item':project.item_name}
		if frappe.db.exists("Site Information",{"project_id":pro}):
			si=frappe.get_doc("Site Information",{"project_id":pro})
			if si.latitude:
				d['lat']=si.latitude
			else:
				d['lat']=""
			if si.longitude:
				d['lon']=si.longitude
			else:
				d['lon']=""
			if si.type_of_roof:
				d['roof']=si.type_of_roof
			else:
				d['roof']=""
		if frappe.db.exists("Schedule Installation",{"project_id":pro}):
					schedule=frappe.get_doc("Schedule Installation",{"project_id":pro})
					print("@@@@@@@@@@@@@@@@@@@@@@@",schedule)
					if schedule.installation_scheduled_on:
						
						d['in']=schedule.installation_scheduled_on
					else:
						d['in']=""
		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

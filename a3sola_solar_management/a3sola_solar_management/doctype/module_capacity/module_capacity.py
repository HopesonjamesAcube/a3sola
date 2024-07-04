# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ModuleCapacity(Document):
	def validate(doc):
		
		
		

		completion_report=frappe.db.exists("Completion Report",{"project_id":doc.project_id})
		if completion_report:
			print(doc.name)

			cr=frappe.get_doc("Completion Report",{"project_id":doc.project_id})
			if cr.serial_no:

				doc.panels.clear()
				for i in cr.serial_no:
						doc.append("panels",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
			if cr.inverter_serial_no:
				doc.inverter.clear()
				for i in cr.inverter_serial_no:
					print(i)
					doc.append("inverter",{"inverter":i.make,"inverter_capacity":i.capacity_of_inverter,"serial_no":i.inverter_serial_no})


		pr=frappe.get_doc("Project",doc.project_id)
		if pr.base_document!='Module Capacity':
			if pr.panel_capacity:
				
				doc.panel_capacity=pr.panel_capacity
			if pr.serial_no and pr.inverter_serial_no:    
				
				doc.serial_no.clear()
				for i in pr.serial_no:
						doc.append("serial_no",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
				if pr.inverter_serial_no:
					doc.inverter_serial_no.clear()
					for i in pr.inverter_serial_no:
						doc.append("inverter_serial_no",{"make":i.make,"capacity_of_inverter":i.capacity_of_inverter,"inverter_serial_no":i.inverter_serial_no})







@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)


		d={'cadd':project.primary_address,'customer':project.customer,'consumer':project.consumer_number,'con':project.contact_number,'em':project.email}

		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d





@frappe.whitelist(allow_guest=True)
def aftersavefetch(doc,pro):
	

	cr=frappe.get_doc('Module Capacity',doc)
	if cr.serial_no and cr.inverter_serial_no:
		

		
		project=frappe.get_doc("Project",pro)
		print(project.name,project.base_document,project.name)
		if project.base_document=='' or project.base_document==None or project.base_document=='Module Capacity':
			
			project.base_document="Module Capacity"
			
			
			project.save()
			project=frappe.get_doc("Project",pro)
			project.save()
			

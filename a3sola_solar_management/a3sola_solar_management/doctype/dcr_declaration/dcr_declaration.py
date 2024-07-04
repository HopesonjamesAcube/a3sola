import frappe
from frappe.model.document import Document

class DCRDeclaration(Document):
	def validate(doc):
		completion_report=frappe.db.exists("Completion Report",{"project_id":doc.project_id})
		if completion_report:
			cr=frappe.get_doc("Completion Report",{"project_id":doc.project_id})

			if cr.serial_no:
				doc.panels.clear()
				count=0
				for i in cr.serial_no:
					count=count+1
					doc.append("panels",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
				doc.no_of_pv_modules=count

		pr=frappe.get_doc("Project",doc.project_id)
		if pr.serial_no and pr.inverter_serial_no:    
			
			doc.serial_no.clear()
			for i in pr.serial_no:
					doc.append("serial_no",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
			
		project = frappe.get_doc('Project',doc.project_id)
		if project.capacity_in_watts:
			doc.pv_module_capacity=project.capacity_in_watts
		if project.number_of_panels:
			doc.no_of_pv_modules=project.number_of_panels
		if project.panel_capacity:
			doc.installed_capacity=project.panel_capacity
		



@frappe.whitelist(allow_guest=True)
def test(doc,pro):

		project = frappe.get_doc('Project',pro)

		print(project.address)
		addr=""
		if project.address:
			add=frappe.get_doc("Address",project.address)

			addr=add.address_line1
			if add.address_line2:
				addr=addr+", "+add.address_line2
			addr=addr+", "+add.city+", "+add.country
		print(project.customer)

		d={'cadd':addr,'customer':project.customer,'con':project.contact_number,'em':project.email}

		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

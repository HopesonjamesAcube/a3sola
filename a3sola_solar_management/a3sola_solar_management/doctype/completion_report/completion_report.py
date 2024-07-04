# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import datetime

class CompletionReport(Document):
	def after_insert(doc):
		project = frappe.get_doc('Project',doc.project_id)
		datetoday=datetime.date.today()
		d = datetime.date.strftime(datetoday, '%Y/%m')
		print(d)
		if project.physical_file_number:
			wrk_ord_ref=str(d)+"/"+project.physical_file_number
			doc.work_order_reference_number=wrk_ord_ref

	def validate(doc):
		
		site_survey=frappe.db.exists("Site Survey",{"project_id":doc.project_id})
		if site_survey:
			ss=frappe.get_doc("Site Survey",{"project_id":doc.project_id})
			if ss.name_of_electrical_station:

				doc.section=ss.name_of_electrical_station
			if ss.name_of_electrical_station:

				doc.section=ss.name_of_electrical_station

		pr=frappe.get_doc("Project",doc.project_id)
		if pr.consumer_number and pr.consumer_number!="Please Fill":
				doc.consumer_number=pr.consumer_number
		if pr.section:
			doc.section=pr.section
		if pr.circle:
			doc.circle=pr.circle
				
		# if doc.consumer_name:
		# 	pro = frappe.get_doc('Project',doc.project_id)
		# 	pro.consumer_name=doc.consumer_name
		# 	pro.save()
		
		

		
		pr=frappe.get_doc("Project",doc.project_id)
		if pr.base_document!='Completion Report':
			if pr.serial_no and pr.inverter_serial_no:    
				
				doc.serial_no.clear()
				for i in pr.serial_no:
						doc.append("serial_no",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
				if pr.inverter_serial_no:
					doc.inverter_serial_no.clear()
					for i in pr.inverter_serial_no:
						doc.append("inverter_serial_no",{"make":i.make,"capacity_of_inverter":i.capacity_of_inverter,"inverter_serial_no":i.inverter_serial_no})







	#
	# def validate(doc):
	# 	ModuleCapacity=frappe.db.exists("Module Capacity",{"project_id":doc.project_id})
	# 	if ModuleCapacity:
	# 		mc=frappe.get_doc("Module Capacity",{"project_id":doc.project_id})
	# 		if doc.serial_no:
	# 			mc.panels.clear()
	#
	# 			for i in doc.serial_no:
	# 			   print(i.spv_module_make)
	# 			   mc.append("panels",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})
	# 		if doc.inverter_serial_no:
	# 			mc.inverter.clear()
	# 			for i in doc.inverter_serial_no:
	# 				mc.append("inverter",{"inverter":i.make,"inverter_capacity":i.capacity_of_inverter,"serial_no":i.inverter_serial_no})

			# mc.save()

		# dcr=frappe.db.exists("DCR Declaration",{"project_id":doc.project_id})
		# print(dcr)
		# if dcr:
		#
		# 	dc=frappe.get_doc("DCR Declaration",{"project_id":doc.project_id})
		#
		# 	dc.save()
		# dcr=frappe.db.exists("DCR Declaration",{"project_id":doc.project_id})
		# print(dcr)
		# if dcr:
		#
		# 	dc=frappe.get_doc("DCR Declaration",{"project_id":doc.project_id})
		#
		# 	dc.save()
		# d_of_work=frappe.db.exists("Details of Work",{"project_id":doc.project_id})
		# print(d_of_work)
		# if d_of_work:
		#
		#
		# 	dw=frappe.get_doc("Details of Work",{"project_id":doc.project_id})
		# 	dw.actual_date_of_completion=doc.work_completion_date
		#
		#
		# 	dw.save()
		#





@frappe.whitelist(allow_guest=True)
def aftersavefetch(doc,pro):
	

	
	cr=frappe.get_doc('Completion Report',doc)
	if cr.serial_no and cr.inverter_serial_no:
		
		project=frappe.get_doc("Project",pro)
		print(project.name,project.base_document,project.name)
		if project.base_document=='' or project.base_document==None or project.base_document=='Completion Report':
			
			
			project.base_document="Completion Report"
			if cr.consumer_name:
				project.consumer_name=cr.consumer_name
			if cr.consumer_number:
				project.consumer_number=cr.consumer_number
			if cr.section:
				project.section=cr.section
			if cr.circle:
				project.circle=cr.circle
			# set base document for project
			project.save()
			# set updated values on project
			project=frappe.get_doc("Project",pro)
			project.save()

	

	ModuleCapacity=frappe.db.exists("Module Capacity",{"project_id":pro})
	if ModuleCapacity:
		mc=frappe.get_doc("Module Capacity",{"project_id":pro})
		mc.save()
	dcr=frappe.db.exists("DCR Declaration",{"project_id":pro})
	print(dcr)
	if dcr:
		dc=frappe.get_doc("DCR Declaration",{"project_id":pro})
		dc.save()

	d_of_work=frappe.db.exists("Details of Work",{"project_id":pro})
	print(d_of_work)
	if d_of_work:
		dw=frappe.get_doc("Details of Work",{"project_id":pro})
		dw.save()

	
		
	








@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.customer)

		d={'cadd':project.primary_address,'customer':project.customer,'consumer':project.consumer_number,'con':project.contact_number}
		if frappe.db.exists("Site Survey",{"project_id":pro}):
			site=frappe.get_doc("Site Survey",{"project_id":pro})

			if site.name_of_electrical_station:
				d['sta']=site.name_of_electrical_station
			else:

				d['sta']=""
		else:

			d['sta']=""
			# if site.number_of_phase:
			# 	d['ph']=site.number_of_phase
			# else:

			# 	d['ph']=""
		ebexist=frappe.db.exists("EB Information",{"project_id":pro})
		if ebexist:
			eb=frappe.get_doc("EB Information",{"project_id":pro})
			if eb.phase:
				d['ph']=eb.phase
			else:

				d['ph']=""
		else:
			d['ph']=""


		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PerformanceRatioTest(Document):
	def validate(doc):
		wdc=0
		wac=0
		irradiance=0
		count=0
		for i in doc.table_20:
			if i.wdc!=None and i.wac!=None and i.irradiance!=None:
				wdc=wdc+i.wdc
				wac=wac+i.wac
				irradiance=irradiance+i.irradiance
				count=count+1
		print(count)
		if wdc!=0 and wac!=0 and irradiance!=0:
			awdc=wdc/count
			awac=wac/count
			airradiance=irradiance/count
			in_eff=doc.inverter_efficiency/100
			doc.average_wdc=round(awdc, 2)
			doc.average_wac=round(awac,2)
			m_effi=doc.efficiency/100
			doc.average_irradiance=round(airradiance,2)
			doc.pr_dc=((awdc)/(airradiance*doc.area*m_effi))*100
			doc.pr_ac=((awac)/(airradiance*doc.area*m_effi*in_eff))*100
			doc.pr_dc=round(doc.pr_dc,2)
			doc.pr_ac=round(doc.pr_ac,2)

		site_survey=frappe.db.exists("Site Survey",{"project_id":doc.project_id})
		if site_survey:
			ss=frappe.get_doc("Site Survey",{"project_id":doc.project_id})
			if ss.circle_name and ss.name_of_electrical_station:
				doc.section_office_or_circle=ss.circle_name+"/"+ss.name_of_electrical_station
				print(doc.section_office_or_circle)
		
		project = frappe.get_doc('Project',doc.project_id)
		if project.number_of_panels:
			doc.solar_pv_capacity=project.number_of_panels
		if project.panel_capacity:
			doc.capacity=project.panel_capacity




@frappe.whitelist(allow_guest=True)
def aftersavefetch(doc,pro):

	if frappe.db.exists("Details of Work",{"project_id":pro}):
		pr=frappe.get_doc("Details of Work",{"project_id":pro})
		pr.save()






@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.consumer_number)


		d={'customer':project.customer,'consno':project.consumer_number,"item":project.item_name}

		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		return d

		# d={'cadd':project.primary_address,'customer':project.customer,'consno':project.consumer_number}


		# print(d)
		# return d

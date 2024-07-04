# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class EBInformation(Document):
 def validate(doc):
		#exist on opportunity to set ss=0
		ss=0

		#check exist on opportunity set value for ss
		project=frappe.get_doc("Project",doc.project_id)
		if project.oppertunity:

			opper=frappe.get_doc("Opportunity",project.oppertunity)
			if opper.site_survey:
				ss=opper.site_survey

		#check is there is any site site survey exit for fetching
		sitesurvey=frappe.db.exists("Site Survey",{"project_id":doc.project_id})

		if sitesurvey:
			if ss:
				ss=frappe.get_doc("Site Survey",ss)
			else:
				ss=frappe.get_doc("Site Survey",{"project_id":doc.project_id})

			if ss.consumer_number:
				doc.consumer_number=ss.consumer_number
			
			if ss.registered_in_kseb_soura:
				doc.registered_in_kseb_soura=ss.registered_in_kseb_soura

			if ss.required_pv_connection:
				doc.required_pv_connection=ss.required_pv_connection

			if ss.number_of_phase:
				doc.phase=ss.number_of_phase
			if ss.name_of_electrical_station:
				doc.section=ss.name_of_electrical_station
			if ss.circle_name:
				doc.circle=ss.circle_name
			if ss.panchayath:
				doc.corporation_or_municipality=ss.panchayath
			

			




@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")  
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.consumer_number)
		

		d={'cadd':project.primary_address,'customer':project.customer,'consno':project.consumer_number}

		
		print(d)
		return d

# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SiteInformation(Document):
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

	
			
		sitesurvey=frappe.db.exists("Site Survey",{"project_id":doc.project_id})
		
		# if not ebexist and not siteexist:
		# 	frappe.throw("Please Complete EB information and Site Information")
		# if not ebexist:
		# 	frappe.throw("Please Complete EB information")
		# if not siteexist:
		# 	frappe.throw("Please Complete Site information")

		if sitesurvey:
			if ss:
				ss=frappe.get_doc("Site Survey",ss)
			else:
				ss=frappe.get_doc("Site Survey",{"project_id":doc.project_id})

				
			ss=frappe.get_doc("Site Survey",{"project_id":doc.project_id})
			if ss.roof_type:
				doc.roof_type=ss.roof_type
			if ss.roof_angle_of_inclination:
				doc.roof_inclination=ss.roof_angle_of_inclination

			if ss.parapet_wall_height:
				doc.parapet_height=ss.parapet_wall_height

			if ss.availability_of_south_facing_module_mounting_area:
				doc.availability_of_south_facing_module_mounting_area=ss.availability_of_south_facing_module_mounting_area
			if ss.building_height_or_number_of_floor:
				doc.building_height_or_number_of_floor=ss.building_height_or_number_of_floor

			if ss.cable_routing_confirmed_by_client:
				doc.cable_routing_confirmed_by_client=ss.cable_routing_confirmed_by_client

			if ss.ajb_to_inverter_cable_length:
				doc.ajb_to_inverter_cable_length=ss.ajb_to_inverter_cable_length

			if ss.spv_module_to_ajb_cable_lenght:
				doc.spv_module_to_ajb_cable_lenght=ss.spv_module_to_ajb_cable_lenght

			if ss.acdb_to_ex_lt_panel_or_db_cable_length:
				doc.acdb_to_ex_lt_panel_or_db_cable_length=ss.acdb_to_ex_lt_panel_or_db_cable_length

			if ss.inverter_to_acdb_cable_length:
				doc.inverter_to_acdb_cable_length=ss.inverter_to_acdb_cable_length

			if ss.earthing_cable_length:
				doc.earthing_cable_length=ss.earthing_cable_length

			if ss.earth_pit_location_confirmed_by_client:
				doc.earth_pit_location_confirmed_by_client=ss.earth_pit_location_confirmed_by_client

			if ss.la_down_conductor_length:
				doc.la_down_conductor_length=ss.la_down_conductor_length
	

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

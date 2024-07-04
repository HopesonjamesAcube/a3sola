# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document




@frappe.whitelist(allow_guest=True)
def test(doc,pro):

	project = frappe.get_doc('Project',pro)

	print(project.address)
	print(project.customer)


	d={'cadd':project.address,'customer':project.customer,'opp':project.oppertunity,'consno':project.consumer_number}
	
	ebexist=frappe.db.exists("EB Information",{"project_id":pro})
	siteexist=frappe.db.exists("Site Information",{"project_id":pro})
	
	# if not ebexist and not siteexist:
	# 	frappe.throw("Please Complete EB information and Site Information")
	# if not ebexist:
	# 	frappe.throw("Please Complete EB information")
	# if not siteexist:
	# 	frappe.throw("Please Complete Site information")

	if  ebexist:
		eb=frappe.get_doc("EB Information",{"project_id":pro})
		
		print(eb.customer)
		if eb:
			if eb.customer:
				d['cu']=eb.customer
			else:
				d['cu']=""
			if eb.circle:
				d['cir']=eb.circle
			else:
				d['cir']=""
			if eb.section:
				d['sec']=eb.section
			if eb.consumer_number:
				d['consu']=eb.consumer_number
			else:
				d['consu']=""

			if eb.registered_in_kseb_soura:
				d['reg']=eb.registered_in_kseb_soura
			else:
				d['reg']=""
			if eb.required_pv_connection:
				d['req']=eb.required_pv_connection
			else:
				d['req']=""
			if eb.phase:
				d['phase']=eb.phase
			else:
				d['phase']=""
	if siteexist:
		site=frappe.get_doc("Site Information",{"project_id":pro})
		if site:
				if site.type_of_roof:
					d['roof']=site.type_of_roof
				else:
					d['roof']=""
				if site.roof_inclination:
					d['incl']=site.roof_inclination
				else:
					d['incl']=""
				if site.parapet_height:
					d['para']=site.parapet_height
				else:
					d['para']=""
				if site.availability_of_south_facing_module_mounting_area:
					d['south']=site.availability_of_south_facing_module_mounting_area
				else:
					d['south']=''
				if site.building_height_or_number_of_floor:
					d['bheight']=site.building_height_or_number_of_floor
				else:
					d['bheight']=""
				if site.cable_routing_confirmed_by_client:
					d['conf']=site.cable_routing_confirmed_by_client
				else:
					d['conf']=""
				if site.ajb_to_inverter_cable_length:
					d['ajb']=site.ajb_to_inverter_cable_length
				else:
					d['ajb']=""
				if site.spv_module_to_ajb_cable_lenght:
					d['spv']=site.spv_module_to_ajb_cable_lenght
				else:
					d['spv']=""
				if site.acdb_to_ex_lt_panel_or_db_cable_length:
					d['acdb']=site.acdb_to_ex_lt_panel_or_db_cable_length
				else:
					d['acdb']=""
				if site.inverter_to_acdb_cable_length:
					d['inve']=site.inverter_to_acdb_cable_length
				else:
					d['inve']=""
				if site.earthing_cable_length:
					d['earth']=site.earthing_cable_length
				else:
					d['earth']=""
				if site.earth_pit_location_confirmed_by_client:
					d['pit']=site.earth_pit_location_confirmed_by_client
				else:
					d['pit']=""
				if site.la_down_conductor_length:
					d['lad']=site.la_down_conductor_length
				else:
					d['lad']=""
				

			# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
				print(d)
	return d


class SiteSurvey(Document):
	def validate(self):
		#Save confirmed item exist in opportunity to site survey
		#check is it item confitrmed on opportunity set it as 0 (assume not confirmd)
		item_confirm=0
		if self.opportunity:
			oppo=frappe.get_doc("Opportunity",self.opportunity)
			for row in oppo.items:
				itm=row.item_code
				print(itm)
				item=frappe.get_doc("Item",row.item_code)
				print(item)
				if item.scheme_name:
					if frappe.db.exists("Product Bundle",item.item_code):
						self.item=item.item_code
						item_confirm=1
					#Set item confirm as 1 
					else:
						frappe.throw("Product Bundle is Not created for item ",item.item_code)

			
		
		if self.item:
			#check item confirmed exist opportunity if exist pass else add it to opportunity
			if item_confirm:
				pass
			else:
				oppo.append("items",{"item_code":self.item,"qty":1})
				oppo.save()


#check for additional items added on table additional_items if exist also that added to opportunity
		if self.additional_items:
			
			
			for i in self.additional_items:
				exist=0
				for j in oppo.items:
					if i.item_code==j.item_code:
						j.qty=i.quantity
						exist=1
				if exist==0:
					oppo.append("items",{"item_code":i.item_code,"qty":i.quantity})
						

			oppo.save()

		




	# feth from basic details to project from current site survey.

		if self.project_id:
			project=frappe.get_doc("Project",self.project_id)
			if self.circle_name:
				
				project.circle=self.circle_name
				
				
			if self.name_of_electrical_station:
				project=frappe.get_doc("Project",self.project_id)
				project.section=self.name_of_electrical_station
			if self.required_pv_connection:	
				project.panel_capacity=self.required_pv_connection

			if self.panchayath:
				project.corporation_or_municipality_or_panchayath=self.panchayath

			project.save()


			if self.additional_items:
				if frappe.db.exists("Quotation",{"project_id":self.project_id}):
					qua=frappe.get_doc("Quotation",{"project_id":self.project_id})
					for i in self.additional_items:
						exist=0
						for j in qua.items:
							if i.item_code==j.item_code:
								j.qty=i.quantity
								exist=1
						if exist==0:
							qua.append("items",{"item_code":i.item_code,"qty":i.quantity})
								

					qua.save()



		# if doc:
		# 	ebexist=frappe.db.exists("EB Information",{"project_id":self.project_id})
		# 	siteexist=frappe.db.exists("Site Information",{"project_id":self.project_id})
		# 	if not ebexist and not siteexist:
		# 		frappe.throw("Please Complete EB information and Site Information")
		# 	if not ebexist:
		# 		frappe.throw("Please Complete EB information")
		# 	if not siteexist:
		# 		frappe.throw("Please Complete Site information")


		# 	eb=frappe.get_doc("EB Information",{"project_id":self.project_id})
		# 	site=frappe.get_doc("Site Information",{"project_id":self.project_id})
		# 	print(eb.customer)

		# 	if eb.customer:
		# 		self.customer_name=eb.customer
		# 	if eb.consumer_number:
		# 		self.consumer_number=eb.consumer_number
		# 	if eb.registered_in_kseb_soura:
		# 		self.registered_in_kseb_soura=eb.registered_in_kseb_soura
		# 	if eb.required_pv_connection:
		# 		self.required_pv_connection=eb.required_pv_connection
		# 	if eb.phase:
		# 		self.number_of_phase=eb.phase




		# 	self.roof_type=site.type_of_roof
		# 	self.roof_angle_of_inclination=site.roof_inclination
		# 	self.parapet_wall_height=site.parapet_height
		# 	self.availability_of_south_facing_module_mounting_area=site.availability_of_south_facing_module_mounting_area
		# 	self.building_height_or_number_of_floor=site.building_height_or_number_of_floor
		# 	self.cable_routing_confirmed_by_client=site.cable_routing_confirmed_by_client
		# 	self.ajb_to_inverter_cable_length=site.ajb_to_inverter_cable_length
		# 	self.spv_module_to_ajb_cable_lenght=site.spv_module_to_ajb_cable_lenght
		# 	self.acdb_to_ex_lt_panel_or_db_cable_length=site.acdb_to_ex_lt_panel_or_db_cable_length
		# 	self.inverter_to_acdb_cable_length=site.inverter_to_acdb_cable_length
		# 	self.earthing_cable_length=site.earthing_cable_length
		# 	self.earth_pit_location_confirmed_by_client=site.earth_pit_location_confirmed_by_client
		# 	self.la_down_conductor_length=site.la_down_conductor_length

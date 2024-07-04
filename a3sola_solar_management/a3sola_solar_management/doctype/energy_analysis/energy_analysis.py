# Copyright (c) 2024, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EnergyAnalysis(Document):
	def validate(doc):
		unit_consumed_month=0
		unit_consumed_day=0
		solar_plant_day=0
		if doc.energy_analysis_type=="Non-TOD Bill":
			for i in doc.energy_anaysis_tod_values:
				if i.unit_consumed_kwh_month:
					print(i.unit_consumed_kwh_month,"''''''''''''''''''")
					unit_consumed_month=float(unit_consumed_month+i.unit_consumed_kwh_month)
				if i.unit_consumed_kwh_day:
					unit_consumed_day=float(unit_consumed_day+i.unit_consumed_kwh_day)
				if i.solar_plant_required_kwp_day:
					solar_plant_day=float(solar_plant_day+i.solar_plant_required_kwp_day)	
			
			
			doc.total_unit_consumed_kwh_month=unit_consumed_month
			doc.total_unit_consumed_kwh_day=unit_consumed_day
			doc.solar_plant_required_kwp=solar_plant_day
		
		if doc.energy_analysis_type=="TOD Bill":
			for i in doc.kseb_bill_study:
				if i.unit_consumed_kwh_month:
					print(i.unit_consumed_kwh_month,"''''''''''''''''''")
					unit_consumed_month=float(unit_consumed_month+i.unit_consumed_kwh_month)
				if i.unit_consumed_kwh_day:
					unit_consumed_day=float(unit_consumed_day+i.unit_consumed_kwh_day)
				if i.solar_plant_required_kwp_day:
					solar_plant_day=float(solar_plant_day+i.solar_plant_required_kwp_day)	
			
			
			doc.total_unit_consumed_kwh_month=unit_consumed_month
			doc.total_unit_consumed_kwh_day=unit_consumed_day
			doc.solar_plant_required_kwp=solar_plant_day
		







@frappe.whitelist(allow_guest=True)
def test(doc,pro):
	d={}
	project = frappe.get_doc('Project',pro)
	if project.consumer_number:
		d["consno"]=project.consumer_number
		return d
	else:
		return d
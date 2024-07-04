# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SolarAgreement(Document):
	pass


@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.customer)
		ebexist=frappe.db.exists("EB Information",{"project_id":pro})
		print("hiiiiiiiiii")
		if not ebexist:
			frappe.throw("Please Complete EB information")
		if ebexist:
			eb=frappe.get_doc("EB Information",{"project_id":pro})
			# site=frappe.get_doc("Site Information",{"project_id":doc.project_id})
			print(eb,"@@@@@@@@@@@@@@@@@@@@@@@")
			# print(site,"########################")
			if eb.spin_number:
				spin=eb.spin_number
			else:
				spin=""
			if eb.code_and_category:
				code=eb.code_and_category
			else:
				code=""
			if eb.survey_no:
				sur=eb.survey_no
			else:
				sur=""
			if eb.village:
				vil=eb.village
			else:
				vil=""
			if eb.corporation_or_municipality:
				cor=eb.corporation_or_municipality
			else:
				cor=""
			if eb.dist_transformer:
				dist=eb.dist_transformer
			else:
				dist=""
			if eb.connected_load:
				con=eb.connected_load
			else:
				con=""
			if eb.section:
				sec=eb.section
			else:
				sec=""

			if eb.required_pv_connection:
				pv=eb.required_pv_connection
			else:
				pv=""

			if eb.circle:
				cir=eb.circle
			else:
				cir=""
		if sec:
			pass

		else:
			if frappe.db.exists("Site Survey",{"project_id":pro}):
						site=frappe.get_doc("Site Survey",{"project_id":pro})
						# if site.circle_name:
						# 	d['cir']=site.circle_name
						# else:
						# 	d['cir']=""
						if site.name_of_electrical_station:
							sec=site.name_of_electrical_station
				



		price=0
		discount=0
		rate=0
		if frappe.db.exists("Quotation",{"project_id":pro}):
			quotation=frappe.get_doc("Quotation",{"project_id":pro})
			

			for row in quotation.items:

				price=price+row.price_list_rate
				discount=discount+row.discount_amount
				rate=rate+row.rate
		# else:
		# 	frappe.throw("No Quotation Created For this Project")

	

		d={'cir':cir,'pv':pv,'sp':spin,'con':con,'cod':code,'su':sur,"dist":dist,'vi':vil,'corp':cor,'cadd':project.primary_address,'customer':project.customer,'sta':sec,'consno':project.consumer_number,'price':price,"discount_amount":discount,"rate":rate,"item":project.item_name}
		

		print(d)
		return d

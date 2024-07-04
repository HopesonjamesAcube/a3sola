# Copyright (c) 2022, Acube Innovations and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
import frappe
from frappe.utils import date_diff


class ScheduleInstallation(Document):
	def on_submit(doc):

		incentivelist=frappe.get_all('Track Incentive Or Commision', filters={'Project_id': doc.project_id,'user':doc.installer})
		print(incentivelist)


		if incentivelist:

			trackincentive=frappe.get_doc('Track Incentive Or Commision', incentivelist[0]['name'])
			trackincentive.allowed_incentive=trackincentive.allowed_incentive+int(doc.amount)
			trackincentive.unpaid=trackincentive.unpaid+int(doc.amount)
			inc="RS. "+str(doc.amount)+" Incentive Allowed"
			trackincentive.append("log",{"date":frappe.utils.now(),"detail":inc})

			trackincentive.save()


		else:

			trackincentive=frappe.new_doc("Track Incentive Or Commision")
			trackincentive.user=doc.installer
			trackincentive.project_id=doc.project_id
			trackincentive.allowed_incentive=int(doc.amount)
			trackincentive.unpaid=trackincentive.unpaid+int(doc.amount)
			inc="RS. "+str(doc.amount)+" Incentive Allowed"
			trackincentive.append("log",{"date":frappe.utils.now(),"detail":inc})
			trackincentive.save()


	def validate(doc):
		if doc.amount:
			doc.total_amount = float(doc.amount)
		if doc.travel_allowance:
			doc.total_amount += doc.travel_allowance
		if doc.other_expenses:
			doc.total_amount += doc.other_expenses


		if not doc.installer_invoice:
			protasks=frappe.get_list("Task",{"project": doc.project_id,"doctypes_name":"Installation Report"})
			installer=frappe.get_doc("Installers",doc.installers)
			
			pi=frappe.new_doc("Purchase Invoice")
			pi.supplier=installer.supplier
			print(pi.supplier)
			print("**************8")

			proset=frappe.get_doc("Project Settings")
			if proset.installer_payment_item or proset.travel_allowance_item or proset.other_expenses_item:
			

				print("values",doc.amount,doc.travel_allowance,doc.other_expenses)
				pi.project=doc.project_id
				if doc.amount:
					pi.append("items",{"item_code":proset.installer_payment_item,"qty":"1","rate":doc.amount})
				if doc.travel_allowance:
					pi.append("items",{"item_code":proset.travel_allowance_item,"qty":"1","rate":doc.travel_allowance})
				if doc.other_expenses:
					pi.append("items",{"item_code":proset.other_expenses_item,"qty":"1","rate":doc.other_expenses})
				

				pi.save()
				doc.installer_invoice=pi.name
		
			
		
@frappe.whitelist(allow_guest=True)
def before(doc,pro):
	sin=frappe.get_doc("Schedule Installation",doc)
	if sin.installation_scheduled_on:
			installer=frappe.get_doc("Installers",sin.installers)
			
			pi=frappe.new_doc("Purchase Invoice")
			pi.supplier=installer.supplier
			print(pi.supplier)
			print("**************8")

			proset=frappe.get_doc("Project Settings")
			if proset.installer_payment_item:
			

				
				pi.project=sin.project_id
				pi.append("items",{"item_code":proset.installer_payment_item,"qty":"1","rate":sin.amount})
				

				pi.save()
		
	return pi.name

			# if protasks:
			# 	tas=frappe.get_doc("Task",protasks[0])
			# 	tas.exp_start_date=doc.installation_scheduled_on
			# 	date1=datetime.strptime(tas.exp_start_date, "%Y/%m/%d")
			# 	date2=datetime.strptime(tas.exp_end_date, "%Y/%m/%d")
			#
			# 	print(tas.exp_start_date)
			# 	delta = (date2 - date1)
			# 	print(f'Difference is {delta.days} days')
			# 	date=delta.days
			# 	print(date)
			# 	frappe.throw("haii")
			#
			#
			# 	tas.save()
			# #



@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)
		tas =""
		print(project.primary_address)
		print(project.customer)
		protasks=frappe.get_list("Task",{"project": pro,"doctypes_name":"Installation Report"})
		if protasks:
			tas=frappe.get_doc("Task",protasks[0])
			print(tas)
			tas=tas.name





		d={'cadd':project.primary_address,'customer':project.customer,'item':project.item_name}

		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		d['tas']=tas
		return d

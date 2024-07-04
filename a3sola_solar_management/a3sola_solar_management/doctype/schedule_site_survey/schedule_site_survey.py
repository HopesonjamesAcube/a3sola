# Copyright (c) 2022, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.desk.form import assign_to



class ScheduleSiteSurvey(Document):

	def validate(doc):
		if doc.expected_start_date and doc.expected_end_date:
			protasks=frappe.get_list("Task",{"project": doc.project_id,"doctypes_name":"Site Survey"})
			if protasks:
				tas=frappe.get_doc("Task",protasks[0])
				tas.exp_start_date=doc.expected_start_date
				tas.exp_end_date=doc.expected_end_date
				print(tas.exp_start_date)

				tas.save()
		# if doc.assigned_to:
		# 			assign_to.add(
		# 				dict(
		# 					assign_to=[doc.assigned_to],
		# 					doctype=doc.get("Site Survey"),
		#
		#
		# 				)
		# 			)
		#
		# 			# set for reference in round robin
		# 			self.db_set("last_user", doc.assigned_to)
		# 			return True






@frappe.whitelist(allow_guest=True)
def test(doc,pro):
		print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
		print(pro)
		project = frappe.get_doc('Project',pro)

		print(project.primary_address)
		print(project.customer)

		protasks=frappe.get_list("Task",{"project": pro,"doctypes_name":"Site Survey"})
		if protasks:
			tas=frappe.get_doc("Task",protasks[0])
			print(tas)
			tas=tas.name


		d={'cadd':project.primary_address,'customer':project.customer,'opp':project.oppertunity}

		# return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
		print(d)
		if tas:
			d['tas']=tas
		return d

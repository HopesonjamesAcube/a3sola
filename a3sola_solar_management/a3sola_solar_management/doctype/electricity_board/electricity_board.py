# Copyright (c) 2022, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ElectricityBoard(Document):
	def validate(self):

		if not frappe.db.exists("Customer",self.board_detls):
			cus=frappe.new_doc("Customer")
			cus.customer_name=self.board_detls
			cus.customer_type="Company"
			if not frappe.db.exists("Customer Group","A3sola"):
				cg=frappe.new_doc("Customer Group")
				cg.customer_group_name="A3sola"
				cg.save()
			cus.customer_group="A3sola"
			cus.territory="India"
			cus.save()
			frappe.msgprint('Customer ' f'<a href="/app/customer/{cus.name}" target="blank">{cus.name} </a> Created Successfully ')
		else:
			pass

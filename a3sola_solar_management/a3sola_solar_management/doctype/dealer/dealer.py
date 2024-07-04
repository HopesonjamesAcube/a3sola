# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Dealer(Document):
	def after_insert(doc):

		suppiler=frappe.new_doc("Supplier")
		exit=frappe.db.exists("Supplier",doc.name)
		if exit:
			frappe.throw("Supplier with Same Name Already Exist")
		suppiler.supplier_name=doc.dealer_name
		suppiler.supplier_type="Company"
		suppiler.supplier_group="All Supplier Groups"
		suppiler.territory="India"
		suppiler.is_installer=1
		suppiler.dealer=doc.name
		suppiler.warehouse=doc.warehouse
		suppiler.user=doc.user
		
		if doc.primary_contact:
			suppiler.supplier_primary_contact=doc.primary_contact
		if doc.primary_address:
			suppiler.supplier_primary_address=doc.primary_address


		suppiler.save()






		customer=frappe.new_doc("Customer")
		customer.customer_name=doc.dealer_name
		customer.customer_type="Company"
		customer.customer_group="Commercial"
		customer.territory="India"
		if doc.primary_contact:
			customer.customer_primary_contact=doc.primary_contact
		if doc.primary_address:
			customer.customer_primary_address=doc.primary_address
		customer.is_installer=1
		customer.dealer=doc.name
		customer.warehouse=doc.warehouse
		customer.user=doc.user
		customer.save()

		
		
            

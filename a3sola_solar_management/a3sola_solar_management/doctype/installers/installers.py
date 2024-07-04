# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Installers(Document):
	def after_insert(doc):


		suppiler=frappe.new_doc("Supplier")
		exit=frappe.db.exists("Supplier",doc.name)

		if not frappe.db.exists("Supplier Group", 'Installer'):
			sg = frappe.new_doc("Supplier Group")
			sg.supplier_group_name = 'Installer'
			sg.parent_supplier_group = 'All Supplier Groups'
			sg.save()
		
		suppiler.supplier_name=doc.installer+"-"+"installer"
		suppiler.supplier_type="Company"
		suppiler.supplier_group="Installer"
		suppiler.territory="India"
		suppiler.is_oinstaller=1
		suppiler.installer=doc.name
		suppiler.user=doc.user
		suppiler.name=doc.installer
		suppiler.purchase_account=doc.purchase_account

		
		if doc.primary_contact:
			suppiler.supplier_primary_contact=doc.primary_contact
		if doc.primary_address:
			suppiler.supplier_primary_address=doc.primary_address


		suppiler.save()






		
		
		
            

# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Documentation(Document):
	def validate(doc):
		
		nav=frappe.get_doc("Navbar Settings")
		if doc.show_on_about:
			
			
			exist=0
			for i in nav.help_dropdown:
				
				if i.item_label=='A3sola Documentation':
					i.hidden=0
					exist=1

			if exist==0:
				
				
				nav.append("help_dropdown",{"item_label":'A3sola Documentation',"item_type":'Route',"route":'/show?id=a73010fe373755c042d722a8a7eaffed6fc694e1'})
		else:
			for i in nav.help_dropdown:
				if i.item_label=='A3sola Documentation':
					i.hidden=1
		nav.save()

		web=frappe.get_doc("Website Settings")
		
		if doc.show_on_website:	
			exist=0
			for i in web.top_bar_items:
				
				if i.label=='A3sola Documentation':
					exist=1
			if exist==0:
				
				web.append("top_bar_items",{"label":'A3sola Documentation',"url":'/show?id=a73010fe373755c042d722a8a7eaffed6fc694e1'})
		else:
			for row in web.top_bar_items:
				if row.label=='A3sola Documentation':
					
						row.delete()
		
		web.save()
		

		
		
			




# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CustomizedDocumentation(Document):
	
		
	def validate(doc):

		#checking initial required webpage and side bar available
		
		webpage=frappe.db.exists("Web Page",'a3sola-documentation')
		if not webpage:
			frappe.msgprint('Please Add Webpage A3Sola Documentation')
			
		side_bar=frappe.db.exists("Website Sidebar",'A3Sola Documentation')
		if not side_bar:
			frappe.msgprint('Please add Website Sidebar A3Sola Documentation')

		

		#check is current document need to add in webpage
		if side_bar and webpage:
			a3sola_side_bar=frappe.get_doc("Website Sidebar",'A3Sola Documentation')
			if doc.view_on_documentation:
		
				
				if a3sola_side_bar.sidebar_items:
			
			
					exist=0
					for i in a3sola_side_bar.sidebar_items:
						
						if i.title==doc.name:
							i.route='/a3sola-documentation?'+'id'+'='+doc.name
							
							exist=1

					if exist==0:
						
						
						a3sola_side_bar.append("sidebar_items",{"title":doc.name,"route":'/a3sola-documentation?'+'id'+'='+doc.name})											
				
			
			else:
				
				
				for row in a3sola_side_bar.sidebar_items:
					if row.title==doc.name:
						
							row.delete()

			a3sola_side_bar.save()



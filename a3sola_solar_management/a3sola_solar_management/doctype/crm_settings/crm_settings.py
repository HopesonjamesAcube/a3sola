# Copyright (c) 2022, Misma and contributors
# For license information, please see license.txt

import frappe

from frappe.model.document import Document
from datetime import datetime

class CRMSettings(Document):
	# Check whether assignment rule exists or not
	# if  frappe.db.exists("Assignment Rule","Lead Assignment"):
	# 	#If exists, call update function 
	# 	def on_update(self): 
	# 		doc=frappe.get_doc("Assignment Rule","Lead Assignment")
	# 		if doc.name:
	# 			print(doc)
	# 			#Clear users table
	# 			doc.users=[]
	# 			#Update with new users
	# 			for user in self.lead_users:
	# 				# Update in users field(Table multiselect) of assignment rule.
	# 				doc.append("users",{"user":user.user_name})
	# 			doc.save()
	# 			frappe.msgprint("Lead Assignment  Updated Successfully")
	
		# Validate called before document is saved.
	
	def validate(self):
		pass
		# if not frappe.db.exists("Assignment Rule","Lead Assignment"):
		
		# 	# Check the field
		# 	print("%%%%%%%%%%%%%%%") 
		# 	# day
		# 	date = datetime.today().strftime('%A')
		# 	print(date)
		# 	#date = datetime.today()

		# 	if self.automate_lead==1:
		# 		# if it is enabled ,create a new assignment rule
		# 		arule=frappe.new_doc("Assignment Rule")
		# 		# Set the fields of assignment rule
		# 		arule.document_type="Lead"
		# 		l=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
		# 		arule.name="Lead Assignment"
		# 		for i in l:
		# 			arule.append("assignment_days",{
		# 				"day": i
		# 			})
		# 		arule.rule="Round Robin"
		# 		arule.due_date_based_on="contact_date"
		# 		arule.description="Lead Assignment"
		# 		# Fetch table multiselect field values(users)
		# 		for user in self.lead_users:
		# 			print(user.user_name)
		# 			# Update in users field(Table multiselect) of assignment rule.
		# 			arule.append("users",{"user":user.user_name})
		# 		# Set conditions
		# 		arule.assign_condition='status=="Lead"'
		# 		arule.unassign_condition='status=="Converted"'
				
		# 		#save doctype
		# 		arule.insert()
		# 		self.lead_assignment_rule=arule.name
		# 		frappe.msgprint("Lead Assignment Rule Created Successfully")
			
		# 	else:
		# 		pass
		# else:
		# 	doc=frappe.get_doc("Assignment Rule","Lead Assignment")
		# 	if doc.name:
		# 		print(doc)
		# 		#Clear users table
		# 		doc.users=[]
		# 		#Update with new users
		# 		for user in self.lead_users:
		# 			# Update in users field(Table multiselect) of assignment rule.
		# 			doc.append("users",{"user":user.user_name})
		# 		doc.save()
		# 		frappe.msgprint("CRM Settings Updated Successfully")

#Upto this


















		# if self.notify_escalation_manager==1:
		# 	notfcn=frappe.get_doc("Notification","Lead Escalated")
		# 	if notfcn.enabled==0:
		# 		notfcn.enabled=1
		# 		notfcn.save()
		# 		frappe.msgprint("Notification for Escalation manager enabled")
		# if self.send_customer_notiication==1:
		# 		# If enabled,Returns Document object of the record identified by doctype and name
		# 		notfcn=frappe.get_doc("Notification","Lead Generated")
		# 		# Enable notification
		# 		if notfcn.enabled==0:
		# 			notfcn.enabled=1
		# 		#Save doctype
		# 		notfcn.save()
		# 		frappe.msgprint("Customer Notification Enabled")
	

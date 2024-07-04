# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document

from frappe.utils.file_manager import save_file








class CustomerCallRecords(Document):
	def validate(doc):
		# check users if current document has value  wav_and_agent_number 
		if doc.wav_and_agent_number:
			userexist=frappe.db.exists("User",{"mobile_no":doc.wav_and_agent_number})
			#if user exist append that user to current document field user for assign need to create assignment role based on field user for work assignment
			if userexist:
				user=frappe.get_doc("User",{"mobile_no":doc.wav_and_agent_number})
				doc.user=user.name
				doc.first_name=user.first_name
			
			# if user not exit assign default user defined in crm setting
			else:
				crm=frappe.get_doc("CRM Settings")
				if crm.voxbay_user:
					doc.user=crm.voxbay_user
		 # if no agent number assign default user defined in crm setting
		else:
				crm=frappe.get_doc("CRM Settings")
				if crm.voxbay_user:
					doc.user=crm.voxbay_user
					user=frappe.get_doc("User",crm.voxbay_user)
					doc.first_name=user.first_name

		# if current document includes track call tables set last row status value to current status of document
		if doc.track_calls:
			print(doc.track_calls,"#################")
			print(len(doc.track_calls),"#################")
			#take length of lead tracking
			length=len(doc.track_calls)
			count=1
			for i in doc.track_calls:
				#check count equal to the length of  trackcalls
				if count==length:
					if i.status:
						#set status of last trackcalls to current status field
						doc.call_status=i.status
				count=count+1
				
		






	def after_insert(doc):

		if doc.caller_number:
			leadexist=frappe.db.exists("Lead",{"number_to_be_contacted":doc.caller_number})
			if leadexist:
				lead=frappe.get_doc("Lead",{"number_to_be_contacted":doc.caller_number})
				doc.lead=lead.name
				print(lead.name)
				print("+++++++++")
				if frappe.db.exists("Opportunity",{"party_name":lead.name}):
					opp=frappe.get_doc("Opportunity",{"party_name":lead.name})
					doc.opportunity=opp.name
					doc.customer=opp.customer
			else:
				leadexist2=frappe.db.exists("Lead",{"whatsapp_number":doc.caller_number})
				if leadexist2:

					lead=frappe.get_doc("Lead",{"whatsapp_number":doc.caller_number})
					doc.lead=lead.name
					print(lead.name)
					print("^^^^^^^^66")
					if frappe.db.exists("Opportunity",{"party_name":lead.name}):
						opp=frappe.get_doc("Opportunity",{"party_name":lead.name})
						doc.opportunity=opp.name
						doc.customer=opp.customer
		doc.save()

		if doc.recording_url:
		
			file=frappe.new_doc("File")
			file.file_name=doc.name
			file.file_url=doc.recording_url
		
			file.is_private=0
			file.attached_to_doctype="Customer Call Records"
			file.attached_to_name=doc.name
			
			file.save()
			
	




@frappe.whitelist(allow_guest=True)
def test(called_number):
	listlead=[]
	leadexist=frappe.db.get_list("Lead",{"number_to_be_contacted":called_number})
	if leadexist:
		for i in leadexist:
			print(i.name)
			listlead=listlead+[i.name]
	leadexist2=frappe.db.get_list("Lead",{"whatsapp_number":called_number})
	if leadexist2:
		for i in leadexist2:
			print(i.name)
			listlead=listlead+[i.name]	
		

	print(listlead)
	return listlead

	# if called_number:
	# 	leadexist=frappe.db.exists("Lead",{"number_to_be_contacted":called_number})
	# 	if leadexist:
	# 		lead=frappe.get_doc("Lead",{"number_to_be_contacted":called_number})
	# 		return "ph"
	# 	else:
	# 		leadexist2=frappe.db.exists("Lead",{"whatsapp_number":called_number})
	# 		if leadexist2:
	# 			lead=frappe.get_doc("Lead",{"whatsapp_number":called_number})
	# 			return "wt"
	# 		else:
	# 			return "ph"
		
	

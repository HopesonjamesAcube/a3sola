# Copyright (c) 2022, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from a3sola_solar_management.setup.install import after_insta

class CustomerTrackingSetting(Document):
    def validate(doc):
        if doc.enable_chatbot:
            after_insta()
        

		
        
	

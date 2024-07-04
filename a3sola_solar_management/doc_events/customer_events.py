import frappe
from frappe.utils import add_to_date
import re

def validate(doc,methods):
    
    
    
    if doc.aadhaar_number:
        crm=frappe.get_doc("CRM Settings")
        a=re.fullmatch('[0-9]{12}',doc.aadhaar_number)
        if a!=None:
            pass
            print("joyel")
        else:
            frappe.throw("Please Check Your Aadhaar Number")

        if crm.unique_aadhaar_number==1:
            
            if frappe.db.exists({"doctype":"Customer","aadhaar_number":doc.aadhaar_number}):
                existing=frappe.get_doc("Customer",{"aadhaar_number":doc.aadhaar_number})
                print(doc.name)
                if existing.name!=doc.name:
                    frappe.throw("Customer with the same aadhar number already exists")



    if doc.lead_name:
        if doc.customer_primary_address:
            ld=frappe.get_doc("Lead",doc.lead_name)
            print(ld.address_link)
            print("#####################")
            ld.address_link=doc.customer_primary_address
            ld.save()
            print(ld.address_link)
            print("###############33333")
        if doc.customer_primary_contact:
            ld=frappe.get_doc("Lead",doc.lead_name)
            print(ld.contact_link)
            ld.contact_link=doc.customer_primary_contact
            ld.save()
            print(ld.contact_link)
            print("$$$$$$$$$$$$$4")



#     # doc.opportunity_name=opp.name
#     settings=frappe.get_doc("Projects Settings")
#     if settings.template_details:
#         for tem in settings.template_details:
#             if opp.expected_start_date:
#                 (project.expected_end_date)=add_to_date((opp.expected_start_date),days=tem.duration,as_string=True)
#             for sd in opp.subsidy_detail:
#                 if not opp.project_template:

#                     if sd.scheme== tem.scheme:
#                         project.project_template=tem.select_template
#                         opp.project_template=project.project_template
#                 elif opp.project_template:
#                     project.project_template=opp.project_template
#         if settings.project_users:
#             for row in settings.project_users:
#                 print(row.full_name)
#                 print(row.user)
#                 project.append("users",{"user":row.user})
#                 project.save()
#                 opp.save()


def after_insert(doc,methods):
    
    if doc.is_installer==1:
        
        dealer=frappe.get_doc("Dealer",doc.dealer)
        dealer.customer=doc.name
        dealer.save()

        if doc.customer_primary_contact:
            contact=frappe.get_doc("Contact",doc.customer_primary_contact)
            contact.append("links",{"link_doctype":"Customer","link_name":doc.name})
            contact.save()
        
        if doc.customer_primary_address:
            address=frappe.get_doc("Address",doc.customer_primary_address)
            address.append("links",{"link_doctype":"Customer","link_name":doc.name})
            address.save()
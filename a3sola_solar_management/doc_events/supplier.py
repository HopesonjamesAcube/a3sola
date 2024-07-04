import frappe
from frappe.utils import add_to_date
import re



def after_insert(doc,methods):
    
    if doc.is_installer==1:
    
        dealer=frappe.get_doc("Dealer",doc.dealer)
        dealer.supplier=doc.name
        dealer.save()
    #link dealer account to corresponding installer account
        if doc.supplier_primary_contact:
            contact=frappe.get_doc("Contact",doc.supplier_primary_contact)
            contact.append("links",{"link_doctype":"Supplier","link_name":doc.name})
            contact.save()
    #link dealer account to corresponding installer account    
        if doc.supplier_primary_address:
            address=frappe.get_doc("Address",doc.supplier_primary_address)
            address.append("links",{"link_doctype":"Supplier","link_name":doc.name})
            address.save()



    if doc.is_oinstaller==1:
     #link supplier account to corresponding installer account
        if doc.installer:
            insta=frappe.get_doc("Installers",doc.installer)
            insta.supplier=doc.name
            insta.save()
    #add supplier in corresponding address and contact
        if doc.supplier_primary_contact:
            contact=frappe.get_doc("Contact",doc.supplier_primary_contact)
            contact.append("links",{"link_doctype":"Supplier","link_name":doc.name})
            contact.save()
        
        if doc.supplier_primary_address:
            address=frappe.get_doc("Address",doc.supplier_primary_address)
            address.append("links",{"link_doctype":"Supplier","link_name":doc.name})
            address.save()



def before_insert(doc,methods):
    pass
    
        

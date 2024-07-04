import frappe
def validate(doc,methods):
  
    if doc.links:
        for lin in doc.links:
            if lin.link_doctype=="Lead":
                print("haiiiiiiiiiiiiiiiii")
                leadexist=frappe.db.exists("Lead",lin.link_name)
                if leadexist:
                    print("Enddddddddddddddddddd")
                    lead=frappe.get_doc("Lead",lin.link_name)
                    print(lead)
                   
                    lead.address_link=doc.name
                    lead.save()
                    
           

def after_insert(doc,methods):
    
    if doc.links:
        
        for lin in doc.links:
            if lin.link_doctype=="Lead":
                leadexist=frappe.db.exists("Lead",lin.link_name)
                if leadexist:
                    print("Enddddddddddddddddddd")
                    lead=frappe.get_doc("Lead",lin.link_name)
                    print(lead)
                   
                    lead.address_link=doc.name
                    lead.save()
                    
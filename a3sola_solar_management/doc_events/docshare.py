import frappe
import re
def after_insert(doc,methods):
    

    #share sharedoc created for opportunity when it shared to corresponing user, share those sharedoc to all user to delete created docshares.
    if doc.share_doctype=='Opportunity':
        userlist=frappe.get_list("User")

        if userlist:
            for i in userlist:
                sharedoc = frappe.new_doc("DocShare")
                sharedoc.share_doctype="DocShare"
                sharedoc.share_name=doc.name

                
                sharedoc.user=i.name
                sharedoc.read=1
                sharedoc.write=1
                
                sharedoc.share=1
                sharedoc.notify=1

                sharedoc.save(ignore_permissions=True)
               

      


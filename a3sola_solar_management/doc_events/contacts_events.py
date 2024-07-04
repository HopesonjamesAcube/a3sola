import frappe
def validate(doc,methods):
    print(doc.name)

    #check whether links available in contact doctype
    if doc.links:
        # Iterate with for loop
        for lin in doc.links:
            #check link doctype is Lead
            if lin.link_doctype=="Lead":
                #Get doctype Lead
                ld=frappe.get_doc("Lead",lin.link_name)
                #check lead has lead contact
                if ld.number_to_be_contacted:
                    #Iterate with for loop
                    doc.phone_nos.clear()
                    # for c in ld.lead_contact:
                    #     #Add phone number from lead contact to default contact list
                    doc.append("phone_nos",{"phone":ld.number_to_be_contacted,"is_primary_mobile_no":1})
                # if ld.email_id:
                #     doc.email_ids.clear()
                #     doc.append("email_ids",{"email_id":ld.email_id})
                        #check whether is primary field is enabled

                            # If enabled set the number as default number
                    # ld.number_to_be_contacted=c.contact_number
                            #Set mail id as default
                    # ld.email_id=c.email_id
                            #ld.phone=c.contact_number

                #Save Lead doctype
                # ld.save()
                # if lead has email id in child table
                # if ld.email_id:
                #     #Set as default email id.
                #     doc.email_id=ld.email_id
    if doc.links:
        for lin in doc.links:
            if lin.link_doctype=="Lead":
                print("haiiiiiiiiiiiiiiiii")
                leadexist=frappe.db.exists("Lead",lin.link_name)
                if leadexist:
                    print("Enddddddddddddddddddd")
                    lead=frappe.get_doc("Lead",lin.link_name)
                    print(lead)
                    lead.contact_link=doc.name
                    lead.save()



import frappe
from frappe.utils import now,add_to_date


def validate(doc,methods):
    if doc.reference_type=="Task":
        task=frappe.get_doc("Task",doc.reference_name)
        # if task.project:
        #     project=frappe.get_doc("Project",task.project)
        #     if task.payment_dependence=='Fully Paid':
        #         if project.average_electricity_bill=='Fully Paid':
        #             pass
                
        #     elif task.payment_dependence=='Half Paid':
        #         if project.average_electricity_bill=='Half Paid' or project.average_electricity_bill=='Fully Paid':
        #             pass
            
        #     elif task.payment_dependence=='Partially Paid':
        #         if project.average_electricity_bill=='Partially Paid' or project.average_electricity_bill=='Half Paid' or project.average_electricity_bill=='Fully Paid':
        #             pass
            
        #     else:
        #         pass




    #check is refernce document is opportunity if it is update update the cc officer and ss-engineer to corresponding fields,This is for enable wati notification
    if doc.reference_type=="Opportunity":
        if doc.status=='Cancelled':
            pass
        else:
           
            opp=frappe.get_doc("Opportunity",doc.reference_name)
            #assign customer name to a field name customer
            doc.customer=opp.customer_name
            customer = frappe.get_doc("Customer", opp.customer)
            print(customer)
            if opp.district_name:
                doc.district=opp.district_name
            if opp.taluk_name:
                doc.taluk=opp.taluk_name
            if opp.contact_number:
                doc.contact_number=opp.contact_number
            # customer = frappe.get_doc('Customer',{'opportunity_name':'CRM-OPP-2022-00002'})
            
            #assign address to a field name address
            address=""
            if customer.customer_primary_address:
                print(customer.customer_primary_address)
                primaryaddress=frappe.get_doc("Address",customer.customer_primary_address)
                address=""
                address=address+str(primaryaddress.address_line1)
                if primaryaddress.address_line2:
                    address=address+","+str(primaryaddress.address_line2)
                if primaryaddress.city :
                    address=address+","+str(primaryaddress.city)
                if primaryaddress.pincode:
                    address=address+","+str(primaryaddress.pincode)
                print(address)
                doc.address=address
            if opp.items:
                for row in opp.items:
                        itm=row.item_code
                        print(itm)
                        item=frappe.get_doc("Item",row.item_code)
                        print(item)
                        doc.item=item.item_name

            if opp.converted_by:
                doc.cc_officer=opp.converted_by
            

def after_insert(doc,methods):


#update the owner of todo to corresponing lead contact by fields.
    if doc.reference_type=="Lead":
        ld=frappe.get_doc("Lead",doc.reference_name)
        print(ld)
        ld.contact_by=doc.owner
        print(ld.contact_by)
        ld.save()

        

    

#update the owner of todo to corresponing opportunity contact by fields.

    if doc.reference_type=="Opportunity":
        opp=frappe.get_doc("Opportunity",doc.reference_name)
        print(opp)
        opp.contact_by=doc.owner


        print(opp.contact_by)
        toadydate=now()

        opp.contact_date=add_to_date(toadydate, years=0, months=0, weeks=0, days=3)
        opp.send_notification=1
        crm=frappe.get_doc("CRM Settings")
        

        opp.append("opportunity_call_track",{"date_and_time":now(),"status":'Assigned',"user":frappe.session.user})


    


        
        if crm.escalation_mannager_for_lead:
            print(crm.escalation_mannager_for_lead,"#################")
            opp.escalation_manager=crm.escalation_mannager_for_lead
        

     
        
        opp.save()

#share corresponing assigned documents to users
    if doc.reference_type!="Track Incentive":
        sharedoc = frappe.new_doc("DocShare")
        sharedoc.share_doctype=doc.reference_type
        sharedoc.share_name=doc.reference_name


        
        sharedoc.user=doc.owner
        sharedoc.read=1
        sharedoc.write=1
        sharedoc.submit=0
        sharedoc.share=1
        sharedoc.notify=1

        sharedoc.save(ignore_permissions=True)
    else:
        
        sharedoc = frappe.new_doc("DocShare")
        sharedoc.share_doctype=doc.reference_type
        sharedoc.share_name=doc.reference_name

        
        sharedoc.user=doc.owner
        sharedoc.read=1
        sharedoc.write=0
        sharedoc.submit=0
        sharedoc.share=1
        sharedoc.notify=1

        sharedoc.save(ignore_permissions=True)



    # if doc.reference_type=="Project":
       
    #     user_roles = frappe.get_roles(doc.owner)
    #     if user_roles:
    #         for i in user_roles:
    #             print(i)
    #             if i=='Restricted':
    #                permission_exist=frappe.db.exists("User Permission",{"user":doc.owner,"allow":"Project"})
    #                if permission_exist:
    #                    pass
    #                else:
    #                     user_permission = frappe.new_doc("User Permission")
    #                     user_permission.user=doc.owner
    #                     user_permission.apply_to_all_doctypes=0
    #                     user_permission.allow='Project'
    #                     user_permission.for_value=doc.reference_name
    #                     user_permission.save()

    # if doc.reference_type=="Task":
    
    #     user_roles = frappe.get_roles(doc.owner)
    #     if user_roles:
    #         for i in user_roles:
    #             print(i)
    #             if i=='Restricted':
    #                 permission_exist=frappe.db.exists("User Permission",{"user":doc.owner,"allow":"Task"})
    #                 if permission_exist:
    #                     pass
    #                 else:   
    #                     user_permission = frappe.new_doc("User Permission")
    #                     user_permission.user=doc.owner
    #                     user_permission.allow='Task'
    #                     user_permission.apply_to_all_doctypes=0
    #                     user_permission.for_value=doc.reference_name
    #                     user_permission.save()


    

         

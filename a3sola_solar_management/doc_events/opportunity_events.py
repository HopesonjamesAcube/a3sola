from venv import create
import frappe
from frappe.utils import add_to_date
import random
import hashlib
import re
import requests
from frappe.utils import now
# To access the method externally from javascript

# when values of an existing document is updated,call update function with arguments(doc,val,with-items,qn) from client script.

@frappe.whitelist(allow_guest=True)
def test(doc,type):
    print("##################3")
    if type=="lead":
        ld=frappe.get_doc("Lead",doc)
        print(ld,"!!!!!!!!!!!!!!!!!!")
        add=""
        if ld.address_link:
            add=frappe.get_doc("Address",ld.address_link)
        print(add,"@@@@@@@@@@@@@")
        return add
    else:
        cu=frappe.get_doc("Customer",doc)
        print(cu,"!!!!!!!!!!!!!!!!!!")
        add=""
        if cu.customer_primary_address:
            add=frappe.get_doc("Address",cu.customer_primary_address)
        print(add,"@@@@@@@@@@@@@")
        return add


# def on_update(doc,method):
#     print(doc.send_notification,"!!!!")
#     print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     doc.send_notification=0
#     print(doc.send_notification,"!!!!")




# def validate(doc,method):
#     print(doc.send_notification)
def validate(doc,method):
    
    if doc.opportunity_call_track:
        print(doc.opportunity_call_track,"#################")
        print(len(doc.opportunity_call_track),"#################")
        #take length of lead tracking
        length=len(doc.opportunity_call_track)
        count=1
        todolist= frappe.get_list("ToDo",filters={"reference_type":'Opportunity',"reference_name":doc.name})
        if not todolist:
            doc.contact_by=None
            doc.first_name=None
            doc.mobile_number=None

        for i in doc.opportunity_call_track:
            #check count equal to the length of lead tracking
            if count==length:
                if i.status:
                    #set status of last lead tracking to current status field
                    doc.call_track_status=i.status
                    if i.status=="Reopened to Telecaller":
                        doc.follow_up="Telecaller"
                        
                            

                        todolist= frappe.get_list("ToDo",filters={"reference_type":'Opportunity',"reference_name":doc.name})
                        if todolist:
                            for i in todolist:
                                print(i)
                                print(i.name)
                                todo=frappe.get_doc("ToDo",i.name)
                                print("^^^^^^^^^^^")
                                print(todo.owner,todo.reference_name)
                                
                                share= frappe.get_list("DocShare",filters={"share_name":todo.reference_name,'user':todo.owner})
                                
                                if share:
                                    for j in share:
                                        try:
                                            sharedoc=frappe.get_doc('DocShare', j.name)
                                            print("66666666")
                                                       
                                            sharedoc.read=0
                                            sharedoc.write=0
                                            sharedoc.submit=0
                                            sharedoc.share=0
                                            sharedoc.notify=0
                                            sharedoc.save()
                                        
                                        except frappe.PermissionError:
                                            # Handle permission error gracefully
                                            frappe.msgprint(frappe._("You don't have the necessary permissions to access this resource."))
                                        
                                        
                                
                                
                                frappe.delete_doc('ToDo', i.name)

                            # if frappe.db.exists({"doctype":"ToDo","owner": doc.contact_by,"reference_type":"Opportunity","reference_name":doc.name}):
                                
                                
                            #     frappe.throw(todos.status)
                            #     todos.status='Cancelled'
                                
                            #     print("$$$$$$$$$$$$$$$$4")
                               
                            #     frappe.delete_doc('ToDo', todos.name)
                                
                            doc.contact_by=None
                            doc.first_name=None
                            doc.mobile_number=None

                        

                        
                    if i.status=="Closed by Telecaller":
                        doc.follow_up="Site Survey Engineer"
                        doc.call_track_status="Fresh Opportunity"
                    

                        doc.append("opportunity_call_track",{"date_and_time":now(),"status":'Fresh Opportunity',"user":frappe.session.user})

                    
            count=count+1
                        
            
   
    
    
            

    


def after_insert(doc,methods):

    
    doc.converted_by=doc.owner
    if doc.converted_by and doc.converted_by!="Administrator":

        if not frappe.db.exists("DocShare",{"share_doctype":"Opportunity","share_name":doc.name,"user":doc.converted_by}):
        

            sharedoc = frappe.new_doc("DocShare")
            sharedoc.share_doctype="Opportunity"
            sharedoc.share_name=doc.name
            sharedoc.user=doc.converted_by
            sharedoc.read=1
            sharedoc.write=1
            sharedoc.submit=0
            sharedoc.share=1
            sharedoc.notify=1

            sharedoc.save(ignore_permissions=True)
        user_roles = frappe.get_roles(doc.converted_by)
        # if user_roles:
        #     for i in user_roles:
        #         print(i)
        #         if i=='Restricted':
        #             permission_exist=frappe.db.exists("User Permission",{"user":doc.converted_by,"allow":"Opportunity"})
        #             if permission_exist:
        #                 pass
        #             else:
        #                 user_permission = frappe.new_doc("User Permission")
        #                 user_permission.user=doc.converted_by
        #                 user_permission.allow='Opportunity'
        #                 user_permission.for_value=doc.name
        #                 user_permission.apply_to_all_doctypes=0
        #                 user_permission.save()
    
    # create a new url
    range_start=10**(10-1)



    range_end=(10**10)-1

    ran=random.randint(range_start,range_end)

    num=doc.name+str(ran)

    result = hashlib.sha1(num.encode())

    print(result.hexdigest())

    tracking_id=result.hexdigest()

    doc.tracking_id=tracking_id
    url=frappe.utils.get_url()

    url=str(url)+"/show?id="+str(tracking_id)
    print(url,"&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    doc.url=url


    # create a shortern url using short.io api
    surl=frappe.get_doc("Shorten Url API Setting")
    if surl.enabled==1:
   

        res = requests.post('https://api.short.io/links', json={
            'domain': surl.domain,
            'originalURL': url,
        }, headers = {
            'authorization': surl.apikey,
            'content-type': 'application/json'
        }, )

        res.raise_for_status()
        data = res.json()
        print(data)
        doc.shorten_url=data['shortURL']

        print(data)


    if doc.opportunity_from=="Lead" and doc.party_name:
        # customer exist checking flag
        exist="no"
        lead= frappe.get_doc("Lead",doc.party_name)
        print(lead,"@@@@@@@@@@")
        if lead.number_to_be_contacted:
            doc.contact_number=lead.number_to_be_contacted
        if lead.aadhaar_number:
            doc.aadhaar_number=lead.aadhaar_number
        crm=frappe.get_doc("CRM Settings")

        if  crm.district_mandatory_in_lead and crm.taluk_madatory_in_leads:
            if not lead.district_name and not lead.taluk_name:
                frappe.throw("Please Fill District and Taluk")
            if not lead.district_name:
                frappe.throw("Please Fill District")
            if not lead.taluk_name:
                frappe.throw("Please Fill Taluk ")

        if crm.taluk_madatory_in_leads:
            if not lead.taluk_name:
                frappe.throw("Please Fill Taluk ")
        if crm.district_mandatory_in_lead:
            if not lead.district_name:
                frappe.throw("Please Fill District")
        
        # if lead.lead_address:
        #     for c in lead.lead_address:
        #         doc.address_list.clear()
        #         doc.append("address_list",{"address":lead.address,"address_line_1":lead.address_line1,"address_line_2":c.address_line_2,"city":c.city,"state":c.state,"country":c.country,"is_primary":c.is_primary})
        # address=""
        # if lead.address_title:
        #     address=address+lead.address_title+"\n"
        # if lead.address_line1:
        #     address=address+lead.address_line1+"\n"
        # if lead.address_line2:
        #     address=address+lead.address_line2+"\n"
        # if lead.city:
        #     address=address+"\n"+lead.city
        # if lead.state and lead.county:
        #     address=address+"\n"+lead.state+", "+lead.county
        #     print(address)
        # doc.customer_address=address
        # if lead.lead_contact:
        #     doc.contact_list.clear()
        #     for c in lead.lead_contact:
        #             doc.append("contact_list",{"contact_number":c.contact_number,"email_id":c.email_id,"is_primary":c.is_primary})

      

        if crm.unique_aadhaar_number:
            if not lead.aadhaar_number:
                frappe.throw("Please Fill Aadhaar Number")
        if crm.not_allow_opportunity_with_same_lead:
            oppoexit=frappe.db.exists({"doctype":"Opportunity","party_name":doc.party_name,"opportunity_from":"Lead"})
            if oppoexit:
                frappe.throw("Opportunity Already Exists for This Lead")


        if lead.aadhaar_number:
                if crm.unique_aadhaar_number:
            
                    if not frappe.db.exists({"doctype":"Customer","aadhaar_number":lead.aadhaar_number}):
                    #if not doc.customer:
                        customer=frappe.new_doc("Customer")
                        customer.customer_name=lead.lead_name
                        customer.customer_type="Company"
                        customer.customer_group="Commercial"
                        customer.territory="India"
                        customer.tax_category="In-State"
                        if lead.email_id:
                            customer.email_id=lead.email_id
                        if lead.number_to_be_contacted:
                            customer.mobile_no=lead.number_to_be_contacted
                        if lead.contact_link:
                            customer.customer_primary_contact=lead.contact_link
                        if lead.whatsapp_number:
                            customer.whatsapp_number=lead.whatsapp_number
                        customer.opportunity_name=doc.name
                        customer.lead_name=lead.name


                        #check if customer name already exists
                        if not frappe.db.exists({"doctype":"Customer","name":lead.lead_name}):
                            print("55444444444444444")
                            pass
                            
                        else:
                            #set exist equal to yes for while loop condition varible initialization
                            exist="yes"
                            no=1
                            name=lead.lead_name
                            dupname=name
                            while exist=="yes":
                                #name=customer name -  no
                                name=dupname+" - "+str(no)
                                print(name)
                                #check customer with new name exists or not
                                if not frappe.db.exists({"doctype":"Customer","name":name}):
                                    break
                                    
                                    
                                else:
                                    no=no+1
                                
                            customer.name=name

                        



                        print(customer.opportunity_name)
                        if doc.contact_list:
                            for con in doc.contact_list:
                                # customer.customer_primary_contact=con.contact_number
                                customer.email_id=con.email_id

                        count=1
                        if lead.aadhaar_number:
                            customer.aadhaar_number=lead.aadhaar_number
                        print(lead.address_link)
                        if lead.address_title==None and lead.address_link==None:
                            frappe.throw('Please Add Address in ' f'<a href="/app/lead/{lead.name}" target="blank">{lead.name} </a> ')
                        if count==1:
                            if lead.address_title:
                                addr=str(lead.address_title)
                                add=(addr.strip())
                                print(add+"1")

                                # addr=addr.replace(' ','')
                                s1= add+"-"+str(lead.address_type)
                                customer.customer_primary_address=(s1.strip())
                                print(customer.customer_primary_address)


                                print(customer.customer_primary_address,"6666666666666666666666666666666")

                                # customer.primary_address=add.address
                                count+=1
                            else:
                                customer.customer_primary_address=lead.address_link


                        customer.save()

                    else:
                        customer=frappe.get_doc("Customer",{"aadhaar_number":lead.aadhaar_number})
                        customer.opportunity_name=doc.name
                        customer.lead_name=lead.name
                        exist="yes"
                        customer.save()
                else:
                    customer=frappe.new_doc("Customer")
                    customer.customer_name=lead.lead_name
                    customer.customer_type="Company"
                    customer.customer_group="Commercial"
                    customer.territory="India"
                    customer.tax_category="In-State"
                    if lead.email_id:
                        customer.email_id=lead.email_id
                    if lead.number_to_be_contacted:
                        customer.mobile_no=lead.number_to_be_contacted
                    if lead.contact_link:
                        customer.customer_primary_contact=lead.contact_link
                    if lead.whatsapp_number:
                        customer.whatsapp_number=lead.whatsapp_number
                    customer.opportunity_name=doc.name
                    customer.lead_name=lead.name



                    #check if customer name already exists
                    if not frappe.db.exists({"doctype":"Customer","name":lead.lead_name}):
                        print("55444444444444444")
                        pass
                        
                    else:
                        #set exist equal to yes for while loop condition varible initialization
                        exist="yes"
                        no=1
                        name=lead.lead_name
                        dupname=name
                        while exist=="yes":
                            #name=customer name -  no
                            name=dupname+" - "+str(no)
                            print(name)
                            #check customer with new name exists or not
                            if not frappe.db.exists({"doctype":"Customer","name":name}):
                                break
                                
                                
                            else:
                                no=no+1
                            
                        customer.name=name

                    



                    print(customer.opportunity_name)
                    if doc.contact_list:
                        for con in doc.contact_list:
                            # customer.customer_primary_contact=con.contact_number
                            customer.email_id=con.email_id

                    count=1
                    if lead.aadhaar_number:
                        customer.aadhaar_number=lead.aadhaar_number
                    print(lead.address_link)
                    if lead.address_title==None and lead.address_link==None:
                        frappe.throw('Please Add Address in ' f'<a href="/app/lead/{lead.name}" target="blank">{lead.name} </a> ')
                    if count==1:
                        if lead.address_title:
                            addr=str(lead.address_title)
                            add=(addr.strip())
                            print(add+"1")

                            # addr=addr.replace(' ','')
                            s1= add+"-"+str(lead.address_type)
                            customer.customer_primary_address=(s1.strip())
                            print(customer.customer_primary_address)


                            print(customer.customer_primary_address,"6666666666666666666666666666666")

                            # customer.primary_address=add.address
                            count+=1
                        else:
                            customer.customer_primary_address=lead.address_link


                    customer.save()
            
        else:
            customer=frappe.new_doc("Customer")
            customer.customer_name=lead.lead_name
            customer.customer_type="Company"
            customer.customer_group="Commercial"
            customer.territory="India"
            customer.tax_category="In-State"
            if lead.email_id:
                customer.email_id=lead.email_id
            if lead.number_to_be_contacted:
                customer.mobile_no=lead.number_to_be_contacted
            if lead.contact_link:
                customer.customer_primary_contact=lead.contact_link
            if lead.whatsapp_number:
                customer.whatsapp_number=lead.whatsapp_number
            customer.opportunity_name=doc.name
            customer.lead_name=lead.name




            if not frappe.db.exists({"doctype":"Customer","name":lead.lead_name}):
                print("55444444444444444")
                pass
                
            else:
                
                exist="yes"
                no=1
                name=lead.lead_name
                dupname=name
                while exist=="yes":
                    name=dupname+" - "+str(no)
                    print(name)
                    if not frappe.db.exists({"doctype":"Customer","name":name}):
                        break
                        
                        
                    else:
                        no=no+1
                    
                customer.name=name
                        



            print(customer.opportunity_name)
            if doc.contact_list:
                for con in doc.contact_list:
                    # customer.customer_primary_contact=con.contact_number
                    customer.email_id=con.email_id

            count=1
            if lead.aadhaar_number:
                customer.aadhaar_number=lead.aadhaar_number
            print(lead.address_link)
            if lead.address_title==None and lead.address_link==None:
                frappe.throw('Please Add Address in ' f'<a href="/app/lead/{lead.name}" target="blank">{lead.name} </a> ')
            if count==1:
                if lead.address_title:
                    addr=str(lead.address_title)
                    add=(addr.strip())
                    print(add+"1")

                    # addr=addr.replace(' ','')
                    s1= add+"-"+str(lead.address_type)
                    customer.customer_primary_address=(s1.strip())
                    print(customer.customer_primary_address)


                    print(customer.customer_primary_address,"6666666666666666666666666666666")

                    # customer.primary_address=add.address
                    count+=1
                else:
                    customer.customer_primary_address=lead.address_link


            customer.save()



        
        doc.customer_address=customer.customer_primary_address
        doc.customer=customer.name
        
        if customer.customer_primary_contact:
            doc.contact_person=customer.customer_primary_contact
        # frappe.throw(customer.name)

        # doc.scheme_name="SOURA"
        # print(doc.scheme_name)
        # doc.board_name="KSEB"
        if doc.items:
            for row in doc.items:
                item=frappe.get_doc("Item",row.item_code)
                print(item)
                if item.scheme_name:
                    scheme=frappe.get_doc("Scheme",item.scheme_name)
                    print(scheme)
                    doc.scheme_name=item.scheme_name
                    lead.scheme_name=item.scheme_name
                    print(doc.scheme_name)
                    if scheme.provided_by:
                        doc.board_name=scheme.provided_by
                    if scheme.subsidy_percentage:
                        doc.subsidy_percentage=scheme.subsidy_percentage
                    if scheme.category:
                        doc.category=scheme.category
            
            if exist=="no":
                frappe.msgprint('Customer ' f'<a href="/app/customer/{customer.name}" target="blank">{customer.name} </a> Created Successfully ')
            else:
                frappe.msgprint('Opportunity Created against ' f'<a href="/app/customer/{customer.name}" target="blank">{customer.name} </a> Successfully')
        doc.save()

    else:
        
        if doc.opportunity_from=="Customer" and doc.party_name:
             customer=frappe.get_doc("Customer",doc.party_name)
             customer.opportunity_name=doc.name
             customer.save()
             doc.customer_address=customer.customer_primary_address
             doc.customer=customer.name
             # frappe.throw(customer.name)

             # doc.scheme_name="SOURA"
             # print(doc.scheme_name)
             # doc.board_name="KSEB"
             if doc.items:
                 for row in doc.items:
                     item=frappe.get_doc("Item",row.item_code)
                     print(item)
                     if item.scheme_name:
                         scheme=frappe.get_doc("Scheme",item.scheme_name)
                         print(scheme)
                         doc.scheme_name=item.scheme_name

                         print(doc.scheme_name)
                         if scheme.provided_by:
                             doc.board_name=scheme.provided_by
                         if scheme.subsidy_percentage:
                             doc.subsidy_percentage=scheme.subsidy_percentage
                         if scheme.category:
                             doc.category=scheme.category
                 doc.save()
             frappe.msgprint('Opportunity Created against ' f'<a href="/app/customer/{customer.name}" target="blank">{customer.name} </a> Successfully')



   



def before_insert(doc,methods):
    if doc.opportunity_from=="Lead" and doc.party_name:
       
        lead= frappe.get_doc("Lead",doc.party_name)
        print(lead,"@@@@@@@@@@")
        if lead.number_to_be_contacted:
            doc.contact_number=lead.number_to_be_contacted
        if lead.aadhaar_number:
            doc.aadhaar_number=lead.aadhaar_number

       

        if lead.whatsapp_number:
            doc.whatsapp_number=lead.whatsapp_number
        if lead.consumer_number:
            doc.consumer_number=lead.consumer_number
    
        if lead.district_name:
            doc.district_name=lead.district_name
        if lead.taluk_name:
            doc.taluk_name=lead.taluk_name

        if lead.ld_source:
            doc.source=lead.ld_source


        

    print("before insertttttttttttttttttttttttttttttt")
    tp=''
    template_id=''
    smst=frappe.get_doc("SMS Template General")
    if smst:
        if smst.template_parameter:
            tp=smst.template_parameter
        if smst.sms_template:
            for i in smst.sms_template:
                if i.document=='Opportunity':
                    template_id=i.template_id


    if tp and template_id:
        
        sms=frappe.get_doc("SMS Settings")
        if sms:
            for i in sms.parameters:
                print(i)
                print(i.parameter)
                if i.parameter==tp:
                    i.value=template_id      
            sms.save()

    #     customer=frappe.get_doc("Customer")
    #     customer.customer_name=lead.lead_name
    #     customer.customer_type="Company"
    #     customer.customer_group="Commercial"
    #     customer.territory="India"
    #     if lead.email_id:
    #         customer.email_id=lead.email_id
    #     if lead.number_to_be_contacted:
    #         customer.mobile_no=lead.number_to_be_contacted
    #         customer.customer_primary_contact=lead.number_to_be_contacted

    #     customer.opportunity_name=doc.name
    #     customer.lead_name=lead.name
    #     if not doc.customer:
    #         doc.customer=customer.customer_name
    #     print(customer.opportunity_name)
    #     if doc.contact_list:
    #         for con in doc.contact_list:
    #             customer.customer_primary_contact=con.contact_number
    #             customer.email_id=con.email_id
    #     customer.mobile_no=customer.customer_primary_contact
    #     count=1
    #     if lead.aadhaar_number:
    #         customer.aadhaar_number=lead.aadhaar_number
    #     print(lead.address_link)
    #     if lead.address_title==None and lead.address_link==None:
    #         frappe.throw('Please Add Address in ' f'<a href="/app/lead/{lead.name}" target="blank">{lead.name} </a> ')
    #     if count==1:
    #         if lead.address_title:
    #             addr=str(lead.address_title)
    #             add=(addr.strip())
    #             print(add+"1")

    #             # addr=addr.replace(' ','')
    #             s1= add+"-"+str(lead.address_type)
    #             customer.customer_primary_address=(s1.strip())
    #             print(customer.customer_primary_address)


    #             print(customer.customer_primary_address,"6666666666666666666666666666666")

    #             # customer.primary_address=add.address
    #             count+=1
    #         else:
    #             customer.customer_primary_address=lead.address_link

    #     customer.save()

    #     doc.customer_address=customer.customer_primary_address
    #     doc.customer=customer.customer_name
    #     # doc.scheme_name="SOURA"
    #     # print(doc.scheme_name)
    #     # doc.board_name="KSEB"
    #     if doc.items:
    #         for row in doc.items:
    #             item=frappe.get_doc("Item",row.item_code)
    #             print(item)
    #             if item.scheme_name:
    #                 scheme=frappe.get_doc("Scheme",item.scheme_name)
    #                 print(scheme)
    #                 doc.scheme_name=item.scheme_name
    #                 lead.scheme_name=item.scheme_name
    #                 print(doc.scheme_name)
    #                 if scheme.provided_by:
    #                     doc.board_name=scheme.provided_by
    #                 if scheme.subsidy_percentage:
    #                     doc.subsidy_percentage=scheme.subsidy_percentage
    #                 if scheme.category:
    #                     doc.category=scheme.category
    #         doc.save()
    #         frappe.msgprint('Customer ' f'<a href="/app/customer/{customer.name}" target="blank">{customer.name} </a> Updated Successfully ')
    # # if doc.create_project==1:

        # if not doc.project_name:
        #     if not frappe.db.exists("Project",doc.party_name):
        #         if doc.items:
        #             for row in doc.items:
        #                 item=frappe.get_doc("Item",row.item_code)
        #                 if item.scheme_name:
        #                     scheme=frappe.get_doc("Scheme",item.scheme_name)
        #                     doc.scheme_name=item.scheme_name
        #                     doc.board_name=scheme.provided_by
        #                     if doc.scheme_name==item.scheme_name:
        #                         if scheme.project_template:
        #                             doc.project_template=scheme.project_template
        #                     else:
        #                         frappe.throw("Item does not match Scheme!!")

    #             lead= frappe.get_doc("Lead",doc.party_name)
    #             last=frappe.get_last_doc('Project')
    #             if last:
    #                 projectname=last.project_name
    #                 splited=projectname.split('-')
    #                 number=splited[1]
    #                 nextid=int(number)+1
    #                 print("+++++++++++++++++++")
    #                 print(nextid)
    #             else:
    #                 nextid="1000"
    #             project=frappe.new_doc("Project")
    #             project.consumer_number=doc.consumer_number
    #             print(doc.name)

    #             project.project_name=lead.lead_name+"-"+str(nextid)
    #             print(project.project_name)
    #             project.project_type="Internal"
    #             project.email=lead.email_id

    #             project.oppertunity=doc.name

    #             if lead.lead_address:
    #                 for c in lead.lead_address:
    #                     project.append("address_list",{"address":c.address,"address_line_1":c.address_line_1,"address_line_2":c.address_line_2,"city":c.city,"state":c.state,"country":c.country,"is_primary":c.is_primary})
    #             if lead.lead_contact:
    #                 for c in lead.lead_contact:
    #                     project.append("contact_list",{"contact_number":c.contact_number,"email_id":c.email_id,"is_primary":c.is_primary})
    #             if doc.expected_start_date:
    #                 project.expected_start_date=doc.expected_start_date
    #             project.customer=doc.customer
    #             settings=frappe.get_doc("Project Settings")
    #             if settings.template_details:
    #                 for tem in settings.template_details:
    #                     if doc.expected_start_date:
    #                         (project.expected_end_date)=add_to_date((doc.expected_start_date),days=tem.duration,as_string=True)
    #                     if not doc.project_template:
    #                         if doc.scheme_name== tem.scheme:
    #                             print(tem.scheme)
    #                             doc.project_template=tem.select_template
    #                             project.project_template=doc.project_template
    #                     elif doc.project_template:
    #                             project.project_template=doc.project_template
    #                 if settings.project_users:
    #                     for row in settings.project_users:
    #                         print(row.full_name)
    #                         print(row.user)
    #                         project.append("users",{"user":row.user})
    #             project.aadhaar_number=doc.aadhaar_number
    #             project.scheme_name=doc.scheme_name
    #             project.board_name=doc.board_name

    #             project.contact_number=doc.contact_number
    #             customer=frappe.get_doc("Customer",doc.customer)
    #             print(doc.customer)
    #             print(customer)
    #             if customer.customer_primary_address:
    #                 primaryaddress=frappe.get_doc("Address",customer.customer_primary_address )
    #                 address=""
    #                 address=address+primaryaddress.address_line1+"\n"
    #                 print(address)
    #                 if primaryaddress.address_line2:
    #                     address=address+primaryaddress.address_line2+"\n"
    #                 if primaryaddress.city:
    #                     address=address+"\n"+primaryaddress.city
    #                     print(address)
    #                 if primaryaddress.state and primaryaddress.county:
    #                     address=address+"\n"+primaryaddress.state+", "+primaryaddress.county
    #                     print(address)
    #                 project.primary_address=address
    #             project.insert()

    #             doc.project_name=project.project_name
    #             doc.project_id=project.name


    #             print(doc.name)
    #         # project.save()
    #         doc.save()

    #         frappe.msgprint('Project ' f'<a href="/app/project/{project.name}" target="blank">{project.name} </a> Created Successfully ')

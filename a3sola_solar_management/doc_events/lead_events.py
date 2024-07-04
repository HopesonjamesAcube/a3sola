
import email
import frappe
import re
import math
import googlemaps
from datetime import datetime
import frappe

# To access the method externally from javascript



 


@frappe.whitelist(allow_guest=True)
# when values of an existing document is updated,call update function with arguments(doc,val,with-items,qn) from client script.
def on_update(doc,val,with_items,qn):
    # Check whether opportunity created with current lead name.
    if not frappe.db.exists({"Opportunity",doc}):
        # Returns lead document
        ld=frappe.get_doc("Lead",doc)
        # frappe.throw("vallllll")
        if ld.emi_customer==1:
            if frappe.db.exists("Bank Loan Application",{"lead":ld.name}):
                bank_loan_provider=frappe.get_doc("Bank Loan Application",{"lead":ld.name})
                if bank_loan_provider.status=="Approved":
                    #Create new opportunity
                    opp = frappe.new_doc("Opportunity")
                    # Set the value opportunity_from to "Lead"
                    opp.opportunity_from = "Lead"
                    #Update lead field in opportunity with name of current lead.
                    opp.lead = ld.name
                    # Update contact_person field in opportunity with lead name.
                    opp.contact_person=ld.contact_link
                    #Update email id and party_name
                    opp.contact_email=ld.email_id
                    opp.taluk=ld.taluk
                    opp.district=ld.district
                    opp.source=ld.ld_source
                    opp.taluk_name=ld.taluk_name
                    opp.district_name=ld.district_name

                    # address=""
                    # if ld.address_title:
                    #     address=address+ld.address_title+"\n"
                    # if ld.address_line1:
                    #     address=address+ld.address_line1+"\n"
                    # if ld.address_line2:
                    #     address=address+ld.address_line2+"\n"
                    # if ld.city:
                    #     address=address+"\n"+ld.city
                    # if ld.state and ld.county:
                    #     address=address+"\n"+ld.state+", "+ld.county
                    #     print(address)
                    # address=address+ld.address_title+"\n"+ld.address_line1+"\n"+ld.address_line2+"\n"+ld.city

                    item=frappe.get_doc("Item",val)

                    if item.scheme_name:
                        scheme=frappe.get_doc("Scheme",item.scheme_name)
                        print(scheme)

                    if item.scheme_name:
                        ld.scheme_name=item.scheme_name

                        if scheme.provided_by:
                            ld.board_name=scheme.provided_by
                        if scheme.subsidy_percentage:
                            ld.subsidy_percent=scheme.subsidy_percentage
                        if scheme.category:
                            ld.category=scheme.category

                    ld.current_status="Opportunity"
                    ld.save()


                    if ld.category:
                        opp.category=ld.category

                    if ld.address_title:
                            opp.append("address_list",{"address":ld.address_title,"address_line_1":ld.address_line1,"address_line_2":ld.address_line2,"city":ld.city,"state":ld.state,"country":ld.country})

                    elif ld.address_link:
                        addr= frappe.get_doc("Address",ld.address_link)
                        print(addr)
                        opp.append("address_list",{"address":addr.address_title,"address_line_1":addr.address_line1,"address_line_2":addr.address_line2,"city":addr.city,"state":addr.state,"country":addr.country})
                        print("he")

                    if ld.number_to_be_contacted:
                        if ld.email_id:

                            opp.append("contact_list",{"contact_number":ld.number_to_be_contacted,"email_id":ld.email_id})
                    

                    opp.party_name=ld.name
                    opp.from_lead=1
                    if ld.whatsapp_number:
                        opp.whatsapp_number=ld.whatsapp_number
                    #Set the with_items field in opportunity to 1
                    opp.with_items=int(with_items)
                    #qn=1
                    #Check whether with_items field is checked
                    if opp.with_items==1:
                    #print(val["Item"])
                    # Fetch items from dialog box variable in client script and add to child table
                        opp.append("items",{"item_code":val,"qty":qn})
                        if frappe.db.exists("SunPower Kit",{"new_item_code":val}):
                            
                            sp_kit=frappe.get_doc("SunPower Kit",{"new_item_code":val})
                            for i in sp_kit.items:
                                opp.append("items",{"item_code":i.item_code,"qty":i.qty})





                    # item=frappe.get_doc("Item",val)
                    # print(item,"212423563")
                    # if item.scheme_name:
                    #     scheme=frappe.get_doc("Scheme",item.scheme_name)
                    #     print(scheme)
                    #     opp.scheme_name=item.scheme_name
                    #     print(opp.scheme_name)
                    #     opp.board_name=scheme.provided_by
                    #  Insert all fields before saving.
                    opp.insert()

                    frappe.msgprint('Opportunity ' f'<a href="/app/opportunity/{opp.name}" target="blank">{opp.name} </a> Created Successfully ')
                else:
                    frappe.throw("Bank Loan Application Submitted is not Approved")
        else:
            opp = frappe.new_doc("Opportunity")
            # Set the value opportunity_from to "Lead"
            opp.opportunity_from = "Lead"
            #Update lead field in opportunity with name of current lead.
            opp.lead = ld.name
            # Update contact_person field in opportunity with lead name.
            opp.contact_person=ld.contact_link
            #Update email id and party_name
            opp.contact_email=ld.email_id
            opp.taluk=ld.taluk
            opp.district=ld.district
            opp.source=ld.ld_source
            opp.taluk_name=ld.taluk_name
            opp.district_name=ld.district_name

            # address=""
            # if ld.address_title:
            #     address=address+ld.address_title+"\n"
            # if ld.address_line1:
            #     address=address+ld.address_line1+"\n"
            # if ld.address_line2:
            #     address=address+ld.address_line2+"\n"
            # if ld.city:
            #     address=address+"\n"+ld.city
            # if ld.state and ld.county:
            #     address=address+"\n"+ld.state+", "+ld.county
            #     print(address)
            # address=address+ld.address_title+"\n"+ld.address_line1+"\n"+ld.address_line2+"\n"+ld.city

            item=frappe.get_doc("Item",val)

            if item.scheme_name:
                scheme=frappe.get_doc("Scheme",item.scheme_name)
                print(scheme)

            if item.scheme_name:
                ld.scheme_name=item.scheme_name

                if scheme.provided_by:
                    ld.board_name=scheme.provided_by
                if scheme.subsidy_percentage:
                    ld.subsidy_percent=scheme.subsidy_percentage
                if scheme.category:
                    ld.category=scheme.category

            ld.current_status="Opportunity"
            ld.save()


            if ld.category:
                opp.category=ld.category

            if ld.address_title:
                    opp.append("address_list",{"address":ld.address_title,"address_line_1":ld.address_line1,"address_line_2":ld.address_line2,"city":ld.city,"state":ld.state,"country":ld.country})

            elif ld.address_link:
                addr= frappe.get_doc("Address",ld.address_link)
                print(addr)
                opp.append("address_list",{"address":addr.address_title,"address_line_1":addr.address_line1,"address_line_2":addr.address_line2,"city":addr.city,"state":addr.state,"country":addr.country})
                print("he")

            if ld.number_to_be_contacted:
                if ld.email_id:

                    opp.append("contact_list",{"contact_number":ld.number_to_be_contacted,"email_id":ld.email_id})
            

            opp.party_name=ld.name
            opp.from_lead=1
            if ld.whatsapp_number:
                opp.whatsapp_number=ld.whatsapp_number
            #Set the with_items field in opportunity to 1
            opp.with_items=int(with_items)
            #qn=1
            #Check whether with_items field is checked
            if opp.with_items==1:
            #print(val["Item"])
            # Fetch items from dialog box variable in client script and add to child table
                opp.append("items",{"item_code":val,"qty":qn})
                if frappe.db.exists("SunPower Kit",{"new_item_code":val}):
                    
                    sp_kit=frappe.get_doc("SunPower Kit",{"new_item_code":val})
                    for i in sp_kit.items:
                        opp.append("items",{"item_code":i.item_code,"qty":i.qty})





            # item=frappe.get_doc("Item",val)
            # print(item,"212423563")
            # if item.scheme_name:
            #     scheme=frappe.get_doc("Scheme",item.scheme_name)
            #     print(scheme)
            #     opp.scheme_name=item.scheme_name
            #     print(opp.scheme_name)
            #     opp.board_name=scheme.provided_by
            #  Insert all fields before saving.
            opp.insert()

            frappe.msgprint('Opportunity ' f'<a href="/app/opportunity/{opp.name}" target="blank">{opp.name} </a> Created Successfully ')
            

    else:
        pass

def validate(doc, methods):
   
                
   
    # if not doc.email_id and not doc.number_to_be_contacted  and not doc.aadhaar_number:
    #     frappe.throw("Please Enter Your Email ID,Mobile Number and Aadhaar Number ")

    # crm= frappe.get_doc("CRM Settings")
    # frappe.msgprint(crm.aml)
    # frappe.throw("y")

    # userlist=frappe.get_list("User")
    # if userlist:
    #     for i in userlist:
    #         user=frappe.get_doc("User",i)
    #         if user.name=="tele@gmail.com":
    #             user_roles = frappe.get_roles(user.name)
    #             if user_roles:
    #                 for i in user_roles:
    #                     print(i)
    #                     if i=="Guest":
    #                         print("yes")
                            
    #                         user.remove_roles("Guest")
    #                         user.save()


                
    print("*******")
    print(doc.contact_by,"*********")
    if doc.lead_tracking:
        print(doc.lead_tracking,"#################")
        print(len(doc.lead_tracking),"#################")
        #take length of lead tracking
        length=len(doc.lead_tracking)
        count=1
        for i in doc.lead_tracking:
            #check count equal to the length of lead tracking
            if count==length:
                if i.status:
                    #set status of last lead tracking to current status field
                    doc.current_status=i.status
            count=count+1
           




    crm=frappe.get_doc("CRM Settings")

    
    #check different validation based on conditions defined on crm setting 

    if crm.notify_escalation_manager==1:
        if crm.escalation_mannager_for_lead:
            print(crm.escalation_mannager_for_lead,"#################")
            doc.escalation_manager=crm.escalation_mannager_for_lead
            doc.enot=1
    else:
        doc.enot=0
    if crm.send_customer_notiication==1:
        doc.cnot=1
    else:
        doc.cnot=0

    print("ray")
    print(crm.aml)

    if crm.consumer_number_mandatory==1:
        if not doc.consumer_number:
            frappe.throw("Please Fill Consumer Number ")
    
    if crm.aml==1:
        if not doc.aadhaar_number:
            frappe.throw("Please Fill Aadhaar Number ")

    if  doc.email_id:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, doc.email_id)):
            pass
        else:
            frappe.throw("Please Check Your Email ID")

    if crm.contact_number_validation==1:
        if doc.number_to_be_contacted:
            r=re.fullmatch('[6-9][0-9]{9}',doc.number_to_be_contacted)
            if r!=None:
                pass

            else:
                frappe.throw("Please Check Your Mobile Number ")
    if doc.consumer_number:
        if not crm.skip_consumer_number_validation:
            c=re.fullmatch('[0-9]{13}',doc.consumer_number)
            if c!=None:
                pass
            else:
                frappe.throw("Please Check Your Consumer Number")
    if doc.aadhaar_number:
        a=re.fullmatch('[0-9]{12}',doc.aadhaar_number)
        if a!=None:
            pass
        else:
            frappe.throw("Please Check Your Aadhaar Number")


  #check phone number or mobile need to mandatory for lead
    if crm.cno_or_mob_man==1:
        if doc.number_to_be_contacted or doc.email_id:
            pass
        else:
            frappe.throw("Please add Contact number Or Email")

            

   
             
    #lead count check for send system notification
    # if doc.contact_by:
    #     total=frappe.db.count("Lead",filters={"contact_by":doc.contact_by})
    #     converted=frappe.db.count("Lead",filters={"contact_by":doc.contact_by,"status":"Converted"})
    #     notinterested=frappe.db.count("Lead",filters={"contact_by":doc.contact_by,"current_status":"Not Interested"})
    #     rejected=frappe.db.count("Lead",filters={"contact_by":doc.contact_by,"current_status":"Rejected"})
    #     invalid=frappe.db.count("Lead",filters={"contact_by":doc.contact_by,"current_status":"Invalid Number"})
    #     print(converted,"converted")
    #     print(notinterested,"notinterested")
    #     print(rejected,"rejected")
    #     print(invalid,"invalid")

    #     balence=total-(notinterested+rejected+invalid)
    #     balence=balence-converted
    #     print(balence,"balence")
    #     if balence<50:
    #         doc.lownot=1

    




@frappe.whitelist(allow_guest=True)
def aftersavefetch(ld):
    
 
    ld=frappe.get_doc("Lead",ld)


    if ld.emi_customer:
         crm=frappe.get_doc("CRM Settings")
         if crm.emi_follow_up_user:

            
            if not frappe.db.exists({"doctype":"ToDo","owner": crm.emi_follow_up_user,"reference_type":"Lead","reference_name":ld.name}):
                ld.follow_up_user=crm.emi_follow_up_user
                todo = frappe.new_doc("ToDo")
                todo.owner = crm.emi_follow_up_user
                todo.description = "Lead Assignment"
                todo.reference_type = "Lead"
                todo.reference_name = ld.name
                todo.assigned_by = frappe.session.user
                todo.save()
                
            

    else:
        crm=frappe.get_doc("CRM Settings")
        if crm.default_follow_up_user:
             if not frappe.db.exists({"doctype":"ToDo","owner": crm.default_follow_up_user,"reference_type":"Lead","reference_name":ld.name}):
                ld.follow_up_user=crm.default_follow_up_user
                todo = frappe.new_doc("ToDo")
                todo.owner = crm.default_follow_up_user
                todo.description = "Lead Assignment"
                todo.reference_type = "Lead"
                todo.reference_name = ld.name
                todo.assigned_by = frappe.session.user
                todo.save()


def before_insert(doc,methods):
    tp=''
    template_id=''
    crm=frappe.get_doc("CRM Settings")

    if crm.not_allow_lead_with_same_contact_numebr:
        if doc.number_to_be_contacted:
            if frappe.db.exists("Lead",{"number_to_be_contacted":doc.number_to_be_contacted}):
                lead=frappe.get_doc("Lead",{"number_to_be_contacted":doc.number_to_be_contacted})
                frappe.throw("Lead with this Mobile Number Already Exists " f'<a href="/app/lead/{lead.name}" target="blank">{lead.name} </a> ')

    smst=frappe.get_doc("SMS Template General")
    if smst:
        if smst.template_parameter:
            tp=smst.template_parameter
        if smst.sms_template:
            for i in smst.sms_template:
                if i.document=='Lead':
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
    distance=0
    if doc.attendance:
        # Check if a "Sales Person Travel" document exists for the current user and date
        if frappe.db.exists("Lead",{"attendance":doc.attendance}):
            lead_data=frappe.get_doc("Lead",{"attendance":doc.attendance})
            location_settings=frappe.get_doc("Location API Settings")
            if location_settings:
                if location_settings.distance_api_enabled:
                    if location_settings.distance_api_enabled==1:

                        if lead_data.latitude and lead_data.longitude and doc.latitude and doc.longitude:
                            def get_road_distance(origin, destination):
                                try:
                                    # Replace 'YOUR_API_KEY' with your actual Google Maps API key.
                                    gmaps = googlemaps.Client(key='AIzaSyDo1hN9bX-BmMJqKQcsjsQzVz8t8bDmgWk')

                                    # Request directions from the Google Maps Directions API.
                                    directions = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())

                                    if directions:
                                        # Extract and return the distance in meters.
                                        distance = directions[0]['legs'][0]['distance']['value']
                                        return distance
                                    else:
                                        return None
                                except Exception as e:
                                    frappe.msgprint(f"Error: {e}")
                                    return None                
                            origin_coordinates = str(lead_data.latitude)+","+str(lead_data.longitude) # Latitude and longitude of the origin
                            destination_coordinates = str(doc.latitude)+","+str(doc.longitude)  # Latitude and longitude of the destination
                            print(lead_data.latitude,lead_data.longitude,doc.longitude,doc.latitude,"88888888888")
                            # Call the function to calculate the road distance.
                            distance = get_road_distance(origin_coordinates, destination_coordinates)
                            # print(distance)
                            if distance:
                                distance=distance/1000
                                print(distance)
                            if frappe.db.exists("Sales Person Travel",{"date": doc.date, "user": frappe.session.user}):
                                sales_travel = frappe.get_doc("Sales Person Travel",{"date": doc.date, "user": frappe.session.user})
                                sales_travel.total_noof_travel +=1
                                if distance or distance==0:
                                    sales_travel.append("travel_itinerarys", {"travel_from": lead_data.place if lead_data.place else None, "travel_to": doc.place if doc.place else None,"distance":distance})
                                sales_travel.save()
        else:
            location_settings=frappe.get_doc("Location API Settings")
            if location_settings:
                if location_settings.distance_api_enabled:
                    if location_settings.distance_api_enabled==1:
                        if frappe.db.exists("Attendance",{"name":doc.attendance}):
                            attendance_data=frappe.get_doc("Attendance",{"name":doc.attendance})
                            print(attendance_data.name)
                            print(attendance_data.latitude,attendance_data.longitude,doc.latitude,doc.longitude,"00000000000000")
                            if attendance_data.latitude and attendance_data.longitude and doc.latitude and doc.longitude:
                                def get_road_distance(origin, destination):
                                    try:
                                        # Replace 'YOUR_API_KEY' with your actual Google Maps API key.
                                        gmaps = googlemaps.Client(key='AIzaSyDo1hN9bX-BmMJqKQcsjsQzVz8t8bDmgWk')

                                        # Request directions from the Google Maps Directions API.
                                        directions = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())

                                        if directions:
                                            # Extract and return the distance in meters.
                                            distance = directions[0]['legs'][0]['distance']['value']
                                            return distance
                                        else:
                                            return None
                                    except Exception as e:
                                        frappe.msgprint(f"Error: {e}")
                                        return None                
                                origin_coordinates = str(attendance_data.latitude)+","+str(attendance_data.longitude) # Latitude and longitude of the origin
                                destination_coordinates = str(doc.latitude)+","+str(doc.longitude)  # Latitude and longitude of the destination
                                # Call the function to calculate the road distance.
                                distance = get_road_distance(origin_coordinates, destination_coordinates)
                                # print(type(distance),distance,"--------------")
                                # frappe.throw("----------------")
                                if distance:
                                    distance=distance/1000
                                    print(distance,"dist")
                                if not frappe.db.exists("Sales Person Travel",{"date": doc.date, "user": frappe.session.user}):
                                    new_sales_travel = frappe.new_doc("Sales Person Travel")
                                    new_sales_travel.date = doc.date
                                    new_sales_travel.user = frappe.session.user
                                    if frappe.db.exists("Employee",{"user_id":frappe.session.user}):
                                        employee=frappe.get_doc("Employee",{"user_id":frappe.session.user})
                                        if employee.name:
                                            new_sales_travel.employee_id=employee.name
                                    new_sales_travel.status = "Pending"
                                    new_sales_travel.total_noof_travel = 1
                                    print(new_sales_travel.date,new_sales_travel.user,new_sales_travel.status,new_sales_travel.total_noof_travel,"6666666666")
                                    
                                    if distance or distance==0:
                                        new_sales_travel.append("travel_itinerarys", {"travel_from": attendance_data.city if attendance_data.city else None, "travel_to": doc.place if doc.place else None,"distance":distance})
                                    else:
                                        new_sales_travel.append("travel_itinerarys", {"travel_from": attendance_data.city if attendance_data.city else None, "travel_to": doc.place if doc.place else None})
                                    new_sales_travel.save()
                                    frappe.msgprint("Sales Person Travel Recorded Succesfully")          

def after_insert(doc,methods):   
    if doc.emi_customer:
         crm=frappe.get_doc("CRM Settings")
         if crm.emi_follow_up_user:

            
            if not frappe.db.exists({"doctype":"ToDo","owner": crm.emi_follow_up_user,"reference_type":"Lead","reference_name":doc.name}):
                doc.follow_up_user=crm.emi_follow_up_user
                todo = frappe.new_doc("ToDo")
                todo.owner = crm.emi_follow_up_user
                todo.description = "Lead Assignment"
                todo.reference_type = "Lead"
                todo.reference_name = doc.name
                todo.assigned_by = frappe.session.user
                todo.save()       

    else:
        crm=frappe.get_doc("CRM Settings")
        if crm.default_follow_up_user:
             if not frappe.db.exists({"doctype":"ToDo","owner": crm.default_follow_up_user,"reference_type":"Lead","reference_name":doc.name}):
                doc.follow_up_user=crm.default_follow_up_user
                todo = frappe.new_doc("ToDo")
                todo.owner = crm.default_follow_up_user
                todo.description = "Lead Assignment"
                todo.reference_type = "Lead"
                todo.reference_name = doc.name
                todo.assigned_by = frappe.session.user
                todo.save()
             

    
   

# def before_insert(doc,methods):
#     tp=''
#     template_id=''
#     crm=frappe.get_doc("CRM Settings")

#     if crm.not_allow_lead_with_same_contact_numebr:
#         if doc.number_to_be_contacted:
#             if frappe.db.exists("Lead",{"number_to_be_contacted":doc.number_to_be_contacted}):
#                 lead=frappe.get_doc("Lead",{"number_to_be_contacted":doc.number_to_be_contacted})
#                 frappe.throw("Lead with this Mobile Number Already Exists " f'<a href="/app/lead/{lead.name}" target="blank">{lead.name} </a> ')

#     smst=frappe.get_doc("SMS Template General")
#     if smst:
#         if smst.template_parameter:
#             tp=smst.template_parameter
#         if smst.sms_template:
#             for i in smst.sms_template:
#                 if i.document=='Lead':
#                     template_id=i.template_id


#     if tp and template_id:
        
#         sms=frappe.get_doc("SMS Settings")
#         if sms:
#             for i in sms.parameters:
#                 print(i)
#                 print(i.parameter)
#                 if i.parameter==tp:
#                     i.value=template_id      
#             sms.save()
   

    


def cron():


    tellecaller=[]
    userlist=frappe.get_list("User")
    if userlist:
        for i in userlist:
            user=frappe.get_doc("User",i)
            user_roles = frappe.get_roles(user.name)
            if user_roles:
                for i in user_roles:
                    print(i)
                    if i=='Telecaller':
                        tellecaller=tellecaller+[user.name]
    print(tellecaller)



    if tellecaller:
        for i in tellecaller:
            print(i)
            total=frappe.db.count("Lead",filters={"contact_by":i})
            # converted=frappe.db.count("Lead",filters={"contact_by":i,"status":"Converted"})
            # notinterested=frappe.db.count("Lead",filters={"contact_by":i,"current_status":"Not Interested"})
            # rejected=frappe.db.count("Lead",filters={"contact_by":i,"current_status":"Rejected"})
            # invalid=frappe.db.count("Lead",filters={"contact_by":i,"current_status":"Invalid Number"})
            # print(total)
            # print(converted,"converted")
            # print(notinterested,"notinterested")
            # print(rejected,"rejected")
            # print(invalid,"invalid")

            # balence=total-(notinterested+rejected+invalid)
            # balence=balence-converted
            # print(balence,"balence")
            fresh=frappe.db.count("Lead",filters={"contact_by":i,"status":"Fresh Lead"})

            if fresh<50 and total>0:
                lead=frappe.get_doc("Lead",{"contact_by":i})

                lead.lownot=1
                lead.save()



@frappe.whitelist()
def get_attendance(user,date):
    print(user)
    data = {}
    if frappe.session.user != "Administrator":
        if frappe.db.exists("Lead",{"date":date,"lead_owner":user}):
            lead = frappe.get_last_doc("Lead",{"date":date,"lead_owner":user})
            data["ld"] = lead.name
        # Check if an Employee record exists for the current user
        if frappe.db.exists("Employee", {"user_id": user}):
            emp = frappe.get_doc("Employee", {"user_id": user})

            # Define a list of status options to check
            status_options = ["Present", "Half Day", "Work From Home"]
            attendance_query = {
                "attendance_date": date,
                "employee_name": emp.employee_name,
                "status": ["in", status_options]
            }
            
            
            attendance_records = frappe.get_all("Attendance", filters=attendance_query)
            
            if attendance_records:
                # Select the first available attendance record
                att = frappe.get_doc("Attendance", attendance_records[0])
                print(att.name, "!!!!!!!!!!")
                data["att"] = att.name
            if frappe.db.exists("Location API Settings"):
               location_settings_val=frappe.get_doc("Location API Settings")
               if location_settings_val.api_key:
                   api=location_settings_val.api_key
                   data["api"]=api
               if location_settings_val.domain:
                   domain=location_settings_val.domain
                   data["domain"]=domain
               if location_settings_val.lead_creation_location_fetching_enabled:
                   lead_creation_api=location_settings_val.lead_creation_location_fetching_enabled
                   data["lead creation api"]=lead_creation_api
            
            return data
        else:
            frappe.msgprint("Employee record not found for the current user.")
            return data



@frappe.whitelist(allow_guest=True)
def call(doc,num):
#   frappe.msgprint("<a href=tel:frm.doc.number_to_be_contacted>frm.doc.number_to_be_contacted</a>")
  frappe.msgprint('Click the number to call ' f'<a href=tel:"{num}">{num} </a>')




@frappe.whitelist(allow_guest=True)
def get_location_api_settings():
    data={}
    if frappe.db.exists("Location API Settings"):
        location_settings_val=frappe.get_doc("Location API Settings")
        if location_settings_val.api_key:
            api=location_settings_val.api_key
            data["api"]=api
            print(api,"valuesss")
        if location_settings_val.domain:
            domain=location_settings_val.domain
            data["domain"]=domain
        if location_settings_val.enabled:
            enabled=location_settings_val.enabled
            data["enabled"]=enabled
        print(data,"valueeeeeeee")
        frappe.msgprint(data)
        return data
    


@frappe.whitelist(allow_guest=True)
def get_doctype_data(doctype, filters=None):
    docList = []
    getList = frappe.db.get_list(doctype, filters=filters)
    for item in getList:
        doc = frappe.get_doc(doctype, item["name"]).as_dict()
        docList.append(doc)

    return docList
# # Check whether opportunity created with current lead name.
# @frappe.whitelist(allow_guest=True)
# def create_opp(doc):
#     if not frappe.db.exists("Opportunity",doc):
#         # Get details of lead
#         ld=frappe.get_doc("Lead",doc)
#         #Create new opportunity
#         opp = frappe.new_doc("Opportunity")
#         # Update fields in opportunity
#         opp.opportunity_from = "Lead"
#         opp.lead = ld.name
#         if ld.lead_address:
#             for c in ld.lead_address:
#                 opp.append("address_list",{"address":c.address,"address_line_1":c.address_line_1,"address_line_2":c.address_line_2,"city":c.city,"state":c.state,"country":c.country,"is_primary":c.is_primary})

#         if ld.lead_contact:
#             for c in ld.lead_contact:
#                 opp.append("contact_list",{"contact_number":c.contact_number,"email_id":c.email_id,"is_primary":c.is_primary})
#         # opp.contact_person=ld.lead_name
#         opp.email_id=ld.email_id
#         opp.party_name=ld.name
#         opp.from_lead=1
#         opp.insert()

    # else:
    #     frappe.throw("Opportunity Already Exist")
# def after_insert(doc,events):

#     primary_add = []
#     if len(doc.lead_address)>0:
#         for con in doc.lead_address:
#             if con.is_primary == 1:
#                 if len(primary_add)>0:
#                     frappe.throw("You can only add one Primary Address.")
#                 else:
#                     primary_add.append(con)
#             con.save()
# def after_insert(doc,methods):
#     address=frappe.get_doc("Address",doc.name)
#     if address.links:
#         for lin in address.links:
#             lin.link_doctype="Lead"
#             lin.link_name=doc.lead_name
#     address.save()
# #     doc.contact_by=ld.owner
#     ld.save()
#     # pr_cn=[]
    #if len(doc.lead_contact)>0:
        # for co in doc.lead_contact:
        #     if co.is_primary==1:
        #         pr_cn.append(co)
        #         if len(pr_cn)>1:
        #             frappe.throw("You can Add Only One Primary Contact")
        #             print(pr_cn)
        #         else:
        #             contact=frappe.get_list("Contact")

    #for row in contact:

                # if con.links:
                        #     for lin in con.links:
                        #         if lin.link_doctype=="Lead" and lin.link_name==doc.name:
                        #             for c in doc.lead_contact:
                        #                 if c.email_id:
                        #                     con.append("email_ids",{"email_id":c.email_id})
                        #                 if c.contact_number:
                        #                     con.append("phone_nos",{"phone":c.contact_number})
                        #             con.insert()
                        #             con.reload()
                        #             frappe.msgprint("Primary Contact Added")



    # if doc.lead_contact:
    #     contact=frappe.get_list("Contact")
    #     for row in contact:
    #         con=frappe.get_doc("Contact",row)
    #         #print(con,"hellooo",contact)
    #         if con.links:
    #             for lin in con.links:
    #                 if lin.link_doctype=="Lead" and lin.link_name==doc.name:
    #                     for c in doc.lead_contact:
    #                         if c.email_id:
    #                             con.append("email_ids",{"email_id":c.email_id})
    #                         if c.contact_number:
    #                             con.append("phone_nos",{"phone":c.contact_number})
    #                         con.save()
    #                 frappe.msgprint(con,"Success")





    # if doc.lead_contact:
    #     contact=frappe.get_list("Contact")
    #     for row in contact:
    #         con=frappe.get_doc("Contact",row.doc)
    #         print(row.doc)
    #         for lin in con.links:
    #             if lin.link_doctype=="Lead" and lin.link_name==doc.name:
    #                     for c in doc.lead_contact:
    #                         con.append("phone_nos", {"phone": c.contact_number})
    #                         print(c.contact_number)
    #                         print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    #                     con.insert()

    # earth_radius = 6371.0

    # # Convert latitude and longitude from degrees to radians
    # lat1 = math.radians(lat1)
    # lon1 = math.radians(lon1)
    # lat2 = math.radians(lat2)
    # lon2 = math.radians(lon2)

    # # Differences in latitude and longitude
    # dlat = lat2 - lat1
    # dlon = lon2 - lon1

    # # Haversine formula
    # a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    # c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    # # Calculate the distance
    # distance = earth_radius * c

    # return distance

import frappe
import re
import requests
from datetime import datetime, timedelta


@frappe.whitelist( allow_guest=True )
def get_all_items(lead_name,email_id,mobile_no,consumer_number,city):
    print(consumer_number)
    #Calling regular expression
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # calling fullmatch function by passing pattern and mobile number
    r=re.fullmatch('[6-9][0-9]{9}',mobile_no)
    c=re.fullmatch('[0-9]{13}',consumer_number)
    if consumer_number:
        if c!=None:
            print("hellooo")   
        else:
            response="Please Check Your Consumer Number"
            return response
    if lead_name and email_id and  mobile_no:
        if(re.fullmatch(regex, email_id)):
            if r!=None: 
                    try:
                        lead=frappe.new_doc("Lead")
                        lead.lead_name=lead_name
                        lead.email_id=email_id
                        lead.mobile_no=mobile_no
                        lead.consumer_number=consumer_number
                        lead.city=city
                        lead.save()
                        response={"lead_name":lead.lead_name,"email_id": lead.email_id,"mobile_no":lead.mobile_no,"consumer_number": lead.consumer_number,"city":lead.city}
                    except Exception as e:
                        response=e
                
              
            else:
                response="Not a Valid Mobile Number"
        else:
            response="Invalid Email ID"    
    else:
        if not email_id and not mobile_no and not lead_name:
            response="Please Enter Your Name,Email ID  and Mobile Number"   
        elif not mobile_no and not lead_name:
            response="Please Enter Your Name and Mobile Number"   
        elif not email_id and not mobile_no:
            response="Please Enter Your Email ID  and Mobile Number"  
        elif  not email_id  and not lead_name:
            response="Please Enter Your Name and Email ID"
        elif not lead_name:
            response="Please Enter Your Name "
        elif not email_id:
            response="Please Enter Your Email ID"
        elif not mobile_no:
            response="Please Enter Your Mobile Number"
    return response







@frappe.whitelist( allow_guest=True )
def create_customer_call(base_url,usr,pwd,authorization,called_number,caller_number,total_call_duration,call_date,call_status,recording_url,wav_and_agent_number,call_uuid,call_start_time,call_end_time,conversation_duration,dtmfseq):

    if usr and pwd and authorization and base_url:
        #call login api

        url=base_url+"/api/method/login"
        body={
            "usr":usr,
            "pwd":pwd,
            "Authorization":authorization
        }


        response = requests.request("POST", url,json=body)

        print(response.text)
        print(response.status_code)

        #check is user is valid or not
        if response.status_code==200:
            print(response.cookies)
            cook=response.cookies
            print(cook.get("sid"))
            sid=cook.get("sid")
            full_name=cook.get("full_name")
            user_id=cook.get("user_id")
            #set cookie of logged user
            cookie="full_name="+full_name+"; sid="+sid+"; user_id="+user_id+";"
            

          
            call_date_time=call_date
            datetime_string =call_date.split(" ")[0]
            format_string = "%Y-%m-%d"

            called_date = datetime.strptime(datetime_string, format_string)

            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

            called_date=str(called_date)

            print(called_date)


            if '+91' in caller_number:
                caller_number=caller_number.replace('+91','')

                        
            url=base_url+"/api/resource/Customer Call Records"
            print(url)
            json={
            "called_number":called_number,
            "caller_number":caller_number,
            "total_call_duration":total_call_duration,
            "call_date":call_date,
            "called_date":called_date,
            "call_date_time":call_date_time,
            "call_status":call_status,
            "recording_url":recording_url,
            "wav_and_agent_number":wav_and_agent_number,
            "call_uuid":call_uuid,
            "call_start_time":call_start_time,
            "call_end_time":call_end_time,
            "conversation_duration":conversation_duration,
            "dtmfseq":dtmfseq,

            }

            #set cookie in header

            headers = {
                            "cookie":cookie,
                            "content-type": "text/json",
                            
                        }

            response = requests.request("POST", url,json=json,headers=headers)

            

           
            return response.text

        else:
            return "Invalid Credentials"
        
     


    # new_customer_call=frappe.new_doc("Customer Call Records")
    # new_customer_call.called_number=called_number   
    # new_customer_call.caller_number=caller_number
    # new_customer_call.total_call_duration=total_call_duration
    # new_customer_call.call_date=call_date
    # new_customer_call.call_status=call_status
    # new_customer_call.recording_url=recording_url
    # new_customer_call.wav_and_agent_number=wav_and_agent_number
    # new_customer_call.call_uuid=call_uuid
    # new_customer_call.call_start_time=call_start_time
    # new_customer_call.call_end_time=call_end_time
    # new_customer_call.conversation_duration=conversation_duration
    # new_customer_call.dtmfseq=dtmfseq
    # new_customer_call.save()
    # return "success"





















"""
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()
    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
        frappe.local.response["message"] = {
            "success_key":0,
            "message":"Authentication Error!"
        }

        return

    api_generate = generate_keys(frappe.session.user)
    user = frappe.get_doc('User', frappe.session.user)

    frappe.response["message"] = {
        "success_key":1,
        "message":"Authentication success",
        "sid":frappe.session.sid,
        "api_key":user.api_key,
        "api_secret":api_generate,
        "username":user.username,
        "email":user.email
    }



def generate_keys(user):
    user_details = frappe.get_doc('User', user)
    api_secret = frappe.generate_hash(length=15)

    if not user_details.api_key:
        api_key = frappe.generate_hash(length=15)
        user_details.api_key = api_key

    user_details.api_secret = api_secret
    user_details.save()

    return api_secret"""
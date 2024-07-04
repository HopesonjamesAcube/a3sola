import frappe
import re
from frappe.utils import today
from datetime import datetime,timedelta
import googlemaps
import pytz

def after_insert(doc, methods):
    if not doc.employee_in_time:
        ist_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist_timezone)
        formatted_time = current_time.strftime("%H:%M:%S")
        print(formatted_time)
        doc.employee_in_time = formatted_time
def on_submit(doc, methods):
        ist_timezone = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist_timezone)
        formatted_time = current_time.strftime("%H:%M:%S")
        print(formatted_time)
        doc.employee_out_time = formatted_time
        location_settings=frappe.get_doc("Location API Settings")
        if location_settings:
            if location_settings.distance_api_enabled:
                if location_settings.distance_api_enabled==1:
                    if frappe.db.exists("Lead",{"lead_owner":frappe.session.user,"date":doc.attendance_date}):
                        lead = frappe.get_last_doc("Lead",{"lead_owner":frappe.session.user,"date":doc.attendance_date})
                        doc.last_created_lead = lead.name
                    if frappe.db.exists("Sales Person Travel",{"date": doc.attendance_date, "user": frappe.session.user}):
                        sales_person_travel_det=frappe.get_doc("Sales Person Travel",{"date": doc.attendance_date, "user": frappe.session.user})
                        sales_person_travel_det.total_noof_travel +=1
                        
                        if lead.latitude and lead.longitude and doc.latitude and doc.longitude:
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
                            origin_coordinates = str(lead.latitude)+","+str(lead.longitude) # Latitude and longitude of the origin
                            destination_coordinates = str(doc.latitude)+","+str(doc.longitude)  # Latitude and longitude of the destination
                            # Call the function to calculate the road distance.
                            distance = get_road_distance(origin_coordinates, destination_coordinates)
                            if distance:
                                distance=distance/1000
                            if distance or distance==0:
                                sales_person_travel_det.append("travel_itinerarys", {"travel_from": lead.place if lead.place else None, "travel_to": doc.city if doc.city else None,"distance":distance})
                            else:
                                sales_person_travel_det.append("travel_itinerarys", {"travel_from": lead.place if lead.place else None, "travel_to": doc.city if doc.city else None})
                            sales_person_travel_det.save()
           
        doc.save()
 


    
         

def validate(doc,methods):
    if doc.docstatus==0:
        doc.employee_out_time=""

          
     
    

#     if not  frappe.db.exists('Leave Type','RH'):
#           new_type=frappe.new_doc('Leave Type')
#           new_type.leave_type_name='RH'
#           new_type.include_holiday=1
#           new_type.save()

#     if doc.attendance_status in['Over time','Additional work']:
#           doc.status='Present'
    
#     elif doc.attendance_status=='RH':
          
#           doc.status='On Leave'
#           doc.leave_type='RH'

#     elif doc.attendance_status=='Sick Leave':
#           doc.status='On Leave'
#           doc.leave_type='Sick Leave'

#     else:
        
#           doc.status=doc.attendance_status
@frappe.whitelist()
def markinattendance(city,area,state,latitude,longitude):
   a=[]
   user = frappe.session.user
   if user !="Administrator":
       if frappe.db.exists("Employee",{"user_id":user}):
           user_det=frappe.get_doc("Employee",{"user_id":user})
           print("user///////////",user_det)
           print(city,area,state,latitude,longitude,"================")
           # Check if attendance for the user on the current date doesn't already exist
           if not frappe.get_all("Attendance", filters={"employee": user_det.name, "attendance_date": frappe.utils.today()}):
               attendance_doc = frappe.new_doc("Attendance")
               attendance_doc.employee = user_det.name
               attendance_doc.attendance_date = frappe.utils.today()
               attendance_doc.city=city
               attendance_doc.area=area
               attendance_doc.state=state
               attendance_doc.latitude=latitude
               attendance_doc.longitude=longitude

            #    current_datetime = datetime.now()
            #    attendance_doc.employee_in_time=current_datetime.strftime("%H:%M:%S")
               ist_timezone = pytz.timezone('Asia/Kolkata')
               current_time = datetime.now(ist_timezone)
               
               formatted_time = current_time.strftime("%H:%M:%S")
               print(formatted_time)
            #    doc.employee_in_time = formatted_time
               attendance_doc.employee_in_time=formatted_time
               attendance_doc.employee_out_time=""
               attendance_doc.status = "Present" # You can set the status as needed
               # attendance_doc.in_time = frappe.utils.now_datetime()
               attendance_doc.fetch_current_location=1
               attendance_doc.save()
               # frappe.throw("ttttttttttttttttttttt")
               frappe.db.commit()
               a.extend([city,state,area,longitude,latitude])
               return a
           else:
               frappe.msgprint("You have already marked attendance for the day")
   else:
       frappe.msgprint("Please Login as an employee to mark attendance")

@frappe.whitelist()
def markoutattendance(city,area,state,latitude,longitude):
   user = frappe.session.user
   if user !="Administrator":
       if frappe.db.exists("Employee",{"user_id":user}):
           user_det=frappe.get_doc("Employee",{"user_id":user})
           # Check if attendance for the user on the current date doesn't already exist
           if frappe.db.exists("Attendance",{"employee": user_det.name, "attendance_date": frappe.utils.today()}):
               attendance_marked=frappe.get_doc("Attendance",{"employee": user_det.name, "attendance_date": frappe.utils.today()})
               if not attendance_marked.employee_out_time:
                   if attendance_marked.employee_in_time:
                    #    current_time = datetime.now()datetime.now().time()
                    #    attendance_marked.employee_out_time =current_time.strftime("%H:%M:%S")
                       ist_timezone = pytz.timezone('Asia/Kolkata')
                       current_time = datetime.now(ist_timezone)
                       formatted_time = current_time.strftime("%H:%M:%S")
                       attendance_marked.employee_out_time=formatted_time
                       attendance_marked.fetch_current_location=1
                       attendance_marked.city=city
                       attendance_marked.area=area
                       attendance_marked.state=state
                       attendance_marked.latitude=latitude
                       attendance_marked.longitude=longitude
                       attendance_marked.save()
                       attendance_marked.submit()
                       return True
                   else:
                       frappe.throw("Please Mark Attendance IN to mark attendance OUT")
               else:
                   frappe.throw("You have already marked attendance OUT for the day")
           else:
               frappe.throw("Please Mark Attendance IN to mark attendance OUT")
   else:
       frappe.msgprint("Please Login as an employee to mark attendance")
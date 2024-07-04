import frappe
from frappe.utils import today
def validate(doc,methods):

    #check employee have attendance marked on todo and ensure that is not in cancelled state
    marked_attendance=0

    att=frappe.get_list("Attendance",filters={'attendance_date': doc.date,'employee': doc.employee},order_by='name asc')
    for i in att:
        att=frappe.get_doc("Attendance",i)
        print(att.docstatus)
        if att.docstatus!=2: 
            marked_attendance=i


    #if attendance marked on todo get the attendance and link id to field attendance
    if marked_attendance:
        attendance=frappe.get_doc("Attendance",marked_attendance)

        doc.attendance=attendance.name

        #update employee out time in attendance with current check-in time     
        out_time=str(doc.time)
        out_time=out_time.split(" ")
        out_time=out_time[1]
        attendance.employee_out_time=out_time
        attendance.save()



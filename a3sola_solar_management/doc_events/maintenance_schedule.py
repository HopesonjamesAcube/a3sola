import frappe

from datetime import datetime, timedelta

def on_submit(doc,methods):
    #create maintenance visits based on dates specified on table schedules

    for row in doc.schedules:
        mv=frappe.new_doc("Maintenance Visit")
        mv.customer=doc.customer
        mv.mntc_date=row.scheduled_date

        datetime_string = str(row.scheduled_date)
        format_string = "%Y-%m-%d"

        date_obj = datetime.strptime(datetime_string, format_string).date()

        for x in range(14):
            d = date_obj - timedelta(days=x)
            print(d.strftime("%Y-%m-%d"))


        mv.mntc_date=d

        


       
        doc.append("purpose",mv)
        for i in doc.items:
            if i.item_code==row.item_code:
                ds=i.description
                break
            else:
                ds="Work assigned as per schedule"

        mv.completion_status="Partially Completed"
        mv.work_completion_status="Not Started"
        mv.maintenance_schedule=doc.name
        mv.customer_address=doc.customer_address
        mv.contact_person=doc.contact_person
        mv.append("purposes",{"item_code":row.item_code,"description":"heeds","work_done":"please fill","service_person":row.sales_person})
        mv.save()






from dataclasses import field
from frappe import _, get_all, get_doc, get_value
from datetime import datetime
import frappe

no_cache = 1

def get_context(context):
    # frappe.get_doc("Project",{"tracking_id":'5fa0ea6303c3deb173119d0bede33c8e077ea462'})

    tracking_id="5fa0ea6303c3deb173119d0bede33c8e077ea462"
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    q="SELECT * FROM `tabProject` WHERE tabProject.tracking_id='%s'"%(tracking_id)
    print(q)
    pro =frappe.db.sql(q,as_dict=True)

    print(pro)


    # form_d= frappe.form_dict
    print("###################################")
    # print(form_d)

    return context

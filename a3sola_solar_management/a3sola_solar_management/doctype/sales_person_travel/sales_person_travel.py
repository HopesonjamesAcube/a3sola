# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesPersonTravel(Document):

    def validate(self):
        total_kms_val = 0  # Initialize the total_km to 0
        total_amount_val=0

        for i in self.travel_itinerarys:
            if i.distance:
                total_kms_val += float(i.distance)  # Sum up the distances
            if i.amount:
                total_amount_val += float(i.amount)

                


        self.total_kms = total_kms_val  # Assign the total_km to the parent document
        self.total_amount=total_amount_val
        self.total_noof_travel=len(self.travel_itinerarys)
@frappe.whitelist()
def get_sales_person_travel(doc):
    data ={}
    sal = frappe.get_doc("Sales Person Travel",doc)
    empl =frappe.get_doc("Employee",{"user_id":sal.user})
    if empl.expense_approver:
        data["approver"] = empl.expense_approver
    else:
        frappe.throw("Please Add Expense Approver for the employee")
    data["empl"]= empl.name
    data["date"] = sal.date

    return data

@frappe.whitelist()
def get_employee_id(user):
    d={"employee":""}
    if frappe.db.exists("Employee",{"user_id":user}):
        emp=frappe.get_doc("Employee",{"user_id":user})
        d["employee"]=emp.name
    return d
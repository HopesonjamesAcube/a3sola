import frappe

from datetime import datetime, timedelta

def validate(doc,methods):
  
        if doc.work_completion_status=="Partially Completed":
                doc.completion_status="Partially Completed"
        if doc.work_completion_status=="Fully Completed":
                doc.completion_status="Fully Completed"

def on_submit(doc,methods):
        pass






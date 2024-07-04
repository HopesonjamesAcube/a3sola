import frappe

def validate(doc,methods):

    doc.project=doc.project_id

    
        






def on_submit(doc,methods):
    if doc.project_id:
        
        protasks=frappe.get_list("Task",filters={"project": doc.project_id},order_by='name asc')
        for i in protasks:
            task=frappe.get_doc("Task",i)
            task.sales_order=doc.name
            # if task.doctypes_name=="Sales Order":
        
            #     task.d_id=doc.name
        
            task.save()
            print(task.sales_order)

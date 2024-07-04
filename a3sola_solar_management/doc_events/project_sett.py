import frappe

def validate(doc,methods):
        if doc.automate_project_assignment==1:
            if doc.template_details:
                for t in doc.template_details:
                    if t.select_template:
                        print("")
            frappe.msgprint("Project Settings Updated Successfully")
                                
                  
            # project_template=frappe.new_doc("Project Template")
            # project_template.name="a3Sola Project Template"
            # project_template.project_type="External"
            # task_list=frappe.get_list("Task")
            # print(task_list)
            # for row in reversed(task_list):
            #     print(row.name)
            #     project_template.append("tasks",{"task":row.name})
            #project_template.insert()
      


































# def on_update(doc,methods):
#     if frappe.db.exists("Project Template","a3sola Project Template"):
#         project_template=frappe.get_doc("Project Template","a3sfola Project Template")
#         doc.tasks=[]
#         task_list=frappe.get_list("Task")
#     for row in reversed(task_list):
#         print(row.name)
#         row.name=""
#         project_template.append("tasks",{"task":row.name})
#     project_template.insert()
#     frappe.msgprint("Project Template Updated Successfully")
import frappe
from frappe.utils import add_to_date
import datetime
from frappe.utils import today

def validate(doc,methods):
   if doc.project:
    #if current document contain project 
    #append contact details by fetch from opportunity
     project=frappe.get_doc("Project",doc.project)
     if project.oppertunity:
        opper=frappe.get_doc("Opportunity",project.oppertunity)
        if opper.contact_number:
            doc.contact_number=opper.contact_number
        if opper.whatsapp_number:
            doc.whatsapp_number=opper.whatsapp_number
        
    #condition code execution unwanted.This make code to be execute only if lead id is empty
     if not doc.lead_id:
          if doc.issue:
                issue=frappe.get_doc("Issue",doc.issue)
                if issue.exp_start_date:
                    doc.exp_start_date=issue.exp_start_date
                if issue.exp_end_date:
                    doc.exp_end_date=issue.exp_end_date
                if issue.priority:
                    doc.priority=issue.priority
          print("testttttttttttttttttt")


        #take main task defined on corresponding project template then use that 
          maintask=""
          project_template=frappe.get_doc("Project Template",project.project_template)
          for row in project_template.tasks:
              if row.subject==doc.subject:
                  maintask=row.task
                  break


          if  maintask:
            originaltask=frappe.get_doc("Task",maintask)
            print(originaltask)
            print(originaltask.name)
            print(originaltask.subject)
            doc.type=originaltask.type
            doc.doctypes_name=originaltask.doctypes_name
            doc.message=originaltask.message
            print(doc.doctypes_name)
            print("++++++++++++++")


            print(originaltask.is_process_status)
            print("hello")
            if originaltask.is_process_status==1:
                doc.is_process_status=1
                print(doc.is_process_status)

            print(doc.project)
            doc.payment_dependence=originaltask.payment_dependence
            doc.show_to_customer=originaltask.show_to_customer
            print(project.oppertunity)
            doc.project_id=doc.project
            if originaltask.assigned_user:
                doc.assigned_user=originaltask.assigned_user




            if originaltask.task_users and originaltask.assigned_user:
                ucount=0
                
                current_user=originaltask.assigned_user
                doc.assigned_user=originaltask.assigned_user
                print(len(originaltask.task_users))
                if len(originaltask.task_users)>1:
                        
                    for i in originaltask.task_users:
                        ucount=ucount+1
                        print(i.user_name)

                        print(current_user)
                        if i.user_name==current_user:
                                    
                            if ucount==len(originaltask.task_users):
                                originaltask.task_users[0].user_name
                                
                                originaltask.assigned_user=originaltask.task_users[0].user_name
                            else:
                                
                                originaltask.assigned_user=originaltask.task_users[ucount].user_name
                            originaltask.save()
                            break

                
                        
                        




            
            doc.customer=project.customer
            
            if project.oppertunity:
                opp=frappe.get_doc("Opportunity",project.oppertunity)
                print(opp.party_name)
                doc.lead_id=opp.party_name

                doc.opportunity=project.oppertunity
                



            print(doc.is_process_status)
            print(type(doc.is_process_status))
            doc.number_of_attachments_allowed=originaltask.number_of_attachments_allowed
            temp_name=project.project_template
            print("^^^^^^^^^^^^^^^^^",temp_name)
            project_template=frappe.get_doc("Project Template",temp_name)
            print(project_template.tasks)

            pstart_date=project.expected_start_date
            nxttask=0
            i=0
            for row in project_template.tasks:
                i=i+1


                if nxttask==1:
                        doc.exp_end_date=add_to_date((pstart_date),days=row.starting_day,as_string=True)
                        nxttask=0


                if row.subject==doc.subject:
                        doc.on=row.order_number
                        doc.ono=row.order_number
                        print(doc.on)
                        doc.exp_start_date=add_to_date((pstart_date),days=row.starting_day,as_string=True)
                        nxttask=1

                        if i==len(project_template.tasks):
                            print("Haiii")
                            doc.exp_end_date=project.expected_end_date
                            print(doc.exp_end_date)


            



            print(doc.exp_end_date)







     print(project.linked_documents)
     count=0
     docids=[]
     for i in  project.linked_documents:
          print(doc.d_id,i.docid)
          print
          if i.docname==doc.doctypes_name:
               count=count+1
               docids=docids+[i.docid]

     complete=3
     print(count)
     project_template=frappe.get_doc("Project Template",project.project_template)

     if doc.status=="Completed":
        for row in project_template.tasks:
            if row.subject==doc.subject:
                maintask=row.task
                if row.is_attachment_mandatory:
                    attachments = frappe.get_all("File", filters={"attached_to_doctype":"task", "attached_to_name":doc.name})
                    if attachments:
                        pass
                    else:
                        frappe.throw("Please add attachment")
        if doc.issue:
           
            issue=frappe.get_doc("Issue",doc.issue)
            issue.status="Closed"
            issue.save()

        

        # if doc.completed_by and doc.is_completed==0:
            
        #     # if doc.latitude:
        #     #     print("haii")
        #     if frappe.db.exists({"doctype":"Employee","user_id": doc.completed_by}):
        #         emp=frappe.get_doc("Employee",{"user_id":doc.completed_by})
        #         today_checkin=frappe.get_list("Employee Checkin",filters={"employee":emp.name,"date":today()},order_by='name asc')
        #         if today_checkin:
        #             last_check_in= frappe.get_doc("Employee Checkin",today_checkin[-1])
        #             if last_check_in.log_type=="IN":
        #                 checkout=frappe.new_doc("Employee Checkin")
        #                 checkout.employee=last_check_in.employee
        #                 checkout.log_type="OUT"
        #                 checkout.latitude=last_check_in.latitude
        #                 checkout.longitude=last_check_in.longitude
        #                 checkout.task=last_check_in.name
        #                 checkout.task=last_check_in.task

        #                 checkout.area=last_check_in.area

        #                 checkout.city=last_check_in.city
        #                 checkout.state=last_check_in.state
        #                 checkout.save()

        #         print(today_checkin)
        #         checkin=frappe.new_doc("Employee Checkin")
        #         checkin.employee=emp.name
        #         checkin.log_type="IN"
        #         checkin.latitude=doc.latitude
        #         checkin.longitude=doc.longitude
        #         checkin.task=doc.name
        #         checkin.area=doc.area
        #         checkin.city=doc.city
        #         checkin.state=doc.state
                
        #         # if doc.my_location:
        #         #     checkin.my_location=doc.my_location
        #         checkin.save()



        


           

         



             

     if count<int(doc.number_of_attachments_allowed):


        if doc.status=="Completed":
          protasks=frappe.get_list("Task",filters={"project": doc.project},order_by='name asc')
          print(protasks)
          complete=1
          for i in protasks:
             tas=frappe.get_doc("Task",i)

             if tas.subject!=doc.subject:

                 print(tas.subject)
                 print(tas.is_completed)

                 if tas.is_completed==0:
                     complete=0
                 else:
                     pass




        print(complete)
        # print("$$$$$$$$$$$$$$$$$$")
        # print(doc.status)
        # print("%555",doc.doctypes_name)
        # frappe.throw("wait")

        if doc.status=="Completed" and doc.doctypes_name==None:

            if doc.is_process_status==1:
                task=doc.subject
                print(task)
                project.pstatus=str(task)+" "+"Completed"
                project.save()
            else:
                pass


        elif doc.status=='Completed' and doc.is_process_status==1:

           if frappe.db.exists(doc.doctypes_name,doc.d_id):
                docu=frappe.get_doc(doc.doctypes_name,doc.d_id)
                task=doc.subject
                if doc.doctypes_name=="Delivery Note":
                    if docu.project==doc.project:
                        if doc.d_id not in docids:


                             project.append("linked_documents",{"docname":doc.doctypes_name,"docid":doc.d_id})

                             if complete==1:
                                 project.pstatus="Project Completed"
                             else:
                                 project.pstatus=str(task)+" "+"Completed"


                             project.save()
                             doc.is_completed=1
                             doc.total_attachments=count+1

                    # else:
                    #     frappe.throw("Please Link Related "+doc.doctypes_name+ " Document Id !")

                elif docu.project_id==doc.project:
                #      task=doc.subject
                #      protasks=frappe.get_list("Task",filters={"project": doc.project},order_by='name asc')
                #      index=next((index for (index, d) in enumerate(protasks) if d["name"] == doc.name),None)
                #      print("*********************")
                #      print(index)
                #      if index !=0:
                          # prevtask=protasks[index-1]['name']
                          # prevtask=frappe.get_doc("Task",prevtask)
                     # if prevtask.is_completed==1:
                     #      if str(task)=="Installation Report":
                     #           project.process_status="Installation Completed"
                     #      elif str(task)=="Completion Report":
                     #           project.process_status="Project Completed"
                     #      else:
                     #           project.process_status=str(task)+" "+"Completed"
                     #      if doc.d_id not in docids:
                     #           project.append("linked_documents",{"docname":doc.doctypes_name,"docid":doc.d_id})
                     #           project.save()
                     #           print("%%%%%%%%%%%%%%%%%%%%")
                     #           print(project.process_status)
                     #           doc.is_completed=1
                     #           doc.total_attachments=count+1
                          # else:
                          #      msg=str(doc.subject)+" Can Not Complete Before "+str(prevtask.subject)
                          #      frappe.throw(msg)
                     # else:
                     # if str(task)=="Installation Report":
                     #           project.process_status="Installation Completed"
                     # elif str(task)=="Completion Report":
                     #      project.process_status="Project Completed"
                     # else:
                     #      project.process_status=str(task)+" "+"Completed"
                     print(complete)

                     if complete==1:
                        project.pstatus="Project Completed"
                     else:
                        project.pstatus=str(task)+" "+"Completed"
                     print("Testtttttttttt")


                     if doc.d_id not in docids:

                          project.append("linked_documents",{"docname":doc.doctypes_name,"docid":doc.d_id})
                          project.save()
                          print("%%%%%%%%%%%%%%%%%%%%")
                          print(project.process_status)
                          doc.is_completed=1
                          doc.total_attachments=count+1

           #      else:
           #           frappe.throw("Please Link Related "+doc.doctypes_name+ " Document Id !")
           # else:
           #      frappe.throw("Please Link Related "+doc.doctypes_name+ " Document Id !")


        elif doc.status=='Completed':
           if frappe.db.exists(doc.doctypes_name,doc.d_id):
                docu=frappe.get_doc(doc.doctypes_name,doc.d_id)
                if doc.doctypes_name=="Delivery Note":
                    if docu.project==doc.project:
                        if doc.d_id not in docids:

                             project.append("linked_documents",{"docname":doc.doctypes_name,"docid":doc.d_id})
                             if complete==1:
                                 project.pstatus="Project Completed"
                             # else:
                             #     project.pstatus=str(doc.subject)+" "+"Completed"
                             project.save()
                             doc.is_completed=1
                             doc.total_attachments=count+1

                    # else:
                    #     frappe.throw("Please Link Related "+doc.doctypes_name+ " Document Id !")

                elif docu.project_id==doc.project:
                     # protasks=frappe.get_list("Task",filters={"project": doc.project},order_by='name asc')
                     # index=next((index for (index, d) in enumerate(protasks) if d["name"] == doc.name),None)
                     # print("*********************")
                     # print(index)
                     # print(protasks)
                     # if index !=0:
                          # prevtask=protasks[index-1]['name']
                          # prevtask=frappe.get_doc("Task",prevtask)
                          # print(prevtask)
                          # if prevtask.is_completed==1:
                          #      if doc.d_id not in docids:
                          #           project.append("linked_documents",{"docname":doc.doctypes_name,"docid":doc.d_id})
                          #           project.save()
                          #           doc.is_completed=1
                          #           doc.total_attachments=count+1
                          # else:
                          #      msg=str(doc.subject)+" Can Not Complete Before "+str(prevtask.subject)
                          #      frappe.throw(msg)
                     # else:
                     if doc.d_id not in docids:

                          project.append("linked_documents",{"docname":doc.doctypes_name,"docid":doc.d_id})
                          print("Completeeeeeeeeeeeeeeeeeeeeee")
                          print(complete)


                          if complete==1:
                              project.pstatus="Project Completed"
                          # else:
                          #     project.pstatus=str(doc.subject)+" "+"Completed"
                          project.save()
                          doc.is_completed=1
                          doc.total_attachments=count+1

           #      else:
           #           frappe.throw("Please Link Related "+doc.doctypes_name+ " Document Id !")
           # else:
           #      frappe.throw("Please Link Related "+doc.doctypes_name+ " Document Id ! ")

     else:
          if doc.doctypes_name=="Delivery Note" or  doc.doctypes_name=="Journal Entry" or doc.doctypes_name=="Sales Order" or doc.doctypes_name=="Payment Entry" or doc.doctypes_name=="Pick List" or doc.doctypes_name=="Quotation":
              pass
          
          elif doc.d_id not in docids:
               frappe.msgprint("The "+doc.project+" Has Already"+str(count)+" "+str(doc.doctypes_name)+" Attachment")
     print("^^^^^^^^^^^^^^^^^^^^^")




def after_insert(doc,methods):
    pass





@frappe.whitelist(allow_guest=True)
def test(doc,pro):

     print(pro)
     project = frappe.get_doc('Project',pro)
     task = frappe.get_doc('Task',doc)
     taskname=task.subject
     print(taskname)
     tasks=frappe.get_list("Task",filters={"project": pro,"subject":taskname})
     print(tasks)
     d={}
     count=1
     for row in tasks:
          d[count]=row['name']
          count=count+1

     return d


@frappe.whitelist(allow_guest=True)
def popup(doc,pro,type):
     print("$$$$$$$$$$$$$$")
     print(type)
     if type=="Sales Order":

         ret=frappe.db.get_list('Quotation', filters={'project_id':pro} )


     if type=="Sales Invoice" or type=="Payment Entry" or type=="Pick List":
         ret=frappe.db.get_list('Sales Order', filters={'project_id':pro} )

     if type=="Delivery Note":
         ret=frappe.db.get_list('Pick List', filters={'project_id':pro} )

     print(ret)
     d={}
     print("bro")
     d['ret']=[]
     # existing=frappe.get_doc("Quotation",'SAL-QTN-2023-00022')
     # print(existing.docstatus)
     for i in ret:
         print(i['name'])
         if type=="Sales Order":
             print(i['name'])
             existing=frappe.get_doc("Quotation",i['name'])
             print("hello")

         if type=="Payment Entry" or type=="Sales Invoice" or type=="Pick List":
             print("tessst")
             existing=frappe.get_doc("Sales Order",i['name'])

         if type=="Delivery Note":
             existing=frappe.get_doc("Pick List",i['name'])
         print("heyyy")

         if existing.docstatus==1:
             print("haiii")
             d['ret']=d['ret']+[i['name']]
     print(d)



     return d

@frappe.whitelist(allow_guest=True)
def exist(doc,pro,type):

     existlist=frappe.get_list(type,filters={'project_id':pro})
     print(existlist)
     print("existtt")
     if existlist:
         return True
     else:
         return False

from dataclasses import field
from frappe import _, get_all, get_doc, get_value
from datetime import datetime
import frappe
from frappe.utils import date_diff
from datetime import datetime
import random
import num2words



no_cache = 1

def get_context(context):
    # frappe.get_doc("Project",{"tracking_id":'5fa0ea6303c3deb173119d0bede33c8e077ea462'})
    form_d= frappe.form_dict

    print(form_d)

    tracking_id=form_d['id']
    context.tracking_id=tracking_id

    q="SELECT * FROM `tabOpportunity` WHERE tabOpportunity.tracking_id='%s'"%(tracking_id)
    oppo =frappe.db.sql(q,as_dict=True)
    print(oppo)
    context.oppodetails=oppo[0]
    print(oppo[0])

    ctrack=frappe.get_doc('Customer Tracking Setting')
 
    context.ctrack=ctrack

    ctrack.chat=0
    if ctrack.enable_chatbot:
        context.chat=1
        context.src=ctrack.src
    
    # issue=frappe.new_doc("Issue")
    # issue.subject="issuesss"
    # issue.customer=oppo[0]['customer']
    # issue.insert()
    # print(issue.subject)
    # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


   
    



    project=frappe.db.exists({'doctype':'Project','tracking_id':tracking_id})
    if project:
        context.proexit=1
        
    else:
        context.proexit=0

    if ctrack.working_hour_start_time:
        ti=str(ctrack.working_hour_start_time)
        tis=ti.split(":")
        count=1
        start=""
        for i in tis:
            if count<3:
                if count==1:
                    start=start+i+":"
                else:
                    start=start+i
            count=count+1
            print(count)
            print(start)

        start=datetime.strptime('09:00', "%H:%M")
        print("*********************************")
        print(start)
        print("^^^^^^^^^^^^6")

        context.stime=start.strftime("%I:%M %p")



    if ctrack.working_hour_end_time:
        ti=str(ctrack.working_hour_end_time)
        tis=ti.split(":")
        count=1
        end=""
        for i in tis:
            if count<3:
                if count==1:
                    end=end+i+":"
                else:
                    end=end+i
            count=count+1
        end=datetime.strptime(end, "%H:%M")
        end=end.strftime("%I:%M %p")
        context.etime=end
        print(end)

    issues=frappe.get_list("Issue",filters={"Opportunity": oppo[0]['name']},order_by='name asc')
    context.issues=issues
    print(issues)




    





    # tracking_id=form_d['id']
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    # q="SELECT * FROM `tabProject` WHERE tabProject.tracking_id='%s'"%(tracking_id)

    # print(q)
    # pro =frappe.db.sql(q,as_dict=True)
    # context.prodetails=pro[0]
    # print(pro[0]['item_name'])
    # c=pro[0]['expected_end_date']
    # context.per=pro[0]['percent_complete']
    # print(pro)
    # if pro[0]['company']:
    #     company=frappe.get_doc('Company',pro[0]['company'])
    #     if company:
    #         fav=company.fav_icon
    #         context.fav=fav


    # now = datetime.now()
    # str_d1=now.date()
    # print(str_d1,"rrrrrrrrrrrrrrrrrrrrrrrrrr")
    # if c:
    #     str_d2 = pro[0]['expected_end_date']
    # # difference between dates in timedelta
    #     delta = (str_d2 - str_d1)
    #     print(f'Difference is {delta.days} days')
    #     date=delta.days
    #     # date=0
    #     context.date=date


    # add=frappe.get_doc("Address",pro[0]['address'])
    # address=""
    # if add.address_line1:
    #     address=address+add.address_line1
    # if add.address_line2:
    #     address=address+" , "+add.address_line2
    # if add.city:
    #     address=address+" , "+add.city
    # if add.state:
    #     address=address+" , "+add.state
    # print(address)
    # context.add=add


    # if frappe.db.exists('Quotation',{'project_id':pro[0]['name']}):
    #     quotation=frappe.get_doc('Quotation',{'project_id':pro[0]['name']})
    #     for i in quotation.items:
    #         price=i.amount
    #         words=frappe.utils.money_in_words(price)
    #         words=words.replace("INR ","Rupees ")
    #         context.words=words
    #         print(words)
    #         print("======================")
    #     print(quotation.rounded_total)
    #     print(quotation.in_words)
    #     context.price=quotation.rounded_total
    #     context.words=quotation.in_words
    # else:
    #     price=""

    #     context.price=''
    #     context.words=''


    # protasks=frappe.get_list("Task",filters={"project": pro[0]['name'],"show_to_customer":1,"status":"Completed"},order_by='name asc')
    # context.protask=protasks
    # print(protasks,"33333333333333333333333333333333")
    # ncprotasks=frappe.get_list("Task",filters={"project": pro[0]['name'],"show_to_customer":1,"status":["not in",["Completed"]]},order_by='name asc')
    # context.ncprotasks=ncprotasks

    # if frappe.db.exists('Sales Invoice',{'project':pro[0]['name']}):
    #     sales_invoice=frappe.get_doc('Sales Invoice',{'project':pro[0]['name']})
    #     print(sales_invoice)
    #     context.sales_invoice=sales_invoice




    # ctrack=frappe.get_doc('Customer Tracking Setting')
    # if frappe.db.exists("Terms and Conditions",ctrack.terms):
    #     termsc=frappe.get_doc('Terms and Conditions',ctrack.terms)
    #     termsc=termsc.format_by_html
    #     context.terms=termsc
    #     print(termsc)
    # context.logo=ctrack.data_3
    # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    # context.color=ctrack.color_theme
    # context.color2=ctrack.color_theme_2
    # context.font=ctrack.font
    # context.address=ctrack.address
    # context.phone=ctrack.phone
    # context.email=ctrack.email
    # context.menu=ctrack.custom_menu
    # context.ctrack=ctrack
    # if ctrack.working_hour_start_time:
    #     ti=str(ctrack.working_hour_start_time)
    #     tis=ti.split(":")
    #     count=1
    #     start=""
    #     for i in tis:
    #         if count<3:
    #             if count==1:
    #                 start=start+i+":"
    #             else:
    #                 start=start+i
    #         count=count+1
    #         print(count)
    #         print(start)

    #     start=datetime.strptime('09:00', "%H:%M")
    #     print("*********************************")
    #     print(start)
    #     print("^^^^^^^^^^^^6")

    #     context.stime=start.strftime("%I:%M %p")



    # if ctrack.working_hour_end_time:
    #     ti=str(ctrack.working_hour_end_time)
    #     tis=ti.split(":")
    #     count=1
    #     end=""
    #     for i in tis:
    #         if count<3:
    #             if count==1:
    #                 end=end+i+":"
    #             else:
    #                 end=end+i
    #         count=count+1
    #     end=datetime.strptime(end, "%H:%M")
    #     end=end.strftime("%I:%M %p")
    #     context.etime=end
    #     print(end)








    # from datetime import date

    # todays_date = date.today()

    # print("Current date: ", todays_date)

    # print("Current year:", todays_date.year)

    # context.year=todays_date.year

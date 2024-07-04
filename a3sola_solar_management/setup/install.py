from __future__ import print_function, unicode_literals

import frappe
from erpnext.accounts.doctype.cash_flow_mapper.default_cash_flow_mapper import DEFAULT_MAPPERS

from frappe import _
from frappe.desk.page.setup_wizard.setup_wizard import add_all_roles_to
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

default_mail_footer = """<div style="padding: 7px; text-align: right; color: #888"><small>Sent via
	<a style="color: #888" href="http://erpnext.org">ERPNext</a></div>"""



import frappe
import os
import json

def after_insta(t=None):
    
    if t==1:
        datapath = frappe.get_app_path('a3sola_solar_management', 'territory.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                if not  frappe.db.exists('Territory',i['name']):
                    newdoc = frappe.new_doc("Territory")

                    
                    for key in  keys_list:
                        newdoc.set(key, i[key])

                    newdoc.insert()

        datapath = frappe.get_app_path('a3sola_solar_management', 'electricity_board.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                if not  frappe.db.exists('Electricity Board',i['name']):
                    newdoc = frappe.new_doc("Electricity Board")

                    
                    for key in  keys_list:
                        print(key,i[key])
                        newdoc.set(key, i[key])

                    newdoc.insert()

            
        
            
        datapath = frappe.get_app_path('a3sola_solar_management', 'task.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                print("New looopppppppppppppppppppppppppppppppppp taskkkkkkkkkkkk")
                print(i['name'],"$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                if not  frappe.db.exists('Task',i['name']):
                    newdoc = frappe.new_doc("Task")


                    
                    for key in  keys_list:
                        print(key,i[key])
                        newdoc.set(key, i[key])

                    newdoc.save()

        
        datapath = frappe.get_app_path('a3sola_solar_management', 'project_type.json')

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                print("New looopppppppppppppppppppppppppppppppppp typeeeeeeeeeeee")
                if not  frappe.db.exists('Project Type',i['name']):
                    newdoc = frappe.new_doc("Project Type")


                    
                    for key in  keys_list:
                        print(key,i[key])
                    

                        newdoc.set(key, i[key])

                    newdoc.save()


        





        datapath = frappe.get_app_path('a3sola_solar_management', 'project_template.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                print("New looopppppppppppppppppppppppppppppppppp templateeeeeeeeeeeeeeeee")
                if not  frappe.db.exists('Project Template',i['name']):
                    newdoc = frappe.new_doc("Project Template")


                    
                    for key in  keys_list:
                        print(key,i[key])
                       
                        newdoc.set(key, i[key])

                    newdoc.insert()

        datapath = frappe.get_app_path('a3sola_solar_management', 'scheme.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                if not  frappe.db.exists('Scheme',i['name']):
                    newdoc = frappe.new_doc("Scheme")


                    
                    for key in  keys_list:
                        print(key)
                        newdoc.set(key, i[key])

                    newdoc.insert()


        datapath = frappe.get_app_path('a3sola_solar_management', 'item_group.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)


    
        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                print("New looopppppppppppppppppppppppppppppppppp item grpppppppppppppp")
                if not  frappe.db.exists('Item Group',i['name']):
                    newdoc = frappe.new_doc("Item Group")


                    
                    for key in  keys_list:
                        print(key,i[key])
                        if key!='company':

                            newdoc.set(key, i[key])

                    newdoc.save()



        company=frappe.defaults.get_user_default("company") 
        comp=frappe.get_doc("Company",company)

        # datapath = frappe.get_app_path('a3sola_solar_management', 'gst_hsn_code.json')
        # print("$$$$$$$$$$$$$$$$")
        # print(datapath)

        # with open(datapath, 'r') as file:
        #     data = json.load(file)
        #     fdict=data[0]
        #     keys_list = list(fdict)
            

        #     for i in data:

        #     # Assuming each item in the JSON represents a document
        #         print("New looopppppppppppppppppppppppppppppppppp itemmmmmmmmmmmmmmmmmmmmmmmm")
        #         if not  frappe.db.exists('GST HSN Code',i['name']):
        #             newdoc = frappe.new_doc("GST HSN Code")


                    
        #             for key in  keys_list:
        #                 print(key,i[key])
                        
        #                 newdoc.set(key, i[key])

        #             newdoc.save()


        datapath = frappe.get_app_path('a3sola_solar_management', 'item.json')
        print("$$$$$$$$$$$$$$$$")
        print(datapath)
        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:
                print(i)

            # Assuming each item in the JSON represents a document
                print("New looopppppppppppppppppppppppppppppppppp itemmmmmmmmmmmmmmmmmmmmmmmm")
                if not  frappe.db.exists('Item',i['item_code']):
                    newdoc = frappe.new_doc("Item")


                    
                    for key in  keys_list:
                        print(key,i[key])
                        
                        if key!='company' and key!='gst_hsn_code':

                            newdoc.set(key, i[key])
                        if key=='gst_hsn_code':
                            if  frappe.db.exists('GST HSN Code',i['name']):
                                newdoc.set(key, i[key])
                                



                    newdoc.save()


        datapath = frappe.get_app_path('a3sola_solar_management', 'product_bundle.json')

        with open(datapath, 'r') as file:
            data = json.load(file)
            fdict=data[0]
            keys_list = list(fdict)
            

            for i in data:

            # Assuming each item in the JSON represents a document
                print("New looopppppppppppppppppppppppppppppppppp bundleeeeeeeeeeeeeeeeeeeeee")
                if not  frappe.db.exists('Product Bundle',i['name']):
                    newdoc = frappe.new_doc("Product Bundle")


                    
                    for key in  keys_list:
                        print(key,i[key])
                    

                        newdoc.set(key, i[key])

                    newdoc.save()






















# def after_install():
#     frappe.get_doc({'doctype': "Task Type", "name": "Site Survey"}).insert()
#     frappe.get_doc({'doctype': "Task Type", "name": "Delivery Note"}).insert()
#     tl=frappe.get_list("Task Type")
#     print("Haii")
#     for i in tl:
#         tt=frappe.get_doc({'doctype': "Task Type", "name": i.name})
        
#         taskname=tt.name
#         if taskname=="Site Survey" or taskname=="Delivery Note":
#             pass
#         else:
#             frappe.get_doc({'doctype': "Task Type", "name": taskname}).insert()



# tl=frappe.get_list("Task Type")
# for i in tl:
#     t=frappe.get_doc({'doctype': "Task Type", "name": i.name})
#     tname=t.name
#     print(t.name)

	
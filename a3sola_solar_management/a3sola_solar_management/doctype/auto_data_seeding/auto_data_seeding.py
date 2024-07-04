# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



import os
import json
 

class AutoDataSeeding(Document):
	def validate(doc):

		if doc.product_bundle and not doc.item:
			frappe.throw("Items Required to create Product bundle")

		if doc.item and not doc.item_group:
			frappe.throw("Item Group Required to create Items")

		if doc.scheme:
			if not doc.project_template or not doc.electricity_board:
				frappe.throw("Project Template and Boards are Required to Scheme")
		
		if doc.project_template and not doc.task:
			
				frappe.throw("Tasks Required to Project Template")

		if doc.item:
			if not doc.scheme:
				frappe.throw("scheme are Required to Items")

		if doc.electricity_board and not doc.territory:
			frappe.throw("Territories are Required to Electricity Board")


		if doc.territory:
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


#check electricity_board is checked for seed
		if doc.electricity_board:
			#take corresponding json that store electricity board
			datapath = frappe.get_app_path('a3sola_solar_management', 'electricity_board.json')
			print("$$$$$$$$$$$$$$$$")
			print(datapath)

			with open(datapath, 'r') as file:
				data = json.load(file)
				fdict=data[0]
				keys_list = list(fdict)
				

				for i in data:

				# Assuming each item in the JSON represents a document create a new  document from it
					if not  frappe.db.exists('Electricity Board',i['name']):
						newdoc = frappe.new_doc("Electricity Board")

						
						for key in  keys_list:
							print(key,i[key])
							newdoc.set(key, i[key])

						newdoc.insert()

#working on same concept above
				
		if doc.task:
			
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

	
			


		if doc.project_template:

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



		if doc.scheme:
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

		if doc.item_group:
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
		if doc.item:
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

		if doc.product_bundle:

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


		if doc.print_formats:
			datapath = frappe.get_app_path('a3sola_solar_management', 'print_format.json')

			with open(datapath, 'r') as file:
				data = json.load(file)
				fdict=data[0]
				keys_list = list(fdict)
				

				for i in data:

				# Assuming each item in the JSON represents a document
					print("New looopppppppppppppppppppppppppppppppppp print format")
					if not  frappe.db.exists('Print Format',i['name']):
						newdoc = frappe.new_doc("Print Format")


						
						for key in  keys_list:
							print(key,i[key])
						

							newdoc.set(key, i[key])

						newdoc.save()



		if doc.project_setting:
			datapath = frappe.get_app_path('a3sola_solar_management', 'project_settings.json')

			with open(datapath, 'r') as file:
				data = json.load(file)
				fdict=data[0]
				keys_list = list(fdict)
				

				

				# Assuming each item in the JSON represents a document
				print("New looopppppppppppppppppppppppppppppppppp project settings")
				
				ps = frappe.get_doc("Project Settings")
				if ps.template_details:
					pass
					
				else:
				
					for key in  keys_list:
						print(key,fdict[key])
					
						if key=='template_details':
							if ps.template_details:
								pass
							else:
								ps.set(key, fdict[key])
						else:
							ps.set(key, fdict[key])
					ps.insert()
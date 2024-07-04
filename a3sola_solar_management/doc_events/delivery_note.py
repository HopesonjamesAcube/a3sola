import frappe
import re
def validate(doc,methods):

      doc.project_id=doc.project
      print("&$%^&&&&&&&&&&&&&&&&&&&")

      #Stock Alert item if it's quantity reaches reorder level based on items on items table
      if doc.items:
            for i in doc.items:
                  print(i.qty)
                  print(i.actual_qty)
                  
                  
                  
                  if i.actual_qty:
                        actual_qty=float(i.actual_qty)
                        qty=float(i.qty)
                        if actual_qty>qty:
                              projected_qty=actual_qty-qty
                              if i.reorder_level:
                                    reorder_level=float(i.reorder_level)
                                    if projected_qty<reorder_level:
                                          item=frappe.get_doc('Item',i.item_code)
                                          item.notification_reorder=1
                                          item.save()
      #Stock Alert item if it's quantity reaches reorder level based on items on packed_items table

      if doc.packed_items:
            for i in doc.packed_items:
                  if i.actual_qty:
                        actual_qty=float(i.actual_qty)
                        qty=float(i.qty)
                        
                        print(i.qty)
                        print(i.actual_qty)
                        if i.actual_qty>qty:
                              projected_qty=actual_qty-qty
                              print(projected_qty)
                              print(i.reorder_level)
                              if i.reorder_level:
                                    reorder_level=float(i.reorder_level)
                                    if projected_qty<reorder_level:
                                          item=frappe.get_doc('Item',i.item_code)
                                          item.notification_reorder=1
                                          item.save()
                                        
                              
                        
                     
                        
     




def after_insert(doc,methods):
      pass
      # sales_orders=frappe.get_all('Sales Order', filters={'Project': doc.project,'docstatus':1})
      # grand_total=0
      # paid_amout=0
      # if sales_orders:
      #       for i in sales_orders:
      #             print("status")
      # frappe.throw('Project is already linked with another sales order')



def on_submit(doc,methods):
   
      customer=frappe.get_doc('Customer',doc.customer)
      if customer.is_installer:
            warehouse=frappe.get_doc('Warehouse',customer.warehouse)
            material_receipt=frappe.new_doc('Stock Entry')
            material_receipt.stock_entry_type='Material Receipt'
            # material_receipt.from_warehouse=doc.set_warehouse
            material_receipt.to_warehouse=customer.warehouse
            for i in doc.items:
                  item=frappe.get_doc('Item',i.item_code)
                  if item.is_stock_item:
                        material_receipt.append('items',{
                              'item_code':i.item_code,
                              'item_name':i.item_name,
                              
                              'qty':i.qty,
                        })
            if doc.packed_items:
                    for i in doc.packed_items:
                        material_receipt.append('items',{'item_code':i.item_code,'item_name':i.item_name,'qty':i.qty})
            material_receipt.save()
            material_receipt.submit()
            frappe.msgprint('Stock Entry for material transfer ' f'<a href="/app/stock-entry/{material_receipt.name}" target="blank">{material_receipt.name} </a> Created Successfully ')
           

      
      sales_orders=frappe.get_all('Sales Order', filters={'Project': doc.project,'docstatus':1})
      per="100%"
      if sales_orders:
            for i in sales_orders:
                  salesorder=frappe.get_doc('Sales Order',i['name'])
                  print("^^^^^^^^^^^^^^^^^^^^^")
                  print(salesorder.per_delivered)
                  if salesorder.per_delivered!="100%":
                        status="not completed"

      if per=="100%":
            delivery_note_task=frappe.get_all('Task', filters={'Project': doc.project,'doctypes_name':"Delivery Note"})
            if delivery_note_task:
                  for i in delivery_note_task:
                        task=frappe.get_doc('Task',i['name'])
                        task.status="Completed"
                        if not task.d_id:
                              task.d_id=doc.name
                        
                        task.save()
            picklist_task=frappe.get_all('Task', filters={'Project': doc.project,'doctypes_name':"Pick List"})
            if picklist_task:
                  for i in picklist_task:
                        task=frappe.get_doc('Task',i['name'])
                        task.status="Completed"
                         
                        task.save()

      if doc.project:             
            doc.project_id=doc.project
            project=frappe.get_doc("Project",doc.project_id)
            count=0
            project.save()
            if doc.spv_serial_no:
                  for i in doc.spv_serial_no:
                              print(count)
                              project.append("serial_no",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})

                              if count==0:
                                    
                                    project.capacity_in_watts=i.each_module_watts   
                                    project.panel_make=i.spv_module_make
                                    project.panel_type=i.spv_module_type

                              count=count+1
            print(count)   


            if doc.inverter_serial_no:
                  count=0
                  
                  for i in doc.inverter_serial_no:
                        if count==0:
                              project.inverter_capacity=int(re.search(r'\d+', i.capacity_of_inverter).group())
                        project.append("inverter_serial_no",{"make":i.make,"capacity_of_inverter":i.capacity_of_inverter,"inverter_serial_no":i.inverter_serial_no})
                        count=count+1

                  capacity_in_watts=str(project.capacity_in_watts)

                  capacity_in_watts=int(re.search(r'\d+', capacity_in_watts).group())
                  project.capacity_in_watts=capacity_in_watts
                  project.number_of_panels=count
                  project.total_capacity=count*int(project.capacity_in_watts) 

                  project.save()
            

def on_update(doc,methods):
      
      if doc.project:
            doc.project_id=doc.project
            project=frappe.get_doc("Project",doc.project_id)
            count=0
            project.save()
            if doc.spv_serial_no:
                  project.serial_no.clear()
                  for i in doc.spv_serial_no:
                              print(count)
                              project.append("serial_no",{"spv_module_make":i.spv_module_make,"each_module_watts":i.each_module_watts,"spv_module_type":i.spv_module_type,"spv_serial_no":i.spv_serial_no,"no_of_modules":i.no_of_modules})

                              if count==0:
                                    
                                    project.capacity_in_watts=i.each_module_watts   
                                    project.panel_make=i.spv_module_make
                                    project.panel_type=i.spv_module_type

                              count=count+1
            print(count)   


            if doc.inverter_serial_no:
                  count=0
                  
                  for i in doc.inverter_serial_no:
                        project.inverter_serial_no.clear()
                        if count==0:
                              project.inverter_capacity=int(re.search(r'\d+', i.capacity_of_inverter).group())
                              project.append("inverter_serial_no",{"make":i.make,"capacity_of_inverter":i.capacity_of_inverter,"inverter_serial_no":i.inverter_serial_no})
                              count=count+1

            capacity_in_watts=str(project.capacity_in_watts)

            capacity_in_watts=int(re.search(r'\d+', capacity_in_watts).group())
            project.capacity_in_watts=capacity_in_watts
            project.number_of_panels=count
            project.total_capacity=count*int(project.capacity_in_watts) 

            project.save()





@frappe.whitelist(allow_guest=True)
def test(doc,pro):

        project = frappe.get_doc('Project',pro)

        print(project.primary_address)
        print(project.customer)

        d={'customer':project.customer}

        # return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
        print(d)
        return d

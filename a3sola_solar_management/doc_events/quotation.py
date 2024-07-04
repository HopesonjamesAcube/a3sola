import frappe
from a3sola_solar_management.attach_document import attach_pdf


# def on_update(doc, methods):
#     if doc.pdf_url:
#         getfile=frappe.get_doc("File",{"file_url":doc.pdf_url})
#         res = getfile.name
#         print(res,"ghjklkjhgghjkkjhgghjkjhhjjhghjjhghjjhfk")
#         frappe.db.delete("File",res)
#         fallback_language = frappe.db.get_single_value("System Settings", "language") or "en"
#         args = {
#             "doctype": doc.doctype,
#             "name": doc.name,
#             "title": doc.get_title(),
#             "lang": getattr(doc, "language", fallback_language),
#             "show_progress": 0
#         }
#         fileurl = execute(**args)
#         doc.pdf_url = fileurl

#         attachments = frappe.get_all("File", filters={"attached_to_doctype":doc.doctype, "attached_to_name":doc.name}, fields=["name", "file_url"])
#         for attachment in attachments:
#             if attachment["file_url"] != fileurl:
#                 attach = get_doc("File", attachment["name"])
#                 attach.delete()



def on_submit(doc,methods):
#complete the corresponing quotation task automatically if it submitted
    if doc.project_id:
        protasks=frappe.get_list("Task",filters={"project": doc.project_id},order_by='name asc')
        for i in protasks:
            task=frappe.get_doc("Task",i)
            task.quotation=doc.name
            if task.doctypes_name=="Quotation":
                task.d_id=doc.name
                task.status="Completed"

                frappe.msgprint('Quotation Task Completed" ' f'<a href="/app/task/{task.name}" target="blank">{task.name} </a> ')
            task.save()


            print(task.quotation)
            # attach_pdf(doc)




def after_insert(doc,methods):
    pass
    # print("afterrrrrrrrrrr")
    # fileurl,url=attach_pdf(doc)
    # doc.pdf_doc=fileurl
    # doc.attachment_url=url






        
    doc.save()

import re


def validate(doc,methods):
    product_bun=0
    for i in doc.items:
            item=frappe.get_doc("Item",i.item_code)
            if item.scheme_name:
                product_bun=item.name
                


                #if scheme based spec and terms defined in project setting auto fetch that to quote
                settings=frappe.get_doc("Project Settings")
                if settings.template_details:
                        template_details=settings.template_details
                        for tem in template_details:
                            if tem.scheme:
                                if item.scheme_name==tem.scheme:
                                    if tem.terms:
                                        doc.tc_name=tem.terms
                                    if tem.print_spec:
                                        doc.quoation_print_specification=tem.print_spec
                                break
                if settings.quotation_letter_head:
                    doc.letter_head=settings.quotation_letter_head
        


    # if product bundle available on item fetch capasity from it's name.
    #fetch capasity and terms and condition details from bundle if it's defined
    if product_bun:
        bundle=frappe.get_doc("Product Bundle",product_bun)
        if not bundle.capacity_of_plant:
            capacity=int(re.search(r'\d+', product_bun).group())
        else:
            capacity=int(bundle.capacity_of_plant)


        if capacity:
            doc.required_capacity=capacity

        if bundle.terms_and_condition:
            doc.tc_name=bundle.terms_and_condition

        if bundle.yearly_generation:
            doc.annual_generation=bundle.yearly_generation

        if bundle.required_area:
            doc.total_area=bundle.required_area


        
    # discount=0
    
    # for i in doc.items:
    #     if i.discount_item:
    #         discount=discount+i.amount
    #         # i.discount_amoount=i.base_price_list_rate
           
    #         # print(i.discount_amoount)
    
    # if discount>0:
    #     doc.item_discounts=discount

    #     if doc.item_discounts_last:
    #         additonal_discount=doc.discount_amount-doc.item_discounts_last
    #         doc.discount_amount=additonal_discount+discount
    #     else:
    #         if doc.discount_amount:
    #             doc.discount_amount=discount+doc.discount_amount
    #         else:
    #             doc.discount_amount=discount
              

    #     doc.item_discounts_last=discount
        
    # else:
    #     if doc.item_discounts_last:
    #         additonal_discount=additonal_discount=doc.discount_amount-doc.item_discounts_last
    #         doc.discount_amount=additonal_discount

    


# fetch print specification details only in the table system specification is empty

    if not doc.system_specification:

        if not doc.quoation_print_specification:
            bundle=''
            for i in doc.items:
                item=frappe.get_doc("Item",i.item_code)
                if item.scheme_name:
                    bundle=item.name
        

            if bundle:
                if frappe.db.exists("Quotation Print Specification",bundle):
                    priqu=frappe.get_doc("Quotation Print Specification",bundle)
                    


                    #fetch data from print spec
                    doc.quoation_print_specification=priqu.name
                    doc.system_specification.clear()


                    doc.total_spec_amount=priqu.total_spec_amount
                    doc.include_total_row_spec=priqu.include_total_row_spec
                    doc.exclude_quantity=priqu.exclude_quantity
                    doc.specification_notes=priqu.specification_notes
                    doc.additional_spec_notes=priqu.additional_spec_notes
                    doc.exclude_total=priqu.exclude_total
                    doc.header=priqu.header
                    doc.include_gst_row=priqu.include_gst_row
                    if priqu.exclude_image:
                        doc.exclude_image=priqu.exclude_image
                    doc.include_page_number=priqu.page_number
                    doc.exclude_amount=priqu.exclude_amount
                    doc.exclude_total=priqu.exclude_total
                    doc.exclude_make=priqu.exclude_make

                    # additional system rates fetching
                    doc.include_total_row2=priqu.include_total_row2
                    doc.exclude_spec2=priqu.exclude_spec2
                    doc.exclude_quanitity2=priqu.exclude_quanitity2
                    doc.exclude_unit_price2=priqu.exclude_unit_price2
                    doc.additional_spec_notes=priqu.additional_spec_notes
                    doc.exclude_tax_column2=priqu.exclude_tax_column2
                    

                    # system rates fetching
                    doc.total_system_rate=priqu.total_system_rate
                    doc.include_total_row1=priqu.include_total_row
                    doc.exclude_spec=priqu.exclude_spec
                    doc.exclude_quanitity=priqu.exclude_quanitity
                    doc.exclude_unit_price=priqu.exclude_unit_price
                    doc.exclude_tax_column=priqu.exclude_tax_colum
                    doc.exclude_total_column=priqu.exclude_total_column
                    doc.rate_notes=priqu.rate_notes
                    doc.exclude_tax_colum=priqu.exclude_tax_colum
                    


                    doc.specification_rates.clear()    
                    for i in priqu.specification_rates:
                        doc.append("specification_rates",{"spec_item":i.spec_item,"spec_details":i.spec_details,"quantity":i.quantity,"unit_price":i.unit_price,"tax_rate":i.tax_rate,"item_tax":i.item_tax,"total_amount":i.total_amount})


                    for i in priqu.system_specification:
                    
                        doc.append("system_specification",{"item":i.item,"specification":i.specification,"qty":i.qty,"make":i.make,"warranty_period":i.warranty_period,"amount":i.amount})
                    doc.quotation_print_images.clear()
                    for i in priqu.other_attachment:
                        doc.append("quotation_print_images",{"order_number":i.order_number,"attachment":i.attachment,"specification":i.specification,"make":i.make,"item_name":i.item_name})

                    produc_bundle=frappe.get_doc("Product Bundle",bundle)
                    
                    for i in produc_bundle.items:
                        if i.print_on_quotation:
                    
                            doc.append("system_specification",{"item":i.item,"specification":i.specification,"qty":i.qty,"make":i.make,"warranty_period":i.warranty_period,"amount":i.amount})
                    doc.additional_points.clear()   
                    doc.additional_points_2.clear() 
                    doc.kseb_charges.clear() 
                    doc.feasibility.clear() 
                    for i in priqu.additional_points:
                        doc.append("additional_points",{"content":i.content})   
            
                    for i in priqu.additional_points_2:
                        doc.append("additional_points_2",{"content":i.content})  
                    
                    for i in priqu.kseb_charges:
                        print("$$$$")
                        print(i.kseb_charge)
                        
                        doc.append("kseb_charges",{"kseb_charge":i.kseb_charge,"additional_spec_item":i.additional_spec_item,"additional_spec_detail":i.additional_spec_detail,"unit_rate":i.unit_rate,"tax_rate":i.tax_rate,"item_tax":i.item_tax,"total_amount":i.total_amount,"quantity":i.quantity,"phase__3_amount":i.phase__3_amount,"phase_1_amount":i.phase_1_amount})  

                    doc.phase_1_total=priqu.phase_1_total
                    doc.phase_3_total=priqu.phase_3_total 
                    for i in priqu.feasibility:
                        doc.append("feasibility",{"content":i.content})  
            
                     
                        
        else:
                bundle=''
                for i in doc.items:
                    item=frappe.get_doc("Item",i.item_code)
                    if item.scheme_name:
                        bundle=item.name
            
                priqu=frappe.get_doc("Quotation Print Specification",doc.quoation_print_specification)


                #fetch data from print spec
                doc.system_specification.clear()


                doc.total_spec_amount=priqu.total_spec_amount
                doc.include_total_row_spec=priqu.include_total_row_spec
                doc.exclude_quantity=priqu.exclude_quantity
                doc.specification_notes=priqu.specification_notes
                doc.additional_spec_notes=priqu.additional_spec_notes
                doc.exclude_total=priqu.exclude_total
                doc.header=priqu.header
                doc.include_gst_row=priqu.include_gst_row
                doc.include_page_number=priqu.page_number
                doc.exclude_amount=priqu.exclude_amount
                if priqu.exclude_image:
                    doc.exclude_image=priqu.exclude_image
                doc.exclude_total=priqu.exclude_total
                doc.include_total_row2=priqu.include_total_row2
                doc.exclude_spec2=priqu.exclude_spec2
                doc.exclude_quanitity2=priqu.exclude_quanitity2
                doc.exclude_unit_price2=priqu.exclude_unit_price2
                doc.additional_spec_notes=priqu.additional_spec_notes
                doc.exclude_tax_column2=priqu.exclude_tax_column2
                doc.exclude_make=priqu.exclude_make


                # system rates fetching
                doc.total_system_rate=priqu.total_system_rate
                doc.include_total_row1=priqu.include_total_row
                doc.exclude_spec=priqu.exclude_spec
                doc.exclude_quanitity=priqu.exclude_quanitity
                doc.exclude_unit_price=priqu.exclude_unit_price
                doc.exclude_tax_column=priqu.exclude_tax_colum
                doc.exclude_total_column=priqu.exclude_total_column
                doc.rate_notes=priqu.rate_notes
                doc.exclude_tax_colum=priqu.exclude_tax_colum

                doc.specification_rates.clear()    
                for i in priqu.specification_rates:
                    doc.append("specification_rates",{"spec_item":i.spec_item,"spec_details":i.spec_details,"quantity":i.quantity,"unit_price":i.unit_price,"tax_rate":i.tax_rate,"item_tax":i.item_tax,"total_amount":i.total_amount})





                for i in priqu.system_specification:
                    
                    doc.append("system_specification",{"item":i.item,"specification":i.specification,"qty":i.qty,"make":i.make,"warranty_period":i.warranty_period,"amount":i.amount,"image":i.image})
                doc.quotation_print_images.clear()    
                for i in priqu.other_attachment:
                    doc.append("quotation_print_images",{"order_number":i.order_number,"attachment":i.attachment,"specification":i.specification,"make":i.make,"item_name":i.item_name})


                if frappe.db.exists("Product Bundle",bundle):
                    produc_bundle=frappe.get_doc("Product Bundle",bundle)
                    
                    
                    for i in produc_bundle.items:
                        if i.print_on_quotation:
                        
                            doc.append("system_specification",{"item":i.item,"specification":i.specification,"qty":i.qty,"make":i.make,"warranty_period":i.warranty_period,"amount":i.amount})
                doc.additional_points.clear()   
                doc.additional_points_2.clear() 
                for i in priqu.additional_points:
                    doc.append("additional_points",{"content":i.content})   
                    
                for i in priqu.additional_points_2:
                    doc.append("additional_points_2",{"content":i.content})   
                
                doc.kseb_charges.clear() 
                doc.feasibility.clear() 

                for i in priqu.kseb_charges:
                        print(i.kseb_charge)
                        
                        
                        doc.append("kseb_charges",{"kseb_charge":i.kseb_charge,"additional_spec_item":i.additional_spec_item,"additional_spec_detail":i.additional_spec_detail,"unit_rate":i.unit_rate,"tax_rate":i.tax_rate,"item_tax":i.item_tax,"total_amount":i.total_amount,"quantity":i.quantity,"phase__3_amount":i.phase__3_amount,"phase_1_amount":i.phase_1_amount}) 
                doc.phase_1_total=priqu.phase_1_total
                doc.phase_3_total=priqu.phase_3_total

                for i in priqu.feasibility:
                        doc.append("feasibility",{"content":i.content}) 


    # bundle=''
    # for i in doc.items:
    #     item=frappe.get_doc("Item",i.item_code)
    #     if item.scheme_name:
    #         bundle=item.name

    # if bundle:
    
    #     bundle=frappe.get_doc("Product Bundle",bundle)

    #     for i in bundle.items:
    #         for j in doc.packed_items:
    #             print(i.item_code,j.item_code)
    #             if i.item_code==j.item_code:
    #                 if j.update_quantity:
    #                     print(i.qty,j.update_quantity)
    #                     print("updateeeee")
    #                     if j.update_quantity!=i.qty:
                            
    #                         i.qty=j.update_quantity
                            

    #     bundle.save()
    #     doc.standard_rate=1
                        




@frappe.whitelist(allow_guest=True)
def before(doc,pack):
    
    print(type(pack))
    quota=frappe.get_doc("Quotation",doc)
    print("beforeeeeeeeeeeeeee")
    print(pack)

    if pack:
        false=False
        res =eval(pack)
    

        for i in res:
            print(i)
            print(type(i))


        bundle=''
        for i in quota.items:
            item=frappe.get_doc("Item",i.item_code)
            if item.scheme_name:
                bundle=item.name

        if bundle:
            bundle=frappe.get_doc("Product Bundle",bundle)

            for i in bundle.items:
                for j in res:
                    print(i.item_code,j['item_code'])
                    if i.item_code==j['item_code']:
                        if j['update_quantity']:
                            print(i.qty,j['update_quantity'])
                            if ['update_quantity']!=i.qty:
                                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                                print(i.qty,j['update_quantity'])
                                i.qty=j['update_quantity']
                                
                                
                
            bundle.save()


    return 1
        





    # for i in pack:
    #     print(i.item_code)
    
       
    
    
    # if not doc.quoation_print_specification:
    #     bundle=''
    #     for i in doc.items:
    #         item=frappe.get_doc("Item",i.item_code)
    #         if item.scheme_name:
    #             bundle=item.name
    

    #     if bundle:
    #         priqu=frappe.get_doc("Quoation Print Specification",bundle)
    #         doc.quoation_print_specification=priqu.name

    #     doc.save()



    


# @frappe.whitelist(allow_guest=True)
# def before(doc):
#     print("beforeeeeeeeeeeeeee")
   
#     doc=frappe.get_doc("Quotation",doc)
#     fileurl,url=attach_pdf(doc)
#     doc.pdf_doc=fileurl
#     doc.attachment_url=url
#     print(doc.pdf_doc,"pdf_doc")
#     doc.save()
   



# def onupdate(doc,methods):
  
#     on_update(doc,methods)



# To access externally




@frappe.whitelist(allow_guest=True)
def test(doc,pro):
    print(doc,"hiiiii++++++++++++++++++++++++++++++++++++++++++++++")
    print(pro)
    project = frappe.get_doc('Project',pro)


    d={'cadd':project.address,'customer':project.customer,'opp':project.oppertunity,'consno':project.consumer_number,'roof':project.type_of_roof,'consno:':project.consumer_number}

    # return frappe.db.sql(f"""SELECT *  FROM tabCustomer WHERE opportunity_name='CRM-OPP-2022-00002'""",as_dict=True)
    # print(d)
    return d
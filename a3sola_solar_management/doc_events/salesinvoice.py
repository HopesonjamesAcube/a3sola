import frappe
from num2words import num2words

def validate(doc,methods):
    if doc.project_id:
        if frappe.db.exists("Project",doc.project_id):
            proj=frappe.get_doc("Project",doc.project_id)
            if proj:
                if proj.item_name:
                    if frappe.db.exists("Product Bundle",proj.item_name):
                        prod_b=frappe.get_doc("Product Bundle",proj.item_name)
                        if prod_b:
                            if frappe.db.exists("Item Price",{"item_code":prod_b.name,"price_list":"Standard Selling"}):
                                item_price=frappe.get_doc("Item Price",{"item_code":prod_b.name,"price_list":"Standard Selling"})
                                if item_price:
                                    if item_price.price_list_rate:
                                        price_val=item_price.price_list_rate
                                        if price_val:
                                            price_val_in_words=num2words(price_val)
                                            if price_val_in_words:
                                                doc.si_amount=price_val_in_words
                                            price_70=price_val*0.70
                                            if price_70:
                                                tax_70=price_70*0.12
                                                tax_70_words=num2words(tax_70)
                                                print(tax_70_words,"jjjjjjjjjjjjjjj")
                                            price_30=price_val*0.30
                                            if price_30:
                                                tax_30=price_30*0.18
                                                tax_30_words=num2words(tax_30)
                                                print(tax_30_words,"jjjjjj77777777777777jjjjjjjjj")
                                            if tax_30 and tax_70:
                                                total_tax_si=tax_30+tax_70
                                                if total_tax_si:
                                                    total_tax_si_words=num2words(total_tax_si)
                                                    if total_tax_si_words:
                                                        doc.si_tax_amount=total_tax_si_words
                                                

                                            
                                
                                

    doc.project=doc.project_id

    print(doc.tax_9)
    t9=0
    t6=0
    print('^^^^^^^^^^^')

    discount_amount=0
    #getting tax 9% tax 6% and item price
    if doc.items:
        for i in doc.items:
            item = frappe.get_doc("Item",i.item_code)
            if i.item_tax_template:    
                if '18' in  i.item_tax_template:
                    t9=((i.rate*9)/100)
                    t9 = round(t9, 2)
                    print(t9)
                    
                    
                    doc.tax_9=t9
                    doc.inv_service=i.rate

                if '12' in  i.item_tax_template:
                    t6=((i.rate*6)/100)

                    t6 = round(t6, 2)
                    print(t6)
                    doc.tax_6=t6
                    
                    
                    doc.inv_solar=i.rate


                if i.discount_amount:
                        discount_amount=discount_amount+i.discount_amount

        print('^^^^^^^^^^^')
        print(discount_amount)
#calculate total tax total of 6% and 9% and update to corresponding fileds
        if t9 and t6:    
        
            total_tax9=round(t9*2, 2)
            total_tax6=round(t6*2, 2)
            doc.total_tax9=total_tax9
            doc.total_tax6=total_tax6


            doc.tax_69=round(t9+t6, 2)

            total_tax=total_tax9+total_tax6

        
            total_tax = round(total_tax, 2)
            doc.tax_total_=total_tax

            
            
            doc.subsidy=discount_amount

            not_rounded=doc.total+total_tax+discount_amount
            rounded=round(doc.total+total_tax+discount_amount)

            if rounded>not_rounded:
                roundoff=rounded-not_rounded
            else:
                roundoff=not_rounded-rounded
            print(rounded)
            print(not_rounded)
            print(roundoff)

            doc.roundoff=round(roundoff, 2)

            doc.total_include_subsidy=rounded
            
            doc.total_taxable=doc.total




def on_submit(doc,methods):
    if doc.project_id:
        protasks = frappe.get_list("Task", filters={"project": doc.project_id}, order_by='name asc')
        for task_data in protasks:
            task = frappe.get_doc("Task", task_data.name)
            if task.doctype == 'Sales Invoice':
                # Assuming 'sales_invoice' is a field in the Task doc
                task.sales_invoice = doc.name
                task.save()
                print(task.sales_invoice)


    if doc.items:
        da=0
        journal=0
        for row in doc.items:
            if row.item_code:
                item=frappe.get_doc("Item",row.item_code)
                print(item)
                if item.scheme_name:
                    scheme=frappe.get_doc("Scheme",item.scheme_name)
                    print(scheme)

                    if scheme.subsidy_paid_to=="Installer":
                        rs=scheme.receivable_account
                        ia=scheme.income_account
                        print(scheme)
                        da=da+row.discount_amount
                        print(da)
                        journal=1
        if journal==1:
            je=frappe.new_doc("Journal Entry")
            je.append("accounts",{"account":rs,"party_type":"Customer","party":scheme.provided_by,"debit_in_account_currency":da})
            je.append("accounts",{"account":ia,"credit_in_account_currency":da})
            je.user_remark="Created against "+ doc.name
            je.save()
            je.submit()
            frappe.msgprint('Journal Entry ' f'<a href="/app/journal-entry/{je.name}" target="blank">{je.name} </a> Submitted Successfully ')




@frappe.whitelist(allow_guest=True)
def si_items(pro):
    s = []
    # Get the project to find the corresponding product bundle item
    pro_doc = frappe.get_doc("Project", pro)

    # Initialize default_comp_acc with a default value
    def_comp_acc = None

    if frappe.db.exists("Global Defaults"):
        global_val=frappe.get_doc("Global Defaults")
        if global_val.default_company:
            default_comp=global_val.default_company
            if default_comp:
                if frappe.db.exists("Company",default_comp):
                    comp=frappe.get_doc("Company",default_comp)
                    if comp:
                        if comp.default_income_account:
                            def_comp_acc=comp.default_income_account
                            print(def_comp_acc)
    if pro_doc.item_name:
        
        # Check existence of product bundle, if exists get invoice items that used for invoice creation
        if frappe.db.exists("Product Bundle", pro_doc.item_name):
            if frappe.get_list("Item", filters={"product_bundle": pro_doc.item_name}):
                inv_items = frappe.get_list("Item", filters={"product_bundle": pro_doc.item_name})
                print("***************")
                print(inv_items, "val_err")

                
                    
                price=0
                for item in inv_items:
                    doc_val = frappe.get_doc("Item", item.name)
                    print(doc_val, "documents")
                    print(item.name)
                    if frappe.db.exists("Item Price",{"item_code":item.name,"price_list":"Standard Selling"}):
                        val=frappe.get_doc("Item Price",{"item_code":item.name,"price_list":"Standard Selling"})
                        print(val,"'''''''''")
                        if val:
                            print("val",val)
                            if val.price_list_rate:
                                # print(val.price_list_rate,"---------------")
                                price=val.price_list_rate
                    # Create a new dictionary for each item
                    item_val = {
                        "itemcode": doc_val.item_code,
                        "itemname": doc_val.item_name,
                        "stockuom": doc_val.stock_uom,
                        "default_comp_acc": def_comp_acc,
                        "price":price
                    }
                    s.append(item_val)
                    

               
                # frappe.throw("error")
                return(s)


            else:
                price1=0
                if frappe.get_doc("Product Bundle", pro_doc.item_name):
                    prod_bundle=frappe.get_doc("Product Bundle", pro_doc.item_name)
                    if prod_bundle:
                        if prod_bundle.invoice_item_details:
                            for j in prod_bundle.invoice_item_details:
                                print(j,"ppppppppppppppppppp")
                                
                                if j.item_name:
                                    print(j.item_name)
                                    if frappe.db.exists("Item",j.item_name):
                                        sal_item=frappe.get_doc("Item",j.item_name)
                                        print(sal_item.name,";;;;;;;;;;;;;;;;;;;;;;;;;;;;")
                                        
                                        if frappe.db.exists("Item Price",{"item_code":sal_item.name,"price_list":"Standard Selling"}):
                                            sal_item_price=frappe.get_doc("Item Price",{"item_code":sal_item.name,"price_list":"Standard Selling"})
                                            if sal_item_price:
                                                
                                                if sal_item_price.price_list_rate:
                                                    # print(val.price_list_rate,"---------------")
                                                    price1=sal_item_price.price_list_rate
                                            
                                        # Create a new dictionary for each item
                                        item_val = {
                                            "itemcode": sal_item.item_code,
                                            "itemname": sal_item.item_name,
                                            "stockuom": sal_item.stock_uom,
                                            "default_comp_acc": def_comp_acc,
                                            "price":price1
                                        }
                                        s.append(item_val)
                            return(s)

            
                


            #     # Create a new dictionary for each item
            #     item_val = {
            #         "itemcode": doc_val.item_code,
            #         "itemname": doc_val.item_name,
            #         "stockuom": doc_val.stock_uom,
            #         "default_comp_acc": def_comp_acc,
            #         "price":price
            #     }
            #     print(item_val, "::::::::::::::::::::")
            #     s.append(item_val)
            #     print(s, ",,,,,,,,,,,,,,,,,,,,,,,,,,,")

            # print(s, "valueeeeeeeeeeeeee")
            # # frappe.throw("error")
            # return(s)

    

                            

        

        
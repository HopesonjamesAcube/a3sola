import frappe

def after_insert(doc,methods):


#create pricing rule for discount for all items under scheme
    if doc.scheme_name:


        
        scheme=frappe.get_doc("Scheme",doc.scheme_name)
        if scheme.subsidy_type=="Subsidy Percentage":
            if scheme.subsidy_percentage:
                prname=doc.name+" Pricing Rule"
                print(prname)
                percentage=scheme.subsidy_percentage

                exist=frappe.db.exists("Pricing Rule",{"title":prname})
                print(exist)
                if not exist:



                    pr=frappe.new_doc("Pricing Rule")
                    e="no"
                    pr.rate_or_discount="Discount Percentage"
                    pr.discount_percentage=percentage
                    print("hiii")




                else:

                    pr=frappe.get_doc("Pricing Rule",{"title":prname})
                    e="yes"
                    pr.rate_or_discount="Discount Percentage"
                    pr.discount_percentage=percentage
                    pr.items.clear()
                pr.title=prname
                print(pr.title)
                print("$$$$$$$$$$$$$$$")
                pr.apply_on="Item Code"
                pr.price_or_product_discount="Price"
                pr.append("items",{"item_code":doc.name,"uom":"Nos"})
                pr.selling=1

                pr.save()
                if e=="no":
                    frappe.msgprint("Pricing Rule for "+doc.name+" Created")
                else:
                    frappe.msgprint("Pricing Rule for "+doc.name+" Updated")

        if scheme.subsidy_type=="Subsidy Amount":
            if scheme.subsidy_amount:
                prname=doc.name+" Pricing Rule"
                amount=scheme.subsidy_amount


                exist=frappe.db.exists("Pricing Rule",{"title":prname})
                if not exist:
                    print("2amounttttttttttt")

                    
                    pr=frappe.new_doc("Pricing Rule")
                    e="no"
                    pr.rate_or_discount="Discount Amount"
                    pr.discount_amount=amount

                else:


                    pr=frappe.get_doc("Pricing Rule",{"title":prname})
                    e="yes"
                    pr.items.clear()
                    pr.rate_or_discount="Discount Amount"
                    pr.discount_amount=amount
                pr.title=prname
                print(pr.title)
                print("$$$$$$$$$$$$$$$")
                pr.apply_on="Item Code"
                pr.price_or_product_discount="Price"
                pr.append("items",{"item_code":doc.name,"uom":"Nos"})
                pr.selling=1

                pr.save()
                if e=="no":
                    frappe.msgprint("Pricing Rule for "+doc.name+" Created")
                else:
                    frappe.msgprint("Pricing Rule for "+doc.name+" Updated")


        

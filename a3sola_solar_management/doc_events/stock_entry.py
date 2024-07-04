import frappe

def validate(doc,methods):

    if doc.stock_entry_type=="Material Issue":
        # frappe.throw("eroorrr")
        if doc.items:
            for i in doc.items:
                if i.allow_zero_valuation_rate==1:
                    i.basic_rate=0
                
    
        
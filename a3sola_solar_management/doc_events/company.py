import frappe
import re
#validation for mobile number
def validate(doc,methods):
    if doc.phone_no:
        r=re.fullmatch('[6-9][0-9]{9}',doc.phone_no)
        if r!=None: 
            pass
        
        else:
            frappe.throw("Please Enter a Valid Phone number ")
    if  doc.support_mail_:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, doc.support_mail_)):
            pass
        else:
            frappe.throw("Please Check Your Email ID")

    # doc_pb=frappe.get_doc("DocType",'Product Bundle')
    # doc_pb.append('links',{'link_doctype':'Quotation Print Specification','link_fieldname':'product_bundle'})
    # doc_pb.append('links',{'link_doctype':'Item','link_fieldname':'invoice_item_for_bundle'})

    # doc_pb.save()


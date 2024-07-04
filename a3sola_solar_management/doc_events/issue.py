import frappe

def validate(doc,methods):
    if doc.opportunity:

        opp=frappe.get_doc("Opportunity",doc.opportunity)
        if opp.project_id:
            doc.project=opp.project_id
        doc.customer=opp.customer
        if opp.opportunity_from=="Lead":
            doc.lead=opp.party_name

        if opp.contact_number:
            doc.contact_number=opp.contact_number
        


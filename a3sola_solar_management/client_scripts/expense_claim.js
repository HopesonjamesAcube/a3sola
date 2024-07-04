frappe.ui.form.on('Expense Claim', {
    sales_person_travel:function(frm){
    if(frm.doc.sales_person_travel){
        frappe.call({
            method: "a3sola_solar_management.a3sola_solar_management.doctype.sales_person_travel.sales_person_travel.get_sales_person_travel",
            //Passing variables as arguments with request
            args: {
                doc:frm.doc.sales_person_travel
                  
            },
            
            //Function passed as an argument to above function. 
            callback: function(r) {
                console.log(r.message)
                frm.set_value("employee",r.message.empl)
                frm.refresh_field("employee")
                frm.set_value("expense_approver",r.message.approver)
                frm.refresh_field("expense_approver")
                frm.clear_table("expenses")
                const target_row = frm.add_child("expenses")
                target_row.expense_date = r.message.date
                target_row.expense_claim_type = "Travel"
                frm.refresh_field("expenses")
            }
        
        })

    }
}
})
// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales Person Travel', {
	user: function(frm) {
		if(frm.doc.user){
		frappe.call({
			method:"a3sola_solar_management.a3sola_solar_management.doctype.sales_person_travel.sales_person_travel.get_employee_id",
			args:{
				user:frm.doc.user,
			},
			callback:function(r){
				if(r.message["employee"]){
					frm.set_value("employee_id",r.message["employee"])
					
				}
				else{
					frm.set_value("employee_id","")
				}
			}

		})

		}else{
			frm.set_value("employee_id","")
		}
	}
});

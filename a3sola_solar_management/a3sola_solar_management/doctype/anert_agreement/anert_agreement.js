// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('ANERT AGREEMENT', {
	// refresh: function(frm) {

	// }


	// refresh: function(frm) {


	

	onload: function (frm) {
		var prev_route = frappe.get_prev_route();



		if (prev_route[1] === 'Task') {

			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );




			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.anert_agreement.anert_agreement.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
				},

				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)


				console.log(frm.customer)
							

				if(r.message.customer)
					{cur_frm.set_value("customer",r.message.customer);
				}						
				if(r.message.cadd)
					{
						cur_frm.set_value("address",r.message.cadd);
				}	
				if(r.message.amount)
					{
						cur_frm.set_value("project_cost",r.message.amount);
				}						
				

				

				frm.refresh_field('address');
				
				frm.refresh_field('customer');
				frm.refresh_field('project_cost')


					   },


				});






		}
	}

});

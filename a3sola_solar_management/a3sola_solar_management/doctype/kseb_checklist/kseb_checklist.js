// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('KSEB Checklist', {
	// refresh: function(frm) {

	// }


	onload: function (frm) {
		var prev_route = frappe.get_prev_route();



		if (prev_route[1] === 'Task') {

			let source_doc = frappe.model.get_doc('Task', prev_route[2]);

			
			frm.set_value("project_id",source_doc.project );
			frm.set_value("name_of_solar_plant_owner",source_doc.customer)
			


			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.kseb_checklist.kseb_checklist.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
				},

				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)


				

				
				// cur_frm.set_value("customer_address",r.message.cadd);
				if(r.message.consno!=undefined){
				cur_frm.set_value("consumer_number",r.message.consno);
				}

				if(r.message.section!=undefined){
					cur_frm.set_value("name_of_electrical_section",r.message.section);
				}

				if(r.message.email!=undefined){
					cur_frm.set_value("email_id",r.message.email);
				}

				if(r.message.address!=undefined){
					cur_frm.set_value("address",r.message.address);
				}

				// if(r.message.address!=undefined){
				// 	cur_frm.set_value("consumer_number",r.message.address);
				// }

				if(r.message.cont_no!=undefined){
					cur_frm.set_value("contact_number_of_consumer",r.message.cont_no);
				}

				// if(r.message.consno!=undefined){
				// 	cur_frm.set_value("consumer_number",r.message.consno);
				// }

				



					   },


				});






		}
	}
});

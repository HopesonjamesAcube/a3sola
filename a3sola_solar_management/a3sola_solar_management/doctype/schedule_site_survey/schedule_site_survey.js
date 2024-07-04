// Copyright (c) 2022, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Schedule Site Survey', {
	validate: function(frm) {
		console.log("haii")
		if(frm.doc.assigned_to){
		frappe.call({
			// specify the server side method to be called.
			//dotted path to a whitelisted backend method
			method: "a3sola_solar_management.a3sola_solar_management.doctype.schedule_site_survey.schedule_site_survey.test",
			//Passing variables as arguments with request
			args: {
				doc:frm.doc.name,
				pro:frm.doc.project_id,
			},

			//Function passed as an argument to above function.
			callback: function(r) {
			//To show message
			console.log(r.message.tas)
			console.log(frm.doc.assigned_to)
										frappe.call({
										// specify the server side method to be called.
										//dotted path to a whitelisted backend method
										method: "frappe.desk.form.assign_to.add",
										//Passing variables as arguments with request
										args: {
											 assign_to: [frm.doc.assigned_to],
											 doctype: 'Task',
												name: r.message.tas,
										},

										//Function passed as an argument to above function.
										callback: function(r) {

										}
									});//inner frappe call


					 },


			});

		}




	},

	onload: function (frm) {
		var prev_route = frappe.get_prev_route();



		if (prev_route[1] === 'Task') {

			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );
			frm.set_value("lead_name",source_doc.lead_id);
			frm.set_value("opportunity_id",source_doc.opportunity);


			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.schedule_site_survey.schedule_site_survey.test",
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

				cur_frm.set_value("customer_name",r.message.customer);

				frm.refresh_field('customer_address');
				frm.refresh_field('customer_name');


					   },


				});






		}
	}
});


// frappe.msgprint(project.customer);
// 			frm.set_value("customer_name",project.customer);
// 			frm.set_value("opportunity_id",project.oppertunity);
// 			let oppertunity = frappe.model.get_doc('Oppertunity', project.oppertunity);
// 			frm.set_value("lead_name",source_doc.lead_id);

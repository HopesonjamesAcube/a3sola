// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Schedule Installation', {
	onload: function(frm) {
		if (!frm.doc.installed_item)
			frappe.throw("Sales Order is not generated and hence installer item (Product Bundle) is not defined.")

	}
});
// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Schedule Installation', {
	// refresh: function(frm) {

	// }
	validate: function(frm) {
		console.log("haii")
		if(frm.doc.installer){
		frappe.call({
			// specify the server side method to be called.
			//dotted path to a whitelisted backend method
			method: "a3sola_solar_management.a3sola_solar_management.doctype.schedule_installation.schedule_installation.test",
			//Passing variables as arguments with request
			args: {
				doc:frm.doc.name,
				pro:frm.doc.project_id,
			},

			//Function passed as an argument to above function.
			callback: function(r) {
			//To show message
			console.log(r.message.tas)
			console.log(frm.doc.installer)
									// 	frappe.call({
									// 	// specify the server side method to be called.
									// 	//dotted path to a whitelisted backend method
									// 	method: "frappe.desk.form.assign_to.add",
									// 	//Passing variables as arguments with request
									// 	args: {
									// 		 assign_to: [frm.doc.installer],
									// 		 doctype: 'Task',
									// 			name: r.message.tas,
									// 	},

									// 	//Function passed as an argument to above function.
									// 	callback: function(r) {

									// 	}
									// });//inner frappe call


					 },


			});

		}




	},
	onload: function (frm) {
		var prev_route = frappe.get_prev_route();


		if (prev_route[1] === 'Task') {
			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );

			console.log(source_doc.project)

			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.schedule_installation.schedule_installation.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
				},

				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)

				console.log(r.message.cadd);

				console.log(frm.customer)
				cur_frm.set_value("customer_address",r.message.cadd);
				cur_frm.set_value("customer_name",r.message.customer);
				cur_frm.set_value("installed_item",r.message.item);
				frm.refresh_field('customer_address');
				frm.refresh_field('customer_name');


					   },


				});






		}
	}
});





// let project = frappe.model.get_doc('Project',source_doc.project);

// 			console.log(project)
// 			frappe.msgprint(project.consumer_number);
// 			frm.set_value("customer_name",project.customer);
// 			frm.set_value("customer_address",project.primary_address);
// 			cur_frm.save();

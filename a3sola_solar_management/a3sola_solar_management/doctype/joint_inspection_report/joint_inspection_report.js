// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Joint Inspection Report', {
	// refresh: function(frm) {

	// }
	onload: function (frm) {
		var prev_route = frappe.get_prev_route();



		if (prev_route[1] === 'Task') {

			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );




			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.joint_inspection_report.joint_inspection_report.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
				},

				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)

				console.log(r.message.cadd)
				console.log(frm.customer)

				cur_frm.set_value("customer_name",r.message.customer);
				cur_frm.set_value("address",r.message.cadd);
				cur_frm.set_value("consumer_number",r.message.consno);

if(r.message.price!=undefined && r.message.discount_amount!=undefined && r.message.rate!=undefined){
				cur_frm.set_value("item_name",r.message.item);
                cur_frm.set_value("amount",r.message.price);
                cur_frm.set_value("subsidy_amount",r.message.discount_amount);
                cur_frm.set_value("net_total",r.message.rate);
					}

                frm.refresh_field('amount');
                frm.refresh_field('subsidy_amount');
                frm.refresh_field('net_total');
                frm.refresh_field('item_name');

				frm.refresh_field('address');
				frm.refresh_field('consumer_number');
				frm.refresh_field('customer_name');


					   },


				});






		}
	}
});

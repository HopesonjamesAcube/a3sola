// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Installation Report', {
	// refresh: function(frm) {

	// }


    onload: function (frm) {
        var prev_route = frappe.get_prev_route();



        if (prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id",source_doc.project );
            console.log(source_doc.project)

            frappe.call({
                // specify the server side method to be called.
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.a3sola_solar_management.doctype.installation_report.installation_report.test",
                //Passing variables as arguments with request
                args: {
                    doc:frm.doc.name,
                    pro:source_doc.project,
                },

                //Function passed as an argument to above function.
                callback: function(r) {
                //To show message
                console.log(r.message.con)

                console.log(r.message.em);

                console.log(frm.customer)
				cur_frm.set_value("mobile_no",r.message.con);
				cur_frm.set_value("email",r.message.em);
                cur_frm.set_value("address",r.message.cadd);
                cur_frm.set_value("customer_name",r.message.customer);
				cur_frm.set_value("consumer_number",r.message.consumer);
                cur_frm.set_value("installation_start_date",r.message.in);
                cur_frm.set_value("type_of_roof",r.message.roof);

        cur_frm.set_value("latitude",r.message.lat);
        cur_frm.set_value("longitude",r.message.lon);
        frm.refresh_field('latitude');
        frm.refresh_field('longitude');
        frm.refresh_field('installation_start_date');
        frm.refresh_field('type_of_roof');



				// cur_frm.set_value("contact",r.message.con);

                frm.refresh_field('address');
				frm.refresh_field('mobile_no');
				frm.refresh_field('email');
                frm.refresh_field('customer_name');
				frm.refresh_field('consumer_number');
        cur_frm.set_value("installed_item",r.message.item);
        frm.refresh_field('installed_item');

        cur_frm.fields_dict['installation_schedule_no'].get_query = function(doc) {

                return {
                    filters:{"project_id":source_doc.project_id}

                 }

            }




                       },


                });




        }
    }
});

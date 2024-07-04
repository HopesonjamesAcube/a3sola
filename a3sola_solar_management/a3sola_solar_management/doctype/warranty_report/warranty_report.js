// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Warranty Report', {
	// refresh: function(frm) {

	// }



    onload: function (frm) {
        var prev_route = frappe.get_prev_route();



        if (prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            console.log("hai")
            console.log(source_doc)
            frm.set_value("project_id",source_doc.project );
            console.log(source_doc.project)

            frappe.call({
                // specify the server side method to be called.
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.a3sola_solar_management.doctype.warranty_report.warranty_report.test",
                //Passing variables as arguments with request
                args: {
                    doc:frm.doc.name,
                    pro:source_doc.project,
                },

                //Function passed as an argument to above function.
                callback: function(r) {
                //To show message


                cur_frm.set_value("customer_name",r.message.customer);
                frm.set_value("item_name",r.message.it);
                frm.refresh_field('item_name');


				// cur_frm.set_value("contact",r.message.con);


                frm.refresh_field('customer_name');
                cur_frm.set_value("invoice_no",r.message.si);
                  frm.refresh_field('invoice_no');








                       },


                });




        }
    }
});

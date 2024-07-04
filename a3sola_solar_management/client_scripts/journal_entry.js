// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Journal Entry', {
	// refresh: function(frm) {

	// }


    onload: function (frm) {
        var prev_route = frappe.get_prev_route();



        if (prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id",source_doc.project );
            console.log(source_doc.project)
            frm.set_value("customer",source_doc.customer );
            frm.refresh_field('customer');
            frm.refresh_field('project_id');

            




        }
    }
});

// Copyright (c) 2024, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('KSEB Completion Report', {
	onload: function (frm) {
		var prev_route = frappe.get_prev_route();
		
		
		
		if (prev_route[1] === 'Task') {
			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );
			if(source_doc.customer){
			frm.set_value("customer",source_doc.customer);
			}
			if(source_doc.consumer_number){
			frm.set_value("consumer_number",source_doc.consumer_number)
			}
			frm.refresh_field('project_id');
		}
	}
});

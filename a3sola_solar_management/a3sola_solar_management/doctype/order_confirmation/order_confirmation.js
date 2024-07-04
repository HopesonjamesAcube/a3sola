// Copyright (c) 2024, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Order Confirmation', {
    onload: function (frm) {
        var prev_route = frappe.get_prev_route();
        
        if (prev_route && prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            if (source_doc.project) {          
            frm.set_value("project_id", source_doc.project);
            }
            if (source_doc.customer) {
                frm.set_value("customer", source_doc.customer);
            }
            if (source_doc.consumer_number) {
                frm.set_value("consumer_number", source_doc.consumer_number);
            }
            frm.refresh_field('project_id');
            if (source_doc.project) { 
            frappe.call({
                method: "a3sola_solar_management.a3sola_solar_management.doctype.order_confirmation.order_confirmation.get_project",
                args: {
                    pro: source_doc.project,
                },
                callback: function (r) {
                    if (r.message.email) {
                        frm.set_value('email', r.message.email);
                        frm.refresh_field('email');
                    }
                    if (r.message.phone) {
                        frm.set_value('phone_number', r.message.phone);
                        frm.refresh_field('phone_number');
                    }
                    frm.refresh_field('customer');
                },
            });
        }
        }
    }
});

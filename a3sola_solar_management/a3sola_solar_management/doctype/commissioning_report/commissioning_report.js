// Copyright (c) 2024, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Commissioning Report', {
    onload: function (frm) {
        var prev_route = frappe.get_prev_route();
        
        if (prev_route && prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id", source_doc.project);
            if (source_doc.customer) {
                frm.set_value("customer", source_doc.customer);
            }
            if (source_doc.consumer_number) {
                frm.set_value("consumer_number", source_doc.consumer_number);
            }
            frm.refresh_field('project_id');

            frappe.call({
                method: "a3sola_solar_management.a3sola_solar_management.doctype.commissioning_report.commissioning_report.test",
                args: {
                    doc: frm.doc.name,
                    pro: source_doc.project,
                },
                callback: function (r) {
                    if (r.message["cadd"]) {
                        frm.set_value('address', r.message["cadd"]);
                        frm.refresh_field('address');
                    }
                    frm.refresh_field('customer');
                },
            });
        }
    }
});
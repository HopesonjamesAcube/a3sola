frappe.ui.form.on('Sales Order', {

    onload: function (frm) {
		var prev_route = frappe.get_prev_route();
		
		console.log("hai")
		
		if (prev_route[1] === 'Quotation') {
	
			let source_doc = frappe.model.get_doc('Quotation', prev_route[2]);
			// Set project ID
			frm.set_value("project",source_doc.project_id);
			console.log("hello")
            frm.refresh_field('project');
        }

		if (prev_route[1] === 'Task') {
	
			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );
			frm.set_value("project",source_doc.project );
			frm.set_value("customer",source_doc.customer );
			frm.refresh_field('project_id');
			frm.refresh_field('project');
		}
    }
})


frappe.ui.form.on("Sales Order Item", {


	discount_item: function(frm,cdt, cdn){
		


			let row=locals[cdt][cdn]

			frm.doc.items.forEach(source_row => {


				if (source_row.discount_item){

					source_row.discount_amount=source_row.base_price_list_rate
					source_row.discount_percentage=100
					source_row.rate=0
					source_row.net_rate=0
					source_row.amount=0
					source_row.base_rate=0
					source_row.base_net_rate=0
					source_row.base_amount=0
					source_row.base_net_amount=0
					source_row.net_amount=0
				}
			
				
				frm.refresh_field("items");  
			})
		

		
		



		
		}
		})
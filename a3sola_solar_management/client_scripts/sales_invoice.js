frappe.ui.form.on('Sales Invoice', {

    onload: function (frm) {
        var prev_route = frappe.get_prev_route();
		if (prev_route[1] === 'Task') {
            console.log("hello")
	
			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );
			frm.set_value("project",source_doc.project );
			frm.set_value("customer",source_doc.customer );
			frm.refresh_field('project_id');
			frm.refresh_field('project');




			if (cur_frm.doc.__islocal){
				//check for invoice items created for project choosen product bundle
			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.doc_events.salesinvoice.si_items",
				//Passing variables as arguments with request
				args: {
					pro:source_doc.project,
					
				},

				
				callback: function(r) {
					console.log("$%^");
					if (r.message && r.message.length > 0) {
						console.log(r.message, "val");
		
						frm.clear_table('items');
						for (var i = 0; i < r.message.length; i++) {
							if(r.message[i]){
								var item = r.message[i];
								console.log(item["itemcode"]);
			
								var target_row = frm.add_child('items');
								if (item["itemcode"]){
									target_row.item_code = item["itemcode"];
									target_row.description=item["itemcode"];
								}
								if(item["itemname"]){
								target_row.item_name = item["itemname"];
								}
								if(item["stockuom"]){
								target_row.uom = item["stockuom"];
								}
								target_row.qty = 1;
								if(item["default_comp_acc"]){
								target_row.income_account = item["default_comp_acc"];
								}
								if(item["price"]){
								target_row.rate = item["price"];
								}
							}
						}
						cur_frm.refresh_fields("items");
					}
				}
  
	
				})
				
			};

		}
    }
})
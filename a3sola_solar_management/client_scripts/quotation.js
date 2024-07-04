// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation', {
	 refresh: function(frm) {
		if (!cur_frm.doc.__islocal){
			cur_frm.add_custom_button(__("Whatsapp"), function() {
				// frappe.msgprint("Custom Information");
				var api_url="https://api.whatsapp.com/send?phone="
				// var phone_number=frm.doc.whatsapp_number
				if (frm.doc.quotation_to=="Lead"){
				frappe.model.with_doc('Lead', frm.doc.party_name, function () {
		
				
		
					let ld = frappe.model.get_doc('Lead',frm.doc.party_name);
					console.log(ld.whatsapp_number)

					var complete_url=api_url.concat(ld.whatsapp_number)
				var complete_url=complete_url.concat("&text=You can check project quotation through the link ",frm.doc.attachment_url,"%0A Thank you.")
			   
				window.open(complete_url, "_blank");
		
				});

			}			
				    //Add confirmation
		
			})
		}

	 },

 
	before_submit: function(frm) {
		if (frm.is_new()){

        // console.log(cur_frm.doc.project_id);
		console.log(frappe.session.user)
		frm.set_value("prepared_by",frappe.session.user);
		frm.refresh_field('prepared_by');
		}
        // if (cur_frm.doc.project_id==undefined){

		// 	console.log(frappe.session.user)
		// 	frm.set_value("prepared_by",frappe.session.user);
		// 	frm.refresh_field('prepared_by');

        // validated = false;
        // }
		// frappe.call({
			
		// 	// specify the server side method to be called.
		// 	//dotted path to a whitelisted backend method
		// 	method: "a3sola_solar_management.doc_events.quotation.before",
		// 	//Passing variables as arguments with request
		// 	args: {
		// 		doc:frm.doc.name,
				
		// 	},

		// 	//Function passed as an argument to above function.
		// 	callback: function(r) {
		// 	//To show message
			

		// 		   },


		// 	})
	
      },

	before_save:function(frm){
		console.log("buudy")

		
		// frappe.call({
		// 	// specify the server side method to be called.
		// 	//dotted path to a whitelisted backend method
		// 	method: "a3sola_solar_management.doc_events.quotation.before",
		// 	//Passing variables as arguments with request
		// 	args: {
		// 		doc:frm.doc.name,
		// 		pack:frm.doc.packed_items
				
		// 	},

		// 	//Function passed as an argument to above function.
		// 	callback: function(r) {
		// 	//To show message
		// 	console.log(r.message)


	

		// 		   },
		// 	});
		
		
	},
	onload: function (frm) {
		if (frm.is_new()){
			frm.set_value("prepared_by",frappe.session.user);
			frm.refresh_field('prepared_by');
		}
		var prev_route = frappe.get_prev_route();

		console.log("hai")

		if (prev_route[1] === 'Task') {


			let source_doc = frappe.model.get_doc('Task', prev_route[2]);
			frm.set_value("project_id",source_doc.project );
			console.log(frappe.session.user)
			


			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.doc_events.quotation.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
				},

				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)


				console.log(frm.customer)


				frm.set_value("type_of_roof",r.message.roof);
				frm.set_value("consumer_number",r.message.consno);



				frm.refresh_field('type_of_roof');
				frm.refresh_field('consumer_number');


					   },


				});






		}
	},

	project_id :function(frm){

		frappe.model.with_doc('Project', frm.doc.project_id, function () {

		let project = frappe.model.get_doc('Project',frm.doc.project_id);
		console.log("hhhh")
		console.log(frm)

		console.log(frm.doc)
		console.log(frappe.session.user)
		if (frm.is_new()){
		frm.set_value("prepared_by",frappe.session.user);
		frm.refresh_field('prepared_by');
		}


	})
}




});



frappe.ui.form.on("Packed Item", {


    update_quantity: function(frm,cdt, cdn){

       
        	frappe.call({
			// specify the server side method to be called.
			//dotted path to a whitelisted backend method
			method: "a3sola_solar_management.doc_events.quotation.before",
			//Passing variables as arguments with request
			args: {
				doc:frm.doc.name,
				pack:frm.doc.packed_items
				
			},

			//Function passed as an argument to above function.
			callback: function(r) {
			//To show message
			console.log(r.message)


	

				   },
			});
		
        }
        })



		frappe.ui.form.on("Quotation Item", {


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


				frappe.ui.form.on("KSEB Charges", {


					phase__3_amount: function(frm,cdt, cdn){
				
					   
						console.log("Executing..")
						
				
							
								var total_cost3=0
				
								frm.doc.kseb_charges.forEach(source_row => {
				
				
									
									if(source_row.phase__3_amount){
									total_cost3=total_cost3+source_row.phase__3_amount;
								}
									
								})
								
								frm.set_value('phase_3_total',total_cost3);
									frm.refresh_field("phase_3_total");  
							
						},
						phase_1_amount: function(frm,cdt, cdn){
				
					   
							console.log("Executing..")
							
					
								
									var total_cost1=0
					
									frm.doc.kseb_charges.forEach(source_row => {
					
					
										
										
										total_cost1=total_cost1+source_row.phase_1_amount;
										
										
									})
									
									frm.set_value('phase_1_total',total_cost1);
										frm.refresh_field("phase_1_total");  
								
							}
						})
				
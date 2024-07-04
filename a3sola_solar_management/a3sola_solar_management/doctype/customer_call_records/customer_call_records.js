// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Call Records', {

	refresh:function(frm) {
		cur_frm.add_custom_button(__("Call"), function() {
			console.log("hello")
			var childTable = cur_frm.add_child("track_calls");
			childTable.date_and_time=frappe.datetime.now_datetime();
			childTable.user=frappe.session.user_fullname
			cur_frm.refresh_fields("track_calls");
			
		  
	
			let d = new frappe.ui.Dialog({
				title: 'Select Phone Number',
			  //Add fields to fetch items
							fields: [
				  {
					label: 'Phone Numbers',
					fieldname: 'ph',
					fieldtype: 'Select',
					options: [frm.doc.caller_number]
	
				  }],
				  primary_action_label: 'Confirm',
	
	
				  primary_action(values) {
					frappe.call({
						// specify the server side method to be called.
						//dotted path to a whitelisted backend method
						method: "a3sola_solar_management.doc_events.lead_events.call",
						//Passing variables as arguments with request
						args: {
							doc:frm.doc.name,
							num:values.ph
						},
					  
			
						});
				  }
				  
				})
				d.show();
	
		 
			
		  
	
	
		})

	},

	lead:function(frm){

		frm.doc.opportunity=""
		frm.refresh_field('opportunity');	
		frm.doc.customer=""
		frm.refresh_field('customer');

		if (frm.doc.called_number!="" ){


				
			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
					method: "a3sola_solar_management.a3sola_solar_management.doctype.customer_call_records.customer_call_records.test",
				//Passing variables as arguments with request
				args: {
					called_number:frm.doc.caller_number,
				   
				},
				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)
		
					cur_frm.fields_dict['lead'].get_query = function(doc) {
						return {
							filters: {
								"name":['in',r.message],
							}
						 }
						}
		   
					   },
	
				});



	}},
	onload_post_render: function(frm) {
		console.log(frm.doc.called_number)

	


		if (frm.doc.caller_number!=undefined){


				
		frappe.call({
            // specify the server side method to be called.
            //dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.customer_call_records.customer_call_records.test",
            //Passing variables as arguments with request
            args: {
                called_number:frm.doc.caller_number,
               
            },
            //Function passed as an argument to above function.
            callback: function(r) {
            //To show message
			console.log(r.message)
	
				cur_frm.fields_dict['lead'].get_query = function(doc) {
					return {
						filters: {
							"name":['in',r.message],
						}
					 }
					}

			
			


       
                   },

            });


           

			

				cur_frm.fields_dict['issue'].get_query = function(doc) {
					return {
						filters: {
							"contact_number": frm.doc.caller_number
						}
					 }
					}

				cur_frm.fields_dict['opportunity'].get_query = function(doc) {
						return {
							filters: {
								"party_name": frm.doc.lead
							}
						 }
						}
	

				
            }

	}
});

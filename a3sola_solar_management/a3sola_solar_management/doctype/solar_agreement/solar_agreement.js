// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Solar Agreement', {
	// refresh: function(frm) {


	

		onload: function (frm) {
			var prev_route = frappe.get_prev_route();



			if (prev_route[1] === 'Task') {

				let source_doc = frappe.model.get_doc('Task', prev_route[2]);
				frm.set_value("project_id",source_doc.project );




				frappe.call({
					// specify the server side method to be called.
					//dotted path to a whitelisted backend method
					method: "a3sola_solar_management.a3sola_solar_management.doctype.solar_agreement.solar_agreement.test",
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
					if(r.message.cir){
						cur_frm.set_value("circle",r.message.cir);
					}
					if(r.message.dist){
						cur_frm.set_value("distribution_transformer_to_which_the_plant_is_connected",r.message.dist);
					}
					if( r.message.customer){cur_frm.set_value("customer_name",r.message.customer);}

					if( r.message.pv){cur_frm.set_value("solar_plant_capacity",r.message.pv); frm.refresh_field('solar_plant_capacity');}
										
					if(r.message.con){cur_frm.set_value("connected_load",r.message.con);}					
					if(r.message.connected_load){frm.refresh_field('connected_load');}						

					if(r.message.customer){cur_frm.set_value("customer_name",r.message.customer);}						
					if(r.message.cadd){cur_frm.set_value("address",r.message.cadd);}						
					if(r.message.section){cur_frm.set_value("section",r.message.section);}						
					if(r.message.consno){cur_frm.set_value("consumer_number",r.message.consno);}						

					if(r.message.sp){cur_frm.set_value("spin_number",r.message.sp);}						
					if(r.message.cod){cur_frm.set_value("code_and_category",r.message.cod);}						
					if(r.message.corp){cur_frm.set_value("corporation_municipality_panchayath",r.message.corp);}						
										frm.refresh_field('corporation_municipality_panchayath');
					if(r.message.su){cur_frm.set_value("survey_no",r.message.su);}						
					if(r.message.vi){cur_frm.set_value("village",r.message.vi);}						
					if(r.message.sta){cur_frm.set_value("section",r.message.sta);}						
					// cur_frm.set_value("village",r.message.vil);

					frm.refresh_field("spin_number");
					frm.refresh_field("code_and_category");
					frm.refresh_field("corporation_municipality_panchayath");
					frm.refresh_field("survey_no");
					frm.refresh_field("village");
					frm.refresh_field("section");


					cur_frm.set_value("quotation_item",r.message.item);
					frm.refresh_field('quotation_item');
					frm.refresh_field('consumer_number');

					frm.refresh_field('address');
					frm.refresh_field('section');
					frm.refresh_field('customer_name');


						   },


					});






			}
		}
	});

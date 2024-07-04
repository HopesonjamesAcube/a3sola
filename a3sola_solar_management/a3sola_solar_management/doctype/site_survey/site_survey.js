// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Site Survey', {

	onload: function (frm) {
		if(frm.doc.longitude && frm.doc.latitude){
			frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+frm.doc.latitude+','+frm.doc.longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
			  frm.refresh_field('my_location');
		}
		var prev_route = frappe.get_prev_route();



		if (prev_route[1] === 'Task') {

			let source_doc = frappe.model.get_doc('Task', prev_route[2]);

			
			frm.set_value("project_id",source_doc.project );
			frm.set_value("customer_name",source_doc.customer);
			frm.set_value("opportunity",source_doc.opportunity);




			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.site_survey.site_survey.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
				},

				//Function passed as an argument to above function.
				callback: function(r) {
				//To show message
				console.log(r.message)
				console.log("%%%")


				console.log(frm.customer)

				
				// cur_frm.set_value("customer_address",r.message.cadd);
				cur_frm.set_value("consumer_number",r.message.consno);
				
				cur_frm.set_value("registered_in_kseb_soura",r.message.reg);
console.log(r.message.phase)
				cur_frm.set_value("required_pv_connection",r.message.req);
				cur_frm.set_value("number_of_phase",r.message.phase);
				cur_frm.set_value("roof_type",r.message.roof);
				cur_frm.set_value("roof_angle_of_inclination",r.message.incl);
				cur_frm.set_value("parapet_wall_height",r.message.para);
				cur_frm.set_value("availability_of_south_facing_module_mounting_area",r.message.south);
				cur_frm.set_value("building_height_or_number_of_floor",r.message.bheight);
				cur_frm.set_value("cable_routing_confirmed_by_client",r.message.conf);
				cur_frm.set_value("ajb_to_inverter_cable_length",r.message.ajb);
				cur_frm.set_value("spv_module_to_ajb_cable_lenght",r.message.spv);
				cur_frm.set_value("acdb_to_ex_lt_panel_or_db_cable_length",r.message.acdb);
				cur_frm.set_value("inverter_to_acdb_cable_length",r.message.inve);
				cur_frm.set_value("earthing_cable_length",r.message.earth);
				cur_frm.set_value("earth_pit_location_confirmed_by_client",r.message.pit);
				cur_frm.set_value("la_down_conductor_length",r.message.lad);
				cur_frm.set_value("circle_name",r.message.cir);
				cur_frm.set_value("name_of_electrical_station",r.message.sec);
				frm.refresh_field('circle_name');
				frm.refresh_field('name_of_electrical_station');






				frm.refresh_field('consumer_number');
				frm.refresh_field('customer_address');
				

				frm.refresh_field('registered_in_kseb_soura');
				frm.refresh_field('required_pv_connection');
				frm.refresh_field('number_of_phase');

				frm.refresh_field('roof_type');
				frm.refresh_field('roof_angle_of_inclination');
				frm.refresh_field('parapet_wall_height');

				frm.refresh_field('availability_of_south_facing_module_mounting_area');
				frm.refresh_field('building_height_or_number_of_floor');
				frm.refresh_field('cable_routing_confirmed_by_client');

				frm.refresh_field('ajb_to_inverter_cable_length');
				frm.refresh_field('spv_module_to_ajb_cable_lenght');
				frm.refresh_field('acdb_to_ex_lt_panel_or_db_cable_length');

				frm.refresh_field('inverter_to_acdb_cable_length');
				frm.refresh_field('earthing_cable_length');
				frm.refresh_field('earth_pit_location_confirmed_by_client');
				frm.refresh_field('la_down_conductor_length');



					   },


				});






		}

		if (prev_route[1] === 'Opportunity') {

			let source_doc = frappe.model.get_doc('Opportunity', prev_route[2]);

			
			frm.set_value("customer_name",source_doc.customer );
			frm.refresh_field("customer_name")
		}



		if (cur_frm.doc.__islocal){


			if (prev_route[1] === 'Task') {

				let source_doc = frappe.model.get_doc('Task', prev_route[2]);
	
				if (source_doc.latitude && source_doc.longitude && source_doc.city && source_doc.state && source_doc.area) {

					frm.set_value("latitude",source_doc.latitude );
					frm.refresh_field("latitude")
					frm.set_value("longitude",source_doc.longitude );
					frm.refresh_field("longitude")
					frm.set_value("city",source_doc.city );
					frm.refresh_field("city")
					frm.set_value("state",source_doc.state );
					frm.refresh_field("state")
					frm.set_value("area",source_doc.area );	
					frm.refresh_field("area")

				}
				else{

			function onPositionRecieved(position){
				var longitude= position.coords.longitude;
				var latitude= position.coords.latitude;
				frm.set_value('longitude',longitude);
				frm.set_value('latitude',latitude);
				console.log(longitude);
				console.log(latitude);
				fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
				 .then(response => response.json())
				.then(data => {
					var city=data['results'][0].components.city;
					var state=data['results'][0].components.state;
					var area=data['results'][0].formatted;
					frm.set_value('city',city);
					frm.set_value('state',state);
					frm.set_value('area',area);
					console.log(data);
	
				})
				.catch(err => console.log(err));
				frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
				frm.refresh_field('my_location');
			}
			
			function locationNotRecieved(positionError){
				console.log(positionError);
			}
			
			if(frm.doc.longitude && frm.doc.latitude){
				frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+frm.doc.latitude+','+frm.doc.longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
				frm.refresh_field('my_location');
			} else {
				if(navigator.geolocation){
					navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
				}
			}
		}
	
		}

		else if (prev_route[1] === 'Opportunity') {


			function onPositionRecieved(position){
				var longitude= position.coords.longitude;
				var latitude= position.coords.latitude;
				frm.set_value('longitude',longitude);
				frm.set_value('latitude',latitude);
				console.log(longitude);
				console.log(latitude);
				fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
				 .then(response => response.json())
				.then(data => {
					var city=data['results'][0].components.city;
					var state=data['results'][0].components.state;
					var area=data['results'][0].formatted;
					frm.set_value('city',city);
					frm.set_value('state',state);
					frm.set_value('area',area);
					console.log(data);
	
				})
				.catch(err => console.log(err));
				frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
				frm.refresh_field('my_location');
			}
			
			function locationNotRecieved(positionError){
				console.log(positionError);
			}
			
			if(frm.doc.longitude && frm.doc.latitude){
				frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+frm.doc.latitude+','+frm.doc.longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
				frm.refresh_field('my_location');
			} else {
				if(navigator.geolocation){
					navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
				}
			}
		



		}




	}
},


longitude: function(frm) {
	if(frm.doc.longitude && frm.doc.latitude){
	var longitude= frm.doc.longitude;
				var latitude= frm.doc.latitude;
				
				console.log(longitude);
				console.log(latitude);
				fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
				 .then(response => response.json())
				.then(data => {
					var city=data['results'][0].components.city;
					var state=data['results'][0].components.state;
					var area=data['results'][0].formatted;
					frm.set_value('city',city);
					frm.set_value('state',state);
					frm.set_value('area',area);
					console.log(data);
	
				})
				.catch(err => console.log(err));
				frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
				frm.refresh_field('my_location');
			}

},

latitude: function(frm) {
	if(frm.doc.longitude && frm.doc.latitude){
	var longitude= frm.doc.longitude;
				var latitude= frm.doc.latitude;
				
				console.log(longitude);
				console.log(latitude);
				fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
				 .then(response => response.json())
				.then(data => {
					var city=data['results'][0].components.city;
					var state=data['results'][0].components.state;
					var area=data['results'][0].formatted;
					frm.set_value('city',city);
					frm.set_value('state',state);
					frm.set_value('area',area);
					console.log(data);
	
				})
				.catch(err => console.log(err));
				frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
				frm.refresh_field('my_location');
			}

}


}


);

frappe.ui.form.on("Site Survey Item", {


    quantity: function(frm,cdt, cdn){

       
        console.log("Executing..")
        

            if (frm.doc.additional_items){

                frm.doc.additional_items.forEach(source_row => {


                    
                    var qty=source_row.quantity;
                    var rate=source_row.rate;
                    var amount=rate*qty
                    console.log("price",amount)
                    source_row.amount=amount;
                    frm.refresh_field("additional_items");  
                })
            }
        }
        })
	

		frappe.ui.form.on("Price Details", {


			total_cost: function(frm,cdt, cdn){
		
			   
				console.log("Executing..")
				
		
					if (frm.doc.price_details){
						var total_cost=0
		
						frm.doc.price_details.forEach(source_row => {
		
		
							
							
							total_cost=total_cost+source_row.total_cost;
							
							
						})
						
						frm.set_value('total_amount',total_cost);
							frm.refresh_field("total_amount");  
					}
				}
				})

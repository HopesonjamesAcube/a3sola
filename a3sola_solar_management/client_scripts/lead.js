// To enable form scripting of lead doctype
frappe.ui.form.on('Lead', {


    onload: function (frm) {
        console.log("onload works in lead")
        if (frm.is_new()){
            var currentDate = frappe.datetime.nowdate();
            frm.set_value("date",currentDate)
            frappe.call({
                method: "a3sola_solar_management.doc_events.lead_events.get_attendance",
                //Passing variables as arguments with request
                args: {
                    user:frappe.session.user,
                    date:frm.doc.date
                   
                },
                //Function passed as an argument to above function.
                callback: function(r) {
                    console.log(r.message,"tttttttttttttttttt")
                    if(r.message.att){
                    frm.set_value("attendance",r.message.att)
                    frm.refresh_field("attendance")
                    }
                    if(r.message.ld){
                    frm.set_value("previous_lead",r.message.ld)
                    frm.refresh_field("previous_lead")
                    }
                    if (typeof r.message === 'object' && r.message !== null) {
                    if(r.message["lead creation api"]=== 1 && r.message["domain"] && r.message["api"]){
                // location fetching
                    
                
            function onPositionRecieved(position){
                var longitude= position.coords.longitude;
                var latitude= position.coords.latitude;
                frm.set_value('longitude',longitude);
                frm.set_value('latitude',latitude);
                console.log(longitude);
                console.log(latitude);
                fetch(r.message["domain"]+latitude+'+'+longitude+'&key='+r.message["api"])
                 .then(response => response.json())
                  .then(data => {
                    var city;
                    if (data['results'][0].components.city) {
                        city = data['results'][0].components.city;
                    } else if (data['results'][0].components.town) {
                        city = data['results'][0].components.town;
                    } else if (data['results'][0].components.village) {
                        city = data['results'][0].components.village;
                    } else if (data['results'][0].components.suburb) {
                        city = data['results'][0].components.suburb;
                    } else if (data['results'][0].components.road) {
                        city = data['results'][0].components.road;
                    } else if (data['results'][0].components.highway) {
                        city = data['results'][0].components.highway;
                    } 
                    console.log(city,"city")
                    console.log(data,"data")
                      var state=data['results'][0].components.state;
                      var area=data['results'][0].formatted;
                      frm.set_value('place',city);
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
            if(navigator.geolocation){
                navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
            }
        }
        }
    }

        })
            

        }



		var prev_route = frappe.get_prev_route();
		
		
		
		if (prev_route[1] === 'Customer Call Records') {
	
			let source_doc = frappe.model.get_doc('Customer Call Records', prev_route[2]);
			frm.set_value("number_to_be_contacted",source_doc.caller_number );
            frm.refresh_field('number_to_be_contacted');


        }
    },
    proposed_project_capacity:function(frm){
        if(frm.doc.proposed_project_capacity && frm.doc.connected_load){
            if(frm.doc.proposed_project_capacity > frm.doc.connected_load){
                frappe.msgprint("Load Enhancement is Required")
            }
        }
    },
    connected_load:function(frm){
        if(frm.doc.proposed_project_capacity && frm.doc.connected_load){
            if(frm.doc.proposed_project_capacity > frm.doc.connected_load){
                frappe.msgprint("Load Enhancement is Required")
            }
        }
    },
    
    
    //Call function after save.
    
	refresh:function(frm) {
  
            {
            cur_frm.fields_dict['board_name'].get_query = function(doc) {
                return {
                    filters: {
                        "customer_group": "A3sola"
                    }
                 }
                }
            }




            //TESTT


if (!cur_frm.doc.__islocal){
    cur_frm.add_custom_button(__("Call"), function() {
        console.log("hello")
        var city_val = "NIL";
        var area_val = "NIL";
        var latitude, longitude;

            frappe.call({
                method: "a3sola_solar_management.doc_events.lead_events.get_location_api_settings",
                //Passing variables as arguments with request
                //Function passed as an argument to above function.
                callback: function(r) {
            if (typeof r.message === 'object' && r.message !== null) {
            if (r.message["enabled"] === 1 && r.message["domain"] && r.message["api"]) {
                // Your code here if the conditions are met
            
            
            function onPositionRecieved(position){
                longitude= position.coords.longitude;
                latitude= position.coords.latitude;
                // frm.set_value('longitude',longitude);
                // frm.set_value('latitude',latitude);
                // console.log(longitude);
                // console.log(latitude);
                console.log(r.message["domain"]+latitude,"Domain",longitude+r.message["api"],"API")
                fetch(r.message["domain"]+latitude+'+'+longitude+'&key='+r.message["api"])
                 .then(response => response.json())
                  .then(data => {

                    if (data['results'][0].components.city) {
                        city_val = data['results'][0].components.city;
                    } else if (data['results'][0].components.town) {
                        city_val = data['results'][0].components.town;
                    } else if (data['results'][0].components.village) {
                        city_val = data['results'][0].components.village;
                    } else if (data['results'][0].components.suburb) {
                        city_val = data['results'][0].components.suburb;
                    } else if (data['results'][0].components.road) {
                        city_val = data['results'][0].components.road;
                    } else if (data['results'][0].components.highway) {
                        city_val = data['results'][0].components.highway;
                    } 
                    
                    // var state_val=data['results'][0].components.state;
                    area_val=data['results'][0].formatted;
                    console.log(city_val,"city")
                    console.log(area_val,"Area Value")
                    // console.log(data,"data")
                    //   frm.set_value('place',city);
                    //   frm.set_value('state',state);
                    //   frm.set_value('area',area);
                    //   console.log(data);
                    console.log("value is before child table",city_val,data,area_val,latitude,longitude)
                    var childTable = cur_frm.add_child("lead_tracking");
                    childTable.date_and_time=frappe.datetime.now_datetime();
                    childTable.user=frappe.session.user_fullname
                    if (longitude){
                        childTable.longitude=longitude

                    }
                    if (latitude){
                        childTable.latitude=latitude

                    }
                    if (city_val){
                        childTable.place=city_val

                    }
                    if (area_val){

                        childTable.area=area_val

                    }
                    cur_frm.refresh_fields("lead_tracking");
                
                  })
                  .catch(err => console.log(err));
                // frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
                //   frm.refresh_field('my_location');
            }
            
            function locationNotRecieved(positionError){
                console.log(positionError);
            }
            if(navigator.geolocation){
                navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
            }
    
        
    } else{
        console.log("this else works")
        var childTable = cur_frm.add_child("lead_tracking");
        childTable.date_and_time=frappe.datetime.now_datetime();
        childTable.user=frappe.session.user_fullname
        cur_frm.refresh_fields("lead_tracking");

    }
    }
    }

    })

        let d = new frappe.ui.Dialog({
            title: 'Select Phone Number',
          //Add fields to fetch items
                        fields: [
              {
                label: 'Phone Numbers',
                fieldname: 'ph',
                fieldtype: 'Select',
                options: [frm.doc.number_to_be_contacted,frm.doc.whatsapp_number]

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
}


//TESTT
if (!cur_frm.doc.__islocal){
    cur_frm.add_custom_button(__("Whatsapp"), function() {
        // frappe.msgprint("Custom Information");
        var api_url="https://api.whatsapp.com/send?phone="
        var phone_number=frm.doc.whatsapp_number
        
        
        var complete_url=api_url.concat(phone_number)
        var complete_url=complete_url.concat("&text=Congratulations Mr/Mrs ",frm.doc.lead_name,`%0A%0A`,"%20%20 Thank you for expressing interest in working with ",frm.doc.company," we are excited at the prospect of working together on this project. Thank you.")
       
        window.open(complete_url, "_blank");

            //Add confirmation

    })
}











        //Add a custom button
        if (!cur_frm.doc.__islocal){
        cur_frm.add_custom_button(__("Confirm"), function() {
            // frappe.msgprint("Custom Information");

                //Add confirmation

                    //Set dialog box to fetch items
					let d = new frappe.ui.Dialog({
						title: 'Select Item',
					//Add fields to fetch items
                        fields: [
							{
								label: 'Item',
								fieldname: 'Item',
								fieldtype: 'Link',
								options: 'Product Bundle',
                                filters: {'disable': 0},
							},
                        // Add fields to enter quantity of items
                            {
                                label:"Quantity",
                                fieldname:"Qty",
                                fieldtype:"Int"
                            },

						],
                        // On confirming Call  server side methods
						primary_action_label: 'Confirm',
						primary_action(values) {
						console.log(values)
            // To access server side methods
		    frappe.call({
            // specify the server side method to be called.
            //dotted path to a whitelisted backend method
            method: "a3sola_solar_management.doc_events.lead_events.on_update",
            //Passing variables as arguments with request
            args: {
                doc:frm.doc.name,
                val:values.Item,
                qn:values.Qty,
                with_items:1
            },
            //Function passed as an argument to above function.
            callback: function(r) {
            //To show message

                
            frappe.msgprint("Opportunity Created Successfully")
       
                   },

            });
            d.hide();
        }
    })
     d.show();
        })
    }

   








},
district_name:function(frm) {

    

        cur_frm.fields_dict['taluk_name'].get_query = function(doc) {
            return {
                filters: {
                    "district": frm.doc.district_name
                }
             }
            }
        

},

after_save:function (frm) {


          

    frappe.call({
        // specify the server side method to be called.
        //dotted path to a whitelisted backend method
        method: "a3sola_solar_management.doc_events.lead_events.aftersavefetch",
        //Passing variables as arguments with request
        args: {
            ld:frm.doc.name,
            
        },


  })

},

// 'fetch_current_location':function(frm){


//     if(frm.doc.fetch_current_location==1){
//         console.log('haii')

    // function onPositionRecieved(position){
    //     var longitude= position.coords.longitude;
    //     var latitude= position.coords.latitude;
    //     frm.set_value('longitude',longitude);
    //     frm.set_value('latitude',latitude);
    //     console.log(longitude);
    //     console.log(latitude);
    //     fetch('https://api.opencagedata.com/geocode/v1/json?q='+latitude+'+'+longitude+'&key=de1bf3be66b546b89645e500ec3a3a28')
    //      .then(response => response.json())
    //       .then(data => {
    //           var city=data['results'][0].components.city;
    //           var state=data['results'][0].components.state;
    //           var area=data['results'][0].formatted;
    //           frm.set_value('place',city);
    //           frm.set_value('state',state);
    //           frm.set_value('area',area);
    //           console.log(data);
    //       })
    //       .catch(err => console.log(err));
    //     frm.set_df_property('my_location','options','<div class="mapouter"><div class="gmap_canvas"><iframe width=100% height="300" id="gmap_canvas" src="https://maps.google.com/maps?q='+latitude+','+longitude+'&t=&z=17&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe><a href="https://yt2.org/youtube-to-mp3-ALeKk00qEW0sxByTDSpzaRvl8WxdMAeMytQ1611842368056QMMlSYKLwAsWUsAfLipqwCA2ahUKEwiikKDe5L7uAhVFCuwKHUuFBoYQ8tMDegUAQCSAQCYAQCqAQdnd3Mtd2l6"></a><br><style>.mapouter{position:relative;text-align:right;height:300px;width:100%;}</style><style>.gmap_canvas {overflow:hidden;background:none!important;height:300px;width:100%;}</style></div></div>');
    //       frm.refresh_field('my_location');
    // }
    
    // function locationNotRecieved(positionError){
    //     console.log(positionError);
    // }
    // if(navigator.geolocation){
    //     navigator.geolocation.getCurrentPosition(onPositionRecieved,locationNotRecieved,{ enableHighAccuracy: true});
    // }

// }
// }


});

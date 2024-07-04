// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Performance Ratio Test', {
	// refresh: function(frm) {

	// }
	onload: function (frm) {
		var prev_route = frappe.get_prev_route();



    if (prev_route[1] === 'Task') {

      let source_doc = frappe.model.get_doc('Task', prev_route[2]);
      frm.set_value("project_id",source_doc.project );






      frappe.call({
        // specify the server side method to be called.
        //dotted path to a whitelisted backend method
        method: "a3sola_solar_management.a3sola_solar_management.doctype.performance_ratio_test.performance_ratio_test.test",
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

        cur_frm.set_value("consumer_name",r.message.customer);

        cur_frm.set_value("consumer_number",r.message.consno);




        frm.refresh_field('consumer_number');
        frm.refresh_field('customer_name');



                     },


                });

								// Calculate
								cur_frm.add_custom_button(__("Calculate"), function() {

										if(frm.doc.efficiency && frm.doc.inverter_efficiency && frm.doc.area){
											var wdc=0
											var wac=0
											var irradiance=0
											var count=0
											console.log(wdc)

											 frm.doc.table_20.forEach(function(entry) {
												if (entry.wdc != null && entry.wac != null && entry.irradiance != null) {

															wdc=wdc+entry.wdc
															wac=wac+entry.wac
															irradiance=irradiance+entry.irradiance
															count=count+1

												}


											 });

											 console.log(irradiance)
											 console.log(wdc)
											 console.log(wac)

											 if (wdc!=0 && wac!=0 && irradiance!=0){
												var awdc=wdc/count
												var awac=wac/count
												var airradiance=irradiance/count

												cur_frm.set_value("average_wac",awac);
												frm.refresh_field('average_wac');
												cur_frm.set_value("average_irradiance",airradiance);
												frm.refresh_field('average_irradiance');
												cur_frm.set_value("average_wdc",awdc);
												frm.refresh_field('average_wdc');


												console.log(awdc)
												console.log(awac)
												console.log(airradiance)
												var m_effi=frm.doc.efficiency/100

												var in_eff=frm.doc.inverter_efficiency/100
												var pr_dc=((awdc)/(airradiance*frm.doc.area*m_effi))*100
												var pr_ac=((awac)/(airradiance*frm.doc.area*m_effi*in_eff))*100
												console.log(pr_ac)
												console.log(pr_dc)
												var roundprac=Math.round((pr_ac + Number.EPSILON) * 100) / 100
												console.log(roundprac)
												var roundprdc=Math.round((pr_dc + Number.EPSILON) * 100) / 100
												cur_frm.set_value("pr_ac",roundprac);

												frm.refresh_field('pr_ac');

												cur_frm.set_value("pr_dc",roundprdc);

												frm.refresh_field('pr_dc');


											}




										}


										// if(frm.doc.efficiency && frm.doc.inverter_efficiency && frm.doc.area){
										// 	console.log("hello")
										// 	frappe.call({
										// 			// specify the server side method to be called.
										// 			//dotted path to a whitelisted backend method
										// 			method: "a3sola_solar_management.a3sola_solar_management.doctype.performance_ratio_test.performance_ratio_test.calc",
										// 			//Passing variables as arguments with request
										// 			args: {
										// 					doc:frm.doc.name,
										// 					area:frm.doc.area,
										// 					ineff:frm.doc.inverter_efficiency,
										// 					effi:frm.doc.efficiency,
										//
										// 					table:cur_frm.doc.table_20,
										// 			},
										//
										//
										// })
										//
										// }
							})



								// Calculate



            }



          },


			    after_save:function (frm) {




			      frappe.call({
			          // specify the server side method to be called.
			          //dotted path to a whitelisted backend method
			          method: "a3sola_solar_management.a3sola_solar_management.doctype.performance_ratio_test.performance_ratio_test.aftersavefetch",
			          //Passing variables as arguments with request
			          args: {
			              doc:frm.doc.name,
			              pro:cur_frm.doc.project_id,
			          },


			    })

			  },

				refresh:function(frm){

					cur_frm.add_custom_button(__("Calculate"), function() {

							if(frm.doc.efficiency && frm.doc.inverter_efficiency && frm.doc.area){
								var wdc=0
								var wac=0
								var irradiance=0
								var count=0
								console.log(wdc)

								 frm.doc.table_20.forEach(function(entry) {
								 	if (entry.wdc != null && entry.wac != null && entry.irradiance != null) {

												wdc=wdc+entry.wdc
												wac=wac+entry.wac
												irradiance=irradiance+entry.irradiance
												count=count+1

								 	}


								 });

								 console.log(irradiance)
								 console.log(wdc)
								 console.log(wac)

								 if (wdc!=0 && wac!=0 && irradiance!=0){
						 			var awdc=wdc/count
						 			var awac=wac/count
						 			var airradiance=irradiance/count

									cur_frm.set_value("average_wac",awac);
					        frm.refresh_field('average_wac');
									cur_frm.set_value("average_irradiance",airradiance);
					        frm.refresh_field('average_irradiance');
									cur_frm.set_value("average_wdc",awdc);
					        frm.refresh_field('average_wdc');


									console.log(awdc)
									console.log(awac)
									console.log(airradiance)
									var m_effi=frm.doc.efficiency/100

									var in_eff=frm.doc.inverter_efficiency/100
									var pr_dc=((awdc)/(airradiance*frm.doc.area*m_effi))*100
									var pr_ac=((awac)/(airradiance*frm.doc.area*m_effi*in_eff))*100
									console.log(pr_ac)
									console.log(pr_dc)
									var roundprac=Math.round((pr_ac + Number.EPSILON) * 100) / 100
									console.log(roundprac)
									var roundprdc=Math.round((pr_dc + Number.EPSILON) * 100) / 100
									cur_frm.set_value("pr_ac",roundprac);

					        frm.refresh_field('pr_ac');

									cur_frm.set_value("pr_dc",roundprdc);

					        frm.refresh_field('pr_dc');


								}










							}


							// if(frm.doc.efficiency && frm.doc.inverter_efficiency && frm.doc.area){
							// 	console.log("hello")
							// 	frappe.call({
							// 			// specify the server side method to be called.
							// 			//dotted path to a whitelisted backend method
							// 			method: "a3sola_solar_management.a3sola_solar_management.doctype.performance_ratio_test.performance_ratio_test.calc",
							// 			//Passing variables as arguments with request
							// 			args: {
							// 					doc:frm.doc.name,
							// 					area:frm.doc.area,
							// 					ineff:frm.doc.inverter_efficiency,
							// 					effi:frm.doc.efficiency,
							//
							// 					table:cur_frm.doc.table_20,
							// 			},
							//
							//
							// })
							//
							// }
				})}


        });
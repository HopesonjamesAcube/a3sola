frappe.ui.form.on('Payment Entry', {

    refresh: function(frm) {
		if (!cur_frm.doc.__islocal){
            if (frm.doc.party_type=='Customer'){
			cur_frm.add_custom_button(__("Whatsapp"), function() {
				// frappe.msgprint("Custom Information");
				var api_url="https://api.whatsapp.com/send?phone="
				// var phone_number=frm.doc.whatsapp_number
				
				frappe.model.with_doc('Customer', frm.doc.party, function () {
		
				
		
					let customer = frappe.model.get_doc('Customer',frm.doc.party);
					console.log(customer.whatsapp_number)

					var complete_url=api_url.concat(customer.whatsapp_number)
				var complete_url=complete_url.concat("&text=Thank you for your recent payment, you can find your receipt through ",frm.doc.attachment_url,"%0A Thank you.")
			   
				window.open(complete_url, "_blank");
		
				});

						
				    //Add confirmation
		
			})}
		}

	 },



    onload: function (frm) {
        var prev_route = frappe.get_prev_route();



        if (prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id",source_doc.project );
            frm.set_value("project",source_doc.project );

            console.log(source_doc.project)
              frm.refresh_field('project');
              frm.refresh_field('project_id');


        }
    },

    project_references_only: function (frm) {

        if(frm.doc.project_references_only){
            
            if(frm.doc.project && frm.doc.references){
                console.log('project_references_only')
                


                    frappe.call({
                        // specify the server side method to be called.
                        //dotted path to a whitelisted backend method
                        method: "a3sola_solar_management.doc_events.payment_entry.pi",
                        //Passing variables as arguments with request
                        args: {
                            pro:frm.doc.project,
                            party:frm.doc.party,
                            
                        },
            
                        //Function passed as an argument to above function.
                        callback: function(r) {
                        //To show message
                        console.log(r)
                        console.log(r.message.length)
                        if(r.message!=0){


                        frm.doc.references.forEach(source_row => {
                            var exist=0;

                        for (var i = 0; i < r.message.length; i++) {
                            
                            
                            if (source_row.reference_name == r.message[i]) {
                               
                                console.log(source_row.reference_name)
                                exist=1;
                            }

                        }
                            
                        if(exist==0){
                            frm.get_field("references").grid.grid_rows[source_row.idx - 1].remove();
                            frm.refresh_field('references');

                        }

                        

                    })}

                        
                        
                        
        
                    
                    
                    

            

            }}
                )


    }}},





    party: function (frm) {
        if (frm.doc.project && frm.doc.party) {
        if(frm.doc.payment_type=="Pay" && frm.doc.party_type=='Employee'){
        

        frappe.call({
            // specify the server side method to be called.
            //dotted path to a whitelisted backend method
            method: "a3sola_solar_management.doc_events.payment_entry.incentive",
            //Passing variables as arguments with request
            args: {
                pro:frm.doc.project,
                party:frm.doc.party,
                type:'employee'
            },

            //Function passed as an argument to above function.
            callback: function(r) {
            //To show message
            console.log(r.message)
            console.log('Employee')
    


           

            if(r.message!=0){
                cur_frm.set_value("paid_amount",r.message);
          
    
                frm.refresh_field('paid_amount');
               
                }
           
          


                   },


            });

        }





        if(frm.doc.payment_type=="Pay" && frm.doc.party_type=='Supplier'){
        

            frappe.call({
                // specify the server side method to be called.
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.doc_events.payment_entry.incentive",
                //Passing variables as arguments with request
                args: {
                    pro:frm.doc.project,
                    party:frm.doc.party,
                    type:'supplier'
                },
    
                //Function passed as an argument to above function.
                callback: function(r) {
                //To show message
                console.log(r.message)
                console.log('supplier')
                console.log(r.message.unpaid)
                console.log(r.message.account)
                console.log("%%%%%")
    
    
               
                if(r.message.unpaid!=0){
                cur_frm.set_value("paid_amount",r.message.unpaid);
          
    
                frm.refresh_field('paid_amount');
               
                }

                if(r.message.account!=0){
                    cur_frm.set_value("paid_from",r.message.account);
                    cur_frm.refresh_field('paid_from');
                }
    
    
                       },
    
    
                });
    
            }


        }

    },


    // before_submit: function(frm) {

        

	// 	frappe.call({
			
	// 		// specify the server side method to be called.
	// 		//dotted path to a whitelisted backend method
	// 		method: "a3sola_solar_management.doc_events.payment_entry.before",
	// 		//Passing variables as arguments with request
	// 		args: {
	// 			doc:frm.doc.name,
				
	// 		},

	// 		//Function passed as an argument to above function.
	// 		callback: function(r) {
	// 		//To show message
			

	// 			   },


	// 		})
	
    //   },
});





// frappe.ui.form.on("Payment Entry Reference", {
  

//     reference_name: function(frm){

//         console.log("Haii")

       
//         if(frm.doc.project && frm.doc.references){
//             console.log('project_references_only')
            


//                 frappe.call({
//                     // specify the server side method to be called.
//                     //dotted path to a whitelisted backend method
//                     method: "a3sola_solar_management.doc_events.payment_entry.pi",
//                     //Passing variables as arguments with request
//                     args: {
//                         pro:frm.doc.project,
//                         party:frm.doc.party,
                        
//                     },
        
//                     //Function passed as an argument to above function.
//                     callback: function(r) {
//                     //To show message
//                     console.log(r)
//                     console.log(r.message.length)
//                     if(r.message!=0){


//                     frm.doc.references.forEach(source_row => {
//                         var exist=0;

//                     for (var i = 0; i < r.message.length; i++) {
                        
                        
//                         if (source_row.reference_name == r.message[i]) {
                           
//                             console.log(source_row.reference_name)
//                             exist=1;
//                         }


//                     }
                        
//                     if(exist==0){
//                         frm.get_field("references").grid.grid_rows[source_row.idx - 1].remove();
//                         frm.refresh_field('references');

//                     }

                    

//                 })}

                    
                    
                    
    
                
                
                

        

//         }}
//             )


// }
//         }
//         })



        

frappe.ui.form.on("Opportunity", {
    "refresh": function(frm) {

        
        console.log("11111111111111111111111111111")
        if (!cur_frm.doc.__islocal){
            cur_frm.fields_dict['site_survey'].get_query = function(doc) {
                return {
                    filters: {
                        "opportunity": frm.doc.name
                    }
                 }
                }


                cur_frm.fields_dict['quotation'].get_query = function(doc) {
                    return {
                        filters: {
                            "party_name": frm.doc.party_name
                        }
                     }
                    }




            if (!cur_frm.doc.__islocal){
                cur_frm.add_custom_button(__("Call"), function() {
                    console.log("hello")
                    var childTable = cur_frm.add_child("opportunity_call_track");
                    childTable.date_and_time=frappe.datetime.now_datetime();
                    childTable.user=frappe.session.user_fullname
                    cur_frm.refresh_fields("opportunity_call_track");
                  
            
                    let d = new frappe.ui.Dialog({
                        title: 'Select Phone Number',
                      //Add fields to fetch items
                                    fields: [
                          {
                            label: 'Phone Numbers',
                            fieldname: 'ph',
                            fieldtype: 'Select',
                            options: [frm.doc.contact_number,frm.doc.whatsapp_number]
            
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
            
            
            
            
            
            
            cur_frm.add_custom_button(__("Whatsapp"), function() {
                // frappe.msgprint("Custom Information");
                var api_url="https://api.whatsapp.com/send?phone="
                var phone_number=frm.doc.whatsapp_number
                
                
                var complete_url=api_url.concat(phone_number)
                var complete_url=complete_url.concat("&text=Congratulations Mr/Mrs ",frm.doc.customer,",%0A%20%20 Thank you for expressing interest in working with ",frm.doc.company," we are excited at the prospect of working together on this project. Thank you. You can Track your project at ",frm.doc.url)
               
               
                window.open(complete_url, "_blank");
            
                    //Add confirmation
            
            })        




            frm.add_custom_button("Track", function(){
    
    
          console.log(window.location.host)
          let route_add=window.location.host
    
          var show='/show?id='
          let r1 = route_add.concat("", show);
    
    
          var tid=frm.doc.tracking_id
    
          let result = frm.doc.url;
    
    
          console.log(result)
          var myWin = window.open(result,"_blank");
        })



    if(!frm.doc.__islocal){
        frm.add_custom_button(__("Project"), function() {
            
    
        //
            if (frm.doc.consumer_number){
    
            frappe.new_doc('Project', {
    
                
    
    
            "project_type":"Internal",
            "consumer_number":cur_frm.doc.consumer_number,
            "aadhaar_number":cur_frm.doc.aadhaar_number,
            "oppertunity":cur_frm.doc.name,
    
            // "scheme_name":cur_frm.doc.scheme_name,
            // "board_name":cur_frm.doc.board_name,
    
    
            })}
            else{
                // if (frm.doc.aadhaar_number==undefined && frm.doc.consumer_number==undefined){
                //     frappe.throw("Please fill Aadhaar number and Consumer number")
                // }
                // else if (frm.doc.consumer_number==undefined){
                    frappe.throw("Please fill Consumer number")


                // }
                // else if (frm.doc.aadhaar_number==undefined){
                // frappe.throw("Please fill Aadhaar number")
                // }
            }
        }, __('Create'));
    
    }
    
    
    
    
    
    
    }

            cur_frm.fields_dict['board_name'].get_query = function(doc) {
                return {
                    filters: {
                        "customer_group": "A3sola"
                    }
                 }
                }




    // var d = locals[cdt][cdn];
    if(frm.doc.converted_by){
        console.log("aa")
    }
    else{
    frm.set_value("converted_by",frappe.session.user);
	frm.refresh_field('converted_by');
    }
    console.log("heuu")


    }   ,
onload:function(frm){
    
        setTimeout(() => {
            $("[data-doctype='Request for Quotation']").hide();
            $("[data-doctype='Supplier Quotation']").hide();
            }, 10);
       
    console.log("2222222222222222222222222222222222222222222222")
cur_frm.fields_dict['customer'].get_query = function(doc) {

    return {
        filters: frm.doc.aadhaar_number?[["aadhaar_number","=",frm.doc.aadhaar_number]]:[]
     }
    }


    if (frm.doc.opportunity_from=="Lead") {
      if (frm.doc.party_name){



        frm.clear_table('address_list')
        frm.clear_table('contact_list')

        console.log("worked")

        frappe.model.with_doc('Lead', frm.doc.party_name, function () {

            let ld = frappe.model.get_doc('Lead',frm.doc.party_name);
            console.log(ld,"###############11111111111111")
            if (ld.number_to_be_contacted){
                frm.doc.contact_number=ld.number_to_be_contacted
            }
            if (ld.aadhaar_number){
                frm.doc.aadhaar_number=ld.aadhaar_number
            }
            if (ld.consumer_number){
               frm.doc.consumer_number=ld.consumer_number
           }

            const target_row=frm.add_child('contact_list')
            console.log("hiiiiii")
            target_row.contact_number =ld.number_to_be_contacted;
            target_row.email_id = ld.email_id;
            frm.refresh_field('contact_list');
            frm.refresh_field('contact_number')




                frappe.call({
                    // specify the server side method to be called.
                    //dotted path to a whitelisted backend method
                    method: "a3sola_solar_management.doc_events.opportunity_events.test",
                    //Passing variables as arguments with request
                    args: {
                       doc:frm.doc.party_name,
                       type:"lead"

                    },

                    //Function passed as an argument to above function.
                    callback: function(r) {
            console.log(r.message.address_title,"###############")
            {

                    const target_row=frm.add_child('address_list')
                    target_row.address =r.message.address_title;
                    target_row.address_line_1 = r.message.address_line1;
                    target_row.address_line_2 = r.message.address_line2;
                    target_row.city=r.message.city;
                    target_row.state=r.message.state;
                    target_row.country=r.message.country;
                    frm.refresh_field('address_list');
            }
         }
                     });

                    }

)}}

else if (frm.doc.opportunity_from="Customer" ){
if (frm.doc.party_name){
frappe.model.with_doc('Customer', frm.doc.party_name, function () {

    let cu = frappe.model.get_doc('Customer',frm.doc.party_name);
    console.log(cu,"@@@@@@@@@@@@@@@@@@@@")
    if (cu.aadhaar_number){
        frm.doc.aadhaar_number=cu.aadhaar_number
    }
    if (cu.mobile_no){
        frm.doc.contact_number=cu.mobile_no
    }
    const target_row=frm.add_child('contact_list')
    console.log("hiiiiii")
    target_row.contact_number =cu.mobile_no;
    target_row.email_id = cu.email_id;
    frm.refresh_field('contact_list');

    frappe.call({
        // specify the server side method to be called.
        //dotted path to a whitelisted backend method
        method: "a3sola_solar_management.doc_events.opportunity_events.test",
        //Passing variables as arguments with request
        args: {
           doc:frm.doc.party_name,
           type:"customer"

        },

        //Function passed as an argument to above function.
        callback: function(r) {
console.log(r.message.address_title,"###############")
{

        const target_row=frm.add_child('address_list')
        target_row.address =r.message.address_title;
        target_row.address_line_1 = r.message.address_line1;
        target_row.address_line_2 = r.message.address_line2;
        target_row.city=r.message.city;
        target_row.state=r.message.state;
        target_row.country=r.message.country;
        frm.refresh_field('address_list');
}
}
         });



})
}


}},
district_name:function(frm) {

    console.log("444444444444444444444444444444444444")

    

    cur_frm.fields_dict['taluk_name'].get_query = function(doc) {
        return {
            filters: {
                "district": frm.doc.district_name
            }
         }
        }
    

},

consumer_number:function(frm){

    console.log("55555555555555555555555555555555555555")


        if (frm.doc.opportunity_from=="Lead"){


            cur_frm.fields_dict['party_name'].get_query = function(doc) {

                return {
                    filters:frm.doc.consumer_number?[["consumer_number","=",frm.doc.consumer_number]]:[]
                        // ["aadhaar_number","=",frm.doc.aadhaar_number]]
                 }
                }

              }


},
aadhaar_number:function(frm){

    console.log("666666666666666666666666666666666666")


    if (frm.doc.opportunity_from=="Customer"){
      console.log(frm.doc.aadhaar_number)
      console.log("^^^")

        cur_frm.fields_dict['party_name'].get_query = function(doc) {

            return {
                filters: frm.doc.aadhaar_number?[["aadhaar_number","=",frm.doc.aadhaar_number]]:[]
             }
            }


          if (frm.doc.aadhaar_number){
            console.log("not empty")
          }else{
            console.log("empty")
            frm.refresh_field('party_name')

          }

          }
          if (frm.doc.aadhaar_number){

                cur_frm.fields_dict['customer'].get_query = function(doc) {
                    return {
                        filters: {
                            "aadhaar_number": frm.doc.aadhaar_number
                        }
                     }
                    }
              }

},

opportunity_from:function(frm){

    console.log("7777777777777777777777777777777777777777777")

  frm.clear_table('address_list')
  frm.clear_table('contact_list')
  frm.doc.aadhaar_number=""
  frm.doc.consumer_number=""
  frm.doc.contact_number=""
  frm.doc.customer_name=""
  frm.doc.customer=""
  frm.refresh_field('aadhaar_number')
  frm.refresh_field('contact_list')
  frm.refresh_field('consumer_number')

  frm.refresh_field('contact_number')
  frm.refresh_field('aadhaar_number')
  frm.refresh_field('customer_name')
  frm.refresh_field('customer')
  frm.refresh_field('address_list')

  console.log(frm.doc.customer)

},


party_name: function (frm) {

    console.log("8888888888888888888888888888888888888")
        // cur_frm.set_df_property("project_template", "set_only_once", 1);


        frm.clear_table('address_list')
        frm.clear_table('contact_list')
        frm.doc.aadhaar_number=""
        frm.doc.consumer_number=""
        frm.doc.contact_number=""
        frm.doc.customer_name=""
        frm.doc.customer=""
        frm.refresh_field('aadhaar_number')
        frm.refresh_field('contact_list')
        frm.refresh_field('consumer_number')

        frm.refresh_field('contact_number')
        frm.refresh_field('aadhaar_number')
        frm.refresh_field('customer_name')
        frm.refresh_field('customer')
        frm.refresh_field('address_list')

        console.log(frm.doc.customer)

        // frappe.msgprint("hii")
        if (frm.doc.opportunity_from=="Lead") {
          if (frm.doc.party_name){



            frm.clear_table('address_list')
            frm.clear_table('contact_list')

            console.log("worked")

            frappe.model.with_doc('Lead', frm.doc.party_name, function () {

                let ld = frappe.model.get_doc('Lead',frm.doc.party_name);
                console.log(ld,"###############11111111111111")
                if (ld.number_to_be_contacted){
                    frm.doc.contact_number=ld.number_to_be_contacted
                }
                if (ld.aadhaar_number){
                    frm.doc.aadhaar_number=ld.aadhaar_number
                }
                if (ld.consumer_number){
                   frm.doc.consumer_number=ld.consumer_number
               }
                const target_row=frm.add_child('contact_list')
                console.log("hiiiiii")
                target_row.contact_number =ld.number_to_be_contacted;
                target_row.email_id = ld.email_id;
                frm.refresh_field('contact_list');




                    frappe.call({
                        // specify the server side method to be called.
                        //dotted path to a whitelisted backend method
                        method: "a3sola_solar_management.doc_events.opportunity_events.test",
                        //Passing variables as arguments with request
                        args: {
                           doc:frm.doc.party_name,
                           type:"lead"

                        },

                        //Function passed as an argument to above function.
                        callback: function(r) {
                console.log(r.message.address_title,"###############")
                {

                        const target_row=frm.add_child('address_list')
                        target_row.address =r.message.address_title;
                        target_row.address_line_1 = r.message.address_line1;
                        target_row.address_line_2 = r.message.address_line2;
                        target_row.city=r.message.city;
                        target_row.state=r.message.state;
                        target_row.country=r.message.country;
                        frm.refresh_field('address_list');
                }
             }
                         });

                        }

)}}





else if (frm.doc.opportunity_from="Customer" ){
  if (frm.doc.party_name){
    frappe.model.with_doc('Customer', frm.doc.party_name, function () {

        let cu = frappe.model.get_doc('Customer',frm.doc.party_name);
        console.log(cu,"@@@@@@@@@@@@@@@@@@@@")
        if (cu.aadhaar_number){
            frm.doc.aadhaar_number=cu.aadhaar_number
        }
        if (cu.mobile_no){
            frm.doc.contact_number=cu.mobile_no
        }
        const target_row=frm.add_child('contact_list')
        console.log("hiiiiii")
        target_row.contact_number =cu.mobile_no;
        target_row.email_id = cu.email_id;
        frm.refresh_field('contact_list');

        frappe.call({
            // specify the server side method to be called.
            //dotted path to a whitelisted backend method
            method: "a3sola_solar_management.doc_events.opportunity_events.test",
            //Passing variables as arguments with request
            args: {
               doc:frm.doc.party_name,
               type:"customer"

            },

            //Function passed as an argument to above function.
            callback: function(r) {
    console.log(r.message.address_title,"###############")
    {

            const target_row=frm.add_child('address_list')
            target_row.address =r.message.address_title;
            target_row.address_line_1 = r.message.address_line1;
            target_row.address_line_2 = r.message.address_line2;
            target_row.city=r.message.city;
            target_row.state=r.message.state;
            target_row.country=r.message.country;
            frm.refresh_field('address_list');
    }
 }
             });



    })
  }


}








                }


})






















// frappe.ui.form.on('Opportunity', {
//     party_name: function (frm) {
//         if (frm.doc.party_name) {

//             frappe.model.with_doc('Project Settings', function () {




//                  //primary
//                  frappe.call({
//                     // specify the server side method to be called.
//                     //dotted path to a whitelisted backend method
//                     method: "a3sola_solar_management.doc_events.opportunity_events.test",
//                     //Passing variables as arguments with request
//                     args: {
//                         doc:frm.doc.name,
//                         scheme:frm.doc.scheme_name,



//                     },

//                     //Function passed as an argument to above function.
//                     callback: function(r) {
//                     //To show message
//                     console.log(r.message)

//                     console.log(r.message.ccon);

//                     console.log(frm.project_name)

//                     cur_frm.set_value('project_template',r.message.temp);
//                     cur_frm.refresh_field('project_template');


//                            },


//                     });






//                 });
//         }



//     },

// });

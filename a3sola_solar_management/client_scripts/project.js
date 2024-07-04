
frappe.ui.form.on('Project', {


    refresh:function(frm){
        {
            cur_frm.fields_dict['board_name'].get_query = function(doc) {
                return {
                    filters: {
                        "customer_group": "A3sola"
                    }
                 }
                }
            }

            {

                cur_frm.fields_dict['oppertunity'].get_query = function(doc) {
                    return {
                        filters: {
                            // "customer_name": frm.doc.project_name,
                            "aadhaar_number":frm.doc.aadhar_number

                        }
                     }
                    }}

            {

                cur_frm.fields_dict['customer'].get_query = function(doc) {
                    return {
                        filters: {
                             "aadhaar_number":frm.doc.aadhar_number

                        }
                     }
                    }}




        console.log(cur_frm.doc.scheme_name)


        if (!cur_frm.doc.scheme_name){
            cur_frm.fields_dict['project_template'].get_query = function(doc) {
                return {
                    filters: {
                        "Project_group": "Off-Grid",

                    }
                 }

            }

            frm.fields_dict['item'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
                return {
                    filters: [
                        ['scheme_name','=','']

                    ]
                }
            }

            }

        else {
            cur_frm.fields_dict['project_template'].get_query = function(doc) {
                return {
                    filters: {
                        "Project_group": "On-Grid"
        }
            }
        }
        frm.fields_dict['item'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
            console.log(frm.doc.scheme_name)
            return {
                filters: [
                    ['scheme_name','=',frm.doc.scheme_name]

                ]
            }
        }

    }




      if (!cur_frm.doc.__islocal){
        frm.add_custom_button("Track Project", function(){




      console.log(window.location.host)
      let route_add=window.location.host

      var show='/show?id='
      let r1 = route_add.concat("", show);


      var tid=frm.doc.tracking_id

      let result = frm.doc.url;


      console.log(result)
      var myWin = window.open(result,"_blank");
    })}},




    scheme_name:function(frm){

      console.log("wiattyy")
      console.log(cur_frm.doc.scheme_name)
        if (cur_frm.doc.scheme_name==''){
          console.log("hai")
            frm.fields_dict['project_template'].get_query = function(doc) {
                return {
                    filters: {
                        "Project_group": "Off-Grid",

                    }
                 }

            }

            frm.fields_dict['item'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
                return {
                    filters: [
                        ['scheme_name','=','']

                    ]
                }
            }

            }

        else {
            cur_frm.fields_dict['project_template'].get_query = function(doc) {
                return {
                    filters: {
                        "Project_group": "On-Grid"
        }
            }
        }
        frm.fields_dict['item'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
            console.log(frm.doc.scheme_name)
            return {
                filters: [
                    ['scheme_name','=',frm.doc.scheme_name]

                ]
            }
        }

    }






},

    customer:function(frm){

        if (frm.doc.customer){
            console.log("hiiiii")
            frappe.model.with_doc('Customer', frm.doc.customer, function () {


                let source_doc = frappe.model.get_doc('Customer', frm.doc.customer);
                if(source_doc.customer_primary_address){
                    cur_frm.set_value("address",source_doc.customer_primary_address);

                    frm.refresh_field('address');
                        // frm.address=source_doc.customer_primary_address;
                if (source_doc.email_id)
                {
                    cur_frm.set_value("email",source_doc.email_id);

                    frm.refresh_field('email');
                    // frm.email=source_doc.email_id;
                }

                }
            })

        }

    },






    oppertunity: function (frm) {
        // cur_frm.set_df_property("project_template", "set_only_once", 1);
        // frappe.msgprint("hii")
        
        if (frm.doc.oppertunity) {
            console.log("^#^&")

            frm.clear_table('address_list')
            frm.clear_table('contact_list')
            frm.clear_table('subsidy_detail')
            frm.clear_table('item')
            console.log("worked")
            frappe.model.with_doc('Opportunity', frm.doc.oppertunity, function () {


                let source_doc = frappe.model.get_doc('Opportunity', frm.doc.oppertunity);
                if (frm.doc.aadhaar_number && frm.doc.consumer_number){

                if(source_doc.consumer_number){
                    

                        frm.consumer_number=source_doc.consumer_number;
                        console.log(frm.consumer_number)
                        cur_frm.set_value("consumer_number",source_doc.consumer_number);
                        frm.refresh_field('consumer_number');}}
                    else{
                        // if (source_doc.aadhaar_number==undefined && source_doc.consumer_number==undefined){
                        //     frappe.throw("Please fill Aadhaar number and Consumer number")
                        // }
                        if (source_doc.consumer_number==undefined){
                            frappe.throw("Please fill Consumer number")
        
        
                        }
                        // else if (source_doc.aadhaar_number==undefined){
                        // frappe.throw("Please fill Aadhaar number")
                        // }
                    }
                    


                        // source_doc.items.forEach(source_row => {


                        //     console.log(source_row.item_code)
                        //      cur_frm.set_value("item_name",source_row.item_code);

                        //      frm.refresh_field('item_name');

                        //  });



                    {

{
                    if (source_doc.scheme_name)
                    {
                    cur_frm.doc.scheme_name = source_doc.scheme_name;
                    }
                    if (source_doc.board_name){
                    cur_frm.doc.board_name = source_doc.board_name;
                    // frm.refresh_field('subsidy_detail');
                    // var scheme=source_row.scheme
                    // var board=source_row.board_details
                    }
                    if (source_doc.category){
                        cur_frm.doc.category = source_doc.category
                    }
                    if (source_doc.subsidy_percentage){
                        cur_frm.doc.subsidy_percentage = source_doc.subsidy_percentage
                    }
                }

                    if  (source_doc.address_list){
                    source_doc.address_list.forEach(source_row => {


                    const target_row=frm.add_child('address_list')
                    target_row.address = source_row.address;
                    target_row.address_line_1 = source_row.address_line_1;
                    target_row.address_line_2 = source_row.address_line_2;
                    target_row.city=source_row.city;
                    target_row.state=source_row.state;
                    target_row.country=source_row.country;
                    frm.refresh_field('address_list');

                    var scheme=source_row.scheme
                    // var board=source_row.board_details

                    console.log(scheme)


                });
            }
//contact table
                if (source_doc.contact_list){
                    source_doc.contact_list.forEach(source_row => {
                    const target_row=frm.add_child('contact_list')
                    target_row.contact_number = source_row.contact_number;
                    target_row.is_primary = source_row.is_primary;
                    target_row.email_id = source_row.email_id;
                    frm.refresh_field('contact_list');

                    var scheme=source_row.scheme
                    // var board=source_row.board_details

                    console.log(scheme)

                });
            };
            
            
            source_doc.items.forEach(source_row => {


                const target_row=frm.add_child('item')
                target_row.item_code = source_row.item_code;
                target_row.description = source_row.description;
                target_row.item_name = source_row.item_name;
                target_row.qty = source_row.qty;

                frm.refresh_field('item');

                console.log("scheme")
                // var board=source_row.board_details


            });

                    //primary
                   frappe.call({
                    // specify the server side method to be called.
                    //dotted path to a whitelisted backend method
                    method: "a3sola_solar_management.doc_events.projects_events.test",
                    //Passing variables as arguments with request
                    args: {
                        doc:frm.doc.name,
                        op:source_doc.name,
 

                    },

                    //Function passed as an argument to above function.
                    callback: function(r) {
                    //To show message
                    console.log(r.message)

                    console.log(r.message.ccon);

                    console.log(frm.project_name)
                    console.log("^^^^^^^^^^^^^^")
                   
                    cur_frm.set_value("customer",r.message.customer);
                    cur_frm.set_value("aadhar_number",r.message.aad);
                    cur_frm.set_value("contact_number",r.message.ccon);
                    cur_frm.set_value("address",r.message.cadd);
                    cur_frm.set_value('primary_address',r.message.padd);
                    cur_frm.set_value('email',r.message.email);
                    cur_frm.set_value('project_template',r.message.tm);
                    cur_frm.set_value('scheme_name',r.message.sc);
                    cur_frm.set_value('board_name',r.message.bd);
                    cur_frm.set_value('project_name',r.message.pn);
                    cur_frm.set_value('subsidy_percentage',r.message.sp);
                    cur_frm.set_value('category',r.message.ct);
                    // cur_frm.set_value('expected_end_date',r.message.ct);



                    frm.refresh_field('address');
                    frm.refresh_field('aadhar_number');
                    frm.refresh_field('scheme_name');
                    frm.refresh_field('board_name');
                    frm.refresh_field('contact_number');
                    frm.refresh_field('customer');
                    frm.refresh_field('primary_address');
                    frm.refresh_field('project_template');
                    frm.refresh_field('project_name');
                    frm.refresh_field('subsidy_percentage');
                    frm.refresh_field('category');
                    // frm.refresh_field('expected_end_date');





                           },


                    });


                    if (cur_frm.doc.scheme_name==undefined){
                        cur_frm.fields_dict['project_template'].get_query = function(doc) {
                            return {
                                filters: {
                                    "Project_group": "Off-Grid",

                                }
                             }

                        }

                        frm.fields_dict['item'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
                            return {
                                filters: [
                                    ['scheme_name','=','']

                                ]
                            }
                        }

                        }

                    else {
                        cur_frm.fields_dict['project_template'].get_query = function(doc) {
                            return {
                                filters: {
                                    "Project_group": "On-Grid"
                    }
                        }
                    }
                    frm.fields_dict['item'].grid.get_field("item_code").get_query = function(doc, cdt, cdn) {
                        console.log(frm.doc.scheme_name)
                        return {
                            filters: [
                                ['scheme_name','=',frm.doc.scheme_name]

                            ]
                        }
                    }

                }


                }


            });



        }},

        expected_start_date: function (frm) {

            let expected_start_date=frm.doc.expected_start_date;
            console.log(expected_start_date)

            if (frm.doc.scheme_name){
                frappe.call({

                method: "a3sola_solar_management.doc_events.projects_events.enddate",

                args: {
                    scheme_name:frm.doc.scheme_name,
                    sdate:expected_start_date,

                },

                callback: function(r) {

                console.log(r)
                console.log(r.message)
                console.log("%%%%%%%%%%%%%%")
                cur_frm.set_value("expected_end_date",r.message);

                frm.refresh_field('expected_end_date');

                       },


                })
              }

            else if (frm.doc.project_template){

                frappe.call({

                    method: "a3sola_solar_management.doc_events.projects_events.enddate2",
    
                    args: {
                        p_template:frm.doc.project_template,
                        sdate:expected_start_date,
    
                    },
    
                    callback: function(r) {
    
                    console.log(r)
                    console.log(r.message)
                    cur_frm.set_value("expected_end_date",r.message);
    
                    frm.refresh_field('expected_end_date');
    
                           },
    
    
                    })
                

                
            }
              

            


        },
        after_save:function (frm) {


          

            frappe.call({
                // specify the server side method to be called.
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.doc_events.projects_events.aftersavefetch",
                //Passing variables as arguments with request
                args: {
                    pro:frm.doc.name,
                    
                },
      
      
          })
      
        }


        })




        // expected_start_date :function(frm){

        //     console.log("Haiiiiiiiiiiiiii")
        //     let expected_start_date=frm.doc.expected_start_date;
        //     console.log(expected_start_date)
        //     frappe.call({
        //         // specify the server side method to be called.
        //         //dotted path to a whitelisted backend method
        //         method: "a3sola_solar_management.doc_events.projects_events.enddate",
        //         //Passing variables as arguments with request
        //         args: {
        //             doc:frm.doc.name,
        //             sdate:expected_start_date,

        //         },

        //         //Function passed as an argument to above function.
        //         callback: function(r) {
        //         //To show message
        //         console.log(r.message)

        //         console.log(r.message.ccon);

        //         console.log(frm.project_name)
        //         cur_frm.set_value("expected_end_date",r.message.end);

        //         frm.refresh_field('expected_end_date');

        //                },


        //         });



        //     };







                //    //primary
                //    frappe.call({
                //     // specify the server side method to be called.
                //     //dotted path to a whitelisted backend method
                //     method: "a3sola_solar_management.doc_events.projects_events.test",
                //     //Passing variables as arguments with request
                //     args: {
                //         doc:frm.doc.name,
                //         op:"CRM-OPP-2022-00002",


                //     },

                //     //Function passed as an argument to above function.
                //     callback: function(r) {
                //     //To show message
                //     console.log(r.message)
                //     console.log(r)
                //     console.log(r.message.ccon);
                //     frm.customer=r.message.customer;
                //     frm.address=r.message.cadd;
                //     frm.contact=r.ccon;
                //     frm.refresh_field('address');
                //     frm.refresh_field('contact');
                //     frm.refresh_field('customer');



                //            },

                //     });



    // frm.doc.customer=source_doc.customer;
    //             frm.refresh_field('customer');
    //             frm.doc.address=source_doc.customer_address;
    //             frm.doc.contact=source_doc.contact_person;
    //             frm.refresh_field('address');
    //             frm.refresh_field('contact');



    // let customer = frappe.model.get_doc(Customer,filters={"opportunity_name": "CRM-OPP-2022-00002"});

    // console.log(customer.customer_primary_address);
    // frm.doc.customer=customer;
    // frm.doc.address=customer.customer_primary_address;
    // frm.doc.contact=customer.customer_primary_contact;

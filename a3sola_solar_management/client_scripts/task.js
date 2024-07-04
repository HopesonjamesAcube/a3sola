


frappe.ui.form.on("Task",{


  "refresh": function(frm) {
    console.log("11111111111111111111111111111")
    if (!cur_frm.doc.__islocal){




        if (!cur_frm.doc.__islocal){
            cur_frm.add_custom_button(__("Call"), function() {
                console.log("hello")
                var childTable = cur_frm.add_child("track_follow_ups");
                childTable.date_and_time=frappe.datetime.now_datetime();
                childTable.user=frappe.session.user_fullname
                cur_frm.refresh_fields("track_follow_ups");
              
        
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
      }
    },

  onload(frm) {
    console.log("hi")

    
      var prev_route = frappe.get_prev_route();
      
      
      
      if (prev_route[1] === 'Issue') {
    
        let source_doc = frappe.model.get_doc('Issue', prev_route[2]);
        frm.set_value("contact_number",source_doc.contact_number );
       
        frm.refresh_field('contact_number');
  }
},
    status:function(frm){

      console.log('hi')
      console.log(frappe.datetime.nowdate())
     
      frm.set_value('completed_on',frappe.datetime.nowdate())

      frm.set_value('completed_by',frappe.session.logged_in_user);
      frm.refresh_field('completed_by');

      if(cur_frm.doc.status=="Completed"){
        console.log('test')
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


    },

    onload_post_render: function (frm) {

      if (cur_frm.doc.doctypes_name=="Sales Order" || cur_frm.doc.doctypes_name=="Sales Invoice" ||cur_frm.doc.doctypes_name=="Payment Entry" || cur_frm.doc.doctypes_name=="Pick List" || cur_frm.doc.doctypes_name=="Delivery Note"){
    frappe.call({
          // specify the server side method to be called.
          //dotted path to a whitelisted backend method
          method: "a3sola_solar_management.doc_events.task_events.exist",
          //Passing variables as arguments with request
          args: {
            doc:frm.doc.name,
            pro:frm.doc.project,
            type:frm.doc.doctypes_name,
          },

          //Function passed as an argument to above function.
          callback: function(r) {
                      //To show message
                      console.log(r.message)
                      console.log(r.message)
                      if (r.message==false){
                          $('#awesomplete_list_15').css('display','none');
                      }


               },//main call back

  })};

  if (cur_frm.doc.doctypes_name=="Sales Order"){
        frappe.call({
              // specify the server side method to be called.
              //dotted path to a whitelisted backend method
              method: "a3sola_solar_management.doc_events.task_events.popup",
              //Passing variables as arguments with request
              args: {
                doc:frm.doc.name,
                pro:frm.doc.project,
                type:frm.doc.doctypes_name,
              },

              //Function passed as an argument to above function.
              callback: function(r) {
                          //To show message
                          console.log(r.message)
                          console.log(r.message.ret)

                          if(!frm.doc.__islocal){
                          frm.add_custom_button(__("Create"), function() {

                          //
                          let d = new frappe.ui.Dialog({
                            title: 'Select Item',
                          //Add fields to fetch items
                                        fields: [
                              {
                                label: 'Quotations',
                                fieldname: 'docu',
                                fieldtype: 'Select',
                                options: r.message.ret

                              }],
                              primary_action_label: 'Confirm',


                              primary_action(values) {
                                          console.log("heyy")

                                          frappe.call({
                                            type: "POST",
                                            method: "frappe.model.mapper.make_mapped_doc",
                                            args: {
                                              method: `erpnext.selling.doctype.quotation.quotation.make_sales_order`,
                                              source_name: values.docu,
                                              args: null,
                                              selected_children: {}
                                            },
                                            freeze: true,
                                            freeze_message:  "",
                                            callback: function(r) {
                                              console.log("hiii")
                                              if (!r.exc) {
                                                frappe.model.sync(r.message);

                                                  frappe.get_doc(
                                                    r.message.doctype,
                                                    r.message.name
                                                  ).__run_link_triggers = true;

                                                frappe.set_route("Form", r.message.doctype, r.message.name);
                                              }
                                            }
                                          });



                                          // frappe.call({
                                          //   method: "erpnext.selling.doctype.quotation.quotation.make_sales_order",
                                          //   frm: quodoc
                                          //   source_name: 'SAL-QTN-2023-00015'
                                          // })

                                  } //Primary action


                            })//dialog
                            d.show();
                          })//button
                          }






                   },//main call back


      })};
      if (cur_frm.doc.doctypes_name=="Sales Invoice"){
      frappe.call({
            // specify the server side method to be called.
            //dotted path to a whitelisted backend method
            method: "a3sola_solar_management.doc_events.task_events.popup",
            //Passing variables as arguments with request
            args: {
              doc:frm.doc.name,
              pro:frm.doc.project,
              type:frm.doc.doctypes_name,
            },

            //Function passed as an argument to above function.
            callback: function(r) {
                        //To show message
                        console.log(r.message)
                        console.log(r.message.ret)

                        if(!frm.doc.__islocal){
                        frm.add_custom_button(__("Create"), function() {

                        //
                        let d = new frappe.ui.Dialog({
                          title: 'Select Item',
                        //Add fields to fetch items
                                      fields: [
                            {
                              label: 'Sales Orders',
                              fieldname: 'docu',
                              fieldtype: 'Select',
                              options: r.message.ret

                            }],
                            primary_action_label: 'Confirm',


                            primary_action(values) {
                                        console.log("heyy")

                                        frappe.call({
                                          type: "POST",
                                          method: "frappe.model.mapper.make_mapped_doc",
                                          args: {
                                            method: `erpnext.selling.doctype.sales_order.sales_order.make_sales_invoice`,
                                            source_name: values.docu,
                                            args: null,
                                              selected_children: {}

                                          },
                                          freeze: true,
                                          freeze_message:  "",
                                          callback: function(r) {
                                            console.log("hiii")
                                            if (!r.exc) {
                                              frappe.model.sync(r.message);

                                                frappe.get_doc(
                                                  r.message.doctype,
                                                  r.message.name
                                                ).__run_link_triggers = true;

                                              frappe.set_route("Form", r.message.doctype, r.message.name);
                                            }
                                          }
                                        });



                                        // frappe.call({
                                        //   method: "erpnext.selling.doctype.quotation.quotation.make_sales_order",
                                        //   frm: quodoc
                                        //   source_name: 'SAL-QTN-2023-00015'
                                        // })

                                } //Primary action


                          })//dialog
                          d.show();
                        })//button
                        }






                 },//main call back


    })};

    if (cur_frm.doc.doctypes_name=="Pick List"){
    frappe.call({
          // specify the server side method to be called.
          //dotted path to a whitelisted backend method
          method: "a3sola_solar_management.doc_events.task_events.popup",
          //Passing variables as arguments with request
          args: {
            doc:frm.doc.name,
            pro:frm.doc.project,
            type:frm.doc.doctypes_name,
          },

          //Function passed as an argument to above function.
          callback: function(r) {
                      //To show message
                      console.log(r.message)
                      console.log(r.message.ret)

                      if(!frm.doc.__islocal){
                      frm.add_custom_button(__("Create"), function() {

                      //
                      let d = new frappe.ui.Dialog({
                        title: 'Select Item',
                      //Add fields to fetch items
                                    fields: [
                          {
                            label: 'Sales Orders',
                            fieldname: 'docu',
                            fieldtype: 'Select',
                            options: r.message.ret

                          }],
                          primary_action_label: 'Confirm',


                          primary_action(values) {
                                      console.log("heyy")

                                      frappe.call({
                                        type: "POST",
                                        method: "frappe.model.mapper.make_mapped_doc",
                                        args: {
                                          method: `erpnext.selling.doctype.sales_order.sales_order.create_pick_list`,
                                          source_name: values.docu,
                                          args: null,
                                          selected_children: {}
                                        },
                                        freeze: true,
                                        freeze_message:  "",
                                        callback: function(r) {
                                          console.log("hiii")
                                          if (!r.exc) {
                                            frappe.model.sync(r.message);

                                              frappe.get_doc(
                                                r.message.doctype,
                                                r.message.name
                                              ).__run_link_triggers = true;

                                            frappe.set_route("Form", r.message.doctype, r.message.name);
                                          }
                                        }
                                      });



                                      // frappe.call({
                                      //   method: "erpnext.selling.doctype.quotation.quotation.make_sales_order",
                                      //   frm: quodoc
                                      //   source_name: 'SAL-QTN-2023-00015'
                                      // })

                              } //Primary action


                        })//dialog
                        d.show();
                      })//button
                      }






               },//main call back


  })};

  if (cur_frm.doc.doctypes_name=="Delivery Note"){
  frappe.call({
        // specify the server side method to be called.
        //dotted path to a whitelisted backend method
        method: "a3sola_solar_management.doc_events.task_events.popup",
        //Passing variables as arguments with request
        args: {
          doc:frm.doc.name,
          pro:frm.doc.project,
          type:frm.doc.doctypes_name,
        },

        //Function passed as an argument to above function.
        callback: function(r) {
                    //To show message
                    console.log(r.message)
                    console.log(r.message.ret)

                    if(!frm.doc.__islocal){
                    frm.add_custom_button(__("Create"), function() {

                    //
                    let d = new frappe.ui.Dialog({
                      title: 'Select Item',
                    //Add fields to fetch items
                                  fields: [
                        {
                          label: 'Pick lists',
                          fieldname: 'docu',
                          fieldtype: 'Select',
                          options: r.message.ret

                        }],
                        primary_action_label: 'Confirm',


                        primary_action(values) {
                                    console.log("heyy")

                                    frappe.call({
                                      type: "POST",
                                      method: "frappe.model.mapper.make_mapped_doc",
                                      args: {
                                        method: `erpnext.stock.doctype.pick_list.pick_list.create_delivery_note`,
                                        source_name: values.docu,
                                        args: null,
                                        selected_children: {}
                                      },
                                      freeze: true,
                                      freeze_message:  "",
                                      callback: function(r) {
                                        console.log("hiii")
                                        if (!r.exc) {
                                          frappe.model.sync(r.message);

                                            frappe.get_doc(
                                              r.message.doctype,
                                              r.message.name
                                            ).__run_link_triggers = true;

                                          frappe.set_route("Form", r.message.doctype, r.message.name);
                                        }
                                      }
                                    });



                                    // frappe.call({
                                    //   method: "erpnext.selling.doctype.quotation.quotation.make_sales_order",
                                    //   frm: quodoc
                                    //   source_name: 'SAL-QTN-2023-00015'
                                    // })

                            } //Primary action


                      })//dialog
                      d.show();
                    })//button
                    }






             },//main call back


  })};

  if (cur_frm.doc.doctypes_name=="Payment Entry"){
  frappe.call({
        // specify the server side method to be called.
        //dotted path to a whitelisted backend method
        method: "a3sola_solar_management.doc_events.task_events.popup",
        //Passing variables as arguments with request
        args: {
          doc:frm.doc.name,
          pro:frm.doc.project,
          type:frm.doc.doctypes_name,
        },

        //Function passed as an argument to above function.
        callback: function(r) {
                    //To show message
                    console.log(r.message)
                    console.log(r.message.ret)

                    if(!frm.doc.__islocal){
                    frm.add_custom_button(__("Create"), function() {

                    //
                    let d = new frappe.ui.Dialog({
                      title: 'Select Item',
                    //Add fields to fetch items
                                  fields: [
                        {
                          label: 'Sales Orders',
                          fieldname: 'docu',
                          fieldtype: 'Select',
                          options: r.message.ret

                        }],
                        primary_action_label: 'Confirm',


                        primary_action(values) {
                                    console.log("heyy")

                                    frappe.call({
                                      type: "POST",
                                      method: "erpnext.accounts.doctype.payment_entry.payment_entry.get_payment_entry",
                                      args: {
                                        dt:'Sales Order',
                                        dn: values.docu,

                                      },
                                      freeze: true,
                                      freeze_message:  "",
                                      callback: function(r) {
                                        console.log("hiii")
                                        if (!r.exc) {
                                          frappe.model.sync(r.message);

                                            frappe.get_doc(
                                              r.message.doctype,
                                              r.message.name
                                            ).__run_link_triggers = true;

                                          frappe.set_route("Form", r.message.doctype, r.message.name);
                                        }
                                      }
                                    });



                                    // frappe.call({
                                    //   method: "erpnext.selling.doctype.quotation.quotation.make_sales_order",
                                    //   frm: quodoc
                                    //   source_name: 'SAL-QTN-2023-00015'
                                    // })

                            } //Primary action


                      })//dialog
                      d.show();
                    })//button
                    }






             },//main call back


  })};








      document.querySelectorAll("[data-fieldname='message']")[1].style.color = 'red'

        if (frm.doc.project){

          



          // frm.set_df_property("doctypes_name", "read_only", frm.is_new() ? 0 : 1);
          // frm.set_df_property("message", "read_only", frm.is_new() ? 0 : 1);
          console.log("refresh")

          // set filters for quotation,sales order,invoice,etc
            cur_frm.fields_dict['quotation'].get_query = function(doc) {
              return {
                  filters: {
                      "project_id": frm.doc.project
                  }
              }
              }
              cur_frm.fields_dict['sales_order'].get_query = function(doc) {
                return {
                    filters: {
                        "project_id": frm.doc.project
                    }
                }
                }
              cur_frm.fields_dict['sales_invoice'].get_query = function(doc) {
                return {
                    filters: {
                        "project_id": frm.doc.project
                    }
                }
                }
              cur_frm.fields_dict['purchase_order'].get_query = function(doc) {
                return {
                    filters: {
                        "project_id": frm.doc.project
                    }
                }
                }

              cur_frm.fields_dict['material_request'].get_query = function(doc) {
                return {
                    filters: {
                        "project_id": frm.doc.project
                    }
                }
                }

                cur_frm.fields_dict['p_i'].get_query = function(doc) {
                  return {
                      filters: {
                          "project_id": frm.doc.project
                      }
                  }
                  }

              cur_frm.fields_dict['purchase_receipt'].get_query = function(doc) {
                return {
                    filters: {
                        "project_id": frm.doc.project
                    }
                }
                }
              

          document.querySelectorAll("[data-fieldname='message']")[1].style.color = 'red'
            // var Var=frappe.db.get_single_value("Task", "project")
            // console.log(Var)


              // document.querySelectorAll("[data-fieldname='message']")[1].style.backgroun = 'red'
            // $('input[data-fieldname="message"]').css("background-color","#FFE4C4");
            // $('input[data-fieldname="message"]').css("color","red")
            //
            // $["data-fieldtype=Small Text,fieldname=message"].css("background-color","#FFE4C4");

            console.log(frm.doc.subject)
            if (frm.doc.doctypes_name=="Sales Order")
                {
                    document.querySelectorAll("[data-fieldname='quotation']")[1].style.color = 'red'
                }

            if (frm.doc.doctypes_name=="Sales Invoice")
                {
                      document.querySelectorAll("[data-fieldname='sales_order']")[1].style.color = 'red'
                }
            if (frm.doc.doctypes_name=="Quotation")
                {
                  console.log("testttt")
                    document.querySelectorAll("[data-fieldname='opportunity']")[1].style.color = 'red'
                }
            if (frm.doc.doctypes_name=="Payment Entry")
                {
                    document.querySelectorAll("[data-fieldname='sales_order']")[1].style.color = 'red'
                }
            if (frm.doc.doctypes_name=="Pick List")
                {
                    document.querySelectorAll("[data-fieldname='sales_order']")[1].style.color = 'red'
                }


            if (frm.doc.doctypes_name=="Delivery Note") {

              document.querySelectorAll("[data-fieldname='sales_order']")[1].style.color = 'red'
              cur_frm.fields_dict['d_id'].get_query = function(doc) {
                  return {
                      filters: {
                          "project": frm.doc.project
                      }
                   }
                  }
            }

            else if (frm.doc.doctypes_name!="Quotation"){

            cur_frm.fields_dict['d_id'].get_query = function(doc) {
                return {
                    filters: {
                        "project_id": frm.doc.project
                    }
                 }
                }
            }


            else{
                if (frm.doc.lead_id){
                cur_frm.fields_dict['d_id'].get_query = function(doc) {
                    return {
                        filters: {
                            "party_name": frm.doc.lead_id
                        }
                     }
                    }
                  }
              else{
                cur_frm.fields_dict['d_id'].get_query = function(doc) {
                    return {
                        filters: {
                            "party_name": frm.doc.customer
                        }
                     }
                    }

              }
              

            }


    }}})





// frappe.ui.form.on("Task",{
//     onload: function (frm) {

//         if (frm.doc.project) {



// 			frappe.call({
// 				// specify the server side method to be called.
// 				//dotted path to a whitelisted backend method
// 				method: "a3sola_solar_management.doc_events.task_events.test",
// 				//Passing variables as arguments with request
// 				args: {
// 					doc:frm.doc.name,
// 					pro:frm.doc.project,

// 				},

// 				//Function passed as an argument to above function.
// 				callback: function(r) {
// 				//To show message
// 				console.log(r)

// 				filters:{
//                     "gender": "TASK-2022-00428"
//                  }

// 				frm.set_df_property('d_id', 'options', ["TASK-2022-00428"])
//                 set_field_options("d_id",["TASK-2022-00428"]);

//                 frm.refresh_field('d_id');


// 					   },


// 				});






// 		}

//     }

// });

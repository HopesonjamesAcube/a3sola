// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Completion Report', {
	// refresh: function(frm) {

	// }

    onload: function (frm) {
        var prev_route = frappe.get_prev_route();



        if (prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id",source_doc.project );
            console.log(source_doc.project)

            frappe.call({
                // specify the server side method to be called.
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.a3sola_solar_management.doctype.completion_report.completion_report.test",
                //Passing variables as arguments with request
                args: {
                    doc:frm.doc.name,
                    pro:source_doc.project,
                },

                //Function passed as an argument to above function.
                callback: function(r) {
                //To show message
                console.log(r.message)

                console.log(r.message.cadd);

                // console.log(frm.customer)
                cur_frm.set_value("address",r.message.cadd);
                cur_frm.set_value("customer_name",r.message.customer);
				cur_frm.set_value("consumer_number",r.message.consumer);
				cur_frm.set_value("contact",r.message.con);
                if(r.message.sta!=undefined){
                cur_frm.set_value("section",r.message.sta);
                }
                cur_frm.set_value("phase",r.message.ph);

                frm.refresh_field('address');
                frm.refresh_field('customer_name');
				frm.refresh_field('consumer_number');
                frm.refresh_field('section');
                frm.refresh_field('phase');





                       },


                });




        }
    },

    after_save:function (frm) { 


          

      frappe.call({
          // specify the server side method to be called.
          //dotted path to a whitelisted backend method
          method: "a3sola_solar_management.a3sola_solar_management.doctype.completion_report.completion_report.aftersavefetch",
          //Passing variables as arguments with request
          args: {
              doc:frm.doc.name,
              pro:cur_frm.doc.project_id,
          },


    })

  }

});
 
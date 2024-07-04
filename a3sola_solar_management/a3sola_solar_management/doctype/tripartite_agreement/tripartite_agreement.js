// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt


frappe.ui.form.on('Tripartite Agreement', {
    onload: function (frm) {
        var prev_route = frappe.get_prev_route();



        if (prev_route[1] === 'Task') {

            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id",source_doc.project );
            frm.set_value("opportunity_id",source_doc.opportunity);




            frappe.call({
                // specify the server side method to be called.
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.a3sola_solar_management.doctype.tripartite_agreement.tripartite_agreement.test",
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

                cur_frm.set_value("customer_name",r.message.customer);
                cur_frm.set_value("consumer_number",r.message.consno);
                cur_frm.set_value("address",r.message.cadd);

                cur_frm.set_value("item",r.message.item);
                if(r.message.price!=undefined  && r.message.discount_amount!=undefined && r.message.rate!=undefined && r.message.rate!=undefined){

                cur_frm.set_value("amount",r.message.price);
                cur_frm.set_value("subsidy_amount",r.message.discount_amount);
                cur_frm.set_value("grand_total",r.message.rate);
                cur_frm.set_value("section",r.message.sta);
             
                
                }
                console.log("^^^^^^^^^^")
                console.log(r.message.capacity)
                if(r.message.capacity!=undefined){
                    cur_frm.set_value("item_capacity",r.message.capacity);
                    frm.refresh_field('item_capacity');
                }
                
                frm.refresh_field('amount');
                frm.refresh_field('subsidy_amount');
                frm.refresh_field('grand_total');
                frm.refresh_field('item');
                frm.refresh_field('section');


                frm.refresh_field('customer_name');
                frm.refresh_field('consumer_number');
                frm.refresh_field('address');


                       },


                });






        }
    }
});

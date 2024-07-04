// To enable form scripting of lead doctype
frappe.ui.form.on('Issue', {




  onload: function (frm) {
		var prev_route = frappe.get_prev_route();
		
		
		
		if (prev_route[1] === 'Customer Call Records') {
	
			let source_doc = frappe.model.get_doc('Customer Call Records', prev_route[2]);
			frm.set_value("contact_number",source_doc.caller_number );
            frm.refresh_field('contact_number');
            frm.set_value("opportunity",source_doc.opportunity);
            frm.refresh_field('opportunity');


        }
    },
    //Call function after save.
	refresh:function(frm) {






            //TESTT


if (!cur_frm.doc.__islocal){
    cur_frm.add_custom_button(__("Call"), function() {
        console.log("hello")
        var childTable = cur_frm.add_child("follow_ups");
        childTable.date_and_time=frappe.datetime.nowdate()
        childTable.user=frappe.session.user_fullname
        cur_frm.refresh_fields("follow_ups");
      

        let d = new frappe.ui.Dialog({
            title: 'Select Phone Number',
          //Add fields to fetch items
                        fields: [
              {
                label: 'Phone Numbers',
                fieldname: 'ph',
                fieldtype: 'Select',
                options: [frm.doc.contact_number]

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














   








},



});

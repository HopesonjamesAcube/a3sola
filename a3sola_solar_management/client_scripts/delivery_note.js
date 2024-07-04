frappe.ui.form.on('Delivery Note', {
  


    onload: function (frm) {
        var prev_route = frappe.get_prev_route();
        
      
        
        if (prev_route[1] === 'Task') {
            let source_doc = frappe.model.get_doc('Task', prev_route[2]);
            frm.set_value("project_id",source_doc.project );
            frm.set_value("project",source_doc.project );
            console.log(source_doc.project)

            frappe.call({
                // specify the server side method to be called. 
                //dotted path to a whitelisted backend method
                method: "a3sola_solar_management.a3sola_solar_management.doctype.service_report.service_report.test",
                //Passing variables as arguments with request
                args: {
                    doc:frm.doc.name,
                    pro:source_doc.project,   
                },
                
                //Function passed as an argument to above function. 
                callback: function(r) {
                //To show message
             
            
                cur_frm.set_value("customer",r.message.customer);
                
                
                // cur_frm.set_value("contact",r.message.con);
                
            
                frm.refresh_field('customer');
                
                


                
                       },
                      
        
                });



            
        }
    }
});
// Copyright (c) 2022, Acube Innovations and contributors
// For license information, please see license.txt

frappe.ui.form.on('Module Capacity', {
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
                method: "a3sola_solar_management.a3sola_solar_management.doctype.module_capacity.module_capacity.test",
                //Passing variables as arguments with request
                args: {
                    doc:frm.doc.name,
                    pro:source_doc.project,   
                },
                
                //Function passed as an argument to above function. 
                callback: function(r) {
                //To show message
              
                


                
                       },
                      
        
                });



            
        }
    },
    after_save:function (frm) {


          

        frappe.call({
            // specify the server side method to be called.
            //dotted path to a whitelisted backend method
            method: "a3sola_solar_management.a3sola_solar_management.doctype.module_capacity.module_capacity.aftersavefetch",
            //Passing variables as arguments with request
            args: {
                doc:frm.doc.name,
                pro:cur_frm.doc.project_id,
            },
  
  
      })
  
    }
});

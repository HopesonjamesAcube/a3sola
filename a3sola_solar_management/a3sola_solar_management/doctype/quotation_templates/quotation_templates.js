// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation Templates', {
	// refresh: function(frm) {

	// }
});

 

frappe.ui.form.on("Header Print Child", {


    variables: function(frm,cdt, cdn){

       
        console.log("Executing..")
        
		let row=locals[cdt][cdn];
            
				if (row.variables){
					
					console.log(row.disable)
					if( row.variables)
					{
						row.content=row.content+" "+row.variables
					}
					row.variables=undefined
					frm.refresh_field("page_header"); 
					frm.refresh_field("page_footer"); 

				}
            
        }
        })

	
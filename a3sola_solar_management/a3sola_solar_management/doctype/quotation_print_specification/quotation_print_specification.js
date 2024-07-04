// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quotation Print Specification', {
	// refresh: function(frm) {

	// }
});


//System spec total calculations
frappe.ui.form.on("System Specification", {


	amount: function(frm,cdt, cdn){

	   
		console.log("Executing..")
		

			
				var total_amount=0

				frm.doc.system_specification.forEach(source_row => {


					if(source_row.amount){
						total_amount=total_amount+parseFloat(source_row.amount);
					}
					
					
				})
				
				frm.set_value('total_spec_amount',total_amount);
					frm.refresh_field("total_spec_amount");  
			
		}
		
		})

//kseb charges total
		frappe.ui.form.on("KSEB Charges", {


			total_amount: function(frm,cdt, cdn){
		
			   
				console.log("Executing..")
				
		
					
						var total_amount=0
		
						frm.doc.kseb_charges.forEach(source_row => {
		
		
							if(source_row.total_amount){
								total_amount=total_amount+source_row.total_amount;
							}
							
							
						})
						
						frm.set_value('phase_3_total',total_amount);
							frm.refresh_field("phase_3_total");  
					
				}
				
				})

//specification rate charges

frappe.ui.form.on("Specification Rate", {




	

	total_amount: function(frm,cdt, cdn){

	   
		console.log("Executing..")
		

			
				var total_amount=0





				frm.doc.specification_rates.forEach(source_row => {


					if(source_row.total_amount){
						console.log(source_row.total_amount)
						total_amount=total_amount+parseFloat(source_row.total_amount);
						console.log(total_amount)
					}
					
					
				})
				
				frm.set_value('total_system_rate',total_amount);
					frm.refresh_field("total_system_rate");  
			
		}
		
		})

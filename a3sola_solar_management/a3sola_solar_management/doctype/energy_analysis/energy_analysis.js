// Copyright (c) 2024, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('Energy Analysis', {
	onload: function(frm) {
		var prev_route = frappe.get_prev_route();
		if (prev_route[1] === 'Task') {

			let source_doc = frappe.model.get_doc('Task', prev_route[2]);

			
			frm.set_value("project_id",source_doc.project );
			frm.set_value("consumer_name",source_doc.customer);
			frm.set_value("opportunity",source_doc.opportunity);
			console.log(frm.project_id)
			if (source_doc.project){
				console.log("projects")
			frappe.call({
				// specify the server side method to be called.
				//dotted path to a whitelisted backend method
				method: "a3sola_solar_management.a3sola_solar_management.doctype.energy_analysis.energy_analysis.test",
				//Passing variables as arguments with request
				args: {
					doc:frm.doc.name,
					pro:source_doc.project,
					
				},

				//Function passed as an argument to above function.
				callback: function(r) {
					console.log(r.message)
				//To show message
				if (r.message["consno"] != null){
					frm.set_value("consumer_number",r.message["consno"]);
				}
				}
			})
		}

		}
	}
});

frappe.ui.form.on('Energy Analysis Child Table', {
    previous_reading_date: function (frm, cdt, cdn) {
        calculateDaysDifference(frm, cdt, cdn);
    },

    present_reading_date: function (frm, cdt, cdn) {
        calculateDaysDifference(frm, cdt, cdn);
    }
});

function calculateDaysDifference(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var previousDate = child.previous_reading_date;
    var presentDate = child.present_reading_date;

    if (previousDate && presentDate) {
        var daysDifference = frappe.datetime.get_day_diff(presentDate, previousDate);
		if (daysDifference>=0){
        frappe.model.set_value(cdt, cdn, 'no_of_days', daysDifference);
		}
		else{
			frappe.model.set_value(cdt, cdn, 'no_of_days', 0);
		}
		
    }
	frm.refresh_field('no_of_days');
}

frappe.ui.form.on('Energy Analysis Child Table', {
    initial_meter_reading: function (frm, cdt, cdn) {
        calculate_reading_change(frm, cdt, cdn);
    },

    final_meter_reading: function (frm, cdt, cdn) {
        calculate_reading_change(frm, cdt, cdn);
    },
	mf:function (frm, cdt, cdn) {
        calculate_unit_consumed(frm, cdt, cdn);
	},
	unit_consumed_kwh_month:function (frm, cdt, cdn) {
        calculate_unit_consumed_per_day(frm, cdt, cdn);
	},
	unit_consumed_kwh_day:function (frm, cdt, cdn) {
        solar_plant_required_kwp(frm, cdt, cdn);
	},
	zone:function (frm, cdt, cdn) {
        solar_plant_required_kwp(frm, cdt, cdn);
	},
});

function calculate_reading_change(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var initial_reading = parseFloat(child.initial_meter_reading);
    var final_reading = parseFloat(child.final_meter_reading);

    if (!isNaN(initial_reading) && !isNaN(final_reading)) {
        var reading_difference =final_reading-initial_reading;

        if (reading_difference >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'unit_consumed_readings', reading_difference);
        }else{
			frappe.model.set_value(cdt, cdn, 'unit_consumed_readings', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'unit_consumed_readings', 0);
	}
	frm.refresh_field('unit_consumed_readings');
}

function calculate_unit_consumed(frm, cdt, cdn){
	var child = locals[cdt][cdn];
    var reading_change = parseFloat(child.unit_consumed_readings);
    var mf = parseFloat(child.mf);

	if (!isNaN(reading_change) && !isNaN(mf)) {
        var reading_consumed =reading_change*mf;

        if (reading_consumed >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_month', reading_consumed);
        }else{
			frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_month', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_month', 0);
	}
	frm.refresh_field('unit_consumed_kwh_month');
}

function calculate_unit_consumed_per_day(frm, cdt, cdn){
	var child = locals[cdt][cdn];
    var unit_consumed_month = parseFloat(child.unit_consumed_kwh_month);
    var number_of_days = parseFloat(child.no_of_days);

	if (!isNaN(unit_consumed_month) && !isNaN(number_of_days)) {
        var reading_consumed_day =unit_consumed_month/number_of_days;

        if (reading_consumed_day >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_day', reading_consumed_day);
        }else{
			frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_day', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_day', 0);
	}
	frm.refresh_field('unit_consumed_kwh_day');
}

function solar_plant_required_kwp(frm, cdt, cdn){
	console.log(";;;;;;;;;;;;;;;;;;;;;;;")
	var child = locals[cdt][cdn];
    var unit_consumed_day = parseFloat(child.unit_consumed_kwh_day);
	

	if (!isNaN(unit_consumed_day)) {
        if(child.zone=="Peak"){
			var solar_plant_val=(unit_consumed_day/4/0.8)
		}else if(child.zone){
			var solar_plant_val=(unit_consumed_day/4)
		}


        if (solar_plant_val >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'solar_plant_required_kwp_day', solar_plant_val);
        }else{
			frappe.model.set_value(cdt, cdn, 'solar_plant_required_kwp_day', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'solar_plant_required_kwp_day', 0);
	}
	frm.refresh_field('solar_plant_required_kwp_day');
}




frappe.ui.form.on('Energy Anaysis Consumer Number Child Table', {
    previous_reading_date: function (frm, cdt, cdn) {
        calculateDaysDifference_consumer(frm, cdt, cdn);
    },

    present_reading_date: function (frm, cdt, cdn) {
        calculateDaysDifference_consumer(frm, cdt, cdn);
    }
});

function calculateDaysDifference_consumer(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var previousDate = child.previous_reading_date;
    var presentDate = child.present_reading_date;

    if (previousDate && presentDate) {
        var daysDifference = frappe.datetime.get_day_diff(presentDate, previousDate);
		if (daysDifference>=0){
        frappe.model.set_value(cdt, cdn, 'no_of_days', daysDifference);
		}
		else{
			frappe.model.set_value(cdt, cdn, 'no_of_days', 0);
		}
		
    }
	frm.refresh_field('no_of_days');
}

frappe.ui.form.on('Energy Anaysis Consumer Number Child Table', {
    initial_meter_reading: function (frm, cdt, cdn) {
        calculate_reading_change_consumer(frm, cdt, cdn);
    },

    final_meter_reading: function (frm, cdt, cdn) {
        calculate_reading_change_consumer(frm, cdt, cdn);
    },
	mf:function (frm, cdt, cdn) {
        calculate_unit_consumed_consumer(frm, cdt, cdn);
	},
	unit_consumed_kwh_month:function (frm, cdt, cdn) {
        calculate_unit_consumed_per_day_consumer(frm, cdt, cdn);
	},
	unit_consumed_kwh_day:function (frm, cdt, cdn) {
        solar_plant_required_kwp_consumer(frm, cdt, cdn);
	},

});

function calculate_reading_change_consumer(frm, cdt, cdn) {
    var child = locals[cdt][cdn];
    var initial_reading = parseFloat(child.initial_meter_reading);
    var final_reading = parseFloat(child.final_meter_reading);

    if (!isNaN(initial_reading) && !isNaN(final_reading)) {
        var reading_difference =final_reading-initial_reading;

        if (reading_difference >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'unit_consumed_readings', reading_difference);
        }else{
			frappe.model.set_value(cdt, cdn, 'unit_consumed_readings', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'unit_consumed_readings', 0);
	}
	frm.refresh_field('unit_consumed_readings');
}

function calculate_unit_consumed_consumer(frm, cdt, cdn){
	var child = locals[cdt][cdn];
    var reading_change = parseFloat(child.unit_consumed_readings);
    var mf = parseFloat(child.mf);

	if (!isNaN(reading_change) && !isNaN(mf)) {
        var reading_consumed =reading_change*mf;

        if (reading_consumed >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_month', reading_consumed);
        }else{
			frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_month', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_month', 0);
	}
	frm.refresh_field('unit_consumed_kwh_month');
}

function calculate_unit_consumed_per_day_consumer(frm, cdt, cdn){
	var child = locals[cdt][cdn];
    var unit_consumed_month = parseFloat(child.unit_consumed_kwh_month);
    var number_of_days = parseFloat(child.no_of_days);

	if (!isNaN(unit_consumed_month) && !isNaN(number_of_days)) {
        var reading_consumed_day =unit_consumed_month/number_of_days;

        if (reading_consumed_day >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_day', reading_consumed_day);
        }else{
			frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_day', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'unit_consumed_kwh_day', 0);
	}
	frm.refresh_field('unit_consumed_kwh_day');
}

function solar_plant_required_kwp_consumer(frm, cdt, cdn){
	console.log(";;;;;;;;;;;;;;;;;;;;;;;")
	var child = locals[cdt][cdn];
    var unit_consumed_day = parseFloat(child.unit_consumed_kwh_day);
	

	if (!isNaN(unit_consumed_day)) {
       
		var solar_plant_val=(unit_consumed_day/4)

        if (solar_plant_val >= 0) {
			
            frappe.model.set_value(cdt, cdn, 'solar_plant_required_kwp_day', solar_plant_val);
        }else{
			frappe.model.set_value(cdt, cdn, 'solar_plant_required_kwp_day', 0);
		}
    }else{
		frappe.model.set_value(cdt, cdn, 'solar_plant_required_kwp_day', 0);
	}
	frm.refresh_field('solar_plant_required_kwp_day');
}
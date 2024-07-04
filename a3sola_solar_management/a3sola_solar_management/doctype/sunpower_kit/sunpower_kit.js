// Copyright (c) 2023, Misma and contributors
// For license information, please see license.txt

frappe.ui.form.on('SunPower Kit', {
	refresh: function (frm) {
		frm.toggle_enable("new_item_code", frm.is_new());
		frm.set_query("new_item_code", () => {
			return {
				query: "a3sola_solar_management.a3sola_solar_management.doctype.sunpower_kit.sunpower_kit.get_new_item_code",
				
			};
		});
	},
});

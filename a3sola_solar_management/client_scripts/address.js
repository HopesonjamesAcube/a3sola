// Filter customer group
frappe.ui.form.on("Attendance", {

    "refresh": function(frm) {

            cur_frm.fields_dict['customer_group'].get_query = function(doc) {

                    return {
                        filters:{"customer_group_name":["!=","A3sola"]}

                     }

                }
            }
        })

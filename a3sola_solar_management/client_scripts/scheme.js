// Filter provided by fields
frappe.ui.form.on("Scheme",{
    refresh: function (frm) {

            {
            cur_frm.fields_dict['provided_by'].get_query = function(doc) {
                return {
                    filters: {
                        "customer_group": "A3sola"
                    }
                 }
                }
            }}
            })

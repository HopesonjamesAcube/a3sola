from . import __version__ as app_version

app_name = "a3sola_solar_management"
app_title = "a3sola Solar Management"
app_publisher = "Misma"
app_description = "Custom App for a3sola Solar Management"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ms@acube.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/a3sola_solar_management/css/a3sola_solar_management.css"
# app_include_js = "/assets/a3sola_solar_management/js/a3sola_solar_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/a3sola_solar_management/css/a3sola_solar_management.css"
# web_include_js = "/assets/a3sola_solar_management/js/a3sola_solar_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "a3sola_solar_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_list_js = {
    "Attendance" : "client_scripts/attendance_list.js"
    }
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "a3sola_solar_management.install.before_install"
# after_install = "a3sola_solar_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "a3sola_solar_management.uninstall.before_uninstall"
# after_uninstall = "a3sola_solar_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "a3sola_solar_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
#doc events
doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#}
"Contact": {
 	"validate":"a3sola_solar_management.doc_events.contacts_events.validate"
 },
 "Customer": {
  	"validate":"a3sola_solar_management.doc_events.customer_events.validate",
      "after_insert":"a3sola_solar_management.doc_events.customer_events.after_insert",
  },
 "Lead": {
 	"validate":"a3sola_solar_management.doc_events.lead_events.validate",
     "before_insert":"a3sola_solar_management.doc_events.lead_events.before_insert",
     "after_insert":"a3sola_solar_management.doc_events.lead_events.after_insert",
 },
 "ToDo": {
 	"after_insert":"a3sola_solar_management.doc_events.todo_events.after_insert",
     "validate":"a3sola_solar_management.doc_events.todo_events.validate",
 },


"Opportunity": {
 "after_insert":"a3sola_solar_management.doc_events.opportunity_events.after_insert",
 "before_insert":"a3sola_solar_management.doc_events.opportunity_events.before_insert",
     # "on_update":"a3sola_solar_management.doc_events.opportunity_events.on_update",

    "validate":"a3sola_solar_management.doc_events.opportunity_events.validate",
  
  },
"Project Settings":{
	"validate":"a3sola_solar_management.doc_events.project_sett.validate",
	#"on_update":"a3sola_solar_management.doc_events.project_sett.on_update"
},
"Task":{
	"validate":"a3sola_solar_management.doc_events.task_events.validate",
"after_insert":"a3sola_solar_management.doc_events.task_events.after_insert"
},
"Address":{
	"validate":"a3sola_solar_management.doc_events.address_events.validate",
    "after_insert":"a3sola_solar_management.doc_events.address_events.after_insert",
#"on_update":"a3sola_solar_management.doc_events.project_sett.on_update"
},
 "Project": {
	"validate":"a3sola_solar_management.doc_events.projects_events.validate",
 "after_insert": "a3sola_solar_management.doc_events.projects_events.after_insert",
 "before_insert":"a3sola_solar_management.doc_events.projects_events.before_insert"
  },
   "Item": {
 "after_insert": "a3sola_solar_management.doc_events.item_events.after_insert"
  },
"Sales Invoice": {
 "on_submit": "a3sola_solar_management.doc_events.salesinvoice.on_submit",
 "validate":"a3sola_solar_management.doc_events.salesinvoice.validate"
  },
"Company":{
	"validate":"a3sola_solar_management.doc_events.company.validate"
},
"Payment Entry":{
	"validate":"a3sola_solar_management.doc_events.payment_entry.validate",
    "on_submit":"a3sola_solar_management.doc_events.payment_entry.on_submit",
    "after_insert":"a3sola_solar_management.doc_events.payment_entry.after_insert"	
},
"Quotation":{
	  
    "after_insert":"a3sola_solar_management.doc_events.quotation.after_insert",
    "on_submit":"a3sola_solar_management.doc_events.quotation.on_submit",
     "validate":"a3sola_solar_management.doc_events.quotation.validate",
},
"Sales Order":{
	"on_submit":"a3sola_solar_management.doc_events.sales_order.on_submit",
    "validate":"a3sola_solar_management.doc_events.sales_order.validate",
    
    
},
"Delivery Note":{
    "validate":"a3sola_solar_management.doc_events.delivery_note.validate",
    "on_submit":"a3sola_solar_management.doc_events.delivery_note.on_submit",
    "after_insert":"a3sola_solar_management.doc_events.delivery_note.after_insert",
    "on_update_after_submit":"a3sola_solar_management.doc_events.delivery_note.on_update",
},
"Employee Checkin":{
    "validate":"a3sola_solar_management.doc_events.Employee_Checkin.validate"  
},
"Maintenance Schedule":{
    "on_submit":"a3sola_solar_management.doc_events.maintenance_schedule.on_submit",
},
"Maintenance Visit":{
    "on_submit":"a3sola_solar_management.doc_events.maintenance_visit.on_submit",
    "validate":"a3sola_solar_management.doc_events.maintenance_visit.validate",
},
"Item Price":{
    "validate":"a3sola_solar_management.doc_events.item_price.validate"
},
"Supplier":{
    "after_insert":"a3sola_solar_management.doc_events.supplier.after_insert",
    "before_insert":"a3sola_solar_management.doc_events.supplier.before_insert",
},
"Issue":{
    "validate":"a3sola_solar_management.doc_events.issue.validate",
}
,
"DocShare":{
    "after_insert":"a3sola_solar_management.doc_events.docshare.after_insert"
},


"Attendance":{

    "validate":"a3sola_solar_management.doc_events.attendance.validate",
    "after_insert":"a3sola_solar_management.doc_events.attendance.after_insert",
    "on_submit":"a3sola_solar_management.doc_events.attendance.on_submit",
},
"Product Bundle":{

    "validate":"a3sola_solar_management.doc_events.product_bundle.validate",
},
"Stock Entry":{
    "validate":"a3sola_solar_management.doc_events.stock_entry.validate"
}



}

override_doctype_class = {
    "Project": "a3sola_solar_management.doc_events.projects_events.Projectc",
}

doctype_js = {

    "Lead": "client_scripts/lead.js",

"Opportunity": "client_scripts/opportunity.js",
"Quotation": "client_scripts/quotation.js",

"Project":"client_scripts/project.js",
"Journal Entry":"client_scripts/journal_entry.js",
"Task":"client_scripts/task.js",
"Sales Order": "client_scripts/salesorder.js",
"Scheme":"client_scripts/scheme.js",
"Delivery Note":"client_scripts/delivery_note.js",
"Customer":"client_scripts/customer.js",
"Payment Entry":"client_scripts/payment_entry.js",
"Employee Incentive":"client_scripts/incentive.js",
"Quality Inspection":"client_scripts/quality.js",
"Employee Checkin":"client_scripts/check_in.js",
"Maintenance Schedule":"client_scripts/maintenance.js",
"Attendance":"client_scripts/attendance.js",
"Issue":"client_scripts/issue.js",
"Sales Invoice":"client_scripts/sales_invoice.js",
"Expense Claim":"client_scripts/expense_claim.js",

}

fixtures = [{'dt':"Workspace"},{'dt':'Customized Documentation'},
           
               
               {'dt':'Assignment Rule'},
            # # {'dt':'Territory'},
            # # {'dt':'Electricity Board'},
            # {'dt':'Task'},{'dt':'Project Template'},
            # # {'dt':'Scheme'},
         
            # {'dt':'Item'},{'dt':'Product Bundle'},
            
# 	{'dt':"Web Page","filters":[
# 	['name',"in",
# 	["A3Sola Documentation"]]
# ]},
{'dt':"Role Profile"},{'dt':"Module Profile"},

# {'dt':"Website Sidebar","filters":[
# 	['name',"in",
# 	["A3Sola Documentation"]]
# ]},

{'dt':"Role","filters":[
	['name',"in",
	["Employees","Main User","Coordinator","Telecaller","Installer","Restricted","Dealer","Basic","Store","Assistant Executives","Assistant Executive","Accountant","Supervisors","Technician"]
	]
]},
# {'dt':"Role Permission for Page and Report"},

  {"dt": "Custom DocPerm", "filters": [
            [
            "role", "in", [
                    "Employees",
                    "Main User",
                    "Guest","Coordinator","Telecaller","Installer","Dealer","Basic","Store","Assistant Executives","Assistant Executive","Accountant","Supervisors","Technician"
    		       ]
                ]
  ]
            },
        ]





# staging_version = '11.x.x'
#
# after_install = "a3sola_solar_management.setup.install.after_install"

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron":{
        "1 5 */1 * *":["a3sola_solar_management.doc_events.lead_events.cron"]
    }
	# "all": [
	# 	"a3sola_solar_management.tasks.all"
	# ],
	# "daily": [
	# 	"a3sola_solar_management.tasks.daily"
	# ],
	# "hourly": [-
	# 	"a3sola_solar_management.tasks.hourly"
	# ],
	# "weekly": [
	# 	"a3sola_solar_management.tasks.weekly"
	# ],
	# "monthly": [
	# 	"a3sola_solar_management.tasks.monthly"
	# ]
}

# Testing
# -------

# before_tests = "a3sola_solar_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "a3sola_solar_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "a3sola_solar_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------
#auth_hooks = [
	#"a3sola_solar_management.auth.validate"
#]

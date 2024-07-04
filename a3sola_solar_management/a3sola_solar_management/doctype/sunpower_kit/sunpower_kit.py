# Copyright (c) 2023, Misma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SunPowerKit(Document):
	def after_insert(doc):
		if not frappe.db.exists("Product Bundle", doc.name):
			pb = frappe.new_doc("Product Bundle")
			pb.new_item_code=doc.new_item_code
			if not frappe.db.exists("Item", 'Bundle item'):
				newitem = frappe.new_doc("Item")
				newitem.item_code = 'Bundle item'
				newitem.item_name = 'Bundle item'
				newitem.item_group = 'All Item Groups'
				newitem.is_stock_item = 0
				newitem.save()

			
			pb.append("items", {
				"item_code": 'Bundle item',
				"qty": 0,
				"description": doc.description,
			})
			pb.save()
			


@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_new_item_code(doctype, txt, searchfield, start, page_len, filters):
	from erpnext.controllers.queries import get_match_cond

	return frappe.db.sql(
		"""select name, item_name, description from tabItem
		where is_stock_item=0 and name not in (select name from `tabSunPower Kit`)
		and %s like %s %s limit %s, %s"""
		% (searchfield, "%s", get_match_cond(doctype), "%s", "%s"),
		("%%%s%%" % txt, start, page_len),
	)

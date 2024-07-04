from jinja2 import Template

import frappe

@frappe.whitelist()
def render_jinja_from_field(doc_name):
    
    doc = frappe.get_doc('Header Print','Header 1-0032')
    jinja_code = doc.your_field_name
    template = Template(jinja_code)
    
    # Assuming you want to render with the same doc's fields as context
    rendered_content = template.render(doc=doc)
    
    return rendered_content

import frappe
from frappe import _, get_doc
from frappe import publish_progress
from frappe.core.doctype.file.file import create_new_folder
from frappe.utils.file_manager import save_file



# def on_update(doc, methods):
#     if doc.pdf_doc:
#         getfile=frappe.get_doc("File",{"file_url":doc.pdf_doc})
#         res = getfile.name
#         print(res,"ghjklkjhgghjkkjhgghjkjhhjjhghjjhghjjhfk")
#         frappe.db.delete("File",res)
#         fallback_language = frappe.db.get_single_value("System Settings", "language") or "en"
#         args = {
#             "doctype": doc.doctype,
#             "name": doc.name,
#             "title": doc.get_title(),
#             "lang": getattr(doc, "language", fallback_language),
#             "show_progress": 0
#         }
#         fileurl = execute(**args)
#         url=frappe.utils.get_url()
#         doc.pdf_doc = fileurl
#         url=str(url)+str(doc.pdf_doc)
#         doc.attachment_url=url

#         attachments = frappe.get_all("File", filters={"attached_to_doctype":doc.doctype, "attached_to_name":doc.name}, fields=["name", "file_url"])
#         for attachment in attachments:
#             if attachment["file_url"] != fileurl:
#                 attach = get_doc("File", attachment["name"])
#                 attach.delete()

 
def attach_pdf(doc, event=None):


    fallback_language = frappe.db.get_single_value("System Settings", "language") or "en"
    args = {
        "doctype": doc.doctype,
        "name": doc.name,
        "title": doc.get_title(),
        "lang": getattr(doc, "language", fallback_language),
        "show_progress": 0
    }
    print("start")
    fileurl = execute(**args)
    
    print("iside start",fileurl)
    document=frappe.get_doc(doc.doctype,doc.name)
  
    document.pdf_doc=fileurl
    url=frappe.utils.get_url()

    url=str(url)+str(document.pdf_doc)
    document.attachment_url=url
    print("^^^^^^")
    # document.save()
    print(fileurl,doc.doctype)  
    return fileurl,url
    # frappe.throw("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")




def enqueue(args):
    """Add method execute with given args to the queue."""
    frappe.enqueue(method=execute, queue='long',
                   timeout=30, is_async=True, **args)


def execute(doctype, name, title, lang=None, show_progress=True):
    """
    Queue calls this method, when it's ready.
    1. Create necessary folders
    2. Get raw PDF data
    3. Save PDF file and attach it to the document
    """
    progress = frappe._dict(title=("Creating PDF ..."), percent=0, doctype=doctype, docname=name)

    if lang:
        frappe.local.lang = lang

    if show_progress:
        publish_progress(**progress)

    doctype_folder = create_folder(_(doctype), "Home")
    title_folder = create_folder(title, doctype_folder)

    if show_progress:
        progress.percent = 33
        publish_progress(**progress)

    pdf_data = get_pdf_data(doctype, name)

    if show_progress:
        progress.percent = 66
        publish_progress(**progress)

    fileurl = save_and_attach(pdf_data, doctype, name, title_folder)
    print("start3")
    print(fileurl,"^^^^^^")

    if show_progress:
        progress.percent = 100
        publish_progress(**progress)

    return fileurl


def create_folder(folder, parent):
    """Make sure the folder exists and return it's name."""
    new_folder_name = "/".join([parent, folder])

    if not frappe.db.exists("File", new_folder_name):
        create_new_folder(folder, parent)

    return new_folder_name


def get_pdf_data(doctype, name):
    """Document -> HTML -> PDF."""
    html = frappe.get_print(doctype, name)
    return frappe.utils.pdf.get_pdf(html)


def save_and_attach(content, to_doctype, to_name, folder):
    """
    Save content to disk and create a File document.
    File document is linked to another document.
    """
    file_name = "{}.pdf".format(to_name.replace(" ", "-").replace("/", "-"))
    fileName = save_file(file_name, content, to_doctype,
              to_name, folder=folder, is_private=0)
    # print(fileName.file_url)
    print("^^^^^^^^^^^")
    print(fileName.name)
    f=frappe.get_doc("File",fileName.name)
    print("start2")
    print(f.file_url)
    return f.file_url


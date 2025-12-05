from flask import Blueprint, render_template, current_app, url_for, request, jsonify, render_template_string
from utils.print_to_terminal import print_to_terminal
# from app.send_email.email import send_email
from app.send_email.email_catalog_OLD import EMAIL_TYPES

from app.email.catalogue_email import EMAILS
from app.email.catalogue_layout import LAYOUTS
from app.email.send_email import send_email

main = Blueprint("main", __name__)

@main.get("/")
def home():
    """
    This is the home page to preview emails.
    It will render the template when you start the server.
    """
    layouts = list(LAYOUTS.keys())
    emails = list(EMAILS.keys())
    return render_template("home.html", active_page="home", layouts=layouts, emails=emails)

@main.get("/about")
def about():
    """
    This is the about page with information about his app.
    """
    return render_template("about.html", active_page="about")

@main.post("/api/render_preview")
def api_render_preview():
    """
    Renders email template preview in homepage.
    """
    data = request.get_json() or {}
    email_type = (data.get("email_type") or "").strip()
    layout_type = (data.get("layout_type") or "").strip()

    email_obj = EMAILS.get(email_type)
    if not email_obj:
        print_to_terminal(f"Email type: {email_type}", "RED")
        return jsonify({"success": False, "error": "Unknown email type."}), 400
    
    layout_obj = LAYOUTS.get(layout_type)
    if not layout_obj:
        print_to_terminal(f"Layout type: {layout_type}", "RED")
        return jsonify({"success": False, "error": "Unknown layout type."}), 400
    
    # Demo values
    demo_vals = {
        "name": "John Doe",
        "email": "john.doe@example.com",
    }

    # Render inline content if present in the object (it may contain Jinja like {{ name }})
    rendered_content = render_template_string(email_obj.get("content", ""), **demo_vals)

    context = {**demo_vals, "email_body": rendered_content}

    if email_obj["template"] != "none":
        path_to_template = layout_obj + email_obj["template"]
        body_html = render_template(path_to_template, **context)
    else:
        return jsonify({"success": False, "error": "Template not available."}), 400

    return jsonify({"success": True, "subject": email_obj["subject"], "html": body_html})



@main.post("/api/send_email")
def api_send_email():
    """
    Sends an email to the recipient provided in the homepage.
    """
    data = request.get_json() or {}
    email_type = (data.get("email_type") or "").strip()
    layout_type = (data.get("layout_type") or "").strip()
    email_address = (data.get("email") or "").strip()

    if not email_address:
        return jsonify({"success": False, "error": "Missing email address."}), 400

    email_obj = EMAILS.get(email_type)
    if not email_obj:
        print_to_terminal(f"Email type: {email_type}", "RED")
        return jsonify({"success": False, "error": "Unknown email type."}), 400
    
    layout_prefix = LAYOUTS.get(layout_type)
    if not layout_prefix:
        print_to_terminal(f"Layout type: {layout_type}", "RED")
        return jsonify({"success": False, "error": "Unknown layout type."}), 400
    
    try:
        send_email(email_address, email_obj, layout_prefix)
    except Exception as e:
        print_to_terminal(f"Error sending email: {e}", "RED")
        return jsonify({"success": False, "error": "Unable to send email."}), 500

    success = f"The email (type: {email_type}, layout: {layout_type}) was sent to you! Check your inbox!"

    return jsonify({"success": True, "message": success})
    
    





# @main.get("/")
# def home():
#     """
#     This is the home page with the form to test email sending.
#     It will render the template when you start the server.
#     """
#     return render_template("index.html", types=list(EMAIL_TYPES.keys()))

# THE BELLOW IS NOT PROPER / DELETE AFTER REVIEWING

@main.route("/preview_email", methods=["GET", "POST"])
def preview_email():
    """
    This is the home page with the form to test email sending.
    It will render the template when you start the server.
    """
    #email_type = request.form.get("type")
    # type_template =EMAIL_TYPES[email_type]["template"]  # email template name
    # subject = EMAIL_TYPES[email_type]["subject"]
    # name="John Doe"
    selected_type = request.form.get("type") or request.args.get("type")
    if not selected_type:
        # default to first key
        selected_type = next(iter(EMAIL_TYPES.keys()))

    return render_template("preview_email.html", types=list(EMAIL_TYPES.keys()), type=selected_type)

@main.post("/api/render_preview_template")
def api_render_preview_template():
    data = request.get_json() or {}
    email_type = (data.get("type") or "").strip()

    email_obj = EMAIL_TYPES.get(email_type)
    if not email_obj:
        print_to_terminal(f"Type: {email_type}", "RED")
        return jsonify({"success": False, "error": "Unknown email type."}), 400
    
    # Demo values
    demo_vals = {
        "name": "John Doe",
        "email": "john.doe@example.com",
    }

    # Render inline content if present in the object (it may contain Jinja like {{ name }})
    rendered_content = render_template_string(email_obj.get("content", ""), **demo_vals)

    context = {**demo_vals, "email_body": rendered_content}

    if email_obj["template"] != "none":
        body_html = render_template(email_obj["template"], **context)
    else:
        body_html = render_template_string(email_obj["content"], **context)

    return jsonify({"success": True, "subject": email_obj["subject"], "html": body_html})

@main.post("/get_email")
def get_email():
    """Handle form submission via Fetch (AJAX)."""
    data = request.get_json() or {}
    name = data.get("name")
    email = data.get("email")
    email_type = data.get("type")

    if not (name and email and email_type):
        return jsonify({"success": False, "error": "Missing fields."}), 400

    try:
        send_email(name, email, email_type)
        return jsonify({"success": True, "message": f"Email '{email_type}' sent to {email}. Check your inbox!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


# @main.route("/", methods=["GET", "POST"])
# def submit_form():
#     """
#     This is the home page with the form to test email sending.
#     It will appear when you start the server.
#     """
#     success = None

#     list_of_email_type_keys = list(EMAIL_TYPES.keys())

#     if request.method == "POST":
#         name = request.form.get("name")
#         email = request.form.get("email")
#         type_selected = request.form.get("type")

#         send_email(name, email, type_selected)
        
#         success = f"The email {type_selected} was sent to you! Check your inbox!"
#         print_to_terminal(f"Form submitted. Name = {name}, Email = {email}, Type = {type_selected}")


#     return render_template("index.html", types=list_of_email_type_keys, success=success)


# FOR TEST PURPOSES ONLY
# @main.route("/")
# def home():
#     return '<h1> Testing the App </h1>'
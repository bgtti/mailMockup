"""
routes.py contain all routes in this project.
These are:
- rendering of the homepage
- rendering of the about page
- email template selection change
- sending the template per email to the given email address
"""
from flask import Blueprint, render_template, request, jsonify, render_template_string
from utils.print_to_terminal import print_to_terminal
from app.email.catalogue_email import EMAILS
from app.email.catalogue_layout import LAYOUTS
from app.email.send_email import send_email

main = Blueprint("main", __name__)

@main.get("/")
def home():
    """
    This renderd the homopage.
    It will render the first email template when you start the server.
    """
    layouts = list(LAYOUTS.keys())
    emails = list(EMAILS.keys())
    return render_template("home.html", active_page="home", layouts=layouts, emails=emails)

@main.get("/about")
def about():
    """
    This will render the about page - which contains information about this project.
    """
    return render_template("about.html", active_page="about")

@main.post("/api/render_preview")
def api_render_preview():
    """
    Sends the selected template in the selected layout to the homepage when user changes type and layout selection.
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
    Sends an email with the selected template to the recipient provided in the homepage.
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
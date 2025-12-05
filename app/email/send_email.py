"""
**ABOUT THIS FILE**

auth/email_helpers.py contains helper functions that send auth-related email to users.
"""
from flask import render_template, render_template_string
from flask_mail import Message as EmailMessage
from utils.print_to_terminal import print_to_terminal
from app import mail, EMAIL_CREDENTIALS

def send_email(recipient_email: str, email_obj: dict, layout_prefix: str) -> None:
    """
    Sends the user a sample email.

    Parameters:
        recipient_email (str): The email address of the recipient.
        email_obj (dict): An object from the EMAILS dictionary (in catalogue_email.py).
        layout_prefix (str): A prefix/path from the LAYOUTS dictionary (in catalogue_layout.py),
                             e.g. "email/layouts/base_".
    """
    # Demo values
    demo_vals = {
        "name": "John Doe",
        "email": recipient_email,
    }

    # Render inline content if present in the object (it may contain Jinja like {{ name }})
    rendered_content = render_template_string(email_obj.get("content", ""), **demo_vals)

    # Context passed to the layout template
    context = {
        **demo_vals,
        "email_body": rendered_content,
    }

    # Build the path to the template file
    # Example: layout_prefix = "email/layouts/base_", email_obj["template"] = "simple.html"
    path_to_template = f"{layout_prefix}{email_obj['template']}"

    email_body = render_template(path_to_template, **context)

    new_email = EmailMessage(
        subject=email_obj["subject"],
        sender=EMAIL_CREDENTIALS["email_address"],
        recipients=[recipient_email],
    )
    new_email.html = email_body

    try:
        mail.send(new_email)
        print_to_terminal(f"Message sent to email {recipient_email}.", "GREEN")
    except Exception as e:
        print_to_terminal(
            "ERROR in send_email in send_email.py (see details below):", "RED"
        )
        print_to_terminal(f"Could not send email. Error: {e}", "YELLOW")
        raise


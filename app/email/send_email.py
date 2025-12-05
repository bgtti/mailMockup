"""
**ABOUT THIS FILE**

auth/email_helpers.py contains helper functions that send auth-related email to users.
"""
import logging
from flask import render_template
from flask_mail import Message as EmailMessage
from utils.print_to_terminal import print_to_terminal
from app import mail, EMAIL_CREDENTIALS
from .catalogue_email import EMAILS

# TODO: Replace app name with the name of your company
APP_NAME = "Your Company"

def send_email(recipient_name: str, recipient_email: str, email_type: str) -> None:
    """
    Sends the user a sample email.

    -----------------------------------------------------------------------------
    **Parameters:**
        recipient_name (str): The name of the user to be addressed in the email.
        recipient_email (str): The email address of the recipient.
        email_type (str): A key from EMAIL dictionary (in email_catalogue.py)
    ```
    """
    email_body = render_template(
        EMAILS[email_type]["template"],  # email template name
        name=recipient_name,
        content=EMAILS[email_type]["content"]
    )
    new_email = EmailMessage(
        subject = f"{EMAILS[email_type]["subject"]}",
        sender = EMAIL_CREDENTIALS["email_address"],
        recipients = [recipient_email]
    )
    new_email.html = email_body

    try:
        mail.send(new_email)
    except Exception as e:
        print_to_terminal(f"ERROR in send_email in email.py (see details bellow):", "RED")
        print_to_terminal(f"Could not send email. Error: {e}", "YELLOW")
    
    print_to_terminal(f"Message sent to email.", "GREEN")



"""
app/emails contain the catalogues for email types and layouts, as well as the helper function that sends an email template to the email address provided by the client.

- catalogue_email: contains all email types available. Each email type has a name, the name of the corresponding template file, and the subject of the email.
- catalogue_layout: contains the names of the available layouts and the template path of each layout folder.
- send_email: contains a helper function used in routes.py to send the requested email to the client.

Every time you decide to add a new layout or email type you will want to make changes to the catalogue files, and make sure you have correct and valid templates in app/templates/emails.
"""
"""
LAYOUTS is a dictionary of layout types where the keys are the layout name and the values are the path to the templates available with the selected layout.
All email templates are in the folder app/templates/emails/layout_X.
Should you decide to add another layout to this project, make sure to add a new folder in app/templates/emails and list it in this dictionary.
"""

LAYOUTS = {
 "Classic": "emails/layout_1/",
 "Modern": "emails/layout_2/",
 "Simple": "emails/layout_3/",
}
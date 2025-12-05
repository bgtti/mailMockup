"""
EMAILS is a dictionary of email types. 
Each contain a subject and the name of the html file associated with it. 
In the "content" value one could store extra information that could be inserted into the jinja template at runtime (in case one template is being used for multiple email types).
Make sure you have a template named appropriately under templates/emails/layout_X.
"""

EMAILS = {
 "Welcome":{
  "subject": "Welcome to MyCompany!",
  "template": "welcome.html",
  "content": ""
 },
 "First_Signup":{
  "subject": "Welcome to YourApp - your journey has just begun!",
  "template": "signup.html",
  "content": ""
 },
 "Onboarding":{
  "subject": "Welcome to YourApp!",
  "template": "onboarding.html",
  "content": ""
 },
 "Verify_Email":{
  "subject": "Confirm your account",
  "template": "verify_email.html",
  "content": ""
 },
 "Reset_Password":{
  "subject": "Reset Password",
  "template": "reset_pass.html",
  "content": ""
 },
 "Free_Trial_Ended":{
  "subject": "Free trial ended",
  "template": "free_trial_end.html",
  "content": ""
 },
 "Account_Deletion":{
  "subject": "Your MyCompany account has been deleted",
  "template": "account_deletion.html",
  "content": ""
 },
 "Newsletter":{
  "subject": "Newsletter",
  "template": "newsletter.html",
  "content": ""
 },
}

#TODO ideas:
"""
Possible additions to the above list:

- invoice issued
- payment successfull
- payment failed
- subscriptions renewed
- free trial ending soon

"""
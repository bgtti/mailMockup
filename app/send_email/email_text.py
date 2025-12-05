
EMAIL_TYPES = {
 "sample":{
  "subject": "A warm welcome!",
  "template": "general.html",
  "content": """
        <p>
            I wanted to personally welcome you to Corporate Email Template Viewer!<br>
            This project is meant to help you plan and visualize automated emails to use in your software project!
        </p>
        <br/>
        <p>
            Automated emails are a must and these should properly represent your brand and feel to the customer!<br>
            You can adapt the Jinja template and visualize your email before incorporating it into your business!
        </p>
        """
 },
 "welcome":{
  "subject": "Welcome to MyCompany!",
  "template": "general.html",
  "content": """
        <p><b>Welcome to MyCompany!</b><p> 
        <br/>
        <p>
            Your account has been created successfully - you can now <a href="#">log in</a> and start exploring everything we offer.
        </p>
        <br/>
        <p>
            You can check out our quick-start guides <a href="#">here</a>!
        </p>
        <p>
            If you have any questions, our support team is here to help.
        </p>
        """
 },
 "signup":{
  "subject": "Welcome to YourApp - your journey has just begun!",
  "template": "general.html",
  "content": """
        <p>
            Thank you for signing up for YourApp!
        </p>
        <p>
            You can now browse all our content and connect to peers!
        </p>
        <br/>
        <p>
            We are excited to guide you through this journey! 
        </p>
        <p>
            Click <a href="#">here</a> to start!
        </p>
        <br/>
        <p>
            Best regards,
        </p>
        """
 },
 "account_confirmation":{
  "subject": "Confirm your account",
  "template": "acct_conf.html",
  "content": ""
 },
 "change_password":{
  "subject": "Change Password",
  "template": "reset_pass.html",
  "content": ""
 },
 "account_deleted":{
  "subject": "Your MyCompany account has been deleted",
  "template": "general.html",
  "content": """
        <p>
            We’re writing to confirm that your MyCompany account has been deleted.
        </p>
        <p>
            All your personal data and account information have been removed from our systems in accordance with our privacy policy.
        </p>
        <br/>
        <p>
            If this deletion was requested by you, no further action is required.
        </p>
        <p>
            If you didn’t request this, please contact our support team immediately: support@mycompany.com
        </p>
        <br/>
        <p>
            Best regards,
        </p>
        """
 },
 
}
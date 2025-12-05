from flask import Flask
import os

#Extensions
from flask_mail import Mail
mail = Mail()
"""`mail` is an instance of `Flask-Mail`, used to send emails through the Flask application."""

from colorama import init
"""'colorama simplifies the process of adding color to text in the terminal."""

#Email credentials
EMAIL_CREDENTIALS = {
    "email_address": os.getenv("EMAIL_ADDRESS", "sample@mail.com") ,
    "email_password": os.getenv("EMAIL_PASSWORD", "tralala") ,
}

#Create app

def create_app(config_class):

    # Create application
    app = Flask(__name__)

    # CONFIG Configuration 
    app.config.from_object(config_class)

    # Initialization of app extensions
    mail.init_app(app) # Initialize flask mail
    init(autoreset=True) # Initialize colorama

    # Blueprints
    from .routes import main
    app.register_blueprint(main)
    # app.register_blueprint(auth, url_prefix='/api/auth')

    @app.route('/test')
    def test_page():
        return '<h1> Testing the App </h1>'

    return app

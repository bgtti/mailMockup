import os
from dotenv import load_dotenv
# from utils.print_to_terminal import print_to_terminal

load_dotenv()

class BaseConfig:
    # BASE_URL = BASE_URLS["backend"]
    SECRET_KEY = "uudiiiduudiiiah"
    
    # Flask-Mail Config
    MAIL_SERVER = "smtp.gmail.com" # consider using mailtrap for testing?
    MAIL_PORT = 465
    MAIL_USERNAME = os.getenv("EMAIL_ADDRESS", "sample@email.com") 
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "tralala") 
    MAIL_DEFAULT_SENDER=os.getenv("EMAIL_ADDRESS", "sample@email.com")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # Cookie settings (tighten for HTTPS)
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = "None" 

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True



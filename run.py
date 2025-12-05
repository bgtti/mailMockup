"""
**run.py is the entry point to the application**: the application script where the instance is defined.
"""
from config import DevelopmentConfig
from app import create_app

app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    
    from utils.print_to_terminal import print_to_terminal
    print_to_terminal(f"App running in HTTP: Dev environment", "BLUE")
    
    app.run() 
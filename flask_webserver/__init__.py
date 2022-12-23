# Initialize application
from flask import Flask

def create_app():
    # Build core
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.config["RECAPTCHA_PUBLIC_KEY"] = ""
    app.config["RECAPTCHA_PARAMETERS"] = {"size": "100%"}
    
    with app.app_context():
        from . import routes
        
        return app
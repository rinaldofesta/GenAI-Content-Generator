from flask import Flask
from app.celery import make_celery

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    
    app.config.from_object('app.config')
    app.secret_key = app.config['SECRET_KEY']  # Set the secret key
    
    celery = make_celery(app)

    from .routes import main
    app.register_blueprint(main)
    
    print("Template Folder: ", app.template_folder)
    print("Static Folder: ", app.static_folder)
    
    return app

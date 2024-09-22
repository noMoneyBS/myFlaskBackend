from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from app.routes.image_routes import image_bp
    app.register_blueprint(image_bp)

    return app

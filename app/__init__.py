from flask import Flask
from config import config
import os

def create_app(config_name=None):
    """Factory function para criar a aplicação Flask"""
    
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

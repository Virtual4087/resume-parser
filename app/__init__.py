from flask import Flask
import os
from config.settings import get_config

def create_app(config_name='dev'):
    """Initialize Flask application with the specified configuration"""
    
    # Create the Flask application instance
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static'
    )
    
    # Load configuration
    app.config.from_object(get_config(config_name))
    
    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Import and register routes
    from app.routes.main_routes import register_routes
    register_routes(app)
    
    return app
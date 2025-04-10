import os
from app import create_app

# Determine environment from ENV variable, default to dev
config_name = os.environ.get('FLASK_ENV', 'dev')

# Create the Flask application with appropriate config
app = create_app(config_name)

if __name__ == '__main__':
    """Run the Flask application"""
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
import os

class Config:
    """Base configuration class"""
    # API Key for Google Gemini API
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', "AIzaSyDquJr4Ph35GmvfNeKihNxGVMurky_NYqU")
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-resume-parser')
    DEBUG = False
    TESTING = False
    
    # File storage settings
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload size

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    
class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    
class ProductionConfig(Config):
    """Production configuration"""
    # Use real environment variables in production
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # In production, this should be set as an environment variable
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

# Configuration dictionary to easily select the right configuration
config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}

def get_config(config_name='dev'):
    """Helper function to get configuration by name"""
    return config_by_name.get(config_name, DevelopmentConfig)
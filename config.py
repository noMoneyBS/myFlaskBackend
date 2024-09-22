import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    UPLOAD_FOLDER = 'uploads'
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')  # setting in bash
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

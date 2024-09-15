import os

class Config:
    # Retrieve the SECRET_KEY from the environment, with a fallback default for development
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Replace 'your_default_secret_key' with a secure default for development

    # SQLAlchemy database connection URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///faqs.db'

    # Disable track modifications to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Retrieve the OpenAI API key from the environment
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Store OpenAI API key in environment variable

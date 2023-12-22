from dotenv import load_dotenv
import os
from extensions import db


load_dotenv()

class ApplicationConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./db.sqlite'

def load_config():
    return ApplicationConfig
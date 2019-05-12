import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# For optional config variables use os.getenv('key') or os.environ.get('key')
# For mandatory config variables use os.eniron['key']

# Application
DEVELOPER_EMAIL = os.environ.get('DEVELOPER_EMAIL', None)
SECRET_KEY = os.environ.get('SECRET_KEY','SECRET_KEY')
APP_NAME = os.environ.get('APP_NAME', 'APP_NAME')

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
APP_KEY = os.environ.get('APP_KEY', 'APP_KEY')

# WEBURI
WEBURI = os.environ.get('WEBURI', 'http://localhost:5000/')
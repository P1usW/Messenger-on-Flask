import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'ivanflaskemail@gmail.com'
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'ivanflaskemail@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'zbmoevtpnlcwhhwm'
    ADMINS = ['ivanflaskemail@gmail.com']
    POSTS_PER_PAGE = 10
    LANGUAGES = ['en', 'ru']
    IAM_TOKEN_YANDEX = os.environ.get('IAM_TOKEN_YANDEX')
    FOLDER_ID_YANDEX = os.environ.get('FOLDER_ID_YANDEX')
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') or 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND') or 'redis://localhost:6379/0'
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME') or 'Ivan'
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD') or 'Shavrin'
    BASIC_AUTH_FORCE = os.environ.get('BASIC_AUTH_FORCE') or False
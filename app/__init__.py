from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail, Message
UPLOAD_FOLDER = "uploads"
app = Flask(__name__)

app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
mail = Mail(app)
app.app_context().push()


csrf = CSRFProtect(app)
from app import views



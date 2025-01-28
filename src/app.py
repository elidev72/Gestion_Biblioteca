from flask import Flask
from flask_migrate import Migrate
from src.database.db_mysql import db, url_db
from src.models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = url_db()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)
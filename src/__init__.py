from flask import Flask
from src.database.db_mysql import db, url_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = url_db()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

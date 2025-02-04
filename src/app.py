from flask import Flask, redirect, url_for, session
from flask_migrate import Migrate
from functools import wraps
from icecream import ic
from src.database.db_mysql import db, url_db, llave_secreta
from src.models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = url_db()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

app.config['SECRET_KEY'] = llave_secreta

def login_requerido(f):
    @wraps(f) # Esto ayuda a mantener la información del nombre de la función original
    def funcion_decoradora(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login')) 
        return f(*args, **kwargs) # Llama a la función original si está logueado
    return funcion_decoradora

# ic.disable()

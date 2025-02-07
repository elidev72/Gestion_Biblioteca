import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

def url_db() -> str:
    USER_DB: str = os.getenv('DB_USER')
    PASS_DB: str = os.getenv('DB_PASSWORD')
    URL_DB: str = os.getenv('DB_HOST')
    NAME_DB: str = os.getenv('DB_NAME')
    return f'mysql+mysqlconnector://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

llave_secreta = os.getenv('SECRET_KEY')

db = SQLAlchemy()

def __manejar_excepcion(e: SQLAlchemyError):
    db.session.rollback()
    raise Exception("ERROR en la capa de acceso a datos") from e

def guardar(dato):
    try:
        db.session.add(dato)
        db.session.commit()
    except SQLAlchemyError as e:
        __manejar_excepcion(e)

def actualizar(dato):
    try:
        db.session.merge(dato)
        db.session.commit()
    except SQLAlchemyError as e:
        __manejar_excepcion(e)

def eliminar(dato):
    try:
        db.session.delete(dato)
        db.session.commit()
    except SQLAlchemyError as e:
        __manejar_excepcion(e)

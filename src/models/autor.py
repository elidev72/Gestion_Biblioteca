from src.database.db_mysql import db
from .persona import Persona

class Autor(Persona):
    libros = db.relationship('Libro', backref='autor', lazy='dynamic')

    def get_tipo(self) -> str:
        return 'Autor'


from src.models.persona import Persona
from src.database.db_mysql import db

class Autor(Persona):
    libros = db.relationship('Libro', backref='autor', lazy='dynamic')

    def get_tipo(self) -> str:
        return 'Autor'


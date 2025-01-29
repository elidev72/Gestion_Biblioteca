from src.database.db_mysql import db
from .persona import Persona

class Bibliotecario(Persona):
    turno = db.Column(db.String(20), nullable=False)
    clave = db.Column(db.String(65), nullable=False)
    prestados = db.relationship('Prestamo', backref='bibliotecario', lazy='dynamic')
    
    def get_tipo(self):
        return 'Bibliotecario'


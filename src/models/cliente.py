from src.database.db_mysql import db
from .persona import Persona

class Cliente(Persona):
    prestamos = db.relationship('Prestamo', backref='cliente', lazy='dynamic')
    
    def get_tipo(self):
        return 'Cliente'

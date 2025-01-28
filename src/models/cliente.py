from src.models.persona import Persona
from src.database.db_mysql import db

class Cliente(Persona):
    prestamos = db.relationship('Prestamo', backref='cliente', lazy='dynamic')
    
    def get_tipo(self):
        return 'Cliente'

from src.models.persona import Persona
from src.database.db_mysql import db

class Bibliotecario(Persona):
    turno = db.Column(db.String(20), nullable=False)
    
    def get_tipo(self):
        return 'Bibliotecario'


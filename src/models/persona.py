from src.database.db_mysql import db

class Persona(db.Model):
    __id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    
    @property
    def id(self) -> int:
        return self.__id
from abc import ABCMeta, abstractmethod
from src.database.db_mysql import db

class PersonaMeta(ABCMeta, type(db.Model)):
    pass

class Persona(db.Model, metaclass=PersonaMeta):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)

    @abstractmethod
    def get_tipo(self) -> str:
        pass

    def __repr__(self):
        return f"{self.get_tipo()}(id='{self.id}', nombre='{self.nombre}', apellido='{self.apellido})"

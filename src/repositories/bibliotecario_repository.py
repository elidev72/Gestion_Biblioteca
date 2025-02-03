from src.models.bibliotecario import Bibliotecario

class BibliotecarioRepository:
    
    @staticmethod
    def traer_por_nombre_y_apellido(nombre: str, apellido: str):
        return Bibliotecario.query.filter_by(nombre=nombre, apellido=apellido).first()

    @staticmethod
    def traer_todos():
        return Bibliotecario.query.all()

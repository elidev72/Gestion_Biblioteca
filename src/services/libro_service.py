from src.app import db
from src.models.libro import Libro
from src.forms.libro_form import LibroForm

class LibroService:
    
    @staticmethod
    def traer_todos():
        return Libro.query.all()
    
    @staticmethod    
    def agregar_libro(libro_form: LibroForm):
        l = Libro()
        
        libro_form.populate_obj(l)
        db.session.add(l)
        db.session.commit()
    
    @staticmethod
    def traer_por_id(id: int):
        return Libro.query.get_or_404(id)

from typing import Callable, List
from src.app import db
from src.models.libro import Libro
from src.forms.libro_form import LibroForm

class LibroService:
    
    @staticmethod
    def traer_todos() -> List[Libro]:
        return Libro.query.all()
    
    @staticmethod    
    def agregar_libro(libro_form: LibroForm) -> None:
        l = Libro()
        
        libro_form.populate_obj(l)
        db.session.add(l)
        db.session.commit()
    
    @staticmethod
    def traer_por_id(id: int) -> Libro:
        return Libro.query.get_or_404(id)
    
    @staticmethod
    def actualizar_libro_prestados(id: int, callback: Callable[[int, int], int]) -> None:
        libro: Libro | None = Libro.query.get(id)
        
        if libro:
            libro.prestados = callback(libro.prestados, 1)
            
            if libro.prestados > libro.total:
                raise ValueError(f'No se puede realizar el prestamo ya que los {libro.total} ejemplares ya fueron asignados.')
            elif libro.prestados < 0:
                raise ValueError(f'Error, libros prestados no pede ser negativo: {libro.prestados}')
            
        else:
            raise ValueError(f'No existe el libro con ID {id}')
        
    @staticmethod
    def editar_libro(libro: Libro, libro_form: LibroForm) -> None:
        if libro:
            libro_form.populate_obj(libro)
            db.session.commit()

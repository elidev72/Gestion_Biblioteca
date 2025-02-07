from datetime import date, timedelta
from flask import session
from src.app import ic
from src.database.db_mysql import guardar, actualizar
from src.utils import suma, resta
from src.models.prestamo import Prestamo
from src.forms.prestamo_form import PrestamoForm
from .libro_service import LibroService as ls

class PrestamoService:
    
    @staticmethod
    def traer_prestamos():
        return Prestamo.query.all()
    
    @staticmethod
    def crear_prestamo(prestamo_form: PrestamoForm, id_libro: int):
        ls.actualizar_libro_prestados(id=id_libro, callback=suma)
        cantidad_dias = prestamo_form.cantidad_dias_de_prestamo.data
        fi = date.today()
        ff = fi + timedelta(days=int(cantidad_dias) if cantidad_dias is not None else 0)
        
        p = Prestamo(
            fecha_inicio=fi,
            fecha_fin = ff,
            cliente_id = prestamo_form.cliente_id.data,
            libro_id = id_libro,
            bibliotecario_id = session['id_bibliotecario']
        )
        
        ic(p)
        
        guardar(p)
    
    @staticmethod
    def devolver_prestamo(id_prestamo: int):
        prestamo: Prestamo | None = Prestamo.query.get_or_404(id_prestamo)
        
        if prestamo:
            ls.actualizar_libro_prestados(id=prestamo.libro_id, callback=resta)
            prestamo.entregado = True
            actualizar(prestamo)
        else:
            raise ValueError(f'No existe prestamo con id {id_prestamo}')

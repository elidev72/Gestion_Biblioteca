from datetime import date, timedelta
from src.app import db, ic
from src.models.prestamo import Prestamo
from src.forms.prestamo_form import PrestamoForm

class PrestamoService:
    
    @staticmethod
    def crear_prestamo(prestamo_form: PrestamoForm, id_bibliotecario: int, id_libro: int):
        p = Prestamo()
        
        prestamo_form.populate_obj(p)
        p.bibliotecario_id = id_bibliotecario
        p.libro_id = id_libro
        p.fecha_inicio = date.today()
        cantidad_dias = prestamo_form.cantidad_dias_de_prestamo.data
        p.fecha_fin = p.fecha_inicio + timedelta(days=int(cantidad_dias) if cantidad_dias is not None else 0)
        
        ic(p)

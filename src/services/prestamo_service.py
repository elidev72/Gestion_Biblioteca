from datetime import date, timedelta
from src.app import db, ic
from src.models import Prestamo, Libro
from src.forms.prestamo_form import PrestamoForm

class PrestamoService:
    
    @staticmethod
    def crear_prestamo(prestamo_form: PrestamoForm, id_libro: int):
        cantidad_dias = prestamo_form.cantidad_dias_de_prestamo.data
        fi = date.today()
        ff = fi + timedelta(days=int(cantidad_dias) if cantidad_dias is not None else 0)
        
        p = Prestamo(
            fecha_inicio=fi,
            fecha_fin = ff,
            # entregado = False,
            cliente_id = prestamo_form.cliente_id.data,
            libro_id = id_libro,
            bibliotecario_id = '2'
        )
        
        ic(p)
        
        try:
            db.session.add(p)
            
            libro: Libro = Libro.query.get(id_libro)
            if libro:
                libro.prestados += 1
                db.session.add(libro)
            
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            ic(e)


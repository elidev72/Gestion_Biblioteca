from src.app import db, ic
from src.models.prestamo import Prestamo
from src.forms.prestamo_form import PrestamoForm

class PrestamoService:
    
    @staticmethod
    def crear_prestamo(prestamo_form: PrestamoForm, id_bibliotecario: int, id_libro: int):
        p = Prestamo()
        
        prestamo_form.populate_obj(p)
        ic(p)

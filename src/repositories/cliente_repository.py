from src.app import db, ic
from src.models.cliente import Cliente
from src.forms.cliente_form import ClienteForm

class ClienteRepository:
    
    @staticmethod
    def crear_cliente(cliente_form: ClienteForm):
        c = Cliente()
        
        cliente_form.populate_obj(c)
        db.session.add(c)
        db.session.commit()
        
        ic(c)
    
    @staticmethod
    def traer_clientes():
        return Cliente.query.all()
    
    @staticmethod
    def traer_cliente_por_id(id: int):
        return Cliente.query.get_or_404(id)

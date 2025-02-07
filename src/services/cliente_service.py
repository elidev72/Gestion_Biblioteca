from src.app import ic
from src.models.cliente import Cliente
from src.forms.cliente_form import ClienteForm
from src.database.db_mysql import guardar, actualizar

class ClienteService:
    
    @staticmethod
    def crear_cliente(cliente_form: ClienteForm):
        c = Cliente()
        
        cliente_form.populate_obj(c)
        ic(c)
        guardar(c)
    
    @staticmethod
    def traer_clientes():
        return Cliente.query.all()
    
    @staticmethod
    def traer_cliente_por_id(id: int):
        return Cliente.query.get_or_404(id)
    
    @staticmethod
    def cantidad_clientes():
        return Cliente.query.count()
    
    @staticmethod
    def editar_cliente(cliente: Cliente, cliente_form: ClienteForm):       
        if cliente:
            cliente_form.populate_obj(cliente)
            actualizar(cliente)

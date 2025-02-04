from src.services.cliente_service import ClienteService as cs

def cliente_existe(id_cliente: int) -> bool:
    return True if id_cliente > 0 and id_cliente <= cs.cantidad_clientes() else False

def suma(a: int, b: int) -> int:
    return a + b

def resta(a: int, b: int) -> int:
    return a - b

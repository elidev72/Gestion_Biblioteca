from flask import redirect, url_for, session
from functools import wraps
from src.services.cliente_service import ClienteService as cs

def login_requerido(f):
    @wraps(f) # Esto ayuda a mantener la información del nombre de la función original
    def funcion_decorada(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login')) 
        return f(*args, **kwargs) # Llama a la función original si está logueado
    return funcion_decorada

def cliente_existe(id_cliente: int) -> bool:
    return True if id_cliente > 0 and id_cliente <= cs.cantidad_clientes() else False

def suma(a: int, b: int) -> int:
    return a + b

def resta(a: int, b: int) -> int:
    return a - b

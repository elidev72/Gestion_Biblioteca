from flask import render_template, request, redirect, url_for
from src.app import app
from src.services.cliente_service import ClienteService, ClienteForm

@app.route('/clientes')
def opciones_cliente():
    return render_template('/cliente/opciones_clientes.html', nombre='A', apellido='A')

@app.route('/clientes/agregar', methods=['GET', 'POST'])
def agregar_cliente():
    cliente_form = ClienteForm()
    retorno = render_template('/cliente/agregar_cliente.html', nombre='A', apellido='A', cf=cliente_form)
    
    if request.method == 'POST':
        if cliente_form.validate_on_submit():
            ClienteService.crear_cliente(cliente_form)
            retorno = redirect(url_for('opciones_cliente'))
    
    return retorno

@app.route('/clientes/ver')
def ver_clientes():
    return render_template('/cliente/ver_clientes.html', nombre='A', apellido='A', clientes=ClienteService.traer_clientes())

@app.route('/cliente/<int:id>')
def detalle_cliente(id: int):
    pass
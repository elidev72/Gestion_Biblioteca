from flask import render_template, request, redirect, url_for
from src.app import app
from src.utils import login_requerido
from src.services.cliente_service import ClienteService as cs, ClienteForm

@app.route('/clientes')
@login_requerido
def opciones_cliente():
    return render_template('/cliente/opciones_clientes.html')

@app.route('/clientes/agregar', methods=['GET', 'POST'])
@login_requerido
def agregar_cliente():
    cliente_form = ClienteForm()
    retorno = render_template('/cliente/agregar_cliente.html', operacion='Agregar', cf=cliente_form)
    
    if request.method == 'POST':
        if cliente_form.validate_on_submit():
            cs.crear_cliente(cliente_form)
            retorno = redirect(url_for('opciones_cliente'))
    
    return retorno

@app.route('/clientes/ver')
@login_requerido
def ver_clientes():
    return render_template('/cliente/ver_clientes.html', clientes=cs.traer_clientes())

@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def editar_cliente(id: int):
    cliente = cs.traer_cliente_por_id(id=id)
    cliente_form = ClienteForm(obj=cliente)
    retorno = render_template('/cliente/agregar_cliente.html', operacion='Editar', cf=cliente_form)
    
    if request.method == 'POST':
        if cliente_form.validate_on_submit():
            cs.editar_cliente(cliente=cliente, cliente_form=cliente_form)
            retorno = redirect(url_for('ver_clientes'))
    
    return retorno

from flask import render_template, request, redirect, url_for
from src.app import app, db
from src.models.cliente import Cliente
from src.forms.cliente_form import ClienteForm

@app.route('/clientes')
def opciones_cliente():
    return render_template('/cliente/opciones_clientes.html', nombre='A', apellido='A')

@app.route('/clientes/agregar', methods=['GET', 'POST'])
def agregar_cliente():
    cliente = Cliente()
    cliente_form = ClienteForm(obj=cliente)
    retorno = render_template('/cliente/agregar_cliente.html', nombre='A', apellido='A', cf=cliente_form)
    
    if request.method == 'POST':
        if cliente_form.validate_on_submit():
            cliente_form.populate_obj(cliente)
            db.session.add(cliente)
            db.session.commit()
            
            retorno = redirect(url_for('opciones_cliente'))
    
    return retorno

@app.route('/clientes/ver')
def ver_clientes():
    clientes = Cliente.query.all()
    return render_template('/cliente/ver_clientes.html', nombre='A', apellido='A', clientes=clientes)

@app.route('/cliente/<int:id>')
def detalle_cliente(id: int):
    pass
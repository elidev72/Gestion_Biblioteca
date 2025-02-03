from flask import render_template, request, redirect, url_for, session
from src.app import app
from src.services.prestamo_service import PrestamoService as ps, PrestamoForm
from src.services.cliente_service import ClienteService as cs

@app.route('/libros/libro/<int:id_libro>/prestar', methods=['GET', 'POST'])
def prestar_libro(id_libro: int):
    session['TOTAL_CLIENTES'] = cs.cantidad_clientes()
    prestamo_form = PrestamoForm()
    retorno = render_template('/prestamo/crear_prestamo.html', nombre='A', apellido='A', id_libro=id_libro, nombre_libro=session['nombre_libro'], pf=prestamo_form)
    
    if request.method == 'POST':
        if prestamo_form.validate_on_submit():
            ps.crear_prestamo(prestamo_form=prestamo_form, id_libro=id_libro)
            retorno = redirect(url_for('detalle_libro', id=id_libro))
            
    return retorno

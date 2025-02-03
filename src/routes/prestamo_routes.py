from flask import render_template, request, redirect, url_for, session
from src.app import app
from src.services.prestamo_service import PrestamoService as ps, PrestamoForm

@app.route('/libros/libro/<int:id_libro>/prestar', methods=['GET', 'POST'])
def prestar_libro(id_libro: int):
    prestamo_form = PrestamoForm()
    retorno = render_template('/prestamo/crear_prestamo.html', nombre='A', apellido='A', id_libro=id_libro, nombre_libro=session['nombre_libro'], pf=prestamo_form)
    
    if request.method == 'POST':
        if prestamo_form.validate_on_submit():
            ps.crear_prestamo(prestamo_form=prestamo_form, id_bibliotecario='2', id_libro=id_libro)
            retorno = redirect(url_for('opciones_libros'))
            
    ps.crear_prestamo(prestamo_form=prestamo_form, id_bibliotecario='2', id_libro=id_libro)
    
    return retorno

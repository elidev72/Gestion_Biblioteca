from flask import render_template, request, redirect, url_for
from src.app import app, login_requerido
from src.services.libro_service import LibroService as ls, LibroForm

@app.route('/libros')
@login_requerido
def opciones_libros():
    return render_template('/libro/opciones_libros.html')

@app.route('/libros/agregar', methods=['GET', 'POST'])
@login_requerido
def agregar_libro():
    libro_form = LibroForm()
    retorno = render_template('/libro/agregar_libro.html', operacion='Agregar', lf=libro_form)
    
    if request.method == 'POST':
        if libro_form.validate_on_submit():
            ls.agregar_libro(libro_form=libro_form)
            retorno = redirect(url_for('opciones_libros'))
    
    return retorno

@app.route('/libros/ver')
@login_requerido
def ver_libros():
    return render_template('/libro/ver_libros.html', libros=ls.traer_todos())

@app.route('/libros/libro/<int:id>')
@login_requerido
def detalle_libro(id: int):
    return render_template('/libro/detalle_libro.html', libro=ls.traer_por_id(id=id))

@app.route('/libros/libro/editar/<int:id>', methods=['GET', 'POST'])
@login_requerido
def editar_libro(id: int):
    libro = ls.traer_por_id(id=id)
    libro_form = LibroForm()
    retorno = render_template('/libro/agregar_libro.html', operacion='Editar', lf=libro_form, id_libro=id)
    
    if request.method == 'POST':
        if libro_form.validate_on_submit():
            ls.editar_libro(libro=libro ,libro_form=libro_form)
            retorno = redirect(url_for('detalle_libro', id=id))
    
    return retorno

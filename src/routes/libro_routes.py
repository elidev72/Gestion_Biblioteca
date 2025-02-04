from flask import render_template, request, redirect, url_for, session
from src.app import app
from src.services.libro_service import LibroService as ls, LibroForm, Libro

@app.route('/libros')
def opciones_libros():
    return render_template('/libro/opciones_libros.html')

@app.route('/libros/agregar', methods=['GET', 'POST'])
def agregar_libro():
    libro_form = LibroForm()
    retorno = render_template('/libro/agregar_libro.html', lf=libro_form)
    
    if request.method == 'POST':
        if libro_form.validate_on_submit():
            ls.agregar_libro(libro_form=libro_form)
            retorno = redirect(url_for('opciones_libros'))
    
    return retorno

@app.route('/libros/ver')
def ver_libros():
    return render_template('/libro/ver_libros.html', libros=ls.traer_todos())

@app.route('/libros/libro/<int:id>')
def detalle_libro(id: int):
    return render_template('/libro/detalle_libro.html', libro=ls.traer_por_id(id=id))
